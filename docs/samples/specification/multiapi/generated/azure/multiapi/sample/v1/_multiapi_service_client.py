# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import MultiapiServiceClientConfiguration
from .operations import MultiapiServiceClientOperationsMixin, OperationGroupOneOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest, HttpResponse

class MultiapiServiceClient(MultiapiServiceClientOperationsMixin):
    """Service client for multiapi client testing.
    
    :ivar operation_group_one: OperationGroupOneOperations operations
    :vartype operation_group_one: azure.multiapi.sample.v1.operations.OperationGroupOneOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param base_url: Service URL
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = MultiapiServiceClientConfiguration(credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operation_group_one = OperationGroupOneOperations(self._client, self._config, self._serialize, self._deserialize)


    def send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.multiapi.sample.v1.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from azure.multiapi.sample.v1.rest import build_test_one_request
        >>> request = build_test_one_request(id=id, message=message, **kwargs)
        <HttpRequest [PUT], url: '/multiapi/testOneEndpoint'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MultiapiServiceClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
