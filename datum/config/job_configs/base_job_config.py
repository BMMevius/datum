from typing import Literal

from ..base_config import BaseConfig


class BaseJobConfig(BaseConfig):
    backend: Literal["tensorflow", "torch"]
