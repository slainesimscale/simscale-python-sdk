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


class SurfaceRefinement(object):
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
        'min_level': 'int',
        'max_level': 'int',
        'cell_zone': 'OneOfSurfaceRefinementCellZone',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'min_level': 'minLevel',
        'max_level': 'maxLevel',
        'cell_zone': 'cellZone',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='SURFACE_V3', name=None, min_level=None, max_level=None, cell_zone=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """SurfaceRefinement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._min_level = None
        self._max_level = None
        self._cell_zone = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if min_level is not None:
            self.min_level = min_level
        if max_level is not None:
            self.max_level = max_level
        if cell_zone is not None:
            self.cell_zone = cell_zone
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this SurfaceRefinement.  # noqa: E501

        A <a href='https://www.simscale.com/docs/simulation-setup/meshing/hex-dominant/#surface-refinement' target='_blank'><b>surface refinement</b></a> can be used to refine the mesh near the surfaces of assigned faces and/or solids. A surface refinement can also be used to create a <u>cell zone</u>.  Schema name: SurfaceRefinement  # noqa: E501

        :return: The type of this SurfaceRefinement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SurfaceRefinement.

        A <a href='https://www.simscale.com/docs/simulation-setup/meshing/hex-dominant/#surface-refinement' target='_blank'><b>surface refinement</b></a> can be used to refine the mesh near the surfaces of assigned faces and/or solids. A surface refinement can also be used to create a <u>cell zone</u>.  Schema name: SurfaceRefinement  # noqa: E501

        :param type: The type of this SurfaceRefinement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this SurfaceRefinement.  # noqa: E501


        :return: The name of this SurfaceRefinement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SurfaceRefinement.


        :param name: The name of this SurfaceRefinement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def min_level(self):
        """Gets the min_level of this SurfaceRefinement.  # noqa: E501

        <p>Specify surface-wise the minimum refinement level for this surface.</p>  # noqa: E501

        :return: The min_level of this SurfaceRefinement.  # noqa: E501
        :rtype: int
        """
        return self._min_level

    @min_level.setter
    def min_level(self, min_level):
        """Sets the min_level of this SurfaceRefinement.

        <p>Specify surface-wise the minimum refinement level for this surface.</p>  # noqa: E501

        :param min_level: The min_level of this SurfaceRefinement.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                min_level is not None and min_level < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_level = min_level

    @property
    def max_level(self):
        """Gets the max_level of this SurfaceRefinement.  # noqa: E501

        <p>Specify surface-wise the maximum refinement level for this surface.</p>  # noqa: E501

        :return: The max_level of this SurfaceRefinement.  # noqa: E501
        :rtype: int
        """
        return self._max_level

    @max_level.setter
    def max_level(self, max_level):
        """Sets the max_level of this SurfaceRefinement.

        <p>Specify surface-wise the maximum refinement level for this surface.</p>  # noqa: E501

        :param max_level: The max_level of this SurfaceRefinement.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_level is not None and max_level < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_level = max_level

    @property
    def cell_zone(self):
        """Gets the cell_zone of this SurfaceRefinement.  # noqa: E501


        :return: The cell_zone of this SurfaceRefinement.  # noqa: E501
        :rtype: OneOfSurfaceRefinementCellZone
        """
        return self._cell_zone

    @cell_zone.setter
    def cell_zone(self, cell_zone):
        """Sets the cell_zone of this SurfaceRefinement.


        :param cell_zone: The cell_zone of this SurfaceRefinement.  # noqa: E501
        :type: OneOfSurfaceRefinementCellZone
        """

        self._cell_zone = cell_zone

    @property
    def topological_reference(self):
        """Gets the topological_reference of this SurfaceRefinement.  # noqa: E501


        :return: The topological_reference of this SurfaceRefinement.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this SurfaceRefinement.


        :param topological_reference: The topological_reference of this SurfaceRefinement.  # noqa: E501
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
        if not isinstance(other, SurfaceRefinement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SurfaceRefinement):
            return True

        return self.to_dict() != other.to_dict()
