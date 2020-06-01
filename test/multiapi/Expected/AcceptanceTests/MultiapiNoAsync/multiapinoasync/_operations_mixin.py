# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
from msrest import Serializer, Deserializer
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    from azure.core import PipelineClient
    from msrest import Deserializer, Serializer

    from .._configuration import MultiapiServiceClientConfiguration


class MultiapiServiceClientOperationsMixin(object):

    def begin_test_lro(
        self,
        product=None,  # type: Optional["models.Product"]
        **kwargs  # type: Any
    ):
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put.
        :type product: ~multiapinoasync.v1.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product, or the result of cls(response)
        :rtype: ~multiapinoasync.v1.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('begin_test_lro')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_test_lro(product, **kwargs)

    def test_one(
        self,
        id,  # type: int
        message=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        """TestOne should be in an SecondVersionOperationsMixin. Returns ModelTwo.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo, or the result of cls(response)
        :rtype: ~multiapinoasync.v2.models.ModelTwo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('test_one')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from .v2.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_one(id, message, **kwargs)

    def test_paging(
        self,
        **kwargs  # type: Any
    ):
        """Returns ModelThree with optionalProperty 'paged'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PagingResult, or the result of cls(response)
        :rtype: ~multiapinoasync.v3.models.PagingResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('test_paging')
        if api_version == '3.0.0':
            from .v3.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_paging(**kwargs)
