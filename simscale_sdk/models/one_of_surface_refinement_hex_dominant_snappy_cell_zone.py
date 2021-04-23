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


class OneOfSurfaceRefinementHexDominantSnappyCellZone(object):
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
        'name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name'
    }

    discriminator_value_class_map = {
        'WITHOUT_CELL_ZONE': 'WithoutCellZone',
        'WITH_CELL_ZONE_V11': 'WithCellZone'
    }

    def __init__(self, type='WITH_CELL_ZONE_V11', name=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSurfaceRefinementHexDominantSnappyCellZone - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name

    @property
    def type(self):
        """Gets the type of this OneOfSurfaceRefinementHexDominantSnappyCellZone.  # noqa: E501

        Schema name: WithCellZone  # noqa: E501

        :return: The type of this OneOfSurfaceRefinementHexDominantSnappyCellZone.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSurfaceRefinementHexDominantSnappyCellZone.

        Schema name: WithCellZone  # noqa: E501

        :param type: The type of this OneOfSurfaceRefinementHexDominantSnappyCellZone.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfSurfaceRefinementHexDominantSnappyCellZone.  # noqa: E501


        :return: The name of this OneOfSurfaceRefinementHexDominantSnappyCellZone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfSurfaceRefinementHexDominantSnappyCellZone.


        :param name: The name of this OneOfSurfaceRefinementHexDominantSnappyCellZone.  # noqa: E501
        :type: str
        """

        self._name = name

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, OneOfSurfaceRefinementHexDominantSnappyCellZone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSurfaceRefinementHexDominantSnappyCellZone):
            return True

        return self.to_dict() != other.to_dict()
