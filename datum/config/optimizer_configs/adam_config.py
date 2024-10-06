from typing import Literal
from .base_optimizer_config import BaseOptimizerConfig


class AdamConfig(BaseOptimizerConfig):
    type: Literal["adam"]
    learning_rate: float = 0.001
    beta_1: float = 0.9
    beta_2: float = 0.999
    epsilon: float = 1e-07
    amsgrad: bool = False
