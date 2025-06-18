import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn.functional as F
import yaml
from IPython.display import clear_output
from tqdm.auto import tqdm


def read_pickle(fname: str):
    """Read pickle"""
    with open(fname, "rb") as stream:
        foo = pickle.load(stream)
    return foo


def write_pickle(to_pickle: object, fname: str):
    """Write pickle"""
    with open(fname, "wb") as stream:
        foo = pickle.dump(to_pickle, stream)
    return foo


def list_duplicates_of(seq, item) -> list:
    # https://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at + 1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


def is_running_notebook() -> bool:
    """See if the code is running in a notebook or not."""
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


def argmax(iterable):
    """argmax"""
    return max(enumerate(iterable), key=lambda x: x[1])[0]


def write_yaml(content: dict, fname: str) -> None:
    """write yaml."""
    with open(fname, "w", encoding="utf-8") as stream:
        yaml.dump(content, stream, indent=2, sort_keys=False)


class ReplayBuffer:
    r"""A simple numpy replay buffer.

    numpy replay buffer is faster than deque or list.
    copied from https://github.com/Curt-Park/rainbow-is-all-you-need

    Attributes:
        state (np.ndarray): Buffer for states, initialized as an array of None
            values of dtype=object.
        next_state (np.ndarray): Buffer for next states, initialized similarly
            to state.
        action (np.ndarray): Buffer for actions, initialized as an array of None
            values of dtype=object.
        reward (np.ndarray): Buffer for rewards.
        done (np.ndarray): Buffer for done flags, initialized as an array of zeros
            of dtype=np.float32.
        max_size (int): Maximum size of the buffer.
        batch_size (int): Batch size for sampling from the buffer.
        pointer (int): Pointer to the current position in the buffer.
        size (int): Current size of the buffer.


    Example:
    ```
    buffer = ReplayBuffer(8, 4)

    for _ in range(6):

        state = {str(i): str(random.randint(0, 10)) for i in range(3)}
        next_state = {str(i): str(random.randint(0, 10)) for i in range(3)}
        action = [random.randint(0, 3) for _ in range(random.randint(1, 10))]
        reward = random.randint(0, 1)
        done = random.choice([False, True])
        buffer.store(
            *[
                state,
                action,
                reward,
                next_state,
                done,
            ]
        )

    sample = buffer.sample_batch()
    ```
    >>> sample
    {'state': array([{'0': '5', '1': '10', '2': '2'}, {'0': '9', '1': '2', '2': '5'},
            {'0': '6', '1': '10', '2': '9'}, {'0': '6', '1': '0', '2': '6'}],
        dtype=object),
    'next_state': array([{'0': '10', '1': '0', '2': '2'}, {'0': '9', '1': '2', '2': '4'},
            {'0': '1', '1': '7', '2': '1'}, {'0': '8', '1': '9', '2': '0'}],
        dtype=object),
    'action': array([np.array([2, 0, 2, 1, 3]), np.array([0, 1, 2]),
            np.array([0, 1, 3, 1, 1, 2, 2]), np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
        dtype=object),
    'reward': array([0., 1., 1., 0.], dtype=float32),
    'done': array([1., 0., 1., 1.], dtype=float32)}

    >>> sample["action"].shape
    (4,)

    """

    def __init__(
        self,
        max_size: int,
        batch_size: int = 32,
    ):
        """Initialize replay buffer.

        Args:
            max_size: size of the buffer
            batch_size: batch size to sample

        Raises:
            ValueError: If batch_size is greater than max_size.

        Note:
            The state, next_state, and action are initialized with `None`
            values and have `dtype=object` to accommodate arbitrary Python objects,
            ensuring flexibility in storing different types of data.

        """

        if batch_size > max_size:
            raise ValueError("batch_size must be smaller than max_size")

        self.state = np.array([None] * max_size, dtype=object)
        self.next_state = np.array([None] * max_size, dtype=object)
        self.action = np.array([None] * max_size, dtype=object)
        self.reward = np.zeros([max_size], dtype=np.float32)
        self.done = np.zeros(max_size, dtype=np.float32)
        self.max_size = max_size
        self.batch_size = batch_size
        (
            self.pointer,
            self.size,
        ) = (
            0,
            0,
        )

    def store(
        self,
        state: np.ndarray,
        action: np.ndarray,
        reward: float,
        next_state: np.ndarray,
        done: bool,
    ) -> None:
        r"""Store the data in the buffer.

        Args:
            state: state
            action: action
            reward: reward
            next_state: next state
            done: done

        """
        self.state[self.pointer] = state
        self.next_state[self.pointer] = next_state
        self.action[self.pointer] = action
        self.reward[self.pointer] = reward
        self.done[self.pointer] = done
        self.pointer = (self.pointer + 1) % self.max_size
        self.size = min(self.size + 1, self.max_size)

    def sample_batch(self) -> dict[str, np.ndarray]:
        r"""Sample a batch of data from the buffer.

        Returns:
            A dictionary of samples from the replay buffer.
                state: np.ndarray,
                next_state: np.ndarray,
                action: np.ndarray,
                reward: np.ndarray,
                done: np.ndarray

        """
        idxs = np.random.choice(self.size, size=self.batch_size, replace=False)
        return dict(
            state=self.state[idxs],
            next_state=self.next_state[idxs],
            action=self.action[idxs],
            reward=self.reward[idxs],
            done=self.done[idxs],
        )

    def __len__(self) -> int:
        return self.size


