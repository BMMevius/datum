from typing import Literal

from .base_loss_config import BaseLossConfig


class SparseCategoricalCrossentropyConfig(BaseLossConfig):
    type: Literal["sparse categorical crossentropy"]
    from_logits: bool = False
