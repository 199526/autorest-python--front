# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_test_one_request
    from ._request_builders_py3 import build_test_different_calls_request
except (SyntaxError, ImportError):
    from ._request_builders import build_test_one_request  # type: ignore
    from ._request_builders import build_test_different_calls_request  # type: ignore

__all__ = [
    'build_test_one_request',
    'build_test_different_calls_request',
]
