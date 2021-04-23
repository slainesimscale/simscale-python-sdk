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


class SimmetrixBoundaryLayerRefinement(object):
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
        'number_of_layers': 'int',
        'total_relative_thickness': 'float',
        'layer_type': 'OneOfSimmetrixBoundaryLayerRefinementLayerType',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'number_of_layers': 'numberOfLayers',
        'total_relative_thickness': 'totalRelativeThickness',
        'layer_type': 'layerType',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='SIMMETRIX_BOUNDARY_LAYER_V13', name=None, number_of_layers=None, total_relative_thickness=None, layer_type=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """SimmetrixBoundaryLayerRefinement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._number_of_layers = None
        self._total_relative_thickness = None
        self._layer_type = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if number_of_layers is not None:
            self.number_of_layers = number_of_layers
        if total_relative_thickness is not None:
            self.total_relative_thickness = total_relative_thickness
        if layer_type is not None:
            self.layer_type = layer_type
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this SimmetrixBoundaryLayerRefinement.  # noqa: E501

        <p><a href='https://www.simscale.com/docs/simulation-setup/meshing/standard/#layer-inflation' target='_blank'><b>Layer inflation</b></a> allows the creation of prismatic boundary layers for certain mesh regions.</p><p>Prismatic layers are mostly used in CFD simulations on no-slip walls in order to efficiently capture the boundary layer velocity profile, but they may be also used in certain structural simulations like stamping or deep-drawing processes.</p><p><img src=\"/spec/resources/help/imgs/simmetrix-layers.png\" class=\"helpPopupImage\"/> The figure shows a sample mesh with boundary layers added.</p>  Schema name: SimmetrixBoundaryLayerRefinement  # noqa: E501

        :return: The type of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimmetrixBoundaryLayerRefinement.

        <p><a href='https://www.simscale.com/docs/simulation-setup/meshing/standard/#layer-inflation' target='_blank'><b>Layer inflation</b></a> allows the creation of prismatic boundary layers for certain mesh regions.</p><p>Prismatic layers are mostly used in CFD simulations on no-slip walls in order to efficiently capture the boundary layer velocity profile, but they may be also used in certain structural simulations like stamping or deep-drawing processes.</p><p><img src=\"/spec/resources/help/imgs/simmetrix-layers.png\" class=\"helpPopupImage\"/> The figure shows a sample mesh with boundary layers added.</p>  Schema name: SimmetrixBoundaryLayerRefinement  # noqa: E501

        :param type: The type of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this SimmetrixBoundaryLayerRefinement.  # noqa: E501


        :return: The name of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimmetrixBoundaryLayerRefinement.


        :param name: The name of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_of_layers(self):
        """Gets the number_of_layers of this SimmetrixBoundaryLayerRefinement.  # noqa: E501

        The <i>Number of layers</i> defines how many prismatic boundary layers should be created. 3 is default.  # noqa: E501

        :return: The number_of_layers of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :rtype: int
        """
        return self._number_of_layers

    @number_of_layers.setter
    def number_of_layers(self, number_of_layers):
        """Sets the number_of_layers of this SimmetrixBoundaryLayerRefinement.

        The <i>Number of layers</i> defines how many prismatic boundary layers should be created. 3 is default.  # noqa: E501

        :param number_of_layers: The number_of_layers of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_layers is not None and number_of_layers > 20):  # noqa: E501
            raise ValueError("Invalid value for `number_of_layers`, must be a value less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_layers is not None and number_of_layers < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_of_layers`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_layers = number_of_layers

    @property
    def total_relative_thickness(self):
        """Gets the total_relative_thickness of this SimmetrixBoundaryLayerRefinement.  # noqa: E501

        It defines the thickness of all prismatic boundary layers combined in relation to the local element size.<img src=\"/spec/resources/help/imgs/simmetrix-overall-layer-thickness.png\" class=\"helpPopupImage\"/>Example 3-layer thickness of 40% (0.4) of the local mesh size.  # noqa: E501

        :return: The total_relative_thickness of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :rtype: float
        """
        return self._total_relative_thickness

    @total_relative_thickness.setter
    def total_relative_thickness(self, total_relative_thickness):
        """Sets the total_relative_thickness of this SimmetrixBoundaryLayerRefinement.

        It defines the thickness of all prismatic boundary layers combined in relation to the local element size.<img src=\"/spec/resources/help/imgs/simmetrix-overall-layer-thickness.png\" class=\"helpPopupImage\"/>Example 3-layer thickness of 40% (0.4) of the local mesh size.  # noqa: E501

        :param total_relative_thickness: The total_relative_thickness of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :type: float
        """

        self._total_relative_thickness = total_relative_thickness

    @property
    def layer_type(self):
        """Gets the layer_type of this SimmetrixBoundaryLayerRefinement.  # noqa: E501


        :return: The layer_type of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :rtype: OneOfSimmetrixBoundaryLayerRefinementLayerType
        """
        return self._layer_type

    @layer_type.setter
    def layer_type(self, layer_type):
        """Sets the layer_type of this SimmetrixBoundaryLayerRefinement.


        :param layer_type: The layer_type of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :type: OneOfSimmetrixBoundaryLayerRefinementLayerType
        """

        self._layer_type = layer_type

    @property
    def topological_reference(self):
        """Gets the topological_reference of this SimmetrixBoundaryLayerRefinement.  # noqa: E501


        :return: The topological_reference of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this SimmetrixBoundaryLayerRefinement.


        :param topological_reference: The topological_reference of this SimmetrixBoundaryLayerRefinement.  # noqa: E501
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
        if not isinstance(other, SimmetrixBoundaryLayerRefinement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimmetrixBoundaryLayerRefinement):
            return True

        return self.to_dict() != other.to_dict()
