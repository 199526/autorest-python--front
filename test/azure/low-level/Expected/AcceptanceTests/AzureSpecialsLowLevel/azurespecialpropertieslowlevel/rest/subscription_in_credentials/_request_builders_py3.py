# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_post_method_global_valid_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
    '1234-5678-9012-3456' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your
    code flow.

    :param subscription_id: The subscription id, which appears in the path, always modeled in
     credentials. The value is always '1234-5678-9012-3456'.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/method/string/none/path/global/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)


def build_post_method_global_null_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
    null, and client-side validation should prevent you from making this call.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your
    code flow.

    :param subscription_id: The subscription id, which appears in the path, always modeled in
     credentials. The value is always '1234-5678-9012-3456'.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop(
        "template_url", "/azurespecials/subscriptionId/method/string/none/path/global/null/{subscriptionId}"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)


def build_post_method_global_not_provided_valid_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
    '1234-5678-9012-3456' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your
    code flow.

    :param subscription_id: The subscription id, which appears in the path, always modeled in
     credentials. The value is always '1234-5678-9012-3456'.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = "2015-07-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/method/string/none/path/globalNotProvided/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_post_path_global_valid_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
    '1234-5678-9012-3456' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your
    code flow.

    :param subscription_id: The subscription id, which appears in the path, always modeled in
     credentials. The value is always '1234-5678-9012-3456'.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/path/string/none/path/global/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)


def build_post_swagger_global_valid_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
    '1234-5678-9012-3456' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your
    code flow.

    :param subscription_id: The subscription id, which appears in the path, always modeled in
     credentials. The value is always '1234-5678-9012-3456'.
    :type subscription_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/swagger/string/none/path/global/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, **kwargs)
