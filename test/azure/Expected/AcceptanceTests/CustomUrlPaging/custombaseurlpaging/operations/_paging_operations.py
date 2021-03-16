# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._protocol import *

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class PagingOperations(object):
    """PagingOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~custombaseurlpaging.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_pages_partial_url(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ProductResult"]
        """A paging operation that combines custom url, paging and partial URL and expect to concat after
        host.

        :param account_name: Account Name.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~custombaseurlpaging.models.ProductResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ProductResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:
                request = prepare_paging_get_pages_partial_url_request(
                    template_url=self.get_pages_partial_url.metadata["url"], **kwargs
                )
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)
                kwargs.pop("content_type", None)
            else:
                request = prepare_paging_get_pages_partial_url_request(
                    template_url=self.get_pages_partial_url.metadata["url"], **kwargs
                )
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)
                kwargs.pop("content_type", None)
                # little hacky, but this code will soon be replaced with code that won't need the hack
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.method = "get"
                request.url = self._client.format_url(next_link, **path_format_arguments)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ProductResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    get_pages_partial_url.metadata = {"url": "/paging/customurl/partialnextlink"}  # type: ignore

    @distributed_trace
    def get_pages_partial_url_operation(
        self,
        account_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.ProductResult"]
        """A paging operation that combines custom url, paging and partial URL with next operation.

        :param account_name: Account Name.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProductResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~custombaseurlpaging.models.ProductResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ProductResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:
                request = prepare_paging_get_pages_partial_url_operation_request(
                    template_url=self.get_pages_partial_url_operation.metadata["url"], **kwargs
                )
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)
                kwargs.pop("content_type", None)
            else:
                request = _get_pages_partial_url_operation_next_request(
                    next_link=next_link, template_url="/paging/customurl/{nextLink}", **kwargs
                )
                path_format_arguments = {
                    "accountName": self._serialize.url("account_name", account_name, "str", skip_quote=True),
                    "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)
                kwargs.pop("content_type", None)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ProductResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    get_pages_partial_url_operation.metadata = {"url": "/paging/customurl/partialnextlinkop"}  # type: ignore
