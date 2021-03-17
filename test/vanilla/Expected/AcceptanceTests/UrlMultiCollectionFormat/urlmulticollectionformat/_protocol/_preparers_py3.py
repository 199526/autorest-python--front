# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import List, Optional

from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()

import xml.etree.ElementTree as ET


def _request(
    method,
    url,
    params=None,
    headers=None,
    content=None,
    form_content=None,
    stream_content=None,
):
    request = HttpRequest(method, url, headers=headers)

    if params:
        request.format_parameters(params)

    if content is not None:
        content_type = request.headers.get("Content-Type")
        if isinstance(content, ET.Element):
            request.set_xml_body(content)
        # https://github.com/Azure/azure-sdk-for-python/issues/12137
        # A string is valid JSON, make the difference between text
        # and a plain JSON string.
        # Content-Type is a good indicator of intent from user
        elif content_type and content_type.startswith("text/"):
            request.set_text_body(content)
        else:
            try:
                request.set_json_body(content)
            except TypeError:
                request.data = content

    if form_content:
        request.set_formdata_body(form_content)
    elif stream_content:
        request.set_streamed_data_body(stream_content)

    return request


def prepare_queries_array_string_multi_null(array_query: Optional[List[str]] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/queries/array/multi/string/null")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if array_query is not None:
        query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_queries_array_string_multi_empty(array_query: Optional[List[str]] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/queries/array/multi/string/empty")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if array_query is not None:
        query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)


def prepare_queries_array_string_multi_valid(array_query: Optional[List[str]] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/queries/array/multi/string/valid")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if array_query is not None:
        query_parameters["arrayQuery"] = [
            _SERIALIZER.query("array_query", q, "str") if q is not None else "" for q in array_query
        ]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("GET", url, query_parameters, header_parameters)
