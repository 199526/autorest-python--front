# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, List, Optional, Union

_SERIALIZER = Serializer()


def build_get_all_with_values_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery='globalStringQuery',
    pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value 'localStringQuery'.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    path_item_string_query = kwargs.pop("path_item_string_query", None)  # type: Optional[str]
    global_string_query = kwargs.pop("global_string_query", None)  # type: Optional[str]
    local_string_query = kwargs.pop("local_string_query", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery",
    )
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if path_item_string_query is not None:
        query_parameters["pathItemStringQuery"] = _SERIALIZER.query(
            "path_item_string_query", path_item_string_query, "str"
        )
    if global_string_query is not None:
        query_parameters["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        query_parameters["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_global_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery=null,
    pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value 'localStringQuery'.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    path_item_string_query = kwargs.pop("path_item_string_query", None)  # type: Optional[str]
    global_string_query = kwargs.pop("global_string_query", None)  # type: Optional[str]
    local_string_query = kwargs.pop("local_string_query", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery",
    )
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if path_item_string_query is not None:
        query_parameters["pathItemStringQuery"] = _SERIALIZER.query(
            "path_item_string_query", path_item_string_query, "str"
        )
    if global_string_query is not None:
        query_parameters["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        query_parameters["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_global_and_local_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """send globalStringPath=globalStringPath, pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery=null,
    pathItemStringQuery='pathItemStringQuery', localStringQuery=null.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain null value.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    path_item_string_query = kwargs.pop("path_item_string_query", None)  # type: Optional[str]
    global_string_query = kwargs.pop("global_string_query", None)  # type: Optional[str]
    local_string_query = kwargs.pop("local_string_query", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null",
    )
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if path_item_string_query is not None:
        query_parameters["pathItemStringQuery"] = _SERIALIZER.query(
            "path_item_string_query", path_item_string_query, "str"
        )
    if global_string_query is not None:
        query_parameters["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        query_parameters["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_local_path_item_query_null_request(
    path_item_string_path,  # type: str
    global_string_path,  # type: str
    local_string_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery='globalStringQuery',
    pathItemStringQuery=null, localStringQuery=null.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: should contain value null.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value null.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    path_item_string_query = kwargs.pop("path_item_string_query", None)  # type: Optional[str]
    global_string_query = kwargs.pop("global_string_query", None)  # type: Optional[str]
    local_string_query = kwargs.pop("local_string_query", None)  # type: Optional[str]

    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null",
    )
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if path_item_string_query is not None:
        query_parameters["pathItemStringQuery"] = _SERIALIZER.query(
            "path_item_string_query", path_item_string_query, "str"
        )
    if global_string_query is not None:
        query_parameters["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        query_parameters["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)
