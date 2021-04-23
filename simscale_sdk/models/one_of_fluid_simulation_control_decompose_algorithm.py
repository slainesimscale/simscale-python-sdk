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


class OneOfFluidSimulationControlDecomposeAlgorithm(object):
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
        'decomposition_order': 'str',
        'delta': 'float',
        'num_subdomain_x': 'int',
        'num_subdomain_y': 'int',
        'num_subdomain_z': 'int'
    }

    attribute_map = {
        'type': 'type',
        'decomposition_order': 'decompositionOrder',
        'delta': 'delta',
        'num_subdomain_x': 'numSubdomainX',
        'num_subdomain_y': 'numSubdomainY',
        'num_subdomain_z': 'numSubdomainZ'
    }

    discriminator_value_class_map = {
        'SCOTCH': 'ScotchDecomposeAlgorithm',
        'HIERARCHICAL': 'HierarchicalDecomposeAlgorithm',
        'SIMPLE': 'SimpleDecomposeAlgorithm'
    }

    def __init__(self, type='SIMPLE', decomposition_order=None, delta=None, num_subdomain_x=None, num_subdomain_y=None, num_subdomain_z=None, local_vars_configuration=None):  # noqa: E501
        """OneOfFluidSimulationControlDecomposeAlgorithm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._decomposition_order = None
        self._delta = None
        self._num_subdomain_x = None
        self._num_subdomain_y = None
        self._num_subdomain_z = None
        self.discriminator = 'type'

        self.type = type
        if decomposition_order is not None:
            self.decomposition_order = decomposition_order
        if delta is not None:
            self.delta = delta
        if num_subdomain_x is not None:
            self.num_subdomain_x = num_subdomain_x
        if num_subdomain_y is not None:
            self.num_subdomain_y = num_subdomain_y
        if num_subdomain_z is not None:
            self.num_subdomain_z = num_subdomain_z

    @property
    def type(self):
        """Gets the type of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501

        Schema name: SimpleDecomposeAlgorithm  # noqa: E501

        :return: The type of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfFluidSimulationControlDecomposeAlgorithm.

        Schema name: SimpleDecomposeAlgorithm  # noqa: E501

        :param type: The type of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def decomposition_order(self):
        """Gets the decomposition_order of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501

        <p>Choose the order of domain decomposition .</p>  # noqa: E501

        :return: The decomposition_order of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :rtype: str
        """
        return self._decomposition_order

    @decomposition_order.setter
    def decomposition_order(self, decomposition_order):
        """Sets the decomposition_order of this OneOfFluidSimulationControlDecomposeAlgorithm.

        <p>Choose the order of domain decomposition .</p>  # noqa: E501

        :param decomposition_order: The decomposition_order of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :type: str
        """
        allowed_values = ["XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and decomposition_order not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `decomposition_order` ({0}), must be one of {1}"  # noqa: E501
                .format(decomposition_order, allowed_values)
            )

        self._decomposition_order = decomposition_order

    @property
    def delta(self):
        """Gets the delta of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501

        Delta is cell skew factor. It represents the cell skewness allowed at the decomposed domain boundaries and is generally kept below 10^{-2}. <a href='https://www.simscale.com/docs/simulation-setup/simulation-control/' target='_blank'>Learn more</a>.  # noqa: E501

        :return: The delta of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :rtype: float
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this OneOfFluidSimulationControlDecomposeAlgorithm.

        Delta is cell skew factor. It represents the cell skewness allowed at the decomposed domain boundaries and is generally kept below 10^{-2}. <a href='https://www.simscale.com/docs/simulation-setup/simulation-control/' target='_blank'>Learn more</a>.  # noqa: E501

        :param delta: The delta of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                delta is not None and delta < 0):  # noqa: E501
            raise ValueError("Invalid value for `delta`, must be a value greater than or equal to `0`")  # noqa: E501

        self._delta = delta

    @property
    def num_subdomain_x(self):
        """Gets the num_subdomain_x of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501

        <p>Define the number of subdomains the mesh is split into in the specific direction.</p>  # noqa: E501

        :return: The num_subdomain_x of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :rtype: int
        """
        return self._num_subdomain_x

    @num_subdomain_x.setter
    def num_subdomain_x(self, num_subdomain_x):
        """Sets the num_subdomain_x of this OneOfFluidSimulationControlDecomposeAlgorithm.

        <p>Define the number of subdomains the mesh is split into in the specific direction.</p>  # noqa: E501

        :param num_subdomain_x: The num_subdomain_x of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_subdomain_x is not None and num_subdomain_x < 1):  # noqa: E501
            raise ValueError("Invalid value for `num_subdomain_x`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_subdomain_x = num_subdomain_x

    @property
    def num_subdomain_y(self):
        """Gets the num_subdomain_y of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501

        <p>Define the number of subdomains the mesh is split into in the specific direction.</p>  # noqa: E501

        :return: The num_subdomain_y of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :rtype: int
        """
        return self._num_subdomain_y

    @num_subdomain_y.setter
    def num_subdomain_y(self, num_subdomain_y):
        """Sets the num_subdomain_y of this OneOfFluidSimulationControlDecomposeAlgorithm.

        <p>Define the number of subdomains the mesh is split into in the specific direction.</p>  # noqa: E501

        :param num_subdomain_y: The num_subdomain_y of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_subdomain_y is not None and num_subdomain_y < 1):  # noqa: E501
            raise ValueError("Invalid value for `num_subdomain_y`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_subdomain_y = num_subdomain_y

    @property
    def num_subdomain_z(self):
        """Gets the num_subdomain_z of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501

        <p>Define the number of subdomains the mesh is split into in the specific direction.</p>  # noqa: E501

        :return: The num_subdomain_z of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :rtype: int
        """
        return self._num_subdomain_z

    @num_subdomain_z.setter
    def num_subdomain_z(self, num_subdomain_z):
        """Sets the num_subdomain_z of this OneOfFluidSimulationControlDecomposeAlgorithm.

        <p>Define the number of subdomains the mesh is split into in the specific direction.</p>  # noqa: E501

        :param num_subdomain_z: The num_subdomain_z of this OneOfFluidSimulationControlDecomposeAlgorithm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_subdomain_z is not None and num_subdomain_z < 1):  # noqa: E501
            raise ValueError("Invalid value for `num_subdomain_z`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_subdomain_z = num_subdomain_z

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
        if not isinstance(other, OneOfFluidSimulationControlDecomposeAlgorithm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfFluidSimulationControlDecomposeAlgorithm):
            return True

        return self.to_dict() != other.to_dict()
