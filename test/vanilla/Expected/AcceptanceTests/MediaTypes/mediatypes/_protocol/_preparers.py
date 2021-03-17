# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import IO, Optional, Union

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


def prepare_analyze_body(
    body=None,  # type: Optional[Union[IO, "_models.SourcePath"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/mediatypes/analyze")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    if header_parameters["Content-Type"].split(";")[0] in ["application/pdf", "image/jpeg", "image/png", "image/tiff"]:
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["stream_content"] = body

    elif header_parameters["Content-Type"].split(";")[0] in ["application/json"]:
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs["content"] = body
    else:
        raise ValueError(
            "The content_type '{}' is not one of the allowed values: "
            "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(
                header_parameters["Content-Type"]
            )
        )

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)


def prepare_content_type_with_encoding(
    body=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "text/plain")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/mediatypes/contentTypeWithEncoding")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = body

    return _request("POST", url, query_parameters, header_parameters, **body_content_kwargs)
