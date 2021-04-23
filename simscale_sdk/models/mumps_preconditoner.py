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


class MUMPSPreconditoner(object):
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
        'actualisation_rate': 'int',
        'memory_percentage_for_pivoting': 'float'
    }

    attribute_map = {
        'type': 'type',
        'actualisation_rate': 'actualisationRate',
        'memory_percentage_for_pivoting': 'memoryPercentageForPivoting'
    }

    def __init__(self, type='MUMPS_LDLT', actualisation_rate=None, memory_percentage_for_pivoting=None, local_vars_configuration=None):  # noqa: E501
        """MUMPSPreconditoner - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._actualisation_rate = None
        self._memory_percentage_for_pivoting = None
        self.discriminator = None

        self.type = type
        if actualisation_rate is not None:
            self.actualisation_rate = actualisation_rate
        if memory_percentage_for_pivoting is not None:
            self.memory_percentage_for_pivoting = memory_percentage_for_pivoting

    @property
    def type(self):
        """Gets the type of this MUMPSPreconditoner.  # noqa: E501

        Schema name: MUMPSPreconditoner  # noqa: E501

        :return: The type of this MUMPSPreconditoner.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MUMPSPreconditoner.

        Schema name: MUMPSPreconditoner  # noqa: E501

        :param type: The type of this MUMPSPreconditoner.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def actualisation_rate(self):
        """Gets the actualisation_rate of this MUMPSPreconditoner.  # noqa: E501

        Set the reactualisation intervall for the preconditioner matrix P. If this value is set to 30 the preconditioner is recomputed just every 30th iteration. This preconditioner is computionally more expensive than the incomplete LDLT factorization but nearer to the exact solution. This setting makes it possible to save computation time by taking advantage of this fact.  # noqa: E501

        :return: The actualisation_rate of this MUMPSPreconditoner.  # noqa: E501
        :rtype: int
        """
        return self._actualisation_rate

    @actualisation_rate.setter
    def actualisation_rate(self, actualisation_rate):
        """Sets the actualisation_rate of this MUMPSPreconditoner.

        Set the reactualisation intervall for the preconditioner matrix P. If this value is set to 30 the preconditioner is recomputed just every 30th iteration. This preconditioner is computionally more expensive than the incomplete LDLT factorization but nearer to the exact solution. This setting makes it possible to save computation time by taking advantage of this fact.  # noqa: E501

        :param actualisation_rate: The actualisation_rate of this MUMPSPreconditoner.  # noqa: E501
        :type: int
        """

        self._actualisation_rate = actualisation_rate

    @property
    def memory_percentage_for_pivoting(self):
        """Gets the memory_percentage_for_pivoting of this MUMPSPreconditoner.  # noqa: E501

        Define how much additional memory should be reserved for the pivoting operations. If MUMPS estimates that the necessary space for factorising the matrix would be 100, choosing a value of 20 would mean that MUMPS allocates a memory space of 120.  # noqa: E501

        :return: The memory_percentage_for_pivoting of this MUMPSPreconditoner.  # noqa: E501
        :rtype: float
        """
        return self._memory_percentage_for_pivoting

    @memory_percentage_for_pivoting.setter
    def memory_percentage_for_pivoting(self, memory_percentage_for_pivoting):
        """Sets the memory_percentage_for_pivoting of this MUMPSPreconditoner.

        Define how much additional memory should be reserved for the pivoting operations. If MUMPS estimates that the necessary space for factorising the matrix would be 100, choosing a value of 20 would mean that MUMPS allocates a memory space of 120.  # noqa: E501

        :param memory_percentage_for_pivoting: The memory_percentage_for_pivoting of this MUMPSPreconditoner.  # noqa: E501
        :type: float
        """

        self._memory_percentage_for_pivoting = memory_percentage_for_pivoting

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
        if not isinstance(other, MUMPSPreconditoner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MUMPSPreconditoner):
            return True

        return self.to_dict() != other.to_dict()
