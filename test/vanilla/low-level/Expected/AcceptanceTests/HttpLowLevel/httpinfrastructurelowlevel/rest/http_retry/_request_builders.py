# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()


def build_head408_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 408 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/408")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="HEAD", url=url, headers=header_parameters, **kwargs)


def build_put500_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 500 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/500")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_patch500_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 500 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/500")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=url, headers=header_parameters, **kwargs)


def build_get502_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 502 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/502")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_options502_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 502 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/502")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="OPTIONS", url=url, headers=header_parameters, **kwargs)


def build_post503_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 503 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/503")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)


def build_delete503_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 503 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/503")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=url, headers=header_parameters, **kwargs)


def build_put504_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 504 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/504")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_patch504_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 504 status code, then 200 after retry.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Simple boolean value true.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Simple boolean value true.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "bool (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/http/retry/504")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=url, headers=header_parameters, **kwargs)
