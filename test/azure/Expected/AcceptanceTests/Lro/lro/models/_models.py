# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class OperationResult(msrest.serialization.Model):
    """OperationResult.

    :param status: The status of the request. Possible values include: "Succeeded", "Failed",
     "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
     "OK".
    :type status: str or ~lro.models.OperationResultStatus
    :param error:
    :type error: ~lro.models.OperationResultError
    """

    _attribute_map = {
        "status": {"key": "status", "type": "str"},
        "error": {"key": "error", "type": "OperationResultError"},
    }

    def __init__(self, **kwargs):
        super(OperationResult, self).__init__(**kwargs)
        self.status = kwargs.get("status", None)
        self.error = kwargs.get("error", None)


class OperationResultError(msrest.serialization.Model):
    """OperationResultError.

    :param code: The error code for an operation failure.
    :type code: int
    :param message: The detailed arror message.
    :type message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(OperationResultError, self).__init__(**kwargs)
        self.code = kwargs.get("code", None)
        self.message = kwargs.get("message", None)


class Resource(msrest.serialization.Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar type: Resource Type.
    :vartype type: str
    :param tags: A set of tags. Dictionary of :code:`<string>`.
    :type tags: dict[str, str]
    :param location: Resource Location.
    :type location: str
    :ivar name: Resource Name.
    :vartype name: str
    """

    _validation = {
        "id": {"readonly": True},
        "type": {"readonly": True},
        "name": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.tags = kwargs.get("tags", None)
        self.location = kwargs.get("location", None)
        self.name = None


class Product(Resource):
    """Product.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar type: Resource Type.
    :vartype type: str
    :param tags: A set of tags. Dictionary of :code:`<string>`.
    :type tags: dict[str, str]
    :param location: Resource Location.
    :type location: str
    :ivar name: Resource Name.
    :vartype name: str
    :param provisioning_state:
    :type provisioning_state: str
    :ivar provisioning_state_values:  Possible values include: "Succeeded", "Failed", "canceled",
     "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
    :vartype provisioning_state_values: str or ~lro.models.ProductPropertiesProvisioningStateValues
    """

    _validation = {
        "id": {"readonly": True},
        "type": {"readonly": True},
        "name": {"readonly": True},
        "provisioning_state_values": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "provisioning_state_values": {"key": "properties.provisioningStateValues", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get("provisioning_state", None)
        self.provisioning_state_values = None


class Sku(msrest.serialization.Model):
    """Sku.

    :param name:
    :type name: str
    :param id:
    :type id: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs.get("name", None)
        self.id = kwargs.get("id", None)


class SubResource(msrest.serialization.Model):
    """SubResource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Sub Resource Id.
    :vartype id: str
    """

    _validation = {
        "id": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SubResource, self).__init__(**kwargs)
        self.id = None


class SubProduct(SubResource):
    """SubProduct.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Sub Resource Id.
    :vartype id: str
    :param provisioning_state:
    :type provisioning_state: str
    :ivar provisioning_state_values:  Possible values include: "Succeeded", "Failed", "canceled",
     "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
    :vartype provisioning_state_values: str or
     ~lro.models.SubProductPropertiesProvisioningStateValues
    """

    _validation = {
        "id": {"readonly": True},
        "provisioning_state_values": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "provisioning_state_values": {"key": "properties.provisioningStateValues", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SubProduct, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get("provisioning_state", None)
        self.provisioning_state_values = None
