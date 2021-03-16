# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import _prepare_xmsclientrequestid_get_request
    from ._preparers_py3 import _prepare_xmsclientrequestid_param_get_request
    from ._preparers_py3 import _prepare_subscriptionincredentials_post_method_global_valid_request
    from ._preparers_py3 import _prepare_subscriptionincredentials_post_method_global_null_request
    from ._preparers_py3 import _prepare_subscriptionincredentials_post_method_global_not_provided_valid_request
    from ._preparers_py3 import _prepare_subscriptionincredentials_post_path_global_valid_request
    from ._preparers_py3 import _prepare_subscriptionincredentials_post_swagger_global_valid_request
    from ._preparers_py3 import _prepare_subscriptioninmethod_post_method_local_valid_request
    from ._preparers_py3 import _prepare_subscriptioninmethod_post_method_local_null_request
    from ._preparers_py3 import _prepare_subscriptioninmethod_post_path_local_valid_request
    from ._preparers_py3 import _prepare_subscriptioninmethod_post_swagger_local_valid_request
    from ._preparers_py3 import _prepare_apiversiondefault_get_method_global_valid_request
    from ._preparers_py3 import _prepare_apiversiondefault_get_method_global_not_provided_valid_request
    from ._preparers_py3 import _prepare_apiversiondefault_get_path_global_valid_request
    from ._preparers_py3 import _prepare_apiversiondefault_get_swagger_global_valid_request
    from ._preparers_py3 import _prepare_apiversionlocal_get_method_local_valid_request
    from ._preparers_py3 import _prepare_apiversionlocal_get_method_local_null_request
    from ._preparers_py3 import _prepare_apiversionlocal_get_path_local_valid_request
    from ._preparers_py3 import _prepare_apiversionlocal_get_swagger_local_valid_request
    from ._preparers_py3 import _prepare_skipurlencoding_get_method_path_valid_request
    from ._preparers_py3 import _prepare_skipurlencoding_get_path_valid_request
    from ._preparers_py3 import _prepare_skipurlencoding_get_swagger_path_valid_request
    from ._preparers_py3 import _prepare_skipurlencoding_get_method_query_valid_request
    from ._preparers_py3 import _prepare_skipurlencoding_get_method_query_null_request
    from ._preparers_py3 import _prepare_skipurlencoding_get_path_query_valid_request
    from ._preparers_py3 import _prepare_skipurlencoding_get_swagger_query_valid_request
    from ._preparers_py3 import _prepare_odata_get_with_filter_request
    from ._preparers_py3 import _prepare_header_custom_named_request_id_request
    from ._preparers_py3 import _prepare_header_custom_named_request_id_param_grouping_request
    from ._preparers_py3 import _prepare_header_custom_named_request_id_head_request
