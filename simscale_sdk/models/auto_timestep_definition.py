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


class AutoTimestepDefinition(object):
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
        'simulation_interval': 'DimensionalTime',
        'maximum_timestep_length': 'RestrictedDimensionalFunctionTime',
        'minimum_timestep_length': 'DimensionalTime',
        'maximum_residual': 'float',
        'retiming_event': 'OneOfAutoTimestepDefinitionRetimingEvent'
    }

    attribute_map = {
        'type': 'type',
        'simulation_interval': 'simulationInterval',
        'maximum_timestep_length': 'maximumTimestepLength',
        'minimum_timestep_length': 'minimumTimestepLength',
        'maximum_residual': 'maximumResidual',
        'retiming_event': 'retimingEvent'
    }

    def __init__(self, type='AUTOMATIC_V27', simulation_interval=None, maximum_timestep_length=None, minimum_timestep_length=None, maximum_residual=None, retiming_event=None, local_vars_configuration=None):  # noqa: E501
        """AutoTimestepDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._simulation_interval = None
        self._maximum_timestep_length = None
        self._minimum_timestep_length = None
        self._maximum_residual = None
        self._retiming_event = None
        self.discriminator = None

        self.type = type
        if simulation_interval is not None:
            self.simulation_interval = simulation_interval
        if maximum_timestep_length is not None:
            self.maximum_timestep_length = maximum_timestep_length
        if minimum_timestep_length is not None:
            self.minimum_timestep_length = minimum_timestep_length
        if maximum_residual is not None:
            self.maximum_residual = maximum_residual
        if retiming_event is not None:
            self.retiming_event = retiming_event

    @property
    def type(self):
        """Gets the type of this AutoTimestepDefinition.  # noqa: E501

        Schema name: AutoTimestepDefinition  # noqa: E501

        :return: The type of this AutoTimestepDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutoTimestepDefinition.

        Schema name: AutoTimestepDefinition  # noqa: E501

        :param type: The type of this AutoTimestepDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def simulation_interval(self):
        """Gets the simulation_interval of this AutoTimestepDefinition.  # noqa: E501


        :return: The simulation_interval of this AutoTimestepDefinition.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._simulation_interval

    @simulation_interval.setter
    def simulation_interval(self, simulation_interval):
        """Sets the simulation_interval of this AutoTimestepDefinition.


        :param simulation_interval: The simulation_interval of this AutoTimestepDefinition.  # noqa: E501
        :type: DimensionalTime
        """

        self._simulation_interval = simulation_interval

    @property
    def maximum_timestep_length(self):
        """Gets the maximum_timestep_length of this AutoTimestepDefinition.  # noqa: E501


        :return: The maximum_timestep_length of this AutoTimestepDefinition.  # noqa: E501
        :rtype: RestrictedDimensionalFunctionTime
        """
        return self._maximum_timestep_length

    @maximum_timestep_length.setter
    def maximum_timestep_length(self, maximum_timestep_length):
        """Sets the maximum_timestep_length of this AutoTimestepDefinition.


        :param maximum_timestep_length: The maximum_timestep_length of this AutoTimestepDefinition.  # noqa: E501
        :type: RestrictedDimensionalFunctionTime
        """

        self._maximum_timestep_length = maximum_timestep_length

    @property
    def minimum_timestep_length(self):
        """Gets the minimum_timestep_length of this AutoTimestepDefinition.  # noqa: E501


        :return: The minimum_timestep_length of this AutoTimestepDefinition.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._minimum_timestep_length

    @minimum_timestep_length.setter
    def minimum_timestep_length(self, minimum_timestep_length):
        """Sets the minimum_timestep_length of this AutoTimestepDefinition.


        :param minimum_timestep_length: The minimum_timestep_length of this AutoTimestepDefinition.  # noqa: E501
        :type: DimensionalTime
        """

        self._minimum_timestep_length = minimum_timestep_length

    @property
    def maximum_residual(self):
        """Gets the maximum_residual of this AutoTimestepDefinition.  # noqa: E501


        :return: The maximum_residual of this AutoTimestepDefinition.  # noqa: E501
        :rtype: float
        """
        return self._maximum_residual

    @maximum_residual.setter
    def maximum_residual(self, maximum_residual):
        """Sets the maximum_residual of this AutoTimestepDefinition.


        :param maximum_residual: The maximum_residual of this AutoTimestepDefinition.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_residual is not None and maximum_residual < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_residual`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_residual = maximum_residual

    @property
    def retiming_event(self):
        """Gets the retiming_event of this AutoTimestepDefinition.  # noqa: E501


        :return: The retiming_event of this AutoTimestepDefinition.  # noqa: E501
        :rtype: OneOfAutoTimestepDefinitionRetimingEvent
        """
        return self._retiming_event

    @retiming_event.setter
    def retiming_event(self, retiming_event):
        """Sets the retiming_event of this AutoTimestepDefinition.


        :param retiming_event: The retiming_event of this AutoTimestepDefinition.  # noqa: E501
        :type: OneOfAutoTimestepDefinitionRetimingEvent
        """

        self._retiming_event = retiming_event

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
        if not isinstance(other, AutoTimestepDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoTimestepDefinition):
            return True

        return self.to_dict() != other.to_dict()
