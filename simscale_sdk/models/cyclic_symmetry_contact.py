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


class CyclicSymmetryContact(object):
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
        'enable_heat_transfer': 'str',
        'axis_origin': 'DimensionalVectorLength',
        'axis_direction': 'DimensionalVectorLength',
        'sector_angle': 'DimensionalAngle',
        'master_topological_reference': 'TopologicalReference',
        'slave_topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'enable_heat_transfer': 'enableHeatTransfer',
        'axis_origin': 'axisOrigin',
        'axis_direction': 'axisDirection',
        'sector_angle': 'sectorAngle',
        'master_topological_reference': 'masterTopologicalReference',
        'slave_topological_reference': 'slaveTopologicalReference'
    }

    def __init__(self, type='CYCLIC_SYMMETRY', name=None, enable_heat_transfer=None, axis_origin=None, axis_direction=None, sector_angle=None, master_topological_reference=None, slave_topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """CyclicSymmetryContact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._enable_heat_transfer = None
        self._axis_origin = None
        self._axis_direction = None
        self._sector_angle = None
        self._master_topological_reference = None
        self._slave_topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if enable_heat_transfer is not None:
            self.enable_heat_transfer = enable_heat_transfer
        if axis_origin is not None:
            self.axis_origin = axis_origin
        if axis_direction is not None:
            self.axis_direction = axis_direction
        if sector_angle is not None:
            self.sector_angle = sector_angle
        if master_topological_reference is not None:
            self.master_topological_reference = master_topological_reference
        if slave_topological_reference is not None:
            self.slave_topological_reference = slave_topological_reference

    @property
    def type(self):
        """Gets the type of this CyclicSymmetryContact.  # noqa: E501

        Schema name: CyclicSymmetryContact  # noqa: E501

        :return: The type of this CyclicSymmetryContact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CyclicSymmetryContact.

        Schema name: CyclicSymmetryContact  # noqa: E501

        :param type: The type of this CyclicSymmetryContact.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this CyclicSymmetryContact.  # noqa: E501


        :return: The name of this CyclicSymmetryContact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CyclicSymmetryContact.


        :param name: The name of this CyclicSymmetryContact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enable_heat_transfer(self):
        """Gets the enable_heat_transfer of this CyclicSymmetryContact.  # noqa: E501


        :return: The enable_heat_transfer of this CyclicSymmetryContact.  # noqa: E501
        :rtype: str
        """
        return self._enable_heat_transfer

    @enable_heat_transfer.setter
    def enable_heat_transfer(self, enable_heat_transfer):
        """Sets the enable_heat_transfer of this CyclicSymmetryContact.


        :param enable_heat_transfer: The enable_heat_transfer of this CyclicSymmetryContact.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO", "HEAT_TRANSFER_ONLY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and enable_heat_transfer not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `enable_heat_transfer` ({0}), must be one of {1}"  # noqa: E501
                .format(enable_heat_transfer, allowed_values)
            )

        self._enable_heat_transfer = enable_heat_transfer

    @property
    def axis_origin(self):
        """Gets the axis_origin of this CyclicSymmetryContact.  # noqa: E501


        :return: The axis_origin of this CyclicSymmetryContact.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._axis_origin

    @axis_origin.setter
    def axis_origin(self, axis_origin):
        """Sets the axis_origin of this CyclicSymmetryContact.


        :param axis_origin: The axis_origin of this CyclicSymmetryContact.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._axis_origin = axis_origin

    @property
    def axis_direction(self):
        """Gets the axis_direction of this CyclicSymmetryContact.  # noqa: E501


        :return: The axis_direction of this CyclicSymmetryContact.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._axis_direction

    @axis_direction.setter
    def axis_direction(self, axis_direction):
        """Sets the axis_direction of this CyclicSymmetryContact.


        :param axis_direction: The axis_direction of this CyclicSymmetryContact.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._axis_direction = axis_direction

    @property
    def sector_angle(self):
        """Gets the sector_angle of this CyclicSymmetryContact.  # noqa: E501


        :return: The sector_angle of this CyclicSymmetryContact.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._sector_angle

    @sector_angle.setter
    def sector_angle(self, sector_angle):
        """Sets the sector_angle of this CyclicSymmetryContact.


        :param sector_angle: The sector_angle of this CyclicSymmetryContact.  # noqa: E501
        :type: DimensionalAngle
        """

        self._sector_angle = sector_angle

    @property
    def master_topological_reference(self):
        """Gets the master_topological_reference of this CyclicSymmetryContact.  # noqa: E501


        :return: The master_topological_reference of this CyclicSymmetryContact.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._master_topological_reference

    @master_topological_reference.setter
    def master_topological_reference(self, master_topological_reference):
        """Sets the master_topological_reference of this CyclicSymmetryContact.


        :param master_topological_reference: The master_topological_reference of this CyclicSymmetryContact.  # noqa: E501
        :type: TopologicalReference
        """

        self._master_topological_reference = master_topological_reference

    @property
    def slave_topological_reference(self):
        """Gets the slave_topological_reference of this CyclicSymmetryContact.  # noqa: E501


        :return: The slave_topological_reference of this CyclicSymmetryContact.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._slave_topological_reference

    @slave_topological_reference.setter
    def slave_topological_reference(self, slave_topological_reference):
        """Sets the slave_topological_reference of this CyclicSymmetryContact.


        :param slave_topological_reference: The slave_topological_reference of this CyclicSymmetryContact.  # noqa: E501
        :type: TopologicalReference
        """

        self._slave_topological_reference = slave_topological_reference

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
        if not isinstance(other, CyclicSymmetryContact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CyclicSymmetryContact):
            return True

        return self.to_dict() != other.to_dict()