def plot_results(
    scores: dict[str, list[float]],
    training_loss: dict[str, list[float]],
    epsilons: list[float],
    q_values: dict[str, dict[str, list[float]]],
    iteration_idx: int,
    num_iterations: int,
    total_maximum_episode_rewards: int,
    default_root_dir: str,
    remember2str,
    forget2str,
    to_plot: str = "all",
    save_fig: bool = False,
) -> None:
    r"""Plot things for DQN training.

    Args:
        scores: a dictionary of scores for train, validation, and test.
        training_loss: a dict of training losses for all, remember, and forget.
        epsilons: a list of epsilons.
        q_values: a dictionary of q_values for train, validation, and test.
        iteration_idx: the current iteration index.
        num_iterations: the total number of iterations.
        total_maximum_episode_rewards: the total maximum episode rewards.
        default_root_dir: the root directory where the results are saved.
        remember2str: a dictionary to convert remember actions to strings.
        forget2str: a dictionary to convert forget actions to strings.
        to_plot: what to plot:
            "all": plot everything
            "training_td_loss": plot training td loss
            "epsilons": plot epsilons
            "scores": plot scores
            "q_value_train": plot q_values for training
            "q_value_val": plot q_values for validation
            "q_value_test": plot q_values for test
        save_fig: whether to save the figure or not

    """
    is_notebook = is_running_notebook()

    if is_notebook:
        clear_output(True)

    if to_plot == "all":
        plt.figure(figsize=(20, 20))

        plt.subplot(333)
        if scores["train"]:
            plt.title(
                f"iteration {iteration_idx} out of {num_iterations}. "
                f"training score: {scores['train'][-1]} out of "
                f"{total_maximum_episode_rewards}"
            )
            plt.plot(scores["train"], label="Training score")
            plt.xlabel("episode")

        if scores["val"]:
            val_means = [round(np.mean(scores).item()) for scores in scores["val"]]
            plt.title(
                f"validation score: {val_means[-1]} out of "
                f"{total_maximum_episode_rewards}"
            )
            plt.plot(val_means, label="Validation score")
            plt.xlabel("episode")

        if scores["test"]:
            plt.title(
                f"test score: {np.mean(scores['test'])} out of "
                f"{total_maximum_episode_rewards}"
            )
            plt.plot(
                [round(np.mean(scores["test"]).item(), 2)] * len(scores["train"]),
                label="Test score",
            )
            plt.xlabel("episode")
        plt.legend(loc="best")

        plt.subplot(331)
        plt.title("training td loss (log scale)")
        plt.plot(training_loss["total"], label="total")
        plt.plot(training_loss["remember"], label="remember")
        plt.plot(training_loss["forget"], label="forget")
        plt.yscale("log")  # Set y-axis to log scale
        plt.xlabel("update counts")
        plt.legend(loc="best")

        plt.subplot(332)
        plt.title("epsilons")
        plt.plot(epsilons)
        plt.xlabel("update counts")

        for subplot_num, split in zip([334, 335, 336], ["train", "val", "test"]):
            plt.subplot(subplot_num)
            plt.title(f"Q-values (remember), {split}")
            for action_number in range(len(remember2str)):
                plt.plot(
                    [
                        q[action_number]
                        for q_value_ in q_values[split]["remember"]
                        for q in q_value_
                    ],
                    label=remember2str[action_number],
                )
            plt.legend(loc="best")
            plt.xlabel("number of actions")

        for subplot_num, split in zip([337, 338, 339], ["train", "val", "test"]):
            plt.subplot(subplot_num)
            plt.title(f"Q-values (forget), {split}")
            for action_number in range(len(forget2str)):
                plt.plot(
                    [
                        q_value_[0][action_number]
                        for q_value_ in q_values[split]["forget"]
                    ],
                    label=forget2str[action_number],
                )
            plt.legend(loc="best")
            plt.xlabel("number of actions")

        plt.subplots_adjust(hspace=0.5)
        if save_fig:
            plt.savefig(os.path.join(default_root_dir, "plot.pdf"))

        if is_notebook:
            plt.show()
        else:
            console(**locals())
            plt.close("all")

    elif to_plot == "training_td_loss":
        plt.figure()
        plt.title("training td loss")
        plt.plot(training_loss["total"], label="total")
        plt.plot(training_loss["remember"], label="remember")
        plt.plot(training_loss["forget"], label="forget")
        plt.xlabel("update counts")
        plt.legend(loc="best")
        plt.subplots_adjust(hspace=0.5)

    elif to_plot == "epsilons":
        plt.figure()
        plt.title("epsilons")
        plt.plot(epsilons)
        plt.xlabel("update counts")
        plt.subplots_adjust(hspace=0.5)

    elif to_plot == "scores":
        plt.figure()

        if scores["train"]:
            plt.title(
                f"iteration {iteration_idx} out of {num_iterations}. "
                f"training score: {scores['train'][-1]} out of "
                f"{total_maximum_episode_rewards}"
            )
            plt.plot(scores["train"], label="Training score")
            plt.xlabel("episode")

        if scores["val"]:
            val_means = [round(np.mean(scores).item()) for scores in scores["val"]]
            plt.title(
                f"validation score: {val_means[-1]} out of "
                f"{total_maximum_episode_rewards}"
            )
            plt.plot(val_means, label="Validation score")
            plt.xlabel("episode")

        if scores["test"]:
            plt.title(
                f"test score: {np.mean(scores['test'])} out of "
                f"{total_maximum_episode_rewards}"
            )
            plt.plot(
                [round(np.mean(scores["test"]).item(), 2)] * len(scores["train"]),
                label="Test score",
            )
            plt.xlabel("episode")
        plt.legend(loc="best")
        plt.subplots_adjust(hspace=0.5)

    else:
        plt.figure(figsize=(20, 13))

        for subplot_num, split in zip([231, 232, 233], ["train", "val", "test"]):
            plt.subplot(subplot_num)
            plt.title(f"Q-values (remember), {split}")
            for action_number in range(len(remember2str)):
                plt.plot(
                    [
                        q_value_[action_number]
                        for q_value_ in q_values[split]["remember"]
                    ],
                    label=f"action {action_number}",
                )
            plt.legend(loc="best")
            plt.xlabel("number of actions")

        for subplot_num, split in zip([234, 235, 236], ["train", "val", "test"]):
            plt.subplot(subplot_num)
            plt.title(f"Q-values (forget), {split}")
            for action_number in range(len(forget2str)):
                plt.plot(
                    [q_value_[action_number] for q_value_ in q_values[split]["forget"]],
                    label=f"action {action_number}",
                )
            plt.legend(loc="best")
            plt.xlabel("number of actions")

        plt.subplots_adjust(hspace=0.5)


