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


class NoSlipVBC(object):
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
        'turbulence_wall': 'str',
        'surface_roughness': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'turbulence_wall': 'turbulenceWall',
        'surface_roughness': 'surfaceRoughness'
    }

    def __init__(self, type='NO_SLIP', turbulence_wall=None, surface_roughness=None, local_vars_configuration=None):  # noqa: E501
        """NoSlipVBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._turbulence_wall = None
        self._surface_roughness = None
        self.discriminator = None

        self.type = type
        if turbulence_wall is not None:
            self.turbulence_wall = turbulence_wall
        if surface_roughness is not None:
            self.surface_roughness = surface_roughness

    @property
    def type(self):
        """Gets the type of this NoSlipVBC.  # noqa: E501

        Schema name: NoSlipVBC  # noqa: E501

        :return: The type of this NoSlipVBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NoSlipVBC.

        Schema name: NoSlipVBC  # noqa: E501

        :param type: The type of this NoSlipVBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def turbulence_wall(self):
        """Gets the turbulence_wall of this NoSlipVBC.  # noqa: E501


        :return: The turbulence_wall of this NoSlipVBC.  # noqa: E501
        :rtype: str
        """
        return self._turbulence_wall

    @turbulence_wall.setter
    def turbulence_wall(self, turbulence_wall):
        """Sets the turbulence_wall of this NoSlipVBC.


        :param turbulence_wall: The turbulence_wall of this NoSlipVBC.  # noqa: E501
        :type: str
        """
        allowed_values = ["WALL_FUNCTION", "FULL_RESOLUTION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and turbulence_wall not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `turbulence_wall` ({0}), must be one of {1}"  # noqa: E501
                .format(turbulence_wall, allowed_values)
            )

        self._turbulence_wall = turbulence_wall

    @property
    def surface_roughness(self):
        """Gets the surface_roughness of this NoSlipVBC.  # noqa: E501


        :return: The surface_roughness of this NoSlipVBC.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._surface_roughness

    @surface_roughness.setter
    def surface_roughness(self, surface_roughness):
        """Sets the surface_roughness of this NoSlipVBC.


        :param surface_roughness: The surface_roughness of this NoSlipVBC.  # noqa: E501
        :type: DimensionalLength
        """

        self._surface_roughness = surface_roughness

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
        if not isinstance(other, NoSlipVBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NoSlipVBC):
            return True

        return self.to_dict() != other.to_dict()
