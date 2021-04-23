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


class OneOfCustomFluidBCPhaseFraction(object):
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
        'equilibrium_contact_angle': 'DimensionalAngle',
        'limit': 'str',
        'advancing_contact_angle': 'DimensionalAngle',
        'receding_contact_angle': 'DimensionalAngle',
        'velocity_scale_of_contact_angle': 'float',
        'gradient': 'DimensionalPhaseFractionGradient',
        'value': 'DimensionalDimensionless',
        'lower_bound': 'float',
        'upper_bound': 'float'
    }

    attribute_map = {
        'type': 'type',
        'equilibrium_contact_angle': 'equilibriumContactAngle',
        'limit': 'limit',
        'advancing_contact_angle': 'advancingContactAngle',
        'receding_contact_angle': 'recedingContactAngle',
        'velocity_scale_of_contact_angle': 'velocityScaleOfContactAngle',
        'gradient': 'gradient',
        'value': 'value',
        'lower_bound': 'lowerBound',
        'upper_bound': 'upperBound'
    }

    discriminator_value_class_map = {
        'CONSTANT_CONTACT_ANGLE': 'ConstantContactAnglePFBC',
        'DYNAMIC_CONTACT_ANGLE': 'DynamicContactAnglePFBC',
        'FIXED_GRADIENT': 'FixedGradientPFBC',
        'FIXED_VALUE': 'FixedValuePFBC',
        'FLOW_DEPENDENT_VALUE': 'FlowDependentValuePFBC',
        'INLET_OUTLET': 'InletOutletPFBC',
        'ZERO_GRADIENT': 'ZeroGradientPFBC',
        'SYMMETRY': 'SymmetryPFBC'
    }

    def __init__(self, type='SYMMETRY', equilibrium_contact_angle=None, limit=None, advancing_contact_angle=None, receding_contact_angle=None, velocity_scale_of_contact_angle=None, gradient=None, value=None, lower_bound=None, upper_bound=None, local_vars_configuration=None):  # noqa: E501
        """OneOfCustomFluidBCPhaseFraction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._equilibrium_contact_angle = None
        self._limit = None
        self._advancing_contact_angle = None
        self._receding_contact_angle = None
        self._velocity_scale_of_contact_angle = None
        self._gradient = None
        self._value = None
        self._lower_bound = None
        self._upper_bound = None
        self.discriminator = 'type'

        self.type = type
        if equilibrium_contact_angle is not None:
            self.equilibrium_contact_angle = equilibrium_contact_angle
        if limit is not None:
            self.limit = limit
        if advancing_contact_angle is not None:
            self.advancing_contact_angle = advancing_contact_angle
        if receding_contact_angle is not None:
            self.receding_contact_angle = receding_contact_angle
        if velocity_scale_of_contact_angle is not None:
            self.velocity_scale_of_contact_angle = velocity_scale_of_contact_angle
        if gradient is not None:
            self.gradient = gradient
        if value is not None:
            self.value = value
        if lower_bound is not None:
            self.lower_bound = lower_bound
        if upper_bound is not None:
            self.upper_bound = upper_bound

    @property
    def type(self):
        """Gets the type of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501

        Schema name: SymmetryPFBC  # noqa: E501

        :return: The type of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfCustomFluidBCPhaseFraction.

        Schema name: SymmetryPFBC  # noqa: E501

        :param type: The type of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def equilibrium_contact_angle(self):
        """Gets the equilibrium_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The equilibrium_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._equilibrium_contact_angle

    @equilibrium_contact_angle.setter
    def equilibrium_contact_angle(self, equilibrium_contact_angle):
        """Sets the equilibrium_contact_angle of this OneOfCustomFluidBCPhaseFraction.


        :param equilibrium_contact_angle: The equilibrium_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: DimensionalAngle
        """

        self._equilibrium_contact_angle = equilibrium_contact_angle

    @property
    def limit(self):
        """Gets the limit of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The limit of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this OneOfCustomFluidBCPhaseFraction.


        :param limit: The limit of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: str
        """
        allowed_values = ["GRADIENT", "NONE", "PHASE_FRACTION", "ZERO_GRADIENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and limit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `limit` ({0}), must be one of {1}"  # noqa: E501
                .format(limit, allowed_values)
            )

        self._limit = limit

    @property
    def advancing_contact_angle(self):
        """Gets the advancing_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The advancing_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._advancing_contact_angle

    @advancing_contact_angle.setter
    def advancing_contact_angle(self, advancing_contact_angle):
        """Sets the advancing_contact_angle of this OneOfCustomFluidBCPhaseFraction.


        :param advancing_contact_angle: The advancing_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: DimensionalAngle
        """

        self._advancing_contact_angle = advancing_contact_angle

    @property
    def receding_contact_angle(self):
        """Gets the receding_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The receding_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._receding_contact_angle

    @receding_contact_angle.setter
    def receding_contact_angle(self, receding_contact_angle):
        """Sets the receding_contact_angle of this OneOfCustomFluidBCPhaseFraction.


        :param receding_contact_angle: The receding_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: DimensionalAngle
        """

        self._receding_contact_angle = receding_contact_angle

    @property
    def velocity_scale_of_contact_angle(self):
        """Gets the velocity_scale_of_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The velocity_scale_of_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: float
        """
        return self._velocity_scale_of_contact_angle

    @velocity_scale_of_contact_angle.setter
    def velocity_scale_of_contact_angle(self, velocity_scale_of_contact_angle):
        """Sets the velocity_scale_of_contact_angle of this OneOfCustomFluidBCPhaseFraction.


        :param velocity_scale_of_contact_angle: The velocity_scale_of_contact_angle of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: float
        """

        self._velocity_scale_of_contact_angle = velocity_scale_of_contact_angle

    @property
    def gradient(self):
        """Gets the gradient of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The gradient of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: DimensionalPhaseFractionGradient
        """
        return self._gradient

    @gradient.setter
    def gradient(self, gradient):
        """Sets the gradient of this OneOfCustomFluidBCPhaseFraction.


        :param gradient: The gradient of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: DimensionalPhaseFractionGradient
        """

        self._gradient = gradient

    @property
    def value(self):
        """Gets the value of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The value of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: DimensionalDimensionless
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneOfCustomFluidBCPhaseFraction.


        :param value: The value of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: DimensionalDimensionless
        """

        self._value = value

    @property
    def lower_bound(self):
        """Gets the lower_bound of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The lower_bound of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: float
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, lower_bound):
        """Sets the lower_bound of this OneOfCustomFluidBCPhaseFraction.


        :param lower_bound: The lower_bound of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                lower_bound is not None and lower_bound > 1):  # noqa: E501
            raise ValueError("Invalid value for `lower_bound`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lower_bound is not None and lower_bound < 0):  # noqa: E501
            raise ValueError("Invalid value for `lower_bound`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lower_bound = lower_bound

    @property
    def upper_bound(self):
        """Gets the upper_bound of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501


        :return: The upper_bound of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :rtype: float
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, upper_bound):
        """Sets the upper_bound of this OneOfCustomFluidBCPhaseFraction.


        :param upper_bound: The upper_bound of this OneOfCustomFluidBCPhaseFraction.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                upper_bound is not None and upper_bound > 1):  # noqa: E501
            raise ValueError("Invalid value for `upper_bound`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                upper_bound is not None and upper_bound < 0):  # noqa: E501
            raise ValueError("Invalid value for `upper_bound`, must be a value greater than or equal to `0`")  # noqa: E501

        self._upper_bound = upper_bound

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
        if not isinstance(other, OneOfCustomFluidBCPhaseFraction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfCustomFluidBCPhaseFraction):
            return True

        return self.to_dict() != other.to_dict()
