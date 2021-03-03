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


class AdvectiveVBC(object):
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
        'relax_boundary': 'bool',
        'far_field_value': 'DimensionalVectorSpeed',
        'relaxation_length_scale': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'relax_boundary': 'relaxBoundary',
        'far_field_value': 'farFieldValue',
        'relaxation_length_scale': 'relaxationLengthScale'
    }

    def __init__(self, type='ADVECTIVE', relax_boundary=None, far_field_value=None, relaxation_length_scale=None, local_vars_configuration=None):  # noqa: E501
        """AdvectiveVBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._relax_boundary = None
        self._far_field_value = None
        self._relaxation_length_scale = None
        self.discriminator = None

        self.type = type
        if relax_boundary is not None:
            self.relax_boundary = relax_boundary
        if far_field_value is not None:
            self.far_field_value = far_field_value
        if relaxation_length_scale is not None:
            self.relaxation_length_scale = relaxation_length_scale

    @property
    def type(self):
        """Gets the type of this AdvectiveVBC.  # noqa: E501


        :return: The type of this AdvectiveVBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AdvectiveVBC.


        :param type: The type of this AdvectiveVBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def relax_boundary(self):
        """Gets the relax_boundary of this AdvectiveVBC.  # noqa: E501


        :return: The relax_boundary of this AdvectiveVBC.  # noqa: E501
        :rtype: bool
        """
        return self._relax_boundary

    @relax_boundary.setter
    def relax_boundary(self, relax_boundary):
        """Sets the relax_boundary of this AdvectiveVBC.


        :param relax_boundary: The relax_boundary of this AdvectiveVBC.  # noqa: E501
        :type: bool
        """

        self._relax_boundary = relax_boundary

    @property
    def far_field_value(self):
        """Gets the far_field_value of this AdvectiveVBC.  # noqa: E501


        :return: The far_field_value of this AdvectiveVBC.  # noqa: E501
        :rtype: DimensionalVectorSpeed
        """
        return self._far_field_value

    @far_field_value.setter
    def far_field_value(self, far_field_value):
        """Sets the far_field_value of this AdvectiveVBC.


        :param far_field_value: The far_field_value of this AdvectiveVBC.  # noqa: E501
        :type: DimensionalVectorSpeed
        """

        self._far_field_value = far_field_value

    @property
    def relaxation_length_scale(self):
        """Gets the relaxation_length_scale of this AdvectiveVBC.  # noqa: E501


        :return: The relaxation_length_scale of this AdvectiveVBC.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._relaxation_length_scale

    @relaxation_length_scale.setter
    def relaxation_length_scale(self, relaxation_length_scale):
        """Sets the relaxation_length_scale of this AdvectiveVBC.


        :param relaxation_length_scale: The relaxation_length_scale of this AdvectiveVBC.  # noqa: E501
        :type: DimensionalLength
        """

        self._relaxation_length_scale = relaxation_length_scale

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
        if not isinstance(other, AdvectiveVBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdvectiveVBC):
            return True

        return self.to_dict() != other.to_dict()
