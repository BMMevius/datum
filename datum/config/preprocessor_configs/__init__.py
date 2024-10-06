from .batch_config import BatchConfig
from .shuffle_config import ShuffleConfig

PreprocessorConfig = BatchConfig | ShuffleConfig
