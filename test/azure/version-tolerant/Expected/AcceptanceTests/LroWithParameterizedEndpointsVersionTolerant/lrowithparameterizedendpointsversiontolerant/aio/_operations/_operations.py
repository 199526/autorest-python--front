# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from json import loads as _loads
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ..._operations._operations import (
    build_poll_with_constant_parameterized_endpoints_request_initial,
    build_poll_with_parameterized_endpoints_request_initial,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class LROWithParamaterizedEndpointsOperationsMixin:
    async def _poll_with_parameterized_endpoints_initial(self, account_name: str, **kwargs: Any) -> Optional[str]:
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[str]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_poll_with_parameterized_endpoints_request_initial()
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    @distributed_trace_async
    async def begin_poll_with_parameterized_endpoints(self, account_name: str, **kwargs: Any) -> AsyncLROPoller[str]:
        """Poll with method and client level parameters in endpoint.

        :param account_name: Account Name. Pass in 'local' to pass test.
        :type account_name: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns str
        :rtype: ~azure.core.polling.AsyncLROPoller[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._poll_with_parameterized_endpoints_initial(
                account_name=account_name, cls=lambda x, y, z: x, **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = AsyncLROBasePolling(
                lro_delay,
                lro_options={"final-state-via": "location"},
                path_format_arguments=path_format_arguments,
                **kwargs
            )
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_poll_with_parameterized_endpoints.metadata = {"url": "/lroParameterizedEndpoints"}  # type: ignore

    async def _poll_with_constant_parameterized_endpoints_initial(
        self, account_name: str, **kwargs: Any
    ) -> Optional[str]:
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[str]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        constant_parameter = kwargs.pop("constant_parameter", "iAmConstant")  # type: str

        request = build_poll_with_constant_parameterized_endpoints_request_initial(
            constant_parameter=constant_parameter,
        )
        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    @distributed_trace_async
    async def begin_poll_with_constant_parameterized_endpoints(
        self, account_name: str, **kwargs: Any
    ) -> AsyncLROPoller[str]:
        """Poll with method and client level parameters in endpoint, with a constant value.

        :param account_name: Account Name. Pass in 'local' to pass test.
        :type account_name: str
        :keyword constant_parameter: Next link for the list operation. The default value is
         "iAmConstant". Note that overriding this default value may result in unsupported behavior.
        :paramtype constant_parameter: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns str
        :rtype: ~azure.core.polling.AsyncLROPoller[str]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        constant_parameter = kwargs.pop("constant_parameter", "iAmConstant")  # type: str
        polling = kwargs.pop("polling", True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._poll_with_constant_parameterized_endpoints_initial(
                account_name=account_name, constant_parameter=constant_parameter, cls=lambda x, y, z: x, **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_poll_with_constant_parameterized_endpoints.metadata = {"url": "/lroConstantParameterizedEndpoints/{constantParameter}"}  # type: ignore
