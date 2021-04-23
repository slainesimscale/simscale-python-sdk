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


class WindTunnelSizeCustom(object):
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
        'height_extension': 'DimensionalLength',
        'side_extension': 'DimensionalLength',
        'inflow_extension': 'DimensionalLength',
        'outflow_extension': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'height_extension': 'heightExtension',
        'side_extension': 'sideExtension',
        'inflow_extension': 'inflowExtension',
        'outflow_extension': 'outflowExtension'
    }

    def __init__(self, type='WIND_TUNNEL_SIZE_CUSTOM', height_extension=None, side_extension=None, inflow_extension=None, outflow_extension=None, local_vars_configuration=None):  # noqa: E501
        """WindTunnelSizeCustom - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._height_extension = None
        self._side_extension = None
        self._inflow_extension = None
        self._outflow_extension = None
        self.discriminator = None

        self.type = type
        if height_extension is not None:
            self.height_extension = height_extension
        if side_extension is not None:
            self.side_extension = side_extension
        if inflow_extension is not None:
            self.inflow_extension = inflow_extension
        if outflow_extension is not None:
            self.outflow_extension = outflow_extension

    @property
    def type(self):
        """Gets the type of this WindTunnelSizeCustom.  # noqa: E501

        Schema name: WindTunnelSizeCustom  # noqa: E501

        :return: The type of this WindTunnelSizeCustom.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WindTunnelSizeCustom.

        Schema name: WindTunnelSizeCustom  # noqa: E501

        :param type: The type of this WindTunnelSizeCustom.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def height_extension(self):
        """Gets the height_extension of this WindTunnelSizeCustom.  # noqa: E501


        :return: The height_extension of this WindTunnelSizeCustom.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._height_extension

    @height_extension.setter
    def height_extension(self, height_extension):
        """Sets the height_extension of this WindTunnelSizeCustom.


        :param height_extension: The height_extension of this WindTunnelSizeCustom.  # noqa: E501
        :type: DimensionalLength
        """

        self._height_extension = height_extension

    @property
    def side_extension(self):
        """Gets the side_extension of this WindTunnelSizeCustom.  # noqa: E501


        :return: The side_extension of this WindTunnelSizeCustom.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._side_extension

    @side_extension.setter
    def side_extension(self, side_extension):
        """Sets the side_extension of this WindTunnelSizeCustom.


        :param side_extension: The side_extension of this WindTunnelSizeCustom.  # noqa: E501
        :type: DimensionalLength
        """

        self._side_extension = side_extension

    @property
    def inflow_extension(self):
        """Gets the inflow_extension of this WindTunnelSizeCustom.  # noqa: E501


        :return: The inflow_extension of this WindTunnelSizeCustom.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._inflow_extension

    @inflow_extension.setter
    def inflow_extension(self, inflow_extension):
        """Sets the inflow_extension of this WindTunnelSizeCustom.


        :param inflow_extension: The inflow_extension of this WindTunnelSizeCustom.  # noqa: E501
        :type: DimensionalLength
        """

        self._inflow_extension = inflow_extension

    @property
    def outflow_extension(self):
        """Gets the outflow_extension of this WindTunnelSizeCustom.  # noqa: E501


        :return: The outflow_extension of this WindTunnelSizeCustom.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._outflow_extension

    @outflow_extension.setter
    def outflow_extension(self, outflow_extension):
        """Sets the outflow_extension of this WindTunnelSizeCustom.


        :param outflow_extension: The outflow_extension of this WindTunnelSizeCustom.  # noqa: E501
        :type: DimensionalLength
        """

        self._outflow_extension = outflow_extension

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
        if not isinstance(other, WindTunnelSizeCustom):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WindTunnelSizeCustom):
            return True

        return self.to_dict() != other.to_dict()
