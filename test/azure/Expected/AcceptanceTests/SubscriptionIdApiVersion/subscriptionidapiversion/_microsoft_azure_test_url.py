# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core.rest import HttpResponse, _StreamContextManager
from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest

from ._configuration import MicrosoftAzureTestUrlConfiguration
from .operations import GroupOperations
from . import models


class MicrosoftAzureTestUrl(object):
    """Some cool documentation.

    :ivar group: GroupOperations operations
    :vartype group: subscriptionidapiversion.operations.GroupOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param base_url: Service URL
    :type base_url: str
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = MicrosoftAzureTestUrlConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self.group = GroupOperations(self._client, self._config, self._serialize, self._deserialize)
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `subscriptionidapiversion.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from subscriptionidapiversion.rest import build_get_sample_resource_group_request
        >>> request = build_get_sample_resource_group_request(subscription_id, resource_group_name)
        <HttpRequest [GET], url: '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/llcwiki

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """
        request_copy = deepcopy(http_request)
        request_copy.url = self._client.format_url(request_copy.url)
        if kwargs.pop("stream_response", False):
            return _StreamContextManager(
                client=self._client,
                request=request_copy,
            )
        pipeline_response = self._client._pipeline.run(request_copy._internal_request, **kwargs)
        response = HttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response,
        )
        response.read()
        return response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MicrosoftAzureTestUrl
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
