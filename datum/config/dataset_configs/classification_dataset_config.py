from typing import Literal
from .base_dataset_config import BaseDatasetConfig


class ClassificationDatasetConfig(BaseDatasetConfig):
    type: Literal["classification dataset"]
