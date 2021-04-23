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


class PressureInletBC(object):
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
        'pressure': 'TotalPBC',
        'pressure_rgh': 'TotalPBC',
        'gauge_pressure': 'OneOfPressureInletBCGaugePressure',
        'gauge_pressure_rgh': 'TotalPBC',
        'temperature': 'OneOfPressureInletBCTemperature',
        'passive_scalars': 'list[FixedValuePSBC]',
        'phase_fraction': 'FixedValuePFBC',
        'net_radiative_heat_flux': 'OneOfPressureInletBCNetRadiativeHeatFlux',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'pressure': 'pressure',
        'pressure_rgh': 'pressureRgh',
        'gauge_pressure': 'gaugePressure',
        'gauge_pressure_rgh': 'gaugePressureRgh',
        'temperature': 'temperature',
        'passive_scalars': 'passiveScalars',
        'phase_fraction': 'phaseFraction',
        'net_radiative_heat_flux': 'netRadiativeHeatFlux',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='PRESSURE_INLET_V31', name=None, pressure=None, pressure_rgh=None, gauge_pressure=None, gauge_pressure_rgh=None, temperature=None, passive_scalars=None, phase_fraction=None, net_radiative_heat_flux=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """PressureInletBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._pressure = None
        self._pressure_rgh = None
        self._gauge_pressure = None
        self._gauge_pressure_rgh = None
        self._temperature = None
        self._passive_scalars = None
        self._phase_fraction = None
        self._net_radiative_heat_flux = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if pressure is not None:
            self.pressure = pressure
        if pressure_rgh is not None:
            self.pressure_rgh = pressure_rgh
        if gauge_pressure is not None:
            self.gauge_pressure = gauge_pressure
        if gauge_pressure_rgh is not None:
            self.gauge_pressure_rgh = gauge_pressure_rgh
        if temperature is not None:
            self.temperature = temperature
        if passive_scalars is not None:
            self.passive_scalars = passive_scalars
        if phase_fraction is not None:
            self.phase_fraction = phase_fraction
        if net_radiative_heat_flux is not None:
            self.net_radiative_heat_flux = net_radiative_heat_flux
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this PressureInletBC.  # noqa: E501

        This boundary condition is suitable for inlet and open boundaries where the value of pressure is known. For Incompressible and Passive Scalar Transport analysis the specific Pressure i.e. Pressure/Density is used.  Schema name: PressureInletBC  # noqa: E501

        :return: The type of this PressureInletBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PressureInletBC.

        This boundary condition is suitable for inlet and open boundaries where the value of pressure is known. For Incompressible and Passive Scalar Transport analysis the specific Pressure i.e. Pressure/Density is used.  Schema name: PressureInletBC  # noqa: E501

        :param type: The type of this PressureInletBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this PressureInletBC.  # noqa: E501


        :return: The name of this PressureInletBC.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PressureInletBC.


        :param name: The name of this PressureInletBC.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pressure(self):
        """Gets the pressure of this PressureInletBC.  # noqa: E501


        :return: The pressure of this PressureInletBC.  # noqa: E501
        :rtype: TotalPBC
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this PressureInletBC.


        :param pressure: The pressure of this PressureInletBC.  # noqa: E501
        :type: TotalPBC
        """

        self._pressure = pressure

    @property
    def pressure_rgh(self):
        """Gets the pressure_rgh of this PressureInletBC.  # noqa: E501


        :return: The pressure_rgh of this PressureInletBC.  # noqa: E501
        :rtype: TotalPBC
        """
        return self._pressure_rgh

    @pressure_rgh.setter
    def pressure_rgh(self, pressure_rgh):
        """Sets the pressure_rgh of this PressureInletBC.


        :param pressure_rgh: The pressure_rgh of this PressureInletBC.  # noqa: E501
        :type: TotalPBC
        """

        self._pressure_rgh = pressure_rgh

    @property
    def gauge_pressure(self):
        """Gets the gauge_pressure of this PressureInletBC.  # noqa: E501


        :return: The gauge_pressure of this PressureInletBC.  # noqa: E501
        :rtype: OneOfPressureInletBCGaugePressure
        """
        return self._gauge_pressure

    @gauge_pressure.setter
    def gauge_pressure(self, gauge_pressure):
        """Sets the gauge_pressure of this PressureInletBC.


        :param gauge_pressure: The gauge_pressure of this PressureInletBC.  # noqa: E501
        :type: OneOfPressureInletBCGaugePressure
        """

        self._gauge_pressure = gauge_pressure

    @property
    def gauge_pressure_rgh(self):
        """Gets the gauge_pressure_rgh of this PressureInletBC.  # noqa: E501


        :return: The gauge_pressure_rgh of this PressureInletBC.  # noqa: E501
        :rtype: TotalPBC
        """
        return self._gauge_pressure_rgh

    @gauge_pressure_rgh.setter
    def gauge_pressure_rgh(self, gauge_pressure_rgh):
        """Sets the gauge_pressure_rgh of this PressureInletBC.


        :param gauge_pressure_rgh: The gauge_pressure_rgh of this PressureInletBC.  # noqa: E501
        :type: TotalPBC
        """

        self._gauge_pressure_rgh = gauge_pressure_rgh

    @property
    def temperature(self):
        """Gets the temperature of this PressureInletBC.  # noqa: E501


        :return: The temperature of this PressureInletBC.  # noqa: E501
        :rtype: OneOfPressureInletBCTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this PressureInletBC.


        :param temperature: The temperature of this PressureInletBC.  # noqa: E501
        :type: OneOfPressureInletBCTemperature
        """

        self._temperature = temperature

    @property
    def passive_scalars(self):
        """Gets the passive_scalars of this PressureInletBC.  # noqa: E501

        Please choose a boundary condition for passive scalar (T).  # noqa: E501

        :return: The passive_scalars of this PressureInletBC.  # noqa: E501
        :rtype: list[FixedValuePSBC]
        """
        return self._passive_scalars

    @passive_scalars.setter
    def passive_scalars(self, passive_scalars):
        """Sets the passive_scalars of this PressureInletBC.

        Please choose a boundary condition for passive scalar (T).  # noqa: E501

        :param passive_scalars: The passive_scalars of this PressureInletBC.  # noqa: E501
        :type: list[FixedValuePSBC]
        """

        self._passive_scalars = passive_scalars

    @property
    def phase_fraction(self):
        """Gets the phase_fraction of this PressureInletBC.  # noqa: E501


        :return: The phase_fraction of this PressureInletBC.  # noqa: E501
        :rtype: FixedValuePFBC
        """
        return self._phase_fraction

    @phase_fraction.setter
    def phase_fraction(self, phase_fraction):
        """Sets the phase_fraction of this PressureInletBC.


        :param phase_fraction: The phase_fraction of this PressureInletBC.  # noqa: E501
        :type: FixedValuePFBC
        """

        self._phase_fraction = phase_fraction

    @property
    def net_radiative_heat_flux(self):
        """Gets the net_radiative_heat_flux of this PressureInletBC.  # noqa: E501


        :return: The net_radiative_heat_flux of this PressureInletBC.  # noqa: E501
        :rtype: OneOfPressureInletBCNetRadiativeHeatFlux
        """
        return self._net_radiative_heat_flux

    @net_radiative_heat_flux.setter
    def net_radiative_heat_flux(self, net_radiative_heat_flux):
        """Sets the net_radiative_heat_flux of this PressureInletBC.


        :param net_radiative_heat_flux: The net_radiative_heat_flux of this PressureInletBC.  # noqa: E501
        :type: OneOfPressureInletBCNetRadiativeHeatFlux
        """

        self._net_radiative_heat_flux = net_radiative_heat_flux

    @property
    def topological_reference(self):
        """Gets the topological_reference of this PressureInletBC.  # noqa: E501


        :return: The topological_reference of this PressureInletBC.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this PressureInletBC.


        :param topological_reference: The topological_reference of this PressureInletBC.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

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
        if not isinstance(other, PressureInletBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PressureInletBC):
            return True

        return self.to_dict() != other.to_dict()
