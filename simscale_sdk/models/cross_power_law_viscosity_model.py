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


class CrossPowerLawViscosityModel(object):
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
        'nu0': 'DimensionalKinematicViscosity',
        'nu_inf': 'DimensionalKinematicViscosity',
        'm': 'DimensionalTime',
        'n': 'DimensionalDimensionless'
    }

    attribute_map = {
        'type': 'type',
        'nu0': 'nu0',
        'nu_inf': 'nuInf',
        'm': 'm',
        'n': 'n'
    }

    def __init__(self, type='CROSS_POWER_LAW', nu0=None, nu_inf=None, m=None, n=None, local_vars_configuration=None):  # noqa: E501
        """CrossPowerLawViscosityModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._nu0 = None
        self._nu_inf = None
        self._m = None
        self._n = None
        self.discriminator = None

        self.type = type
        if nu0 is not None:
            self.nu0 = nu0
        if nu_inf is not None:
            self.nu_inf = nu_inf
        if m is not None:
            self.m = m
        if n is not None:
            self.n = n

    @property
    def type(self):
        """Gets the type of this CrossPowerLawViscosityModel.  # noqa: E501

        Choose between <a href='https://www.simscale.com/docs/simulation-setup/materials/#newtonian-model' target='_blank'>Newtonian</a> and <a href='https://www.simscale.com/docs/simulation-setup/materials/non-newtonian-models/' target='_blank'>Non-Newtonian</a> viscosity models.  Schema name: CrossPowerLawViscosityModel  # noqa: E501

        :return: The type of this CrossPowerLawViscosityModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CrossPowerLawViscosityModel.

        Choose between <a href='https://www.simscale.com/docs/simulation-setup/materials/#newtonian-model' target='_blank'>Newtonian</a> and <a href='https://www.simscale.com/docs/simulation-setup/materials/non-newtonian-models/' target='_blank'>Non-Newtonian</a> viscosity models.  Schema name: CrossPowerLawViscosityModel  # noqa: E501

        :param type: The type of this CrossPowerLawViscosityModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def nu0(self):
        """Gets the nu0 of this CrossPowerLawViscosityModel.  # noqa: E501


        :return: The nu0 of this CrossPowerLawViscosityModel.  # noqa: E501
        :rtype: DimensionalKinematicViscosity
        """
        return self._nu0

    @nu0.setter
    def nu0(self, nu0):
        """Sets the nu0 of this CrossPowerLawViscosityModel.


        :param nu0: The nu0 of this CrossPowerLawViscosityModel.  # noqa: E501
        :type: DimensionalKinematicViscosity
        """

        self._nu0 = nu0

    @property
    def nu_inf(self):
        """Gets the nu_inf of this CrossPowerLawViscosityModel.  # noqa: E501


        :return: The nu_inf of this CrossPowerLawViscosityModel.  # noqa: E501
        :rtype: DimensionalKinematicViscosity
        """
        return self._nu_inf

    @nu_inf.setter
    def nu_inf(self, nu_inf):
        """Sets the nu_inf of this CrossPowerLawViscosityModel.


        :param nu_inf: The nu_inf of this CrossPowerLawViscosityModel.  # noqa: E501
        :type: DimensionalKinematicViscosity
        """

        self._nu_inf = nu_inf

    @property
    def m(self):
        """Gets the m of this CrossPowerLawViscosityModel.  # noqa: E501


        :return: The m of this CrossPowerLawViscosityModel.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._m

    @m.setter
    def m(self, m):
        """Sets the m of this CrossPowerLawViscosityModel.


        :param m: The m of this CrossPowerLawViscosityModel.  # noqa: E501
        :type: DimensionalTime
        """

        self._m = m

    @property
    def n(self):
        """Gets the n of this CrossPowerLawViscosityModel.  # noqa: E501


        :return: The n of this CrossPowerLawViscosityModel.  # noqa: E501
        :rtype: DimensionalDimensionless
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this CrossPowerLawViscosityModel.


        :param n: The n of this CrossPowerLawViscosityModel.  # noqa: E501
        :type: DimensionalDimensionless
        """

        self._n = n

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
        if not isinstance(other, CrossPowerLawViscosityModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossPowerLawViscosityModel):
            return True

        return self.to_dict() != other.to_dict()
