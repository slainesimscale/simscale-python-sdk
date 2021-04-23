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


class OneOfNewtonResolutionTypeConvergenceCriteria(object):
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
        'tolerance': 'float'
    }

    attribute_map = {
        'type': 'type',
        'tolerance': 'tolerance'
    }

    discriminator_value_class_map = {
        'RELATIVE': 'RelativeConvergenceCriteria',
        'ABSOLUTE': 'AbsoluteConvergenceCriteria'
    }

    def __init__(self, type='ABSOLUTE', tolerance=None, local_vars_configuration=None):  # noqa: E501
        """OneOfNewtonResolutionTypeConvergenceCriteria - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._tolerance = None
        self.discriminator = 'type'

        self.type = type
        if tolerance is not None:
            self.tolerance = tolerance

    @property
    def type(self):
        """Gets the type of this OneOfNewtonResolutionTypeConvergenceCriteria.  # noqa: E501

        <p>Select the type of convergence criterion for the nonlinear solution method.</p> <br /><br />Important remarks: <br /><ul><li>Choose <b>absolute</b> if you want convergence to be reached when the maximum residual of all degrees of freedom of a given Newton iteration is lower than the given tolerance.</li><li>Choose <b>relative</b> if the same criteria as <b>absolute</b> will be checked but for the maximum relative residual i.e. maximum absolute residual divided by external force. Please note, if no external force is involved e.g. two far objects coming in contact, then using relative criteria will lead to singularity and convergence will not be attained.</li></ul>  Schema name: AbsoluteConvergenceCriteria  # noqa: E501

        :return: The type of this OneOfNewtonResolutionTypeConvergenceCriteria.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfNewtonResolutionTypeConvergenceCriteria.

        <p>Select the type of convergence criterion for the nonlinear solution method.</p> <br /><br />Important remarks: <br /><ul><li>Choose <b>absolute</b> if you want convergence to be reached when the maximum residual of all degrees of freedom of a given Newton iteration is lower than the given tolerance.</li><li>Choose <b>relative</b> if the same criteria as <b>absolute</b> will be checked but for the maximum relative residual i.e. maximum absolute residual divided by external force. Please note, if no external force is involved e.g. two far objects coming in contact, then using relative criteria will lead to singularity and convergence will not be attained.</li></ul>  Schema name: AbsoluteConvergenceCriteria  # noqa: E501

        :param type: The type of this OneOfNewtonResolutionTypeConvergenceCriteria.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def tolerance(self):
        """Gets the tolerance of this OneOfNewtonResolutionTypeConvergenceCriteria.  # noqa: E501

        <p>Set the threshold value for convergence detection for the relative convergence criteria. If the maximum relative error of all DOFs fall below this value the current time step is considered convergent.</p></p> <br /><br />Important remarks: <br /><ul><li>In most of the cases using a lower value for tolerance may lead to hard or no convergence. Therefore, it is always recommended to start with a higher value e.g. 10<sup>-3</sup> or 10<sup>-4</sup>. Please also note that increasing the threshold value may effect the solution results. </li></ul>  # noqa: E501

        :return: The tolerance of this OneOfNewtonResolutionTypeConvergenceCriteria.  # noqa: E501
        :rtype: float
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Sets the tolerance of this OneOfNewtonResolutionTypeConvergenceCriteria.

        <p>Set the threshold value for convergence detection for the relative convergence criteria. If the maximum relative error of all DOFs fall below this value the current time step is considered convergent.</p></p> <br /><br />Important remarks: <br /><ul><li>In most of the cases using a lower value for tolerance may lead to hard or no convergence. Therefore, it is always recommended to start with a higher value e.g. 10<sup>-3</sup> or 10<sup>-4</sup>. Please also note that increasing the threshold value may effect the solution results. </li></ul>  # noqa: E501

        :param tolerance: The tolerance of this OneOfNewtonResolutionTypeConvergenceCriteria.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                tolerance is not None and tolerance < 0):  # noqa: E501
            raise ValueError("Invalid value for `tolerance`, must be a value greater than or equal to `0`")  # noqa: E501

        self._tolerance = tolerance

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
        if not isinstance(other, OneOfNewtonResolutionTypeConvergenceCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfNewtonResolutionTypeConvergenceCriteria):
            return True

        return self.to_dict() != other.to_dict()
