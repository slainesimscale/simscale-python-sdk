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


class OneOfConstAnIsoTransportOrientation(object):
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
        'unit_vector1': 'DimensionalVectorLength',
        'unit_vector2': 'DimensionalVectorLength'
    }

    attribute_map = {
        'type': 'type',
        'unit_vector1': 'unitVector1',
        'unit_vector2': 'unitVector2'
    }

    discriminator_value_class_map = {
        'CARTESIAN': 'CartesianOrientation',
        'CUSTOM': 'CustomOrientation'
    }

    def __init__(self, type='CUSTOM', unit_vector1=None, unit_vector2=None, local_vars_configuration=None):  # noqa: E501
        """OneOfConstAnIsoTransportOrientation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._unit_vector1 = None
        self._unit_vector2 = None
        self.discriminator = 'type'

        self.type = type
        if unit_vector1 is not None:
            self.unit_vector1 = unit_vector1
        if unit_vector2 is not None:
            self.unit_vector2 = unit_vector2

    @property
    def type(self):
        """Gets the type of this OneOfConstAnIsoTransportOrientation.  # noqa: E501

        Schema name: CustomOrientation  # noqa: E501

        :return: The type of this OneOfConstAnIsoTransportOrientation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfConstAnIsoTransportOrientation.

        Schema name: CustomOrientation  # noqa: E501

        :param type: The type of this OneOfConstAnIsoTransportOrientation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def unit_vector1(self):
        """Gets the unit_vector1 of this OneOfConstAnIsoTransportOrientation.  # noqa: E501


        :return: The unit_vector1 of this OneOfConstAnIsoTransportOrientation.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._unit_vector1

    @unit_vector1.setter
    def unit_vector1(self, unit_vector1):
        """Sets the unit_vector1 of this OneOfConstAnIsoTransportOrientation.


        :param unit_vector1: The unit_vector1 of this OneOfConstAnIsoTransportOrientation.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._unit_vector1 = unit_vector1

    @property
    def unit_vector2(self):
        """Gets the unit_vector2 of this OneOfConstAnIsoTransportOrientation.  # noqa: E501


        :return: The unit_vector2 of this OneOfConstAnIsoTransportOrientation.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._unit_vector2

    @unit_vector2.setter
    def unit_vector2(self, unit_vector2):
        """Sets the unit_vector2 of this OneOfConstAnIsoTransportOrientation.


        :param unit_vector2: The unit_vector2 of this OneOfConstAnIsoTransportOrientation.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._unit_vector2 = unit_vector2

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
        if not isinstance(other, OneOfConstAnIsoTransportOrientation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfConstAnIsoTransportOrientation):
            return True

        return self.to_dict() != other.to_dict()
