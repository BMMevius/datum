from typing import Iterable

from pydantic import Field

from ..base_config import BaseConfig
from ..preprocessor_configs import PreprocessorConfig


class BaseDatasetConfig(BaseConfig):
    preprocessors: Iterable[PreprocessorConfig] = Field(default_factory=list)
