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


class OneOfDerivedHeatFluxWallThermal(object):
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
        'contact_resistance': 'DimensionalContactResistance',
        'contact_conductance': 'DimensionalThermalTransmittance',
        'conductivity_thickness_pairs': 'list[ConductivityThicknessPair]'
    }

    attribute_map = {
        'type': 'type',
        'contact_resistance': 'contactResistance',
        'contact_conductance': 'contactConductance',
        'conductivity_thickness_pairs': 'conductivityThicknessPairs'
    }

    discriminator_value_class_map = {
        'NO_RESISTANCE': 'NoWallThermal',
        'TOTAL_RESISTANCE': 'TotalResistanceWallThermal',
        'SPECIFIC_CONDUCTANCE': 'SpecificConductanceWallThermal',
        'CONTACT_INTERFACE_MATERIAL': 'LayerWallThermal'
    }

    def __init__(self, type='CONTACT_INTERFACE_MATERIAL', contact_resistance=None, contact_conductance=None, conductivity_thickness_pairs=None, local_vars_configuration=None):  # noqa: E501
        """OneOfDerivedHeatFluxWallThermal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._contact_resistance = None
        self._contact_conductance = None
        self._conductivity_thickness_pairs = None
        self.discriminator = 'type'

        self.type = type
        if contact_resistance is not None:
            self.contact_resistance = contact_resistance
        if contact_conductance is not None:
            self.contact_conductance = contact_conductance
        if conductivity_thickness_pairs is not None:
            self.conductivity_thickness_pairs = conductivity_thickness_pairs

    @property
    def type(self):
        """Gets the type of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501

        Schema name: LayerWallThermal  # noqa: E501

        :return: The type of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfDerivedHeatFluxWallThermal.

        Schema name: LayerWallThermal  # noqa: E501

        :param type: The type of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def contact_resistance(self):
        """Gets the contact_resistance of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501


        :return: The contact_resistance of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501
        :rtype: DimensionalContactResistance
        """
        return self._contact_resistance

    @contact_resistance.setter
    def contact_resistance(self, contact_resistance):
        """Sets the contact_resistance of this OneOfDerivedHeatFluxWallThermal.


        :param contact_resistance: The contact_resistance of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501
        :type: DimensionalContactResistance
        """

        self._contact_resistance = contact_resistance

    @property
    def contact_conductance(self):
        """Gets the contact_conductance of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501


        :return: The contact_conductance of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501
        :rtype: DimensionalThermalTransmittance
        """
        return self._contact_conductance

    @contact_conductance.setter
    def contact_conductance(self, contact_conductance):
        """Sets the contact_conductance of this OneOfDerivedHeatFluxWallThermal.


        :param contact_conductance: The contact_conductance of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501
        :type: DimensionalThermalTransmittance
        """

        self._contact_conductance = contact_conductance

    @property
    def conductivity_thickness_pairs(self):
        """Gets the conductivity_thickness_pairs of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501


        :return: The conductivity_thickness_pairs of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501
        :rtype: list[ConductivityThicknessPair]
        """
        return self._conductivity_thickness_pairs

    @conductivity_thickness_pairs.setter
    def conductivity_thickness_pairs(self, conductivity_thickness_pairs):
        """Sets the conductivity_thickness_pairs of this OneOfDerivedHeatFluxWallThermal.


        :param conductivity_thickness_pairs: The conductivity_thickness_pairs of this OneOfDerivedHeatFluxWallThermal.  # noqa: E501
        :type: list[ConductivityThicknessPair]
        """

        self._conductivity_thickness_pairs = conductivity_thickness_pairs

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
        if not isinstance(other, OneOfDerivedHeatFluxWallThermal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfDerivedHeatFluxWallThermal):
            return True

        return self.to_dict() != other.to_dict()
