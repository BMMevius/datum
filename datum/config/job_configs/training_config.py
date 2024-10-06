from typing import Literal

from ..dataset_configs import DatasetConfig
from ..model_configs import ModelConfig
from .base_job_config import BaseJobConfig


class TrainingConfig(BaseJobConfig):
    type: Literal["training"]
    train_dataset: DatasetConfig
    validation_dataset: DatasetConfig
    test_dataset: DatasetConfig
    model: ModelConfig
