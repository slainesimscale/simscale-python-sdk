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


class ManualSimericsMeshSettings(object):
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
        'minimum_cell_size': 'DimensionalLength',
        'maximum_cell_size': 'DimensionalLength',
        'cell_size_on_surfaces': 'DimensionalLength',
        'enable_growth_rate': 'bool',
        'growth_rate': 'int'
    }

    attribute_map = {
        'type': 'type',
        'minimum_cell_size': 'minimumCellSize',
        'maximum_cell_size': 'maximumCellSize',
        'cell_size_on_surfaces': 'cellSizeOnSurfaces',
        'enable_growth_rate': 'enableGrowthRate',
        'growth_rate': 'growthRate'
    }

    def __init__(self, type='MANUAL_SETTINGS', minimum_cell_size=None, maximum_cell_size=None, cell_size_on_surfaces=None, enable_growth_rate=None, growth_rate=None, local_vars_configuration=None):  # noqa: E501
        """ManualSimericsMeshSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._minimum_cell_size = None
        self._maximum_cell_size = None
        self._cell_size_on_surfaces = None
        self._enable_growth_rate = None
        self._growth_rate = None
        self.discriminator = None

        self.type = type
        if minimum_cell_size is not None:
            self.minimum_cell_size = minimum_cell_size
        if maximum_cell_size is not None:
            self.maximum_cell_size = maximum_cell_size
        if cell_size_on_surfaces is not None:
            self.cell_size_on_surfaces = cell_size_on_surfaces
        if enable_growth_rate is not None:
            self.enable_growth_rate = enable_growth_rate
        if growth_rate is not None:
            self.growth_rate = growth_rate

    @property
    def type(self):
        """Gets the type of this ManualSimericsMeshSettings.  # noqa: E501

        Schema name: ManualSimericsMeshSettings  # noqa: E501

        :return: The type of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ManualSimericsMeshSettings.

        Schema name: ManualSimericsMeshSettings  # noqa: E501

        :param type: The type of this ManualSimericsMeshSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def minimum_cell_size(self):
        """Gets the minimum_cell_size of this ManualSimericsMeshSettings.  # noqa: E501


        :return: The minimum_cell_size of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._minimum_cell_size

    @minimum_cell_size.setter
    def minimum_cell_size(self, minimum_cell_size):
        """Sets the minimum_cell_size of this ManualSimericsMeshSettings.


        :param minimum_cell_size: The minimum_cell_size of this ManualSimericsMeshSettings.  # noqa: E501
        :type: DimensionalLength
        """

        self._minimum_cell_size = minimum_cell_size

    @property
    def maximum_cell_size(self):
        """Gets the maximum_cell_size of this ManualSimericsMeshSettings.  # noqa: E501


        :return: The maximum_cell_size of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._maximum_cell_size

    @maximum_cell_size.setter
    def maximum_cell_size(self, maximum_cell_size):
        """Sets the maximum_cell_size of this ManualSimericsMeshSettings.


        :param maximum_cell_size: The maximum_cell_size of this ManualSimericsMeshSettings.  # noqa: E501
        :type: DimensionalLength
        """

        self._maximum_cell_size = maximum_cell_size

    @property
    def cell_size_on_surfaces(self):
        """Gets the cell_size_on_surfaces of this ManualSimericsMeshSettings.  # noqa: E501


        :return: The cell_size_on_surfaces of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._cell_size_on_surfaces

    @cell_size_on_surfaces.setter
    def cell_size_on_surfaces(self, cell_size_on_surfaces):
        """Sets the cell_size_on_surfaces of this ManualSimericsMeshSettings.


        :param cell_size_on_surfaces: The cell_size_on_surfaces of this ManualSimericsMeshSettings.  # noqa: E501
        :type: DimensionalLength
        """

        self._cell_size_on_surfaces = cell_size_on_surfaces

    @property
    def enable_growth_rate(self):
        """Gets the enable_growth_rate of this ManualSimericsMeshSettings.  # noqa: E501


        :return: The enable_growth_rate of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_growth_rate

    @enable_growth_rate.setter
    def enable_growth_rate(self, enable_growth_rate):
        """Sets the enable_growth_rate of this ManualSimericsMeshSettings.


        :param enable_growth_rate: The enable_growth_rate of this ManualSimericsMeshSettings.  # noqa: E501
        :type: bool
        """

        self._enable_growth_rate = enable_growth_rate

    @property
    def growth_rate(self):
        """Gets the growth_rate of this ManualSimericsMeshSettings.  # noqa: E501

        The <i>Growth rate</i> defines the cell size ratio between interior cell size and surface cell size. It needs to be <b>a whole number</b> always greater than 1 and smaller or equal to 8, such that the cell size increases towards the interior of the mesh.  # noqa: E501

        :return: The growth_rate of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: int
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, growth_rate):
        """Sets the growth_rate of this ManualSimericsMeshSettings.

        The <i>Growth rate</i> defines the cell size ratio between interior cell size and surface cell size. It needs to be <b>a whole number</b> always greater than 1 and smaller or equal to 8, such that the cell size increases towards the interior of the mesh.  # noqa: E501

        :param growth_rate: The growth_rate of this ManualSimericsMeshSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                growth_rate is not None and growth_rate > 8):  # noqa: E501
            raise ValueError("Invalid value for `growth_rate`, must be a value less than or equal to `8`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                growth_rate is not None and growth_rate < 1):  # noqa: E501
            raise ValueError("Invalid value for `growth_rate`, must be a value greater than or equal to `1`")  # noqa: E501

        self._growth_rate = growth_rate

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
        if not isinstance(other, ManualSimericsMeshSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManualSimericsMeshSettings):
            return True

        return self.to_dict() != other.to_dict()
