# coding: utf-8

"""
    SimScale API

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from simscale_sdk.configuration import Configuration


class TableDefinedProbeLocations(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'table_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'table_id': 'tableId'
    }

    def __init__(self, type='TABULAR', table_id=None, local_vars_configuration=None):  # noqa: E501
        """TableDefinedProbeLocations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._table_id = None
        self.discriminator = None

        self.type = type
        if table_id is not None:
            self.table_id = table_id

    @property
    def type(self):
        """Gets the type of this TableDefinedProbeLocations.  # noqa: E501


        :return: The type of this TableDefinedProbeLocations.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TableDefinedProbeLocations.


        :param type: The type of this TableDefinedProbeLocations.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def table_id(self):
        """Gets the table_id of this TableDefinedProbeLocations.  # noqa: E501

        The ID of the imported table.  # noqa: E501

        :return: The table_id of this TableDefinedProbeLocations.  # noqa: E501
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this TableDefinedProbeLocations.

        The ID of the imported table.  # noqa: E501

        :param table_id: The table_id of this TableDefinedProbeLocations.  # noqa: E501
        :type: str
        """

        self._table_id = table_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TableDefinedProbeLocations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TableDefinedProbeLocations):
            return True

        return self.to_dict() != other.to_dict()
