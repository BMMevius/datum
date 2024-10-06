from typing import Literal

from .base_preprocessor_config import BasePreprocessorConfig


class BatchConfig(BasePreprocessorConfig):
    type: Literal["batch"]
    batch_size: int
    drop_remainder: bool = False
    num_parallel_calls: int | None = None
    deterministic: bool = True
