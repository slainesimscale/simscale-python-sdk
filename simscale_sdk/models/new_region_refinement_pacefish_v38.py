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


class NewRegionRefinementPacefishV38(object):
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
        'mesh_sizing': 'OneOfNewRegionRefinementPacefishV38MeshSizing',
        'geometry_primitive_uuids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'mesh_sizing': 'meshSizing',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids'
    }

    def __init__(self, type='REGION_PACEFISH_V38', name=None, mesh_sizing=None, geometry_primitive_uuids=None, local_vars_configuration=None):  # noqa: E501
        """NewRegionRefinementPacefishV38 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._mesh_sizing = None
        self._geometry_primitive_uuids = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if mesh_sizing is not None:
            self.mesh_sizing = mesh_sizing
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def type(self):
        """Gets the type of this NewRegionRefinementPacefishV38.  # noqa: E501

        Schema name: NewRegionRefinementPacefishV38  # noqa: E501

        :return: The type of this NewRegionRefinementPacefishV38.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NewRegionRefinementPacefishV38.

        Schema name: NewRegionRefinementPacefishV38  # noqa: E501

        :param type: The type of this NewRegionRefinementPacefishV38.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this NewRegionRefinementPacefishV38.  # noqa: E501


        :return: The name of this NewRegionRefinementPacefishV38.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewRegionRefinementPacefishV38.


        :param name: The name of this NewRegionRefinementPacefishV38.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mesh_sizing(self):
        """Gets the mesh_sizing of this NewRegionRefinementPacefishV38.  # noqa: E501


        :return: The mesh_sizing of this NewRegionRefinementPacefishV38.  # noqa: E501
        :rtype: OneOfNewRegionRefinementPacefishV38MeshSizing
        """
        return self._mesh_sizing

    @mesh_sizing.setter
    def mesh_sizing(self, mesh_sizing):
        """Sets the mesh_sizing of this NewRegionRefinementPacefishV38.


        :param mesh_sizing: The mesh_sizing of this NewRegionRefinementPacefishV38.  # noqa: E501
        :type: OneOfNewRegionRefinementPacefishV38MeshSizing
        """

        self._mesh_sizing = mesh_sizing

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this NewRegionRefinementPacefishV38.  # noqa: E501


        :return: The geometry_primitive_uuids of this NewRegionRefinementPacefishV38.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this NewRegionRefinementPacefishV38.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this NewRegionRefinementPacefishV38.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

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
        if not isinstance(other, NewRegionRefinementPacefishV38):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewRegionRefinementPacefishV38):
            return True

        return self.to_dict() != other.to_dict()
