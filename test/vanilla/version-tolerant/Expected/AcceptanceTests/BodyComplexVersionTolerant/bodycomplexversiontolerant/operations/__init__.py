# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import BasicOperations
from ._operations import PrimitiveOperations
from ._operations import ArrayOperations
from ._operations import DictionaryOperations
from ._operations import InheritanceOperations
from ._operations import PolymorphismOperations
from ._operations import PolymorphicrecursiveOperations
from ._operations import ReadonlypropertyOperations
from ._operations import FlattencomplexOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BasicOperations",
    "PrimitiveOperations",
    "ArrayOperations",
    "DictionaryOperations",
    "InheritanceOperations",
    "PolymorphismOperations",
    "PolymorphicrecursiveOperations",
    "ReadonlypropertyOperations",
    "FlattencomplexOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
