# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import _rest, models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class LROsCustomHeaderOperations(object):
    """LROsCustomHeaderOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~lro.models
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

    def _put_async_retry_succeeded_initial(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Product"
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        if product is not None:
            content = self._serialize.body(product, "Product")
            content = json.dumps(content)
        else:
            content = None

        request = _rest.lr_os_custom_header.build_put_async_retry_succeeded_request_initial(
            content=content,
            content_type=content_type,
            template_url=self._put_async_retry_succeeded_initial.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Azure-AsyncOperation"] = self._deserialize(
            "str", response.headers.get("Azure-AsyncOperation")
        )
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _put_async_retry_succeeded_initial.metadata = {"url": "/lro/customheader/putasync/retry/succeeded"}  # type: ignore

    @distributed_trace
    def begin_put_async_retry_succeeded(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.Product"]
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running put request, service returns a 200 to the initial request, with an
        entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the Azure-
        AsyncOperation header for operation status.

        :param product: Product to put.
        :type product: ~lro.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the ARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either Product or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~lro.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._put_async_retry_succeeded_initial(product=product, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

            deserialized = self._deserialize("Product", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        if polling is True:
            polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_put_async_retry_succeeded.metadata = {"url": "/lro/customheader/putasync/retry/succeeded"}  # type: ignore

    def _put201_creating_succeeded200_initial(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Product"
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        if product is not None:
            content = self._serialize.body(product, "Product")
            content = json.dumps(content)
        else:
            content = None

        request = _rest.lr_os_custom_header.build_put201_creating_succeeded200_request_initial(
            content=content,
            content_type=content_type,
            template_url=self._put201_creating_succeeded200_initial.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("Product", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("Product", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _put201_creating_succeeded200_initial.metadata = {"url": "/lro/customheader/put/201/creating/succeeded/200"}  # type: ignore

    @distributed_trace
    def begin_put201_creating_succeeded200(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.Product"]
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running put request, service returns a 201 to the initial request, with an
        entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
        returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param product: Product to put.
        :type product: ~lro.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the ARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either Product or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~lro.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Product"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._put201_creating_succeeded200_initial(product=product, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Product", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_put201_creating_succeeded200.metadata = {"url": "/lro/customheader/put/201/creating/succeeded/200"}  # type: ignore

    def _post202_retry200_initial(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        if product is not None:
            content = self._serialize.body(product, "Product")
            content = json.dumps(content)
        else:
            content = None

        request = _rest.lr_os_custom_header.build_post202_retry200_request_initial(
            content=content,
            content_type=content_type,
            template_url=self._post202_retry200_initial.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    _post202_retry200_initial.metadata = {"url": "/lro/customheader/post/202/retry/200"}  # type: ignore

    @distributed_trace
    def begin_post202_retry200(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running post request, service returns a 202 to the initial request, with
        'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

        :param product: Product to put.
        :type product: ~lro.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the ARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._post202_retry200_initial(product=product, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_post202_retry200.metadata = {"url": "/lro/customheader/post/202/retry/200"}  # type: ignore

    def _post_async_retry_succeeded_initial(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        if product is not None:
            content = self._serialize.body(product, "Product")
            content = json.dumps(content)
        else:
            content = None

        request = _rest.lr_os_custom_header.build_post_async_retry_succeeded_request_initial(
            content=content,
            content_type=content_type,
            template_url=self._post_async_retry_succeeded_initial.metadata["url"],
            **kwargs
        )
        request.url = self._client.format_url(request.url)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Azure-AsyncOperation"] = self._deserialize(
            "str", response.headers.get("Azure-AsyncOperation")
        )
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    _post_async_retry_succeeded_initial.metadata = {"url": "/lro/customheader/postasync/retry/succeeded"}  # type: ignore

    @distributed_trace
    def begin_post_async_retry_succeeded(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
        all requests. Long running post request, service returns a 202 to the initial request, with an
        entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the Azure-
        AsyncOperation header for operation status.

        :param product: Product to put.
        :type product: ~lro.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the ARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._post_async_retry_succeeded_initial(product=product, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_post_async_retry_succeeded.metadata = {"url": "/lro/customheader/postasync/retry/succeeded"}  # type: ignore
