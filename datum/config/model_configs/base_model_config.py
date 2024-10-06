from typing import Iterable

from pydantic import Field

from ..base_config import BaseConfig
from ..loss_configs import LossConfig
from ..metric_configs import MetricConfig
from ..optimizer_configs import OptimizerConfig


class BaseModelConfig(BaseConfig):
    loss: LossConfig
    optimizer: OptimizerConfig
    training_metrics: Iterable[MetricConfig] = Field(default_factory=list)
    validation_metrics: Iterable[MetricConfig] = Field(default_factory=list)
    test_metrics: Iterable[MetricConfig] = Field(default_factory=list)
    load_path: str | None = None
