from typing import Literal

from jaxtyping import PyTree

Row = dict[str, PyTree]
StrDTypes = Literal[
    "float16",
    "float32",
    "float64",
    "int8",
    "int16",
    "int32",
    "int64",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "string",
    "complex64",
    "complex128",
]