def console(
    scores: dict,
    training_loss: list,
    iteration_idx: int,
    num_iterations: int,
    total_maximum_episode_rewards: int,
    **kwargs,
) -> None:
    r"""Print the dqn training to the console."""
    if scores["train"]:
        tqdm.write(
            f"iteration {iteration_idx} out of {num_iterations}.\n"
            f"training score: "
            f"{scores['train'][-1]} out of {total_maximum_episode_rewards}"
        )

    if scores["val"]:
        val_means = [round(np.mean(scores).item()) for scores in scores["val"]]
        tqdm.write(
            f"validation score: {val_means[-1]} "
            f"out of {total_maximum_episode_rewards}"
        )

    if scores["test"]:
        tqdm.write(
            f"test score: {np.mean(scores['test'])} out of "
            f"{total_maximum_episode_rewards}"
        )

    tqdm.write(f"training loss (all): {training_loss['total'][-1]}\n")
    print()


def save_final_results(
    scores: dict[str, list[float]],
    training_loss: dict[str, list[float]],
    default_root_dir: str,
    q_values: dict[str, dict[str, list[float]]],
    self: object,
    save_the_agent: bool = False,
) -> None:
    r"""Save dqn train / val / test results.

    Args:
        scores: a dictionary of scores for train, validation, and test.
        training_loss: a dict of training losses for all, remember, and forget
        default_root_dir: the root directory where the results are saved.
        q_values: a dictionary of q_values for train, validation, and test.
        self: the agent object.
        save_the_agent: whether to save the agent or not.

    """
    results = {
        "train_score": scores["train"],
        "validation_score": [
            {
                "mean": round(np.mean(scores).item(), 2),
                "std": round(np.std(scores).item(), 2),
            }
            for scores in scores["val"]
        ],
        "test_score": {
            "mean": round(np.mean(scores["test"]).item(), 2),
            "std": round(np.std(scores["test"]).item(), 2),
        },
        "training_loss": {
            key: [None if np.isnan(val_) else val_ for val_ in val]
            for key, val in training_loss.items()
        },
    }
    write_yaml(results, os.path.join(default_root_dir, "results.yaml"))

    q_values_ = {
        key: {
            key_: [
                [
                    [None if np.isnan(num_) else float(num_) for num_ in num]
                    for num in val__.tolist()
                ]
                for val__ in val_
            ]
            for key_, val_ in val.items()
        }
        for key, val in q_values.items()
    }

    write_yaml(q_values_, os.path.join(default_root_dir, "q_values.yaml"))
    if save_the_agent:
        write_pickle(self, os.path.join(default_root_dir, "agent.pkl"))


