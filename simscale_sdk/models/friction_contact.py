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


class FrictionContact(object):
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
        'contact_solution_method': 'OneOfFrictionContactContactSolutionMethod',
        'friction_coefficient': 'OneOfFrictionContactFrictionCoefficient',
        'fictitious_clearance': 'OneOfFrictionContactFictitiousClearance',
        'master_topological_reference': 'TopologicalReference',
        'slave_topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'contact_solution_method': 'contactSolutionMethod',
        'friction_coefficient': 'frictionCoefficient',
        'fictitious_clearance': 'fictitiousClearance',
        'master_topological_reference': 'masterTopologicalReference',
        'slave_topological_reference': 'slaveTopologicalReference'
    }

    def __init__(self, type='FRICTION_CONTACT', name=None, contact_solution_method=None, friction_coefficient=None, fictitious_clearance=None, master_topological_reference=None, slave_topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """FrictionContact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._contact_solution_method = None
        self._friction_coefficient = None
        self._fictitious_clearance = None
        self._master_topological_reference = None
        self._slave_topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if contact_solution_method is not None:
            self.contact_solution_method = contact_solution_method
        if friction_coefficient is not None:
            self.friction_coefficient = friction_coefficient
        if fictitious_clearance is not None:
            self.fictitious_clearance = fictitious_clearance
        if master_topological_reference is not None:
            self.master_topological_reference = master_topological_reference
        if slave_topological_reference is not None:
            self.slave_topological_reference = slave_topological_reference

    @property
    def type(self):
        """Gets the type of this FrictionContact.  # noqa: E501

        Schema name: FrictionContact  # noqa: E501

        :return: The type of this FrictionContact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FrictionContact.

        Schema name: FrictionContact  # noqa: E501

        :param type: The type of this FrictionContact.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this FrictionContact.  # noqa: E501


        :return: The name of this FrictionContact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FrictionContact.


        :param name: The name of this FrictionContact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def contact_solution_method(self):
        """Gets the contact_solution_method of this FrictionContact.  # noqa: E501


        :return: The contact_solution_method of this FrictionContact.  # noqa: E501
        :rtype: OneOfFrictionContactContactSolutionMethod
        """
        return self._contact_solution_method

    @contact_solution_method.setter
    def contact_solution_method(self, contact_solution_method):
        """Sets the contact_solution_method of this FrictionContact.


        :param contact_solution_method: The contact_solution_method of this FrictionContact.  # noqa: E501
        :type: OneOfFrictionContactContactSolutionMethod
        """

        self._contact_solution_method = contact_solution_method

    @property
    def friction_coefficient(self):
        """Gets the friction_coefficient of this FrictionContact.  # noqa: E501


        :return: The friction_coefficient of this FrictionContact.  # noqa: E501
        :rtype: OneOfFrictionContactFrictionCoefficient
        """
        return self._friction_coefficient

    @friction_coefficient.setter
    def friction_coefficient(self, friction_coefficient):
        """Sets the friction_coefficient of this FrictionContact.


        :param friction_coefficient: The friction_coefficient of this FrictionContact.  # noqa: E501
        :type: OneOfFrictionContactFrictionCoefficient
        """

        self._friction_coefficient = friction_coefficient

    @property
    def fictitious_clearance(self):
        """Gets the fictitious_clearance of this FrictionContact.  # noqa: E501


        :return: The fictitious_clearance of this FrictionContact.  # noqa: E501
        :rtype: OneOfFrictionContactFictitiousClearance
        """
        return self._fictitious_clearance

    @fictitious_clearance.setter
    def fictitious_clearance(self, fictitious_clearance):
        """Sets the fictitious_clearance of this FrictionContact.


        :param fictitious_clearance: The fictitious_clearance of this FrictionContact.  # noqa: E501
        :type: OneOfFrictionContactFictitiousClearance
        """

        self._fictitious_clearance = fictitious_clearance

    @property
    def master_topological_reference(self):
        """Gets the master_topological_reference of this FrictionContact.  # noqa: E501


        :return: The master_topological_reference of this FrictionContact.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._master_topological_reference

    @master_topological_reference.setter
    def master_topological_reference(self, master_topological_reference):
        """Sets the master_topological_reference of this FrictionContact.


        :param master_topological_reference: The master_topological_reference of this FrictionContact.  # noqa: E501
        :type: TopologicalReference
        """

        self._master_topological_reference = master_topological_reference

    @property
    def slave_topological_reference(self):
        """Gets the slave_topological_reference of this FrictionContact.  # noqa: E501


        :return: The slave_topological_reference of this FrictionContact.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._slave_topological_reference

    @slave_topological_reference.setter
    def slave_topological_reference(self, slave_topological_reference):
        """Sets the slave_topological_reference of this FrictionContact.


        :param slave_topological_reference: The slave_topological_reference of this FrictionContact.  # noqa: E501
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
        if not isinstance(other, FrictionContact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FrictionContact):
            return True

        return self.to_dict() != other.to_dict()
