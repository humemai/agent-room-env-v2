"""A simple MLP with dueling DQN support."""

import torch
from torch.nn.init import xavier_normal_


class MLP(torch.nn.Module):
    """Multi-layer perceptron with ReLU activation functions.

    Attributes:
        input_size: Input size of the linear layer.
        hidden_size: Hidden size of the linear layer.
        num_hidden_layers: Number of layers in the MLP.
        n_actions: Number of actions.
        device: "cpu" or "cuda".
        dueling_dqn: Whether to use dueling DQN.

    """

    def __init__(
        self,
        n_actions: int,
        input_size: int,
        hidden_size: int,
        device: str,
        num_hidden_layers: int = 1,
        dueling_dqn: bool = True,
    ) -> None:
        """Initialize the MLP.

        Args:
            n_actions: Number of actions.
            input_size: Input size of the linear layer.
            hidden_size: Hidden size of the linear layer.
            device: "cpu" or "cuda".
            num_hidden_layers: int, number of layers in the MLP.
            dueling_dqn: Whether to use dueling DQN.

        """
        super(MLP, self).__init__()
        self.device = device
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.n_actions = n_actions
        self.dueling_dqn = dueling_dqn

        # Define the layers for the advantage stream
        advantage_layers = []
        advantage_layers.append(
            torch.nn.Linear(self.input_size, self.hidden_size, device=self.device)
        )
        advantage_layers.append(torch.nn.ReLU())
        for _ in range(self.num_hidden_layers - 1):
            advantage_layers.append(
                torch.nn.Linear(self.hidden_size, self.hidden_size, device=self.device)
            )
            advantage_layers.append(torch.nn.ReLU())
        advantage_layers.append(
            torch.nn.Linear(self.hidden_size, self.n_actions, device=self.device)
        )
        self.advantage_layer = torch.nn.Sequential(*advantage_layers)

        if self.dueling_dqn:
            # Define the layers for the value stream
            value_layers = []
            value_layers.append(
                torch.nn.Linear(self.input_size, self.hidden_size, device=self.device)
            )
            value_layers.append(torch.nn.ReLU())
            for _ in range(self.num_hidden_layers - 1):
                value_layers.append(
                    torch.nn.Linear(
                        self.hidden_size, self.hidden_size, device=self.device
                    )
                )
                value_layers.append(torch.nn.ReLU())
            value_layers.append(
                torch.nn.Linear(self.hidden_size, 1, device=self.device)
            )
            self.value_layer = torch.nn.Sequential(*value_layers)

        # Apply Xavier initialization to all layers
        self._apply_xavier_initialization()

    def _apply_xavier_initialization(self):
        """Applies Xavier Normal initialization to all linear layers."""
        for m in self.modules():
            if isinstance(m, torch.nn.Linear):
                xavier_normal_(m.weight)
                if m.bias is not None:
                    m.bias.data.zero_()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass of the neural network.

        Args:
            x: Input tensor. The shape is (batch_size, lstm_hidden_size).
        Returns:
            torch.Tensor: Output tensor. The shape is (batch_size, n_actions).

        """

        if self.dueling_dqn:
            value = self.value_layer(x)
            advantage = self.advantage_layer(x)
            q = value + advantage - advantage.mean(dim=-1, keepdim=True)
        else:
            q = self.advantage_layer(x)

        return q
