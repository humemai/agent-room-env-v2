"""A lot copied from https://github.com/migalkin/StarE"""

import torch
import torch_scatter
from torch_scatter import scatter_add, scatter_max


def maybe_num_nodes(index, num_nodes=None):
    return index.max().item() + 1 if num_nodes is None else num_nodes


def softmax(src, index, num_nodes=None) -> torch.Tensor:
    r"""Computes a sparsely evaluated softmax.
    Given a value tensor :attr:`src`, this function first groups the values
    along the first dimension based on the indices specified in :attr:`index`,
    and then proceeds to compute the softmax individually for each group.

    Args:
        src (Tensor): The source tensor.
        index (LongTensor): The indices of elements for applying the softmax.
        num_nodes (int, optional): The number of nodes, *i.e.*
            :obj:`max_val + 1` of :attr:`index`. (default: :obj:`None`)

    Returns:
        out: The softmax values.

    """

    num_nodes = maybe_num_nodes(index, num_nodes)

    out = src - scatter_max(src, index, dim=0, dim_size=num_nodes)[0][index]
    out = out.exp()
    out = out / (scatter_add(out, index, dim=0, dim_size=num_nodes)[index] + 1e-16)

    return out


def com_mult(a, b):
    r1, i1 = a[..., 0], a[..., 1]
    r2, i2 = b[..., 0], b[..., 1]
    return torch.stack([r1 * r2 - i1 * i2, r1 * i2 + i1 * r2], dim=-1)


def conj(a):
    a[..., 1] = -a[..., 1]
    return a


def cconv(a, b):
    return torch.irfft(
        com_mult(torch.rfft(a, 1), torch.rfft(b, 1)), 1, signal_sizes=(a.shape[-1],)
    )


def ccorr(a, b):
    return torch.irfft(
        com_mult(conj(torch.rfft(a, 1)), torch.rfft(b, 1)),
        1,
        signal_sizes=(a.shape[-1],),
    )