def compute_loss_remember(
    batch: dict,
    device: str,
    dqn: torch.nn.Module,
    dqn_target: torch.nn.Module,
    ddqn: bool,
    gamma: float,
) -> torch.Tensor:
    r"""Return the DQN td loss for the short-term memory management policy (remember).

    G_t   = r + gamma * v(s_{t+1})  if state != Terminal
          = r                       otherwise

    Args:
        batch: A dictionary of samples from the replay buffer.
            state: np.ndarray,
            action: np.ndarray,
            reward: float,
            next_state: np.ndarray,
            done: bool,
        device: cpu or cuda
        dqn: dqn model
        dqn_target: dqn target model
        ddqn: whether to use double dqn or not
        gamma: discount factor

    Returns:
        loss: TD loss for short-term memory management (remember policy)

    """
    state = batch["state"]
    state_next = batch["next_state"]
    action = [
        torch.LongTensor(np.array([num.item() for num in a])).reshape(-1, 1).to(device)
        for a in batch["action"]
    ]
    reward = torch.FloatTensor(batch["reward"]).to(device)
    done = torch.FloatTensor(batch["done"]).to(device)

    # Forward pass on current state to get Q-values
    q_value_current = dqn(state, policy_type="remember")

    # Forward pass on next state to get Q-values
    q_value_next = dqn_target(state_next, policy_type="remember")

    if ddqn:
        q_value_for_action = dqn(state_next, policy_type="remember")

    q_value_current_batch = []
    q_value_target_batch = []

    # note that the observations are assumed to be randomized.
    min_lens = [min(len(i), len(j)) for i, j in zip(q_value_current, q_value_next)]

    for idx in range(len(min_lens)):
        min_len = min_lens[idx]

        action_ = action[idx][:min_len]
        q_value_current_ = q_value_current[idx][:min_len]
        q_value_current_chosen = q_value_current_.gather(1, action_)
        q_value_next_ = q_value_next[idx][:min_len]

        if ddqn:
            # Double DQN: Use current DQN to select actions, target DQN to evaluate
            # those actions
            q_value_for_action_ = q_value_for_action[idx][:min_len]
            action_next = q_value_for_action_.argmax(dim=1, keepdim=True)
            q_value_next_chosen = q_value_next_.gather(1, action_next).detach()
        else:
            # Vanilla DQN: Use target DQN to get max Q-value for next state
            q_value_next_chosen = q_value_next_.max(dim=1, keepdim=True)[0].detach()

        # Compute the target Q-values considering whether the state is terminal
        q_value_target_ = reward[idx] + gamma * q_value_next_chosen * (1 - done[idx])

        q_value_current_batch.append(q_value_current_chosen)
        q_value_target_batch.append(q_value_target_)

    q_value_current_batch = torch.concat(q_value_current_batch, dim=0)
    q_value_target_batch = torch.concat(q_value_target_batch, dim=0)

    assert q_value_current_batch.shape == q_value_target_batch.shape

    # Calculate loss
    loss = F.smooth_l1_loss(q_value_current_batch, q_value_target_batch)

    return loss


