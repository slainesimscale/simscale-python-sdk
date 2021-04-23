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


class InitialTimestepsWriteControl(object):
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
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type='INITIAL', local_vars_configuration=None):  # noqa: E501
        """InitialTimestepsWriteControl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self.discriminator = None

        self.type = type

    @property
    def type(self):
        """Gets the type of this InitialTimestepsWriteControl.  # noqa: E501

        <p>Define how frequently intermediate results should be saved. With the selection of <b>initial time steps</b> only the user defined time steps are stored in the result and by selecting <b>all computed time steps</b> also intermediate results that were created by the automatic time stepping are saved. With the selection of <b>write interval</b> a specific write frequency can be chosen which reduces the result size. Finally using <b>user defined time steps</b> there can either be a constant time increment for result storage given or a table with varying time intervals analogous to the <b>time step length</b> definition.</p>  Schema name: InitialTimestepsWriteControl  # noqa: E501

        :return: The type of this InitialTimestepsWriteControl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InitialTimestepsWriteControl.

        <p>Define how frequently intermediate results should be saved. With the selection of <b>initial time steps</b> only the user defined time steps are stored in the result and by selecting <b>all computed time steps</b> also intermediate results that were created by the automatic time stepping are saved. With the selection of <b>write interval</b> a specific write frequency can be chosen which reduces the result size. Finally using <b>user defined time steps</b> there can either be a constant time increment for result storage given or a table with varying time intervals analogous to the <b>time step length</b> definition.</p>  Schema name: InitialTimestepsWriteControl  # noqa: E501

        :param type: The type of this InitialTimestepsWriteControl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, InitialTimestepsWriteControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InitialTimestepsWriteControl):
            return True

        return self.to_dict() != other.to_dict()
