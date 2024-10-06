from typing import Literal
from .base_preprocessor_config import BasePreprocessorConfig


class ShuffleConfig(BasePreprocessorConfig):
    type: Literal["shuffle"]
    buffer_size: int
    seed: int | None = None
    reshuffle_each_iteration: bool = True