def compute_loss_forget(
    batch: dict,
    device: str,
    dqn: torch.nn.Module,
    dqn_target: torch.nn.Module,
    ddqn: bool,
    gamma: float,
) -> torch.Tensor:
    r"""Return the DQN td loss for forget policy.

    G_t   = r + gamma * v(s_{t+1})  if state != Terminal
          = r                       otherwise

    Args:
        batch: A dictionary of samples from the replay buffer.
            state: np.ndarray,
            action: np.ndarray,
            reward: float,
            next_state: np.ndarray,
            done: bool,
        device: cpu or cuda
        dqn: dqn model
        dqn_target: dqn target model
        ddqn: whether to use double dqn or not
        gamma: discount factor

    Returns:
        loss: TD loss for the long-term memory management (forget policy)

    """

    state = batch["state"]
    state_next = batch["next_state"]
    action = torch.LongTensor(
        np.array([num.item() for num in batch["action"]]).reshape(-1, 1)
    ).to(device)
    reward = torch.FloatTensor(batch["reward"]).reshape(-1, 1).to(device)
    done = torch.FloatTensor(batch["done"]).reshape(-1, 1).to(device)

    # Forward pass on current state to get Q-values
    q_value_current = dqn(state, policy_type="forget")

    q_value_current = torch.concat(q_value_current)
    q_value_current = q_value_current.gather(1, action)

    q_value_next = dqn_target(state_next, policy_type="forget")
    q_value_next = torch.concat(q_value_next)

    if ddqn:
        # Double DQN: Use current DQN to select actions, target DQN to evaluate those
        # actions
        q_value_for_action = dqn(state_next, policy_type="forget")
        q_value_for_action = torch.concat(q_value_for_action)
        action_next = q_value_for_action.argmax(dim=1, keepdim=True)
        q_value_next = q_value_next.gather(1, action_next).detach()
    else:
        # Vanilla DQN: Use target DQN to get max Q-value for next state
        q_value_next = q_value_next.max(dim=1, keepdim=True)[0].detach()

    # Compute the target Q-values considering whether the state is terminal
    q_value_target = reward + gamma * q_value_next * (1 - done)

    assert q_value_current.shape == q_value_target.shape

    # Calculate loss
    loss = F.smooth_l1_loss(q_value_current, q_value_target)

    return loss


