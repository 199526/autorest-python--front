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

def build_head300_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 300 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/300"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get300_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 300 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/300"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_head301_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 301 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/301"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get301_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 301 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/301"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put301_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put true Boolean value in request returns 301.  This request should not be automatically
    redirected, but should return the received 301 to the caller for evaluation.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Simple boolean value true. Known values are True and None. Default value is
     True.
    :paramtype json: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/301"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_head302_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 302 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/302"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get302_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Return 302 status code and redirect to /http/success/200.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/302"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_patch302_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Patch true Boolean value in request returns 302.  This request should not be automatically
    redirected, but should return the received 302 to the caller for evaluation.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Simple boolean value true. Known values are True and None. Default value is
     True.
    :paramtype json: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/302"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_post303_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Post true Boolean value in request returns 303.  This request should be automatically
    redirected usign a get, ultimately returning a 200 status code.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Simple boolean value true. Known values are True and None. Default value is
     True.
    :paramtype json: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/303"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_head307_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Redirect with 307, resulting in a 200 success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get307_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Redirect get with 307, resulting in a 200 success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_options307_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """options redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="OPTIONS",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put307_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Simple boolean value true. Known values are True and None. Default value is
     True.
    :paramtype json: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_patch307_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Patch redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Simple boolean value true. Known values are True and None. Default value is
     True.
    :paramtype json: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_post307_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Post redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Simple boolean value true. Known values are True and None. Default value is
     True.
    :paramtype json: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_delete307_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Delete redirected with 307, resulting in a 200 after redirect.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Simple boolean value true. Known values are True and None. Default value is
     True.
    :paramtype json: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/http/redirect/307"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_headers,
        **kwargs
    )
