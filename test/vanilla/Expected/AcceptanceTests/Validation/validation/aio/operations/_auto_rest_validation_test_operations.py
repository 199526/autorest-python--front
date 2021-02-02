# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestValidationTestOperationsMixin:
    def _validation_of_method_parameters_request(self, resource_group_name: str, id: int, **kwargs: Any) -> HttpRequest:
        api_version = "1.0.0"
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._validation_of_method_parameters_request.metadata["url"])  # type: ignore
        path_format_arguments = {
            "subscriptionId": self._serialize.url("self._config.subscription_id", self._config.subscription_id, "str"),
            "resourceGroupName": self._serialize.url(
                "resource_group_name",
                resource_group_name,
                "str",
                max_length=10,
                min_length=3,
                pattern=r"[a-zA-Z0-9\']+",
            ),
            "id": self._serialize.url("id", id, "int", maximum=1000, minimum=100, multiple=10),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters["apiVersion"] = self._serialize.query("api_version", api_version, "str")

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _validation_of_method_parameters_request.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}  # type: ignore

    @distributed_trace_async
    async def validation_of_method_parameters(
        self, resource_group_name: str, id: int, **kwargs: Any
    ) -> "_models.Product":
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product, or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._validation_of_method_parameters_request(
            resource_group_name=resource_group_name, id=id, **kwargs
        )
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validation_of_method_parameters.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}  # type: ignore

    def _validation_of_body_request(
        self, resource_group_name: str, id: int, body: Optional["_models.Product"] = None, **kwargs: Any
    ) -> HttpRequest:
        api_version = "1.0.0"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._validation_of_body_request.metadata["url"])  # type: ignore
        path_format_arguments = {
            "subscriptionId": self._serialize.url("self._config.subscription_id", self._config.subscription_id, "str"),
            "resourceGroupName": self._serialize.url(
                "resource_group_name", resource_group_name, "str", max_length=10, min_length=3, pattern=r"[a-zA-Z0-9]+"
            ),
            "id": self._serialize.url("id", id, "int", maximum=1000, minimum=100, multiple=10),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters["apiVersion"] = self._serialize.query("api_version", api_version, "str")

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "Product")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _validation_of_body_request.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}  # type: ignore

    @distributed_trace_async
    async def validation_of_body(
        self, resource_group_name: str, id: int, body: Optional["_models.Product"] = None, **kwargs: Any
    ) -> "_models.Product":
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param body:
        :type body: ~validation.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product, or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _body = body
        request = self._validation_of_body_request(resource_group_name=resource_group_name, id=id, body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validation_of_body.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}  # type: ignore

    def _get_with_constant_in_path_request(self, **kwargs: Any) -> HttpRequest:
        constant_param = "constant"

        # Construct URL
        url = kwargs.pop("template_url", self._get_with_constant_in_path_request.metadata["url"])  # type: ignore
        path_format_arguments = {
            "constantParam": self._serialize.url("constant_param", constant_param, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        return self._client.get(url, query_parameters, header_parameters)

    _get_with_constant_in_path_request.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}  # type: ignore

    @distributed_trace_async
    async def get_with_constant_in_path(self, **kwargs: Any) -> None:
        """get_with_constant_in_path.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_with_constant_in_path_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    get_with_constant_in_path.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}  # type: ignore

    def _post_with_constant_in_body_request(
        self, body: Optional["_models.Product"] = None, **kwargs: Any
    ) -> HttpRequest:
        constant_param = "constant"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = kwargs.pop("template_url", self._post_with_constant_in_body_request.metadata["url"])  # type: ignore
        path_format_arguments = {
            "constantParam": self._serialize.url("constant_param", constant_param, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "Product")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

    _post_with_constant_in_body_request.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}  # type: ignore

    @distributed_trace_async
    async def post_with_constant_in_body(
        self, body: Optional["_models.Product"] = None, **kwargs: Any
    ) -> "_models.Product":
        """post_with_constant_in_body.

        :param body:
        :type body: ~validation.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product, or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _body = body
        request = self._post_with_constant_in_body_request(body=_body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_with_constant_in_body.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}  # type: ignore