def update_model(
    forget_policy: str,
    remember_policy: str,
    replay_buffer_remember: ReplayBuffer,
    replay_buffer_forget: ReplayBuffer,
    device: str,
    ddqn: bool,
    gamma: float,
    use_gradient_clipping: bool = True,
    gradient_clip_value: float = 1.0,
    separate_networks: bool = False,
    # Shared network parameters
    optimizer: torch.optim.Optimizer = None,
    dqn: torch.nn.Module = None,
    dqn_target: torch.nn.Module = None,
    # Separate network parameters
    optimizer_forget: torch.optim.Optimizer = None,
    optimizer_remember: torch.optim.Optimizer = None,
    dqn_forget: torch.nn.Module = None,
    dqn_target_forget: torch.nn.Module = None,
    dqn_remember: torch.nn.Module = None,
    dqn_target_remember: torch.nn.Module = None,
) -> tuple[float, float, float]:
    r"""Update the model by gradient descent.

    Args:
        forget_policy: Forget policy type
        remember_policy: Remember policy type
        replay_buffer_remember: replay buffer for remember policy
        replay_buffer_forget: replay buffer for forget policy
        device: cpu or cuda
        ddqn: whether to use double dqn or not
        gamma: discount factor
        use_gradient_clipping: Whether to use gradient clipping.
        gradient_clip_value: The maximum norm for gradient clipping.
        separate_networks: Whether using separate networks for policies
        optimizer: optimizer for shared network
        dqn: shared dqn model
        dqn_target: shared dqn target model
        optimizer_forget: optimizer for forget network
        optimizer_remember: optimizer for remember network
        dqn_forget: forget dqn model
        dqn_target_forget: forget dqn target model
        dqn_remember: remember dqn model
        dqn_target_remember: remember dqn target model

    Returns:
        loss_remember, loss_forget, loss_combined
    """
    loss_remember = torch.tensor(0.0, device=device)
    loss_forget = torch.tensor(0.0, device=device)

    if remember_policy == "rl":
        batch_remember = replay_buffer_remember.sample_batch()
        batch_remember = {
            "state": batch_remember["state"],
            "action": batch_remember["action"],
            "reward": batch_remember["reward"],
            "next_state": batch_remember["next_state"],
            "done": batch_remember["done"],
        }
        
        if separate_networks:
            loss_remember = compute_loss_remember(
                batch_remember, device, dqn_remember, dqn_target_remember, ddqn, gamma
            )
            if optimizer_remember is not None:
                optimizer_remember.zero_grad()
                loss_remember.backward()
                if use_gradient_clipping:
                    torch.nn.utils.clip_grad_norm_(dqn_remember.parameters(), gradient_clip_value)
                optimizer_remember.step()
        else:
            loss_remember = compute_loss_remember(
                batch_remember, device, dqn, dqn_target, ddqn, gamma
            )

    if forget_policy == "rl":
        batch_forget = replay_buffer_forget.sample_batch()
        batch_forget = {
            "state": batch_forget["state"],
            "action": batch_forget["action"],
            "reward": batch_forget["reward"],
            "next_state": batch_forget["next_state"],
            "done": batch_forget["done"],
        }

        if separate_networks:
            loss_forget = compute_loss_forget(
                batch_forget, device, dqn_forget, dqn_target_forget, ddqn, gamma
            )
            if optimizer_forget is not None:
                optimizer_forget.zero_grad()
                loss_forget.backward()
                if use_gradient_clipping:
                    torch.nn.utils.clip_grad_norm_(dqn_forget.parameters(), gradient_clip_value)
                optimizer_forget.step()
        else:
            loss_forget = compute_loss_forget(
                batch_forget, device, dqn, dqn_target, ddqn, gamma
            )

    # For shared networks, update once with combined loss
    if not separate_networks and (remember_policy == "rl" or forget_policy == "rl"):
        loss = loss_remember + loss_forget
        optimizer.zero_grad()
        loss.backward()
        if use_gradient_clipping:
            torch.nn.utils.clip_grad_norm_(dqn.parameters(), gradient_clip_value)
        optimizer.step()
    else:
        loss = loss_remember + loss_forget

    loss_remember = loss_remember.detach().cpu().numpy().item()
    loss_forget = loss_forget.detach().cpu().numpy().item()
    loss = loss.detach().cpu().numpy().item()

    return loss_remember, loss_forget, loss


def select_action(
    state: list[list],
    greedy: bool,
    dqn: torch.nn.Module,
    epsilon: float,
    policy_type: str,
) -> tuple[np.ndarray, np.ndarray]:
    r"""Select action(s) from the input state, with epsilon-greedy policy.

    Args:
        state: This is the input to the neural network. Make sure that it's compatible
            with the input shape of the neural network. It's very likely that this
            looks like a list of quadruples.
        greedy: always pick greedy action if True
        dqn: dqn model
        epsilon: epsilon
        policy_type: "remember" or "forget"

    Returns:
        selected_actions: dimension is [num_actions_taken]
        q_values: dimension is [num_actions_taken, action_space_dim]

    """
    # Since dqn requires a batch dimension, we need to encapsulate the state in a list
    q_values = dqn(np.array([state], dtype=object), policy_type=policy_type)

    q_values = q_values[0]  # remove the dummy batch dimension
    q_values = q_values.detach().cpu().numpy()

    action_space_dim = q_values.shape[1]

    if greedy or epsilon < np.random.random():
        selected_actions = q_values.argmax(axis=1)
    else:
        selected_actions = np.random.randint(0, action_space_dim, size=len(q_values))

    return selected_actions, q_values


