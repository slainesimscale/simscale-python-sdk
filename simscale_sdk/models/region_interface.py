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


class RegionInterface(object):
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
        'interface_thermal': 'OneOfRegionInterfaceInterfaceThermal',
        'master_topological_reference': 'TopologicalReference',
        'slave_topological_reference': 'TopologicalReference',
        'is_partial': 'bool',
        'custom_modified': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'interface_thermal': 'interfaceThermal',
        'master_topological_reference': 'masterTopologicalReference',
        'slave_topological_reference': 'slaveTopologicalReference',
        'is_partial': 'isPartial',
        'custom_modified': 'customModified'
    }

    def __init__(self, type='REGION_INTERFACE', name=None, interface_thermal=None, master_topological_reference=None, slave_topological_reference=None, is_partial=None, custom_modified=None, local_vars_configuration=None):  # noqa: E501
        """RegionInterface - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._interface_thermal = None
        self._master_topological_reference = None
        self._slave_topological_reference = None
        self._is_partial = None
        self._custom_modified = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if interface_thermal is not None:
            self.interface_thermal = interface_thermal
        if master_topological_reference is not None:
            self.master_topological_reference = master_topological_reference
        if slave_topological_reference is not None:
            self.slave_topological_reference = slave_topological_reference
        if is_partial is not None:
            self.is_partial = is_partial
        if custom_modified is not None:
            self.custom_modified = custom_modified

    @property
    def type(self):
        """Gets the type of this RegionInterface.  # noqa: E501

        Schema name: RegionInterface  # noqa: E501

        :return: The type of this RegionInterface.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RegionInterface.

        Schema name: RegionInterface  # noqa: E501

        :param type: The type of this RegionInterface.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this RegionInterface.  # noqa: E501


        :return: The name of this RegionInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegionInterface.


        :param name: The name of this RegionInterface.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def interface_thermal(self):
        """Gets the interface_thermal of this RegionInterface.  # noqa: E501


        :return: The interface_thermal of this RegionInterface.  # noqa: E501
        :rtype: OneOfRegionInterfaceInterfaceThermal
        """
        return self._interface_thermal

    @interface_thermal.setter
    def interface_thermal(self, interface_thermal):
        """Sets the interface_thermal of this RegionInterface.


        :param interface_thermal: The interface_thermal of this RegionInterface.  # noqa: E501
        :type: OneOfRegionInterfaceInterfaceThermal
        """

        self._interface_thermal = interface_thermal

    @property
    def master_topological_reference(self):
        """Gets the master_topological_reference of this RegionInterface.  # noqa: E501


        :return: The master_topological_reference of this RegionInterface.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._master_topological_reference

    @master_topological_reference.setter
    def master_topological_reference(self, master_topological_reference):
        """Sets the master_topological_reference of this RegionInterface.


        :param master_topological_reference: The master_topological_reference of this RegionInterface.  # noqa: E501
        :type: TopologicalReference
        """

        self._master_topological_reference = master_topological_reference

    @property
    def slave_topological_reference(self):
        """Gets the slave_topological_reference of this RegionInterface.  # noqa: E501


        :return: The slave_topological_reference of this RegionInterface.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._slave_topological_reference

    @slave_topological_reference.setter
    def slave_topological_reference(self, slave_topological_reference):
        """Sets the slave_topological_reference of this RegionInterface.


        :param slave_topological_reference: The slave_topological_reference of this RegionInterface.  # noqa: E501
        :type: TopologicalReference
        """

        self._slave_topological_reference = slave_topological_reference

    @property
    def is_partial(self):
        """Gets the is_partial of this RegionInterface.  # noqa: E501


        :return: The is_partial of this RegionInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_partial

    @is_partial.setter
    def is_partial(self, is_partial):
        """Sets the is_partial of this RegionInterface.


        :param is_partial: The is_partial of this RegionInterface.  # noqa: E501
        :type: bool
        """

        self._is_partial = is_partial

    @property
    def custom_modified(self):
        """Gets the custom_modified of this RegionInterface.  # noqa: E501


        :return: The custom_modified of this RegionInterface.  # noqa: E501
        :rtype: bool
        """
        return self._custom_modified

    @custom_modified.setter
    def custom_modified(self, custom_modified):
        """Sets the custom_modified of this RegionInterface.


        :param custom_modified: The custom_modified of this RegionInterface.  # noqa: E501
        :type: bool
        """

        self._custom_modified = custom_modified

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
        if not isinstance(other, RegionInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegionInterface):
            return True

        return self.to_dict() != other.to_dict()
