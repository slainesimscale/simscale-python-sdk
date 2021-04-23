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


class OneOfAutomaticLayerOnLayerType(object):
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
        'first_layer_size': 'DimensionalLength',
        'growth_rate': 'float'
    }

    attribute_map = {
        'type': 'type',
        'first_layer_size': 'firstLayerSize',
        'growth_rate': 'growthRate'
    }

    discriminator_value_class_map = {
        'FRACTIONAL_HEIGHT_1': 'FractionalHeight1',
        'FRACTIONAL_HEIGHT_2': 'FractionalHeight2'
    }

    def __init__(self, type='FRACTIONAL_HEIGHT_2', first_layer_size=None, growth_rate=None, local_vars_configuration=None):  # noqa: E501
        """OneOfAutomaticLayerOnLayerType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._first_layer_size = None
        self._growth_rate = None
        self.discriminator = 'type'

        self.type = type
        if first_layer_size is not None:
            self.first_layer_size = first_layer_size
        if growth_rate is not None:
            self.growth_rate = growth_rate

    @property
    def type(self):
        """Gets the type of this OneOfAutomaticLayerOnLayerType.  # noqa: E501

        Schema name: FractionalHeight2  # noqa: E501

        :return: The type of this OneOfAutomaticLayerOnLayerType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfAutomaticLayerOnLayerType.

        Schema name: FractionalHeight2  # noqa: E501

        :param type: The type of this OneOfAutomaticLayerOnLayerType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def first_layer_size(self):
        """Gets the first_layer_size of this OneOfAutomaticLayerOnLayerType.  # noqa: E501


        :return: The first_layer_size of this OneOfAutomaticLayerOnLayerType.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._first_layer_size

    @first_layer_size.setter
    def first_layer_size(self, first_layer_size):
        """Sets the first_layer_size of this OneOfAutomaticLayerOnLayerType.


        :param first_layer_size: The first_layer_size of this OneOfAutomaticLayerOnLayerType.  # noqa: E501
        :type: DimensionalLength
        """

        self._first_layer_size = first_layer_size

    @property
    def growth_rate(self):
        """Gets the growth_rate of this OneOfAutomaticLayerOnLayerType.  # noqa: E501

        The <i>Growth rate</i> defines the thickness ratio between adjacent boundary layer cells. It needs to be always greater than 1 such that the layer thickness increases towards the interior of the mesh. For the same number of layers and overall thickness the larger the growth rate is inversely proportional to the first cell thickness. <img src=\"/spec/resources/help/imgs/simmetrix-layer-growth-rate.png\" class=\"helpPopupImage\"/>Example of each cell being 1.5 times thicker than its adjacent.  # noqa: E501

        :return: The growth_rate of this OneOfAutomaticLayerOnLayerType.  # noqa: E501
        :rtype: float
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, growth_rate):
        """Sets the growth_rate of this OneOfAutomaticLayerOnLayerType.

        The <i>Growth rate</i> defines the thickness ratio between adjacent boundary layer cells. It needs to be always greater than 1 such that the layer thickness increases towards the interior of the mesh. For the same number of layers and overall thickness the larger the growth rate is inversely proportional to the first cell thickness. <img src=\"/spec/resources/help/imgs/simmetrix-layer-growth-rate.png\" class=\"helpPopupImage\"/>Example of each cell being 1.5 times thicker than its adjacent.  # noqa: E501

        :param growth_rate: The growth_rate of this OneOfAutomaticLayerOnLayerType.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                growth_rate is not None and growth_rate < 1):  # noqa: E501
            raise ValueError("Invalid value for `growth_rate`, must be a value greater than or equal to `1`")  # noqa: E501

        self._growth_rate = growth_rate

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
        if not isinstance(other, OneOfAutomaticLayerOnLayerType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfAutomaticLayerOnLayerType):
            return True

        return self.to_dict() != other.to_dict()
