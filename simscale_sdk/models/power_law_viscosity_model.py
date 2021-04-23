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


class PowerLawViscosityModel(object):
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
        'k': 'DimensionalKinematicViscosity',
        'n': 'DimensionalDimensionless',
        'nu_min': 'DimensionalKinematicViscosity',
        'nu_max': 'DimensionalKinematicViscosity'
    }

    attribute_map = {
        'type': 'type',
        'k': 'k',
        'n': 'n',
        'nu_min': 'nuMin',
        'nu_max': 'nuMax'
    }

    def __init__(self, type='POWER_LAW', k=None, n=None, nu_min=None, nu_max=None, local_vars_configuration=None):  # noqa: E501
        """PowerLawViscosityModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._k = None
        self._n = None
        self._nu_min = None
        self._nu_max = None
        self.discriminator = None

        self.type = type
        if k is not None:
            self.k = k
        if n is not None:
            self.n = n
        if nu_min is not None:
            self.nu_min = nu_min
        if nu_max is not None:
            self.nu_max = nu_max

    @property
    def type(self):
        """Gets the type of this PowerLawViscosityModel.  # noqa: E501

        Choose between <a href='https://www.simscale.com/docs/simulation-setup/materials/#newtonian-model' target='_blank'>Newtonian</a> and <a href='https://www.simscale.com/docs/simulation-setup/materials/non-newtonian-models/' target='_blank'>Non-Newtonian</a> viscosity models.  Schema name: PowerLawViscosityModel  # noqa: E501

        :return: The type of this PowerLawViscosityModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PowerLawViscosityModel.

        Choose between <a href='https://www.simscale.com/docs/simulation-setup/materials/#newtonian-model' target='_blank'>Newtonian</a> and <a href='https://www.simscale.com/docs/simulation-setup/materials/non-newtonian-models/' target='_blank'>Non-Newtonian</a> viscosity models.  Schema name: PowerLawViscosityModel  # noqa: E501

        :param type: The type of this PowerLawViscosityModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def k(self):
        """Gets the k of this PowerLawViscosityModel.  # noqa: E501


        :return: The k of this PowerLawViscosityModel.  # noqa: E501
        :rtype: DimensionalKinematicViscosity
        """
        return self._k

    @k.setter
    def k(self, k):
        """Sets the k of this PowerLawViscosityModel.


        :param k: The k of this PowerLawViscosityModel.  # noqa: E501
        :type: DimensionalKinematicViscosity
        """

        self._k = k

    @property
    def n(self):
        """Gets the n of this PowerLawViscosityModel.  # noqa: E501


        :return: The n of this PowerLawViscosityModel.  # noqa: E501
        :rtype: DimensionalDimensionless
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this PowerLawViscosityModel.


        :param n: The n of this PowerLawViscosityModel.  # noqa: E501
        :type: DimensionalDimensionless
        """

        self._n = n

    @property
    def nu_min(self):
        """Gets the nu_min of this PowerLawViscosityModel.  # noqa: E501


        :return: The nu_min of this PowerLawViscosityModel.  # noqa: E501
        :rtype: DimensionalKinematicViscosity
        """
        return self._nu_min

    @nu_min.setter
    def nu_min(self, nu_min):
        """Sets the nu_min of this PowerLawViscosityModel.


        :param nu_min: The nu_min of this PowerLawViscosityModel.  # noqa: E501
        :type: DimensionalKinematicViscosity
        """

        self._nu_min = nu_min

    @property
    def nu_max(self):
        """Gets the nu_max of this PowerLawViscosityModel.  # noqa: E501


        :return: The nu_max of this PowerLawViscosityModel.  # noqa: E501
        :rtype: DimensionalKinematicViscosity
        """
        return self._nu_max

    @nu_max.setter
    def nu_max(self, nu_max):
        """Sets the nu_max of this PowerLawViscosityModel.


        :param nu_max: The nu_max of this PowerLawViscosityModel.  # noqa: E501
        :type: DimensionalKinematicViscosity
        """

        self._nu_max = nu_max

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
        if not isinstance(other, PowerLawViscosityModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PowerLawViscosityModel):
            return True

        return self.to_dict() != other.to_dict()