def save_validation(
    scores_temp: list,
    scores: dict,
    default_root_dir: str,
    num_episodes: int,
    validation_interval: int,
    val_file_names: list,
    dqn: torch.nn.Module,
) -> None:
    r"""Keep the best validation model.

    Args:
        scores_temp: a list of validation scores for the current validation episode.
        scores: a dictionary of scores for train, validation, and test.
        default_root_dir: the root directory where the results are saved.
        num_episodes: number of episodes run so far
        validation_interval: the interval to validate the model.
        val_file_names: a list of dirnames for the validation models.
        dqn: the dqn model to save (for shared networks only).

    Note:
        This function is primarily for shared networks. For separate networks,
        use the _save_separate_networks_validation method in DQNAgent.
    """
    mean_score = round(np.mean(scores_temp).item())

    filename = os.path.join(
        default_root_dir, f"episode={num_episodes}_val-score={mean_score}.pt"
    )
    
    # Save the network state dict
    if dqn is not None:
        torch.save(dqn.state_dict(), filename)
    else:
        # Handle case where no network is provided (shouldn't happen)
        raise ValueError("No network provided for validation save")

    val_file_names.append(filename)

    for _ in range(validation_interval):
        scores["val"].append(scores_temp)

    scores_to_compare = []
    for fn in val_file_names:
        score = int(fn.split("val-score=")[-1].split(".pt")[0])
        scores_to_compare.append(score)

    indexes = list_duplicates_of(scores_to_compare, max(scores_to_compare))
    file_to_keep = val_file_names[indexes[-1]]

    for fn in val_file_names:
        if fn != file_to_keep:
            os.remove(fn)
            val_file_names.remove(fn)


def save_states_q_values_actions(
    states: list[list[list]],
    q_values: list[dict],
    actions: list[dict],
    default_root_dir: str,
    val_or_test: str,
    num_episodes: int | None = None,
) -> None:
    r"""Save states, q_values, and actions.

    Args:
        states: a list of states.
        q_values: a list of q_values.
        actions: a list of actions.
        default_root_dir: the root directory where the results are saved.
        val_or_test: "val" or "test"
        num_episodes: the current validation episode.

    """
    filename_template = (
        f"states_q_values_actions_val_episode={num_episodes}.yaml"
        if val_or_test.lower() == "val"
        else "states_q_values_actions_test.yaml"
    )

    filename = os.path.join(default_root_dir, filename_template)

    assert len(states) == len(q_values) == len(actions)
    to_save = [
        {
            "state": s,
            "q_values_forget": [
                [None if np.isnan(num_) else float(num_) for num_ in num]
                for num in q["forget"].tolist()
            ],
            "action_forget": [
                None if np.isnan(num) else int(num) for num in a["forget"].tolist()
            ],
            "q_values_remember": [
                [None if np.isnan(num_) else float(num_) for num_ in num]
                for num in q["remember"].tolist()
            ],
            "action_remember": [
                None if np.isnan(num) else int(num) for num in a["remember"].tolist()
            ],
        }
        for s, q, a in zip(states, q_values, actions)
    ]
    write_yaml(to_save, filename)


def target_hard_update(
    dqn: torch.nn.Module,
    dqn_target: torch.nn.Module,
) -> None:
    r"""Hard update: update target with local.

    Args:
        dqn: dqn model
        dqn_target: dqn target model
    """
    dqn_target.load_state_dict(dqn.state_dict())


def update_epsilon(
    epsilon: float, max_epsilon: float, min_epsilon: float, epsilon_decay_until: int
) -> float:
    r"""Linearly decrease epsilon

    Args:
        epsilon: current epsilon
        max_epsilon: initial epsilon
        min_epsilon: minimum epsilon
        epsilon_decay_until: the last iteration index to decay epsilon

    Returns:
        epsilon: updated epsilon

    """
    epsilon = max(
        min_epsilon, epsilon - (max_epsilon - min_epsilon) / epsilon_decay_until
    )

    return epsilon
