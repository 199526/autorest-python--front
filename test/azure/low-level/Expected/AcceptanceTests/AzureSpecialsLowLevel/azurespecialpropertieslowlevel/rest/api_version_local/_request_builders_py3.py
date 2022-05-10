# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._serialization import Serializer

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_get_method_local_valid_request(
    **kwargs: Any
) -> HttpRequest:
    """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: This should appear as a method parameter, use value '2.0'. Default value
     is "2.0". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2.0"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/azurespecials/apiVersion/method/string/none/query/local/2.0"

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_method_local_null_request(
    *,
    api_version: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Get method with api-version modeled in the method.  pass in api-version = null to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: This should appear as a method parameter, use value null, this should
     result in no serialized parameter. Default value is None.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/azurespecials/apiVersion/method/string/none/query/local/null"

    # Construct parameters
    if api_version is not None:
        _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_path_local_valid_request(
    **kwargs: Any
) -> HttpRequest:
    """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: This should appear as a method parameter, use value '2.0'. Default value
     is "2.0". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2.0"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/azurespecials/apiVersion/path/string/none/query/local/2.0"

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_swagger_local_valid_request(
    **kwargs: Any
) -> HttpRequest:
    """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: The api version, which appears in the query, the value is always '2.0'.
     Default value is "2.0". Note that overriding this default value may result in unsupported
     behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2.0"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/azurespecials/apiVersion/swagger/string/none/query/local/2.0"

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
