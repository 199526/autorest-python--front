﻿# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from async_generator import yield_, async_generator
from msrest.exceptions import ValidationError

from azurespecialpropertieslowlevel.aio import AutoRestAzureSpecialParametersTestClient
from azurespecialpropertieslowlevel.rest import (
    skip_url_encoding,
    subscription_in_credentials,
    subscription_in_method,
    api_version_default,
    api_version_local,
    odata,
)

import pytest

@pytest.fixture
def valid_subscription():
    return '1234-5678-9012-3456'

@pytest.fixture
@async_generator
async def client(valid_subscription, credential, authentication_policy):
    async with AutoRestAzureSpecialParametersTestClient(
        credential, valid_subscription, base_url="http://localhost:3000", authentication_policy=authentication_policy
    ) as client:
        await yield_(client)

@pytest.fixture
def body_parameter():
    return 1234

@pytest.fixture
def header_parameter():
    return 'header'

@pytest.fixture
def query_parameter():
    return 21

@pytest.fixture
def path_parameter():
    return 'path'


@pytest.fixture
def unencoded_path():
    return 'path1/path2/path3'

@pytest.fixture
def unencoded_query():
    return 'value1&q2=value2&q3=value3'

@pytest.fixture
def send_request(client, base_send_request):
    async def _send_request(request):
        return await base_send_request(client, request)
    return _send_request

@pytest.mark.asyncio
async def test_subscription_in_credentials(send_request, valid_subscription):
    # valid_api_version = '2.0'
    request = subscription_in_credentials.build_post_method_global_not_provided_valid_request(subscription_id=valid_subscription)
    await send_request(request)
    request = subscription_in_credentials.build_post_method_global_valid_request(subscription_id=valid_subscription)
    await send_request(request)
    request = subscription_in_credentials.build_post_path_global_valid_request(subscription_id=valid_subscription)
    await send_request(request)
    request = subscription_in_credentials.build_post_swagger_global_valid_request(subscription_id=valid_subscription)
    await send_request(request)

@pytest.mark.asyncio
async def test_subscription_in_method(send_request, valid_subscription):
    request = subscription_in_method.build_post_method_local_valid_request(valid_subscription)
    await send_request(request)
    request = subscription_in_method.build_post_path_local_valid_request(valid_subscription)
    await send_request(request)
    request = subscription_in_method.build_post_swagger_local_valid_request(valid_subscription)
    await send_request(request)
    with pytest.raises(ValidationError):
        request = subscription_in_method.build_post_method_local_null_request(None)

@pytest.mark.asyncio
async def test_api_version_default(send_request):
    request = api_version_default.build_get_method_global_not_provided_valid_request()
    await send_request(request)
    request = api_version_default.build_get_method_global_valid_request()
    await send_request(request)
    request = api_version_default.build_get_path_global_valid_request()
    await send_request(request)
    request = api_version_default.build_get_swagger_global_valid_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_api_version_local(send_request):
    request = api_version_local.build_get_method_local_valid_request()
    await send_request(request)
    request = api_version_local.build_get_method_local_null_request()
    await send_request(request)
    request = api_version_local.build_get_path_local_valid_request()
    await send_request(request)
    request = api_version_local.build_get_swagger_local_valid_request()
    await send_request(request)

@pytest.mark.asyncio
async def test_skip_url_encoding(send_request, unencoded_path, unencoded_query):
    request = skip_url_encoding.build_get_method_path_valid_request(unencoded_path)
    await send_request(request)
    request = skip_url_encoding.build_get_path_valid_request(unencoded_path)
    await send_request(request)
    request = skip_url_encoding.build_get_swagger_path_valid_request()
    await send_request(request)
    request = skip_url_encoding.build_get_method_query_valid_request(q1=unencoded_query)
    await send_request(request)
    request = skip_url_encoding.build_get_path_query_valid_request(q1=unencoded_query)
    await send_request(request)
    request = skip_url_encoding.build_get_swagger_query_valid_request()
    await send_request(request)
    request = skip_url_encoding.build_get_method_query_null_request()
    await send_request(request)
    request = skip_url_encoding.build_get_method_query_null_request(q1=None)
    await send_request(request)

@pytest.mark.asyncio
async def test_azure_odata(send_request):
    request = odata.build_get_with_filter_request(filter="id gt 5 and name eq 'foo'", top=10, orderby="id")
    await send_request(request)
