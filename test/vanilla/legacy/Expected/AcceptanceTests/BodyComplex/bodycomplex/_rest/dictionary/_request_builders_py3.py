# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Dict, List, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_get_valid_request(**kwargs: Any) -> HttpRequest:
    """Get complex types with dictionary property.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "defaultProgram": {
                    "str": "str (optional)"
                }
            }
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/complex/dictionary/typed/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_valid_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put complex types with dictionary property.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put a dictionary with 5 key-value pairs:
     "txt":"notepad", "bmp":"mspaint", "xls":"excel", "exe":"", "":null.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put a dictionary with 5 key-value pairs:
     "txt":"notepad", "bmp":"mspaint", "xls":"excel", "exe":"", "":null.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "defaultProgram": {
                    "str": "str (optional)"
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/complex/dictionary/typed/valid")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_get_empty_request(**kwargs: Any) -> HttpRequest:
    """Get complex types with dictionary property which is empty.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "defaultProgram": {
                    "str": "str (optional)"
                }
            }
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/complex/dictionary/typed/empty")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_empty_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Put complex types with dictionary property which is empty.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put an empty dictionary.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put an empty dictionary.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "defaultProgram": {
                    "str": "str (optional)"
                }
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/complex/dictionary/typed/empty")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_get_null_request(**kwargs: Any) -> HttpRequest:
    """Get complex types with dictionary property which is null.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "defaultProgram": {
                    "str": "str (optional)"
                }
            }
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/complex/dictionary/typed/null")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_get_not_provided_request(**kwargs: Any) -> HttpRequest:
    """Get complex types with dictionary property while server doesn't provide a response payload.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "defaultProgram": {
                    "str": "str (optional)"
                }
            }
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/complex/dictionary/typed/notprovided")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)
