from typing import Literal
from .base_metric_config import BaseMetricConfig


class LossMetricConfig(BaseMetricConfig):
    type: Literal["loss metric"]
