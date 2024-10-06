from abc import ABC

from pydantic import BaseModel


class BaseObject(BaseModel, ABC):
    name: str
