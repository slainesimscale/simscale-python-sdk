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


class OneOfCustomFluidBCVelocity(object):
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
        'relaxation_length_scale': 'DimensionalLength',
        'gradient': 'DimensionalVectorSpecificTurbulenceDissipationRate',
        'value': 'DimensionalVectorSpeed',
        'flow_rate': 'OneOfFlowRateMeanInletVBCFlowRate',
        'turbulence_wall': 'str',
        'orientation_reference': 'str',
        'surface_roughness': 'DimensionalLength',
        'phase': 'str',
        'mean_velocity': 'DimensionalSpeed',
        'rotation': 'AngularRotation',
        'domain_length_scale': 'DimensionalLength',
        'eddy_length_scale': 'DimensionalFunctionLength',
        'velocity': 'DimensionalVectorFunctionSpeed',
        'reynolds_stress_tensor': 'StressTensorPressure'
    }

    attribute_map = {
        'type': 'type',
        'relax_boundary': 'relaxBoundary',
        'far_field_value': 'farFieldValue',
        'relaxation_length_scale': 'relaxationLengthScale',
        'gradient': 'gradient',
        'value': 'value',
        'flow_rate': 'flowRate',
        'turbulence_wall': 'turbulenceWall',
        'orientation_reference': 'orientationReference',
        'surface_roughness': 'surfaceRoughness',
        'phase': 'phase',
        'mean_velocity': 'meanVelocity',
        'rotation': 'rotation',
        'domain_length_scale': 'domainLengthScale',
        'eddy_length_scale': 'eddyLengthScale',
        'velocity': 'velocity',
        'reynolds_stress_tensor': 'reynoldsStressTensor'
    }

    discriminator_value_class_map = {
        'ADVECTIVE': 'AdvectiveVBC',
        'SYMMETRY': 'SymmetryVBC',
        'FIXED_GRADIENT': 'FixedGradientVBC',
        'FIXED_VALUE': 'FixedValueVBC',
        'FIXED_MEAN': 'MeanValueVBC',
        'FLOW_RATE_INLET_VELOCITY': 'FlowRateInletVBC',
        'FLOW_RATE_MEAN_INLET_VELOCITY': 'FlowRateMeanInletVBC',
        'FREESTREAM': 'FreestreamVBC',
        'INLET_OUTLET': 'InletOutletVBC',
        'MOVING_WALL_VELOCITY': 'MovingWallVBC',
        'NO_SLIP': 'NoSlipVBC',
        'OUTLET_MEAN_PHASE': 'OutletMeanPhaseVBC',
        'PRESSURE_INLET_VELOCITY': 'PressureInletVBC',
        'PRESSURE_INLET_OUTLET_VELOCITY': 'PressureInletOutletVBC',
        'ROTATING_WALL_VELOCITY': 'RotatingWallVBC',
        'ZERO_GRADIENT': 'ZeroGradientVBC',
        'SLIP': 'SlipVBC',
        'TURBULENT_DFSEM_INLET': 'TurbulentDFSEMInletVBC'
    }

    def __init__(self, type='TURBULENT_DFSEM_INLET', relax_boundary=None, far_field_value=None, relaxation_length_scale=None, gradient=None, value=None, flow_rate=None, turbulence_wall=None, orientation_reference=None, surface_roughness=None, phase=None, mean_velocity=None, rotation=None, domain_length_scale=None, eddy_length_scale=None, velocity=None, reynolds_stress_tensor=None, local_vars_configuration=None):  # noqa: E501
        """OneOfCustomFluidBCVelocity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._relax_boundary = None
        self._far_field_value = None
        self._relaxation_length_scale = None
        self._gradient = None
        self._value = None
        self._flow_rate = None
        self._turbulence_wall = None
        self._orientation_reference = None
        self._surface_roughness = None
        self._phase = None
        self._mean_velocity = None
        self._rotation = None
        self._domain_length_scale = None
        self._eddy_length_scale = None
        self._velocity = None
        self._reynolds_stress_tensor = None
        self.discriminator = 'type'

        self.type = type
        if relax_boundary is not None:
            self.relax_boundary = relax_boundary
        if far_field_value is not None:
            self.far_field_value = far_field_value
        if relaxation_length_scale is not None:
            self.relaxation_length_scale = relaxation_length_scale
        if gradient is not None:
            self.gradient = gradient
        if value is not None:
            self.value = value
        if flow_rate is not None:
            self.flow_rate = flow_rate
        if turbulence_wall is not None:
            self.turbulence_wall = turbulence_wall
        if orientation_reference is not None:
            self.orientation_reference = orientation_reference
        if surface_roughness is not None:
            self.surface_roughness = surface_roughness
        if phase is not None:
            self.phase = phase
        if mean_velocity is not None:
            self.mean_velocity = mean_velocity
        if rotation is not None:
            self.rotation = rotation
        if domain_length_scale is not None:
            self.domain_length_scale = domain_length_scale
        if eddy_length_scale is not None:
            self.eddy_length_scale = eddy_length_scale
        if velocity is not None:
            self.velocity = velocity
        if reynolds_stress_tensor is not None:
            self.reynolds_stress_tensor = reynolds_stress_tensor

    @property
    def type(self):
        """Gets the type of this OneOfCustomFluidBCVelocity.  # noqa: E501

        Schema name: TurbulentDFSEMInletVBC  # noqa: E501

        :return: The type of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfCustomFluidBCVelocity.

        Schema name: TurbulentDFSEMInletVBC  # noqa: E501

        :param type: The type of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def relax_boundary(self):
        """Gets the relax_boundary of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The relax_boundary of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: bool
        """
        return self._relax_boundary

    @relax_boundary.setter
    def relax_boundary(self, relax_boundary):
        """Sets the relax_boundary of this OneOfCustomFluidBCVelocity.


        :param relax_boundary: The relax_boundary of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: bool
        """

        self._relax_boundary = relax_boundary

    @property
    def far_field_value(self):
        """Gets the far_field_value of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The far_field_value of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalVectorSpeed
        """
        return self._far_field_value

    @far_field_value.setter
    def far_field_value(self, far_field_value):
        """Sets the far_field_value of this OneOfCustomFluidBCVelocity.


        :param far_field_value: The far_field_value of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalVectorSpeed
        """

        self._far_field_value = far_field_value

    @property
    def relaxation_length_scale(self):
        """Gets the relaxation_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The relaxation_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._relaxation_length_scale

    @relaxation_length_scale.setter
    def relaxation_length_scale(self, relaxation_length_scale):
        """Sets the relaxation_length_scale of this OneOfCustomFluidBCVelocity.


        :param relaxation_length_scale: The relaxation_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalLength
        """

        self._relaxation_length_scale = relaxation_length_scale

    @property
    def gradient(self):
        """Gets the gradient of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The gradient of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalVectorSpecificTurbulenceDissipationRate
        """
        return self._gradient

    @gradient.setter
    def gradient(self, gradient):
        """Sets the gradient of this OneOfCustomFluidBCVelocity.


        :param gradient: The gradient of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalVectorSpecificTurbulenceDissipationRate
        """

        self._gradient = gradient

    @property
    def value(self):
        """Gets the value of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The value of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalVectorSpeed
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneOfCustomFluidBCVelocity.


        :param value: The value of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalVectorSpeed
        """

        self._value = value

    @property
    def flow_rate(self):
        """Gets the flow_rate of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The flow_rate of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: OneOfFlowRateMeanInletVBCFlowRate
        """
        return self._flow_rate

    @flow_rate.setter
    def flow_rate(self, flow_rate):
        """Sets the flow_rate of this OneOfCustomFluidBCVelocity.


        :param flow_rate: The flow_rate of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: OneOfFlowRateMeanInletVBCFlowRate
        """

        self._flow_rate = flow_rate

    @property
    def turbulence_wall(self):
        """Gets the turbulence_wall of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The turbulence_wall of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: str
        """
        return self._turbulence_wall

    @turbulence_wall.setter
    def turbulence_wall(self, turbulence_wall):
        """Sets the turbulence_wall of this OneOfCustomFluidBCVelocity.


        :param turbulence_wall: The turbulence_wall of this OneOfCustomFluidBCVelocity.  # noqa: E501
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
    def orientation_reference(self):
        """Gets the orientation_reference of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The orientation_reference of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: str
        """
        return self._orientation_reference

    @orientation_reference.setter
    def orientation_reference(self, orientation_reference):
        """Sets the orientation_reference of this OneOfCustomFluidBCVelocity.


        :param orientation_reference: The orientation_reference of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: str
        """
        allowed_values = ["GEOMETRY", "FLOW_DOMAIN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and orientation_reference not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `orientation_reference` ({0}), must be one of {1}"  # noqa: E501
                .format(orientation_reference, allowed_values)
            )

        self._orientation_reference = orientation_reference

    @property
    def surface_roughness(self):
        """Gets the surface_roughness of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The surface_roughness of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._surface_roughness

    @surface_roughness.setter
    def surface_roughness(self, surface_roughness):
        """Sets the surface_roughness of this OneOfCustomFluidBCVelocity.


        :param surface_roughness: The surface_roughness of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalLength
        """

        self._surface_roughness = surface_roughness

    @property
    def phase(self):
        """Gets the phase of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The phase of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this OneOfCustomFluidBCVelocity.


        :param phase: The phase of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: str
        """
        allowed_values = ["PHASE_0", "PHASE_1"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and phase not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `phase` ({0}), must be one of {1}"  # noqa: E501
                .format(phase, allowed_values)
            )

        self._phase = phase

    @property
    def mean_velocity(self):
        """Gets the mean_velocity of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The mean_velocity of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalSpeed
        """
        return self._mean_velocity

    @mean_velocity.setter
    def mean_velocity(self, mean_velocity):
        """Sets the mean_velocity of this OneOfCustomFluidBCVelocity.


        :param mean_velocity: The mean_velocity of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalSpeed
        """

        self._mean_velocity = mean_velocity

    @property
    def rotation(self):
        """Gets the rotation of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The rotation of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: AngularRotation
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this OneOfCustomFluidBCVelocity.


        :param rotation: The rotation of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: AngularRotation
        """

        self._rotation = rotation

    @property
    def domain_length_scale(self):
        """Gets the domain_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The domain_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._domain_length_scale

    @domain_length_scale.setter
    def domain_length_scale(self, domain_length_scale):
        """Sets the domain_length_scale of this OneOfCustomFluidBCVelocity.


        :param domain_length_scale: The domain_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalLength
        """

        self._domain_length_scale = domain_length_scale

    @property
    def eddy_length_scale(self):
        """Gets the eddy_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The eddy_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalFunctionLength
        """
        return self._eddy_length_scale

    @eddy_length_scale.setter
    def eddy_length_scale(self, eddy_length_scale):
        """Sets the eddy_length_scale of this OneOfCustomFluidBCVelocity.


        :param eddy_length_scale: The eddy_length_scale of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalFunctionLength
        """

        self._eddy_length_scale = eddy_length_scale

    @property
    def velocity(self):
        """Gets the velocity of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The velocity of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: DimensionalVectorFunctionSpeed
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this OneOfCustomFluidBCVelocity.


        :param velocity: The velocity of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: DimensionalVectorFunctionSpeed
        """

        self._velocity = velocity

    @property
    def reynolds_stress_tensor(self):
        """Gets the reynolds_stress_tensor of this OneOfCustomFluidBCVelocity.  # noqa: E501


        :return: The reynolds_stress_tensor of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :rtype: StressTensorPressure
        """
        return self._reynolds_stress_tensor

    @reynolds_stress_tensor.setter
    def reynolds_stress_tensor(self, reynolds_stress_tensor):
        """Sets the reynolds_stress_tensor of this OneOfCustomFluidBCVelocity.


        :param reynolds_stress_tensor: The reynolds_stress_tensor of this OneOfCustomFluidBCVelocity.  # noqa: E501
        :type: StressTensorPressure
        """

        self._reynolds_stress_tensor = reynolds_stress_tensor

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
        if not isinstance(other, OneOfCustomFluidBCVelocity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfCustomFluidBCVelocity):
            return True

        return self.to_dict() != other.to_dict()
