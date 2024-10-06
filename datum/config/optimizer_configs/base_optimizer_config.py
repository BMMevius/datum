from ..base_config import BaseConfig


class BaseOptimizerConfig(BaseConfig):
    learning_rate: float
    weight_decay: float | None = None
    clipnorm: float | None = None
    clipvalue: float | None = None
    global_clipnorm: float | None = None
    use_ema: bool = False
    ema_momentum: float = 0.99
    ema_overwrite_frequency: int | None = None
    loss_scale_factor: float | None = None
    gradient_accumulation_steps: int | None = None
