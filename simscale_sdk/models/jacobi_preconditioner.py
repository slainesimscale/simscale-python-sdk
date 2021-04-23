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


class JacobiPreconditioner(object):
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
        'renumbering_method': 'str'
    }

    attribute_map = {
        'type': 'type',
        'renumbering_method': 'renumberingMethod'
    }

    def __init__(self, type='JACOBI', renumbering_method=None, local_vars_configuration=None):  # noqa: E501
        """JacobiPreconditioner - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._renumbering_method = None
        self.discriminator = None

        self.type = type
        if renumbering_method is not None:
            self.renumbering_method = renumbering_method

    @property
    def type(self):
        """Gets the type of this JacobiPreconditioner.  # noqa: E501

        Schema name: JacobiPreconditioner  # noqa: E501

        :return: The type of this JacobiPreconditioner.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JacobiPreconditioner.

        Schema name: JacobiPreconditioner  # noqa: E501

        :param type: The type of this JacobiPreconditioner.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def renumbering_method(self):
        """Gets the renumbering_method of this JacobiPreconditioner.  # noqa: E501

        Choose the renumbering method for the system matrix entries:<ul><li><p><b>RCMK</b> uses the algorithm of <i>Reverse Cuthill-MacKee</i> for the renumbering. It often effectively reduces the matrig storage space and the matrix factorization time.</p></ul><ul><li><p>When <b>inactive</b> is selected no renumbering is done. This option should only be chosen for testing purposes.</p></ul>  # noqa: E501

        :return: The renumbering_method of this JacobiPreconditioner.  # noqa: E501
        :rtype: str
        """
        return self._renumbering_method

    @renumbering_method.setter
    def renumbering_method(self, renumbering_method):
        """Sets the renumbering_method of this JacobiPreconditioner.

        Choose the renumbering method for the system matrix entries:<ul><li><p><b>RCMK</b> uses the algorithm of <i>Reverse Cuthill-MacKee</i> for the renumbering. It often effectively reduces the matrig storage space and the matrix factorization time.</p></ul><ul><li><p>When <b>inactive</b> is selected no renumbering is done. This option should only be chosen for testing purposes.</p></ul>  # noqa: E501

        :param renumbering_method: The renumbering_method of this JacobiPreconditioner.  # noqa: E501
        :type: str
        """
        allowed_values = ["RCMK", "INACTIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and renumbering_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `renumbering_method` ({0}), must be one of {1}"  # noqa: E501
                .format(renumbering_method, allowed_values)
            )

        self._renumbering_method = renumbering_method

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
        if not isinstance(other, JacobiPreconditioner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JacobiPreconditioner):
            return True

        return self.to_dict() != other.to_dict()
