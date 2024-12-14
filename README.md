# Agent for RoomEnv-v2

[![DOI](https://zenodo.org/badge/776465360.svg)](https://doi.org/10.5281/zenodo.10876433)
[![DOI](https://img.shields.io/badge/Paper-PDF-red.svg)](https://arxiv.org/pdf/2408.05861)

## [RoomEnv-v2](https://github.com/humemai/room-env/blob/main/README-v2.md)

This repo introduces the gynmasium compatible room-env, where both the hidden states and
partial observations are represented as knowledge graphs. The agent is required to come
up with two policies—1. maze navigation (exploration) and 2. question answering. It's
highly recommended for the agent to have a long-term memory.

## [LSTM agent](./lstm/README.md)

This agent inroduces a memory management policy. Although this policy wasn't required by
the RoomEnv-v2, the agent shows that it's better this way since this policy can capture
the hidden state as its long-term memory.

## [GNN agent](./gnn/README.md)

The drawback of the LSTM agent is that the memory management policy is trained
separately from the other two policies. Therefore the GNN agent shows that the memory
management policy and the exploration policy can be trained together, leading to higher
peroformance. Training two policies can lead to non-stationary behavior. To fix this,
this agent leverages a GNN backbone and the MARL framework to train the two policies.

## [GNN-CB agent](./cb/README.md)

The LSTM and GNN agents were concerned with learning the exploration and memory
management policies, while the question answering policy was untouched. They fixed the
question answering policy with a logic-based (SPARQL) heuristics. This was necessary
since this policy also works as a reward function, and it's not easy to train this
polciy along with the other two policies. Therefore the GNN-CB agent introduces a
contextual bandit algorithm to "fine-tune" the question answering policy, resulting in a
better performance.

## [Cite our paper](https://arxiv.org/abs/2408.05861)

```bibtex
@misc{kim2024leveragingknowledgegraphbasedhumanlike,
      title={Leveraging Knowledge Graph-Based Human-Like Memory Systems to Solve Partially Observable Markov Decision Processes},
      author={Taewoon Kim and Vincent François-Lavet and Michael Cochez},
      year={2024},
      eprint={2408.05861},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2408.05861},
}
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn,
inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
1. Run `make test && make style && make quality` in the root repo directory, to ensure
   code quality.
1. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
1. Push to the Branch (`git push origin feature/AmazingFeature`)
1. Open a Pull Request

## Authors

- [Taewoon Kim](https://taewoon.kim/)
- [Michael Cochez](https://www.cochez.nl/)
- [Vincent Francois-Lavet](http://vincent.francois-l.be/)
