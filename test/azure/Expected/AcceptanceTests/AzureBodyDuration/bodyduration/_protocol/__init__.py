# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_duration_get_null
    from ._preparers_py3 import prepare_duration_put_positive_duration
    from ._preparers_py3 import prepare_duration_get_positive_duration
    from ._preparers_py3 import prepare_duration_get_invalid
except (SyntaxError, ImportError):
    from ._preparers import prepare_duration_get_null  # type: ignore
    from ._preparers import prepare_duration_put_positive_duration  # type: ignore
    from ._preparers import prepare_duration_get_positive_duration  # type: ignore
    from ._preparers import prepare_duration_get_invalid  # type: ignore

__all__ = [
    "prepare_duration_get_null",
    "prepare_duration_put_positive_duration",
    "prepare_duration_get_positive_duration",
    "prepare_duration_get_invalid",
]
