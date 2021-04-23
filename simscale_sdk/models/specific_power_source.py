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


class SpecificPowerSource(object):
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
        'heat_flux': 'DimensionalFunctionVolumetricPower',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'heat_flux': 'heatFlux',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids'
    }

    def __init__(self, type='SPECIFIC_V23', name=None, heat_flux=None, topological_reference=None, geometry_primitive_uuids=None, local_vars_configuration=None):  # noqa: E501
        """SpecificPowerSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._heat_flux = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if heat_flux is not None:
            self.heat_flux = heat_flux
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def type(self):
        """Gets the type of this SpecificPowerSource.  # noqa: E501

        Schema name: SpecificPowerSource  # noqa: E501

        :return: The type of this SpecificPowerSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpecificPowerSource.

        Schema name: SpecificPowerSource  # noqa: E501

        :param type: The type of this SpecificPowerSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this SpecificPowerSource.  # noqa: E501


        :return: The name of this SpecificPowerSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SpecificPowerSource.


        :param name: The name of this SpecificPowerSource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def heat_flux(self):
        """Gets the heat_flux of this SpecificPowerSource.  # noqa: E501


        :return: The heat_flux of this SpecificPowerSource.  # noqa: E501
        :rtype: DimensionalFunctionVolumetricPower
        """
        return self._heat_flux

    @heat_flux.setter
    def heat_flux(self, heat_flux):
        """Sets the heat_flux of this SpecificPowerSource.


        :param heat_flux: The heat_flux of this SpecificPowerSource.  # noqa: E501
        :type: DimensionalFunctionVolumetricPower
        """

        self._heat_flux = heat_flux

    @property
    def topological_reference(self):
        """Gets the topological_reference of this SpecificPowerSource.  # noqa: E501


        :return: The topological_reference of this SpecificPowerSource.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this SpecificPowerSource.


        :param topological_reference: The topological_reference of this SpecificPowerSource.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this SpecificPowerSource.  # noqa: E501


        :return: The geometry_primitive_uuids of this SpecificPowerSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this SpecificPowerSource.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this SpecificPowerSource.  # noqa: E501
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
        if not isinstance(other, SpecificPowerSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpecificPowerSource):
            return True

        return self.to_dict() != other.to_dict()