except (SyntaxError, ImportError):
    from ._preparers import _prepare_xmsclientrequestid_get_request  # type: ignore
    from ._preparers import _prepare_xmsclientrequestid_param_get_request  # type: ignore
    from ._preparers import _prepare_subscriptionincredentials_post_method_global_valid_request  # type: ignore
    from ._preparers import _prepare_subscriptionincredentials_post_method_global_null_request  # type: ignore
    from ._preparers import _prepare_subscriptionincredentials_post_method_global_not_provided_valid_request  # type: ignore
    from ._preparers import _prepare_subscriptionincredentials_post_path_global_valid_request  # type: ignore
    from ._preparers import _prepare_subscriptionincredentials_post_swagger_global_valid_request  # type: ignore
    from ._preparers import _prepare_subscriptioninmethod_post_method_local_valid_request  # type: ignore
    from ._preparers import _prepare_subscriptioninmethod_post_method_local_null_request  # type: ignore
    from ._preparers import _prepare_subscriptioninmethod_post_path_local_valid_request  # type: ignore
    from ._preparers import _prepare_subscriptioninmethod_post_swagger_local_valid_request  # type: ignore
    from ._preparers import _prepare_apiversiondefault_get_method_global_valid_request  # type: ignore
    from ._preparers import _prepare_apiversiondefault_get_method_global_not_provided_valid_request  # type: ignore
    from ._preparers import _prepare_apiversiondefault_get_path_global_valid_request  # type: ignore
    from ._preparers import _prepare_apiversiondefault_get_swagger_global_valid_request  # type: ignore
    from ._preparers import _prepare_apiversionlocal_get_method_local_valid_request  # type: ignore
    from ._preparers import _prepare_apiversionlocal_get_method_local_null_request  # type: ignore
    from ._preparers import _prepare_apiversionlocal_get_path_local_valid_request  # type: ignore
    from ._preparers import _prepare_apiversionlocal_get_swagger_local_valid_request  # type: ignore
    from ._preparers import _prepare_skipurlencoding_get_method_path_valid_request  # type: ignore
    from ._preparers import _prepare_skipurlencoding_get_path_valid_request  # type: ignore
    from ._preparers import _prepare_skipurlencoding_get_swagger_path_valid_request  # type: ignore
    from ._preparers import _prepare_skipurlencoding_get_method_query_valid_request  # type: ignore
    from ._preparers import _prepare_skipurlencoding_get_method_query_null_request  # type: ignore
    from ._preparers import _prepare_skipurlencoding_get_path_query_valid_request  # type: ignore
    from ._preparers import _prepare_skipurlencoding_get_swagger_query_valid_request  # type: ignore
    from ._preparers import _prepare_odata_get_with_filter_request  # type: ignore
    from ._preparers import _prepare_header_custom_named_request_id_request  # type: ignore
    from ._preparers import _prepare_header_custom_named_request_id_param_grouping_request  # type: ignore
    from ._preparers import _prepare_header_custom_named_request_id_head_request  # type: ignore

__all__ = [
    "_prepare_xmsclientrequestid_get_request",
    "_prepare_xmsclientrequestid_param_get_request",
    "_prepare_subscriptionincredentials_post_method_global_valid_request",
    "_prepare_subscriptionincredentials_post_method_global_null_request",
    "_prepare_subscriptionincredentials_post_method_global_not_provided_valid_request",
    "_prepare_subscriptionincredentials_post_path_global_valid_request",
    "_prepare_subscriptionincredentials_post_swagger_global_valid_request",
    "_prepare_subscriptioninmethod_post_method_local_valid_request",
    "_prepare_subscriptioninmethod_post_method_local_null_request",
    "_prepare_subscriptioninmethod_post_path_local_valid_request",
    "_prepare_subscriptioninmethod_post_swagger_local_valid_request",
    "_prepare_apiversiondefault_get_method_global_valid_request",
    "_prepare_apiversiondefault_get_method_global_not_provided_valid_request",
    "_prepare_apiversiondefault_get_path_global_valid_request",
    "_prepare_apiversiondefault_get_swagger_global_valid_request",
    "_prepare_apiversionlocal_get_method_local_valid_request",
    "_prepare_apiversionlocal_get_method_local_null_request",
    "_prepare_apiversionlocal_get_path_local_valid_request",
    "_prepare_apiversionlocal_get_swagger_local_valid_request",
    "_prepare_skipurlencoding_get_method_path_valid_request",
    "_prepare_skipurlencoding_get_path_valid_request",
    "_prepare_skipurlencoding_get_swagger_path_valid_request",
    "_prepare_skipurlencoding_get_method_query_valid_request",
    "_prepare_skipurlencoding_get_method_query_null_request",
    "_prepare_skipurlencoding_get_path_query_valid_request",
    "_prepare_skipurlencoding_get_swagger_query_valid_request",
    "_prepare_odata_get_with_filter_request",
    "_prepare_header_custom_named_request_id_request",
    "_prepare_header_custom_named_request_id_param_grouping_request",
    "_prepare_header_custom_named_request_id_head_request",
]
