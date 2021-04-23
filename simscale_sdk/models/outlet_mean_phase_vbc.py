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


class OutletMeanPhaseVBC(object):
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
        'phase': 'str',
        'mean_velocity': 'DimensionalSpeed'
    }

    attribute_map = {
        'type': 'type',
        'phase': 'phase',
        'mean_velocity': 'meanVelocity'
    }

    def __init__(self, type='OUTLET_MEAN_PHASE', phase=None, mean_velocity=None, local_vars_configuration=None):  # noqa: E501
        """OutletMeanPhaseVBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._phase = None
        self._mean_velocity = None
        self.discriminator = None

        self.type = type
        if phase is not None:
            self.phase = phase
        if mean_velocity is not None:
            self.mean_velocity = mean_velocity

    @property
    def type(self):
        """Gets the type of this OutletMeanPhaseVBC.  # noqa: E501

        Schema name: OutletMeanPhaseVBC  # noqa: E501

        :return: The type of this OutletMeanPhaseVBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OutletMeanPhaseVBC.

        Schema name: OutletMeanPhaseVBC  # noqa: E501

        :param type: The type of this OutletMeanPhaseVBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def phase(self):
        """Gets the phase of this OutletMeanPhaseVBC.  # noqa: E501


        :return: The phase of this OutletMeanPhaseVBC.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this OutletMeanPhaseVBC.


        :param phase: The phase of this OutletMeanPhaseVBC.  # noqa: E501
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
        """Gets the mean_velocity of this OutletMeanPhaseVBC.  # noqa: E501


        :return: The mean_velocity of this OutletMeanPhaseVBC.  # noqa: E501
        :rtype: DimensionalSpeed
        """
        return self._mean_velocity

    @mean_velocity.setter
    def mean_velocity(self, mean_velocity):
        """Sets the mean_velocity of this OutletMeanPhaseVBC.


        :param mean_velocity: The mean_velocity of this OutletMeanPhaseVBC.  # noqa: E501
        :type: DimensionalSpeed
        """

        self._mean_velocity = mean_velocity

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
        if not isinstance(other, OutletMeanPhaseVBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutletMeanPhaseVBC):
            return True

        return self.to_dict() != other.to_dict()
