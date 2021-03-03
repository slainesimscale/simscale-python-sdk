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


class EigenModeVerification(object):
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
        'stop_error': 'bool',
        'threshold': 'float',
        'precision_shift': 'float'
    }

    attribute_map = {
        'stop_error': 'stopError',
        'threshold': 'threshold',
        'precision_shift': 'precisionShift'
    }

    def __init__(self, stop_error=None, threshold=None, precision_shift=None, local_vars_configuration=None):  # noqa: E501
        """EigenModeVerification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stop_error = None
        self._threshold = None
        self._precision_shift = None
        self.discriminator = None

        if stop_error is not None:
            self.stop_error = stop_error
        if threshold is not None:
            self.threshold = threshold
        if precision_shift is not None:
            self.precision_shift = precision_shift

    @property
    def stop_error(self):
        """Gets the stop_error of this EigenModeVerification.  # noqa: E501


        :return: The stop_error of this EigenModeVerification.  # noqa: E501
        :rtype: bool
        """
        return self._stop_error

    @stop_error.setter
    def stop_error(self, stop_error):
        """Sets the stop_error of this EigenModeVerification.


        :param stop_error: The stop_error of this EigenModeVerification.  # noqa: E501
        :type: bool
        """

        self._stop_error = stop_error

    @property
    def threshold(self):
        """Gets the threshold of this EigenModeVerification.  # noqa: E501


        :return: The threshold of this EigenModeVerification.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this EigenModeVerification.


        :param threshold: The threshold of this EigenModeVerification.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                threshold is not None and threshold < 0):  # noqa: E501
            raise ValueError("Invalid value for `threshold`, must be a value greater than or equal to `0`")  # noqa: E501

        self._threshold = threshold

    @property
    def precision_shift(self):
        """Gets the precision_shift of this EigenModeVerification.  # noqa: E501


        :return: The precision_shift of this EigenModeVerification.  # noqa: E501
        :rtype: float
        """
        return self._precision_shift

    @precision_shift.setter
    def precision_shift(self, precision_shift):
        """Sets the precision_shift of this EigenModeVerification.


        :param precision_shift: The precision_shift of this EigenModeVerification.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                precision_shift is not None and precision_shift < 0):  # noqa: E501
            raise ValueError("Invalid value for `precision_shift`, must be a value greater than or equal to `0`")  # noqa: E501

        self._precision_shift = precision_shift

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
        if not isinstance(other, EigenModeVerification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EigenModeVerification):
            return True

        return self.to_dict() != other.to_dict()
