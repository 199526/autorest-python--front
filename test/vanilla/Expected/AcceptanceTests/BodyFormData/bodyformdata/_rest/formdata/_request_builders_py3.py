# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, IO, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_upload_file_request(
    *, files: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Upload file.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword files: Multipart input for files. See the template in our example to find the input
     shape.
    :paramtype files: dict[str, Any]
    :keyword content: Multipart input for files. See the template in our example to find the input
     shape.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # multipart input template you can fill out and use as your `files` input.
            files = {
                "file_content": "IO. File to upload.",
                "file_name": "str. File name to upload. Name has to be spelled exactly as written here."
            }
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfile")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, files=files, content=content, **kwargs)


def build_upload_file_via_body_request(*, content: IO, **kwargs: Any) -> HttpRequest:
    """Upload file.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword content: File to upload.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfile")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, content=content, **kwargs)


def build_upload_files_request(
    *, files: Optional[Dict[str, Any]] = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    """Upload multiple files.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword files: Multipart input for files. See the template in our example to find the input
     shape.
    :paramtype files: dict[str, Any]
    :keyword content: Multipart input for files. See the template in our example to find the input
     shape.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # multipart input template you can fill out and use as your `files` input.
            files = {
                "file_content": [
                    "IO. Files to upload."
                ]
            }
    """
    content_type = kwargs.pop("content_type", None)
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfiles")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, files=files, content=content, **kwargs)
