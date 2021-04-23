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


class LayerAdditionHexDominantSnappy(object):
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
        'name': 'str',
        'layers': 'int',
        'expansion_ratio': 'float',
        'min_thickness': 'float',
        'first_layer_thickness': 'float',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'layers': 'layers',
        'expansion_ratio': 'expansionRatio',
        'min_thickness': 'minThickness',
        'first_layer_thickness': 'firstLayerThickness',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='LAYER_ADDITION_HEX_DOMINANT_SNAPPY', name=None, layers=None, expansion_ratio=None, min_thickness=None, first_layer_thickness=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """LayerAdditionHexDominantSnappy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._layers = None
        self._expansion_ratio = None
        self._min_thickness = None
        self._first_layer_thickness = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if layers is not None:
            self.layers = layers
        if expansion_ratio is not None:
            self.expansion_ratio = expansion_ratio
        if min_thickness is not None:
            self.min_thickness = min_thickness
        if first_layer_thickness is not None:
            self.first_layer_thickness = first_layer_thickness
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this LayerAdditionHexDominantSnappy.  # noqa: E501

        <a href='https://www.simscale.com/docs/simulation-setup/meshing/hex-dominant/#layers-refinement' target='_blank'><b>Inflated boundary layers</b></a> are used to resolve the boundary layer near walls (no-slip) which are in contact with the fluid. Using boundary layers is generally recommended for turbulent simulations.  Schema name: LayerAdditionHexDominantSnappy  # noqa: E501

        :return: The type of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LayerAdditionHexDominantSnappy.

        <a href='https://www.simscale.com/docs/simulation-setup/meshing/hex-dominant/#layers-refinement' target='_blank'><b>Inflated boundary layers</b></a> are used to resolve the boundary layer near walls (no-slip) which are in contact with the fluid. Using boundary layers is generally recommended for turbulent simulations.  Schema name: LayerAdditionHexDominantSnappy  # noqa: E501

        :param type: The type of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this LayerAdditionHexDominantSnappy.  # noqa: E501


        :return: The name of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LayerAdditionHexDominantSnappy.


        :param name: The name of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def layers(self):
        """Gets the layers of this LayerAdditionHexDominantSnappy.  # noqa: E501

        The number of <b>layers</b> defines how many boundary layers should be created.  # noqa: E501

        :return: The layers of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :rtype: int
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this LayerAdditionHexDominantSnappy.

        The number of <b>layers</b> defines how many boundary layers should be created.  # noqa: E501

        :param layers: The layers of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                layers is not None and layers < 0):  # noqa: E501
            raise ValueError("Invalid value for `layers`, must be a value greater than or equal to `0`")  # noqa: E501

        self._layers = layers

    @property
    def expansion_ratio(self):
        """Gets the expansion_ratio of this LayerAdditionHexDominantSnappy.  # noqa: E501

        <p>The <b>Expansion ratio</b> determines how the boundary layers grow in thickness from the wall to the internal mesh. The larger the ratio, the larger each cell layer will be in comparison to the neighbouring layer closer to the wall.</p><p><img src=\"/spec/resources/help/imgs/shm_bl_expansion-ratio.png\" class=\"helpPopupImage\"/> The figure shows a ratio of 1.3.</p>  # noqa: E501

        :return: The expansion_ratio of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :rtype: float
        """
        return self._expansion_ratio

    @expansion_ratio.setter
    def expansion_ratio(self, expansion_ratio):
        """Sets the expansion_ratio of this LayerAdditionHexDominantSnappy.

        <p>The <b>Expansion ratio</b> determines how the boundary layers grow in thickness from the wall to the internal mesh. The larger the ratio, the larger each cell layer will be in comparison to the neighbouring layer closer to the wall.</p><p><img src=\"/spec/resources/help/imgs/shm_bl_expansion-ratio.png\" class=\"helpPopupImage\"/> The figure shows a ratio of 1.3.</p>  # noqa: E501

        :param expansion_ratio: The expansion_ratio of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                expansion_ratio is not None and expansion_ratio < 0):  # noqa: E501
            raise ValueError("Invalid value for `expansion_ratio`, must be a value greater than or equal to `0`")  # noqa: E501

        self._expansion_ratio = expansion_ratio

    @property
    def min_thickness(self):
        """Gets the min_thickness of this LayerAdditionHexDominantSnappy.  # noqa: E501

        Specifies the <b>overall minimum thickness of all layers combined</b>. In case the overall thickness falls below this minimum thickness, no layers will be added for the affected areas.  # noqa: E501

        :return: The min_thickness of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :rtype: float
        """
        return self._min_thickness

    @min_thickness.setter
    def min_thickness(self, min_thickness):
        """Sets the min_thickness of this LayerAdditionHexDominantSnappy.

        Specifies the <b>overall minimum thickness of all layers combined</b>. In case the overall thickness falls below this minimum thickness, no layers will be added for the affected areas.  # noqa: E501

        :param min_thickness: The min_thickness of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                min_thickness is not None and min_thickness > 2):  # noqa: E501
            raise ValueError("Invalid value for `min_thickness`, must be a value less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_thickness is not None and min_thickness < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_thickness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_thickness = min_thickness

    @property
    def first_layer_thickness(self):
        """Gets the first_layer_thickness of this LayerAdditionHexDominantSnappy.  # noqa: E501

        Specifies the height (thickness) of the <b>first layer</b> that is closest to the surface. The first layer thickness is specified <b>relative</b> to the neighboring volume cell size after refinements.  # noqa: E501

        :return: The first_layer_thickness of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :rtype: float
        """
        return self._first_layer_thickness

    @first_layer_thickness.setter
    def first_layer_thickness(self, first_layer_thickness):
        """Sets the first_layer_thickness of this LayerAdditionHexDominantSnappy.

        Specifies the height (thickness) of the <b>first layer</b> that is closest to the surface. The first layer thickness is specified <b>relative</b> to the neighboring volume cell size after refinements.  # noqa: E501

        :param first_layer_thickness: The first_layer_thickness of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                first_layer_thickness is not None and first_layer_thickness < 0):  # noqa: E501
            raise ValueError("Invalid value for `first_layer_thickness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._first_layer_thickness = first_layer_thickness

    @property
    def topological_reference(self):
        """Gets the topological_reference of this LayerAdditionHexDominantSnappy.  # noqa: E501


        :return: The topological_reference of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this LayerAdditionHexDominantSnappy.


        :param topological_reference: The topological_reference of this LayerAdditionHexDominantSnappy.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

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
        if not isinstance(other, LayerAdditionHexDominantSnappy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LayerAdditionHexDominantSnappy):
            return True

        return self.to_dict() != other.to_dict()
