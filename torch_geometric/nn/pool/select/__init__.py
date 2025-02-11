r"""Node-selection package.

This package provides classes for node selection methods in graph pooling
scenarios.
"""

from .base import Select, SelectOutput
from .sag import SelectSAG
from .topk import SelectTopK

__all__ = [
    'Select',
    'SelectOutput',
    'SelectTopK',
    'SelectSAG',
]
