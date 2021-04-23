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


class SutherlandTransport(object):
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
        'reference_viscosity': 'DimensionalDynamicViscosity',
        'reference_temperature': 'DimensionalTemperature',
        'ts': 'DimensionalTemperature',
        'thermo': 'OneOfSutherlandTransportThermo'
    }

    attribute_map = {
        'type': 'type',
        'reference_viscosity': 'referenceViscosity',
        'reference_temperature': 'referenceTemperature',
        'ts': 'ts',
        'thermo': 'thermo'
    }

    def __init__(self, type='SUTHERLAND', reference_viscosity=None, reference_temperature=None, ts=None, thermo=None, local_vars_configuration=None):  # noqa: E501
        """SutherlandTransport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._reference_viscosity = None
        self._reference_temperature = None
        self._ts = None
        self._thermo = None
        self.discriminator = None

        self.type = type
        if reference_viscosity is not None:
            self.reference_viscosity = reference_viscosity
        if reference_temperature is not None:
            self.reference_temperature = reference_temperature
        if ts is not None:
            self.ts = ts
        if thermo is not None:
            self.thermo = thermo

    @property
    def type(self):
        """Gets the type of this SutherlandTransport.  # noqa: E501

        Schema name: SutherlandTransport  # noqa: E501

        :return: The type of this SutherlandTransport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SutherlandTransport.

        Schema name: SutherlandTransport  # noqa: E501

        :param type: The type of this SutherlandTransport.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def reference_viscosity(self):
        """Gets the reference_viscosity of this SutherlandTransport.  # noqa: E501


        :return: The reference_viscosity of this SutherlandTransport.  # noqa: E501
        :rtype: DimensionalDynamicViscosity
        """
        return self._reference_viscosity

    @reference_viscosity.setter
    def reference_viscosity(self, reference_viscosity):
        """Sets the reference_viscosity of this SutherlandTransport.


        :param reference_viscosity: The reference_viscosity of this SutherlandTransport.  # noqa: E501
        :type: DimensionalDynamicViscosity
        """

        self._reference_viscosity = reference_viscosity

    @property
    def reference_temperature(self):
        """Gets the reference_temperature of this SutherlandTransport.  # noqa: E501


        :return: The reference_temperature of this SutherlandTransport.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._reference_temperature

    @reference_temperature.setter
    def reference_temperature(self, reference_temperature):
        """Sets the reference_temperature of this SutherlandTransport.


        :param reference_temperature: The reference_temperature of this SutherlandTransport.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._reference_temperature = reference_temperature

    @property
    def ts(self):
        """Gets the ts of this SutherlandTransport.  # noqa: E501


        :return: The ts of this SutherlandTransport.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this SutherlandTransport.


        :param ts: The ts of this SutherlandTransport.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._ts = ts

    @property
    def thermo(self):
        """Gets the thermo of this SutherlandTransport.  # noqa: E501


        :return: The thermo of this SutherlandTransport.  # noqa: E501
        :rtype: OneOfSutherlandTransportThermo
        """
        return self._thermo

    @thermo.setter
    def thermo(self, thermo):
        """Sets the thermo of this SutherlandTransport.


        :param thermo: The thermo of this SutherlandTransport.  # noqa: E501
        :type: OneOfSutherlandTransportThermo
        """

        self._thermo = thermo

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
        if not isinstance(other, SutherlandTransport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SutherlandTransport):
            return True

        return self.to_dict() != other.to_dict()
