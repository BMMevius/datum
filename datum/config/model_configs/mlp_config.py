from typing import Literal

from .base_model_config import BaseModelConfig


class MlpConfig(BaseModelConfig):
    type: Literal["multi-layer perceptron", "mlp"]