def rotate(h, r):
    # re: first half, im: second half
    # assume embedding dim is the last dimension
    d = h.shape[-1]
    h_re, h_im = torch.split(h, d // 2, -1)
    r_re, r_im = torch.split(r, d // 2, -1)
    return torch.cat([h_re * r_re - h_im * r_im, h_re * r_im + h_im * r_re], dim=-1)


def scatter_(name, src, index, dim_size=None) -> torch.Tensor:
    r"""Aggregates all values from the :attr:`src` tensor at the indices
    specified in the :attr:`index` tensor along the first dimension.
    If multiple indices reference the same location, their contributions
    are aggregated according to :attr:`name` (either :obj:`"add"`,
    :obj:`"mean"` or :obj:`"max"`).

    Args:
        name (string): The aggregation to use (:obj:`"add"`, :obj:`"mean"`,
            :obj:`"max"`).
        src (Tensor): The source tensor.
        index (LongTensor): The indices of elements to scatter.
        dim_size (int, optional): Automatically create output tensor with size
            :attr:`dim_size` in the first dimension. If set to :attr:`None`, a
            minimal sized output tensor is returned. (default: :obj:`None`)

    Returns:
        Tensor: The aggregated tensor.
    """

    assert name in ["add", "mean", "max"]

    op = getattr(torch_scatter, "scatter_{}".format(name))
    fill_value = -1e38 if name == "max" else 0
    out = op(src, index, 0, None, dim_size, fill_value)
    if isinstance(out, tuple):
        out = out[0]

    if name == "max":
        out[out == fill_value] = 0

    return out


def extract_entities_and_relations(sample: list[list]) -> tuple[list[str], list[str]]:
    r"""Extract entities and relations from a sample.

    Args:
        sample: A list of quadruples: (head, relation, tail, qualifiers).

    Returns:
        entities: A list of entities.
        relations: A list of relations.

    """
    entities = set()
    relations = set()
    for quadruple in sample:
        head, relation, tail, quals = quadruple
        entities.add(head)
        entities.add(tail)
        relations.add(relation)
        relations.add(relation + "_inv")
        for q_rel, q_entity in quals.items():
            relations.add(q_rel)
            if isinstance(q_entity, list):
                entities.add(str(max(q_entity)))
            else:
                entities.add(str(round(q_entity)))

    entities = sorted(list(entities), reverse=True)
    relations = sorted(list(relations), reverse=True)

    return entities, relations


def process_graph(
    sample: list[list],
) -> tuple[
    list,
    list,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    int,
]:
    r"""Process a sample in a batch. All the indexes are local to the sample. When you
    batch multiple samples, you need to offset some of the indexes to make them global.

    Args:
        graph: A list of quadruples: (head, relation, tail, qualifiers).

        [['dep_007', 'atlocation', 'room_000', {'current_time': 2, 'strength': 1}],
        ['agent', 'atlocation', 'room_000', {'current_time': 2, 'strength': 1}],
        ['room_000', 'west', 'wall', {'current_time': 2, 'strength': 1}],
        ['room_000', 'north', 'wall', {'current_time': 2, 'strength': 1.8}],
        ['dep_001',
        'atlocation',
        'room_000',
        {'current_time': 2, 'timestamp': [0, 1]}],
        ['room_000', 'south', 'room_004', {'current_time': 2, 'timestamp': [1]}],
        ['room_000',
        'east',
        'room_001',
        {'current_time': 2, 'timestamp': [0], 'strength': 1}]]

    Returns:
        entities: The shape is [num_entities in the sample]
        relations: The shape is [num_relations in the sample]
        edge_idx: The shape is [2, num_quadruples]
        edge_type: The shape is [num_quadruples]
        quals: The shape is [3, number of qualifier key-value pairs]

        edge_idx_inv: The shape is [2, num_quadruples]
        edge_type_inv: The shape is [num_quadruples]
        quals_inv: The shape is [3, number of qualifier key-value pairs]

        short_memory_idx: The shape is [number of short-term memories]
            the idx indexes `edge_idx` and `edge_type`
        agent_entity_idx: One scalar value. the idx indexes `entity_embeddings`


    """
    entities, relations = extract_entities_and_relations(sample)
    entity_to_idx = {entity: idx for idx, entity in enumerate(entities)}
    relation_to_idx = {relation: idx for idx, relation in enumerate(relations)}

    edge_idx = []
    edge_type = []
    quals = []

    edge_idx_inv = []
    edge_type_inv = []
    quals_inv = []

    short_memory_idx = []
    agent_entity_idx = None

    for i, quadruple in enumerate(sample):
        head, relation, tail, qualifiers = quadruple

        if head == "agent":
            agent_entity_idx = entity_to_idx[head]

        if tail == "agent":
            agent_entity_idx = entity_to_idx[tail]

        edge_idx.append([entity_to_idx[head], entity_to_idx[tail]])
        edge_type.append(relation_to_idx[relation])

        edge_idx_inv.append([entity_to_idx[tail], entity_to_idx[head]])
        edge_type_inv.append(relation_to_idx[relation + "_inv"])

        for q_rel, q_entity in qualifiers.items():

            if q_rel == "timestamp":
                q_entity_str = str(round(max(q_entity)))
            elif q_rel == "current_time":
                q_entity_str = str(round(q_entity))
                short_memory_idx.append(i)
            elif q_rel == "strength":
                q_entity_str = str(round(q_entity))
            else:
                raise ValueError(f"Unknown qualifier: {q_rel}")

            quals.append(
                [
                    relation_to_idx[q_rel],
                    entity_to_idx[q_entity_str],
                    i,
                ]
            )
            quals_inv.append(
                [
                    relation_to_idx[q_rel],
                    entity_to_idx[q_entity_str],
                    i,
                ]
            )
    if agent_entity_idx is None:
        raise ValueError("No agent entity found in the sample")
    return (
        entities,
        relations,
        torch.tensor(edge_idx).T,
        torch.tensor(edge_type),
        torch.tensor(quals).T,
        torch.tensor(edge_idx_inv).T,
        torch.tensor(edge_type_inv),
        torch.tensor(quals_inv).T,
        torch.tensor(short_memory_idx),
        agent_entity_idx,
    )
