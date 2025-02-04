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


class VelocityInletBC(object):
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
        'velocity': 'OneOfVelocityInletBCVelocity',
        'temperature': 'OneOfVelocityInletBCTemperature',
        'passive_scalars': 'list[FixedValuePSBC]',
        'phase_fraction': 'FixedValuePFBC',
        'turbulence_intensity': 'OneOfVelocityInletBCTurbulenceIntensity',
        'dissipation_type': 'OneOfVelocityInletBCDissipationType',
        'net_radiative_heat_flux': 'OneOfVelocityInletBCNetRadiativeHeatFlux',
        'radiative_intensity_ray': 'OneOfVelocityInletBCRadiativeIntensityRay',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'velocity': 'velocity',
        'temperature': 'temperature',
        'passive_scalars': 'passiveScalars',
        'phase_fraction': 'phaseFraction',
        'turbulence_intensity': 'turbulenceIntensity',
        'dissipation_type': 'dissipationType',
        'net_radiative_heat_flux': 'netRadiativeHeatFlux',
        'radiative_intensity_ray': 'radiativeIntensityRay',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='VELOCITY_INLET_V3', name=None, velocity=None, temperature=None, passive_scalars=None, phase_fraction=None, turbulence_intensity=None, dissipation_type=None, net_radiative_heat_flux=None, radiative_intensity_ray=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """VelocityInletBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._velocity = None
        self._temperature = None
        self._passive_scalars = None
        self._phase_fraction = None
        self._turbulence_intensity = None
        self._dissipation_type = None
        self._net_radiative_heat_flux = None
        self._radiative_intensity_ray = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if velocity is not None:
            self.velocity = velocity
        if temperature is not None:
            self.temperature = temperature
        if passive_scalars is not None:
            self.passive_scalars = passive_scalars
        if phase_fraction is not None:
            self.phase_fraction = phase_fraction
        if turbulence_intensity is not None:
            self.turbulence_intensity = turbulence_intensity
        if dissipation_type is not None:
            self.dissipation_type = dissipation_type
        if net_radiative_heat_flux is not None:
            self.net_radiative_heat_flux = net_radiative_heat_flux
        if radiative_intensity_ray is not None:
            self.radiative_intensity_ray = radiative_intensity_ray
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this VelocityInletBC.  # noqa: E501

        This boundary condition imposes a known <b>velocity</b>-based constraint at an inlet.  Schema name: VelocityInletBC  # noqa: E501

        :return: The type of this VelocityInletBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VelocityInletBC.

        This boundary condition imposes a known <b>velocity</b>-based constraint at an inlet.  Schema name: VelocityInletBC  # noqa: E501

        :param type: The type of this VelocityInletBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this VelocityInletBC.  # noqa: E501


        :return: The name of this VelocityInletBC.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VelocityInletBC.


        :param name: The name of this VelocityInletBC.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def velocity(self):
        """Gets the velocity of this VelocityInletBC.  # noqa: E501


        :return: The velocity of this VelocityInletBC.  # noqa: E501
        :rtype: OneOfVelocityInletBCVelocity
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this VelocityInletBC.


        :param velocity: The velocity of this VelocityInletBC.  # noqa: E501
        :type: OneOfVelocityInletBCVelocity
        """

        self._velocity = velocity

    @property
    def temperature(self):
        """Gets the temperature of this VelocityInletBC.  # noqa: E501


        :return: The temperature of this VelocityInletBC.  # noqa: E501
        :rtype: OneOfVelocityInletBCTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this VelocityInletBC.


        :param temperature: The temperature of this VelocityInletBC.  # noqa: E501
        :type: OneOfVelocityInletBCTemperature
        """

        self._temperature = temperature

    @property
    def passive_scalars(self):
        """Gets the passive_scalars of this VelocityInletBC.  # noqa: E501

        Please choose a boundary condition for passive scalar (T).  # noqa: E501

        :return: The passive_scalars of this VelocityInletBC.  # noqa: E501
        :rtype: list[FixedValuePSBC]
        """
        return self._passive_scalars

    @passive_scalars.setter
    def passive_scalars(self, passive_scalars):
        """Sets the passive_scalars of this VelocityInletBC.

        Please choose a boundary condition for passive scalar (T).  # noqa: E501

        :param passive_scalars: The passive_scalars of this VelocityInletBC.  # noqa: E501
        :type: list[FixedValuePSBC]
        """

        self._passive_scalars = passive_scalars

    @property
    def phase_fraction(self):
        """Gets the phase_fraction of this VelocityInletBC.  # noqa: E501


        :return: The phase_fraction of this VelocityInletBC.  # noqa: E501
        :rtype: FixedValuePFBC
        """
        return self._phase_fraction

    @phase_fraction.setter
    def phase_fraction(self, phase_fraction):
        """Sets the phase_fraction of this VelocityInletBC.


        :param phase_fraction: The phase_fraction of this VelocityInletBC.  # noqa: E501
        :type: FixedValuePFBC
        """

        self._phase_fraction = phase_fraction

    @property
    def turbulence_intensity(self):
        """Gets the turbulence_intensity of this VelocityInletBC.  # noqa: E501


        :return: The turbulence_intensity of this VelocityInletBC.  # noqa: E501
        :rtype: OneOfVelocityInletBCTurbulenceIntensity
        """
        return self._turbulence_intensity

    @turbulence_intensity.setter
    def turbulence_intensity(self, turbulence_intensity):
        """Sets the turbulence_intensity of this VelocityInletBC.


        :param turbulence_intensity: The turbulence_intensity of this VelocityInletBC.  # noqa: E501
        :type: OneOfVelocityInletBCTurbulenceIntensity
        """

        self._turbulence_intensity = turbulence_intensity

    @property
    def dissipation_type(self):
        """Gets the dissipation_type of this VelocityInletBC.  # noqa: E501


        :return: The dissipation_type of this VelocityInletBC.  # noqa: E501
        :rtype: OneOfVelocityInletBCDissipationType
        """
        return self._dissipation_type

    @dissipation_type.setter
    def dissipation_type(self, dissipation_type):
        """Sets the dissipation_type of this VelocityInletBC.


        :param dissipation_type: The dissipation_type of this VelocityInletBC.  # noqa: E501
        :type: OneOfVelocityInletBCDissipationType
        """

        self._dissipation_type = dissipation_type

    @property
    def net_radiative_heat_flux(self):
        """Gets the net_radiative_heat_flux of this VelocityInletBC.  # noqa: E501


        :return: The net_radiative_heat_flux of this VelocityInletBC.  # noqa: E501
        :rtype: OneOfVelocityInletBCNetRadiativeHeatFlux
        """
        return self._net_radiative_heat_flux

    @net_radiative_heat_flux.setter
    def net_radiative_heat_flux(self, net_radiative_heat_flux):
        """Sets the net_radiative_heat_flux of this VelocityInletBC.


        :param net_radiative_heat_flux: The net_radiative_heat_flux of this VelocityInletBC.  # noqa: E501
        :type: OneOfVelocityInletBCNetRadiativeHeatFlux
        """

        self._net_radiative_heat_flux = net_radiative_heat_flux

    @property
    def radiative_intensity_ray(self):
        """Gets the radiative_intensity_ray of this VelocityInletBC.  # noqa: E501


        :return: The radiative_intensity_ray of this VelocityInletBC.  # noqa: E501
        :rtype: OneOfVelocityInletBCRadiativeIntensityRay
        """
        return self._radiative_intensity_ray

    @radiative_intensity_ray.setter
    def radiative_intensity_ray(self, radiative_intensity_ray):
        """Sets the radiative_intensity_ray of this VelocityInletBC.


        :param radiative_intensity_ray: The radiative_intensity_ray of this VelocityInletBC.  # noqa: E501
        :type: OneOfVelocityInletBCRadiativeIntensityRay
        """

        self._radiative_intensity_ray = radiative_intensity_ray

    @property
    def topological_reference(self):
        """Gets the topological_reference of this VelocityInletBC.  # noqa: E501


        :return: The topological_reference of this VelocityInletBC.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this VelocityInletBC.


        :param topological_reference: The topological_reference of this VelocityInletBC.  # noqa: E501
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
        if not isinstance(other, VelocityInletBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VelocityInletBC):
            return True

        return self.to_dict() != other.to_dict()
