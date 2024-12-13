from typing import Literal

import torch
import transformers


class Llm:
    """A class for the Llama3.1 model

    Attributes:
        model_id: The model ID to use.
        quantization: The quantization to use.
        quantization_config: The quantization config.
        pipeline: The pipeline.
        messages: The messages

    """

    def __init__(
        self,
        model_id: str = "meta-llama/Meta-Llama-3.1-8B-Instruct",
        quantization: Literal["16bit", "8bit", "4bit"] = "16bit",
        max_new_tokens: int = 256,
    ) -> None:
        """Init Llama class.

        Args:
            model_id: The model ID to use. Defaults to
            "meta-llama/Meta-Llama-3.1-8B-Instruct".
            quantization: The quantization to use. Defaults to "16bit".
            max_new_tokens: The maximum number of tokens to generate. Defaults to 256.

        """

        self.model_id = model_id
        self.quantization = quantization
        self.max_new_tokens = max_new_tokens

        if "16" in self.quantization:
            self.quantization_config = None
        elif "8" in self.quantization:
            self.quantization_config = {"load_in_8bit": True}
        elif "4" in self.quantization:
            self.quantization_config = {"load_in_4bit": True}

        self.load_model()
        self.messages = []

    def load_model(self) -> None:
        """Load the model."""
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_id,
            model_kwargs={
                "torch_dtype": torch.bfloat16,
                "quantization_config": self.quantization_config,
            },
            device_map="auto",
        )

    def reset(self) -> None:
        """Reset the conversation."""
        self.messages = []

    def add_system_instruction(self, propmt: str) -> None:
        """Add a system instruction to the model.

        Args:
            propmt: The instruction to add.

        """
        self.messages.append({"role": "system", "content": propmt})

    def talk_to_llm(self, message: str) -> str:
        """Write a user message to the model.

        Args:
            message: The message to write.
            max_new_tokens: The maximum number of tokens to generate. Defaults to 256.

        Returns:
            The generated message.

        """
        self.messages.append({"role": "user", "content": message})
        with torch.no_grad():
            outputs = self.pipeline(
                self.messages,
                max_new_tokens=self.max_new_tokens,
            )
        new_message = outputs[0]["generated_text"][-1]
        self.messages.append(new_message)

        return new_message["content"]
