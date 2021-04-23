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


class PowerLawMedium(object):
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
        'name': 'str',
        'linear_coefficient': 'float',
        'exponent_coefficient': 'float',
        'orientation': 'OneOfPowerLawMediumOrientation',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'linear_coefficient': 'linearCoefficient',
        'exponent_coefficient': 'exponentCoefficient',
        'orientation': 'orientation',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids'
    }

    def __init__(self, type='POWER_LAW', name=None, linear_coefficient=None, exponent_coefficient=None, orientation=None, topological_reference=None, geometry_primitive_uuids=None, local_vars_configuration=None):  # noqa: E501
        """PowerLawMedium - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._linear_coefficient = None
        self._exponent_coefficient = None
        self._orientation = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if linear_coefficient is not None:
            self.linear_coefficient = linear_coefficient
        if exponent_coefficient is not None:
            self.exponent_coefficient = exponent_coefficient
        if orientation is not None:
            self.orientation = orientation
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def type(self):
        """Gets the type of this PowerLawMedium.  # noqa: E501

        Schema name: PowerLawMedium  # noqa: E501

        :return: The type of this PowerLawMedium.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PowerLawMedium.

        Schema name: PowerLawMedium  # noqa: E501

        :param type: The type of this PowerLawMedium.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this PowerLawMedium.  # noqa: E501


        :return: The name of this PowerLawMedium.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PowerLawMedium.


        :param name: The name of this PowerLawMedium.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def linear_coefficient(self):
        """Gets the linear_coefficient of this PowerLawMedium.  # noqa: E501


        :return: The linear_coefficient of this PowerLawMedium.  # noqa: E501
        :rtype: float
        """
        return self._linear_coefficient

    @linear_coefficient.setter
    def linear_coefficient(self, linear_coefficient):
        """Sets the linear_coefficient of this PowerLawMedium.


        :param linear_coefficient: The linear_coefficient of this PowerLawMedium.  # noqa: E501
        :type: float
        """

        self._linear_coefficient = linear_coefficient

    @property
    def exponent_coefficient(self):
        """Gets the exponent_coefficient of this PowerLawMedium.  # noqa: E501


        :return: The exponent_coefficient of this PowerLawMedium.  # noqa: E501
        :rtype: float
        """
        return self._exponent_coefficient

    @exponent_coefficient.setter
    def exponent_coefficient(self, exponent_coefficient):
        """Sets the exponent_coefficient of this PowerLawMedium.


        :param exponent_coefficient: The exponent_coefficient of this PowerLawMedium.  # noqa: E501
        :type: float
        """

        self._exponent_coefficient = exponent_coefficient

    @property
    def orientation(self):
        """Gets the orientation of this PowerLawMedium.  # noqa: E501


        :return: The orientation of this PowerLawMedium.  # noqa: E501
        :rtype: OneOfPowerLawMediumOrientation
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this PowerLawMedium.


        :param orientation: The orientation of this PowerLawMedium.  # noqa: E501
        :type: OneOfPowerLawMediumOrientation
        """

        self._orientation = orientation

    @property
    def topological_reference(self):
        """Gets the topological_reference of this PowerLawMedium.  # noqa: E501


        :return: The topological_reference of this PowerLawMedium.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this PowerLawMedium.


        :param topological_reference: The topological_reference of this PowerLawMedium.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this PowerLawMedium.  # noqa: E501


        :return: The geometry_primitive_uuids of this PowerLawMedium.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this PowerLawMedium.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this PowerLawMedium.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

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
        if not isinstance(other, PowerLawMedium):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PowerLawMedium):
            return True

        return self.to_dict() != other.to_dict()
