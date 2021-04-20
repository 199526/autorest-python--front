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
    from typing import Any, IO, Optional, Union

_SERIALIZER = Serializer()


def build_test_paging_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Returns ModelThree with optionalProperty 'paged'.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/paging')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
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
    :keyword greeting_in_chinese: pass in 'nihao' to pass test.
    :paramtype greeting_in_chinese: str
    :keyword greeting_in_french: pass in 'bonjour' to pass test.
    :paramtype greeting_in_french: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    greeting_in_english = kwargs.pop('greeting_in_english')  # type: str
    greeting_in_chinese = kwargs.pop('greeting_in_chinese', None)  # type: Optional[str]
    greeting_in_french = kwargs.pop('greeting_in_french', None)  # type: Optional[str]
    api_version = "3.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if greeting_in_french is not None:
        header_parameters['greetingInFrench'] = _SERIALIZER.header("greeting_in_french", greeting_in_french, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')
    if greeting_in_chinese is not None:
        header_parameters['greetingInChinese'] = _SERIALIZER.header("greeting_in_chinese", greeting_in_chinese, 'str')
    header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

