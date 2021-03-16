# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Optional, Union

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


def prepare_header_param_existing_key_request(user_agent_parameter: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/existingkey")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["User-Agent"] = _SERIALIZER.header("user_agent_parameter", user_agent_parameter, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_existing_key_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/existingkey")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_protected_key_request(content_type: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/protectedkey")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_protected_key_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/protectedkey")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_integer_request(scenario: str, value: int, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/integer")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_integer_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/integer")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_long_request(scenario: str, value: int, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/long")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "long")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_long_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/long")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_float_request(scenario: str, value: float, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/float")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "float")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_float_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/float")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_double_request(scenario: str, value: float, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/double")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "float")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_double_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/double")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_bool_request(scenario: str, value: bool, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/bool")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "bool")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_bool_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/bool")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_string_request(scenario: str, value: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/string")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    if value is not None:
        header_parameters["value"] = _SERIALIZER.header("value", value, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_string_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/string")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_date_request(scenario: str, value: datetime.date, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/date")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "date")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_date_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/date")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_datetime_request(scenario: str, value: datetime.datetime, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/datetime")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "iso-8601")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_datetime_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/datetime")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_datetime_rfc1123_request(
    scenario: str, value: Optional[datetime.datetime] = None, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/datetimerfc1123")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    if value is not None:
        header_parameters["value"] = _SERIALIZER.header("value", value, "rfc-1123")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_datetime_rfc1123_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/datetimerfc1123")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_duration_request(scenario: str, value: datetime.timedelta, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/duration")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "duration")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_duration_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/duration")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_byte_request(scenario: str, value: bytearray, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/byte")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["value"] = _SERIALIZER.header("value", value, "bytearray")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_byte_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/byte")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_param_enum_request(
    scenario: str, value: Optional[Union[str, "_models.GreyscaleColors"]] = None, **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/param/prim/enum")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    if value is not None:
        header_parameters["value"] = _SERIALIZER.header("value", value, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_response_enum_request(scenario: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/response/prim/enum")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["scenario"] = _SERIALIZER.header("scenario", scenario, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)


def prepare_header_custom_request_id_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/header/custom/x-ms-client-request-id/9C4D50EE-2D56-4CD3-8152-34347DC9F2B0")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return _request("POST", url, query_parameters, header_parameters)
