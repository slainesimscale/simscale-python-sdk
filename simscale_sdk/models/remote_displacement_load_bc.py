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


class RemoteDisplacementLoadBC(object):
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
        'displacement': 'DimensionalPartialVectorFunctionLength',
        'rotation': 'DimensionalPartialVectorFunctionAngle',
        'external_point': 'DimensionalVectorLength',
        'deformation_behavior': 'str',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'displacement': 'displacement',
        'rotation': 'rotation',
        'external_point': 'externalPoint',
        'deformation_behavior': 'deformationBehavior',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='REMOTE_DISPLACEMENT_LOAD', name=None, displacement=None, rotation=None, external_point=None, deformation_behavior=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """RemoteDisplacementLoadBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._displacement = None
        self._rotation = None
        self._external_point = None
        self._deformation_behavior = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if displacement is not None:
            self.displacement = displacement
        if rotation is not None:
            self.rotation = rotation
        if external_point is not None:
            self.external_point = external_point
        if deformation_behavior is not None:
            self.deformation_behavior = deformation_behavior
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this RemoteDisplacementLoadBC.  # noqa: E501

        This boundary condition restrains the displacement of a face or edge relative to a specified remote point. Therefore the assignment is connected to the remote point with RBE3 (deformable) or MPC (undeformable) conditions and the defined constraints are applied to the remote point.<br /><br />Important remarks: <br /><ul><li>As the assignments are connected to the remote point, additional constraints on these nodes may lead to overconstrained systems.</li><li>If the number of nodes of the assigment is large (>1000> it is recommended to use the <b>MUMPS</b> or <b>PETSC</b> solver.</li><i>This boundary condition is only valid for small rotations. For large rotations, please use <b>Rotating motion</b> boundary conditions.</i></ul>   Schema name: RemoteDisplacementLoadBC  # noqa: E501

        :return: The type of this RemoteDisplacementLoadBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RemoteDisplacementLoadBC.

        This boundary condition restrains the displacement of a face or edge relative to a specified remote point. Therefore the assignment is connected to the remote point with RBE3 (deformable) or MPC (undeformable) conditions and the defined constraints are applied to the remote point.<br /><br />Important remarks: <br /><ul><li>As the assignments are connected to the remote point, additional constraints on these nodes may lead to overconstrained systems.</li><li>If the number of nodes of the assigment is large (>1000> it is recommended to use the <b>MUMPS</b> or <b>PETSC</b> solver.</li><i>This boundary condition is only valid for small rotations. For large rotations, please use <b>Rotating motion</b> boundary conditions.</i></ul>   Schema name: RemoteDisplacementLoadBC  # noqa: E501

        :param type: The type of this RemoteDisplacementLoadBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this RemoteDisplacementLoadBC.  # noqa: E501


        :return: The name of this RemoteDisplacementLoadBC.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RemoteDisplacementLoadBC.


        :param name: The name of this RemoteDisplacementLoadBC.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def displacement(self):
        """Gets the displacement of this RemoteDisplacementLoadBC.  # noqa: E501


        :return: The displacement of this RemoteDisplacementLoadBC.  # noqa: E501
        :rtype: DimensionalPartialVectorFunctionLength
        """
        return self._displacement

    @displacement.setter
    def displacement(self, displacement):
        """Sets the displacement of this RemoteDisplacementLoadBC.


        :param displacement: The displacement of this RemoteDisplacementLoadBC.  # noqa: E501
        :type: DimensionalPartialVectorFunctionLength
        """

        self._displacement = displacement

    @property
    def rotation(self):
        """Gets the rotation of this RemoteDisplacementLoadBC.  # noqa: E501


        :return: The rotation of this RemoteDisplacementLoadBC.  # noqa: E501
        :rtype: DimensionalPartialVectorFunctionAngle
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this RemoteDisplacementLoadBC.


        :param rotation: The rotation of this RemoteDisplacementLoadBC.  # noqa: E501
        :type: DimensionalPartialVectorFunctionAngle
        """

        self._rotation = rotation

    @property
    def external_point(self):
        """Gets the external_point of this RemoteDisplacementLoadBC.  # noqa: E501


        :return: The external_point of this RemoteDisplacementLoadBC.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._external_point

    @external_point.setter
    def external_point(self, external_point):
        """Sets the external_point of this RemoteDisplacementLoadBC.


        :param external_point: The external_point of this RemoteDisplacementLoadBC.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._external_point = external_point

    @property
    def deformation_behavior(self):
        """Gets the deformation_behavior of this RemoteDisplacementLoadBC.  # noqa: E501

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entitiy is allowed to deform, selecting <b>undeformable</b> leads to a rigid entity.</p>  # noqa: E501

        :return: The deformation_behavior of this RemoteDisplacementLoadBC.  # noqa: E501
        :rtype: str
        """
        return self._deformation_behavior

    @deformation_behavior.setter
    def deformation_behavior(self, deformation_behavior):
        """Sets the deformation_behavior of this RemoteDisplacementLoadBC.

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entitiy is allowed to deform, selecting <b>undeformable</b> leads to a rigid entity.</p>  # noqa: E501

        :param deformation_behavior: The deformation_behavior of this RemoteDisplacementLoadBC.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFORMABLE", "UNDEFORMABLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deformation_behavior not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deformation_behavior` ({0}), must be one of {1}"  # noqa: E501
                .format(deformation_behavior, allowed_values)
            )

        self._deformation_behavior = deformation_behavior

    @property
    def topological_reference(self):
        """Gets the topological_reference of this RemoteDisplacementLoadBC.  # noqa: E501


        :return: The topological_reference of this RemoteDisplacementLoadBC.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this RemoteDisplacementLoadBC.


        :param topological_reference: The topological_reference of this RemoteDisplacementLoadBC.  # noqa: E501
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
        if not isinstance(other, RemoteDisplacementLoadBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteDisplacementLoadBC):
            return True

        return self.to_dict() != other.to_dict()
