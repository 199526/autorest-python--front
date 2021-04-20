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


def build_test_one_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """TestOne should be in an FirstVersionOperationsMixin.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword id: An int parameter.
    :paramtype id: int
    :keyword message: An optional string parameter.
    :paramtype message: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    id = kwargs.pop('id')  # type: int
    message = kwargs.pop('message', None)  # type: Optional[str]
    api_version = "1.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testOneEndpoint')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['id'] = _SERIALIZER.query("id", id, 'int')
    if message is not None:
        query_parameters['message'] = _SERIALIZER.query("message", message, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_test_lro_request_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put in whatever shape of Product you want, will return a Product with id equal to 100.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: Product to put.
    :paramtype json: Any
    :keyword content: Product to put.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "id": "int (optional)"
            }
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/lro')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_test_lro_and_paging_request_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A long-running paging operation that includes a nextLink that has 10 pages.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword client_request_id:
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    client_request_id = kwargs.pop('client_request_id', None)  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', None)  # type: Optional[int]
    timeout = kwargs.pop('timeout', 30)  # type: Optional[int]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/lroAndPaging')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')
    if timeout is not None:
        header_parameters['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    if maxresults is not None:
        header_parameters['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_test_different_calls_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Has added parameters across the API versions.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword greeting_in_english: pass in 'hello' to pass test.
    :paramtype greeting_in_english: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    greeting_in_english = kwargs.pop('greeting_in_english')  # type: str
    api_version = "1.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

