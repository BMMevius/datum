from typing import Literal

from ..base_config import BaseConfig


class BaseLossConfig(BaseConfig):
    reduction: Literal["none", "mean", "sum"] = "mean"
