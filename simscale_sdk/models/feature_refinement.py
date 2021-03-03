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


class FeatureRefinement(object):
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
        'included_angle': 'DimensionalAngle',
        'distance_refinement_levels': 'list[RefinementLevel]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'included_angle': 'includedAngle',
        'distance_refinement_levels': 'distanceRefinementLevels'
    }

    def __init__(self, type='FEATURE', name=None, included_angle=None, distance_refinement_levels=None, local_vars_configuration=None):  # noqa: E501
        """FeatureRefinement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._included_angle = None
        self._distance_refinement_levels = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if included_angle is not None:
            self.included_angle = included_angle
        if distance_refinement_levels is not None:
            self.distance_refinement_levels = distance_refinement_levels

    @property
    def type(self):
        """Gets the type of this FeatureRefinement.  # noqa: E501


        :return: The type of this FeatureRefinement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FeatureRefinement.


        :param type: The type of this FeatureRefinement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this FeatureRefinement.  # noqa: E501


        :return: The name of this FeatureRefinement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureRefinement.


        :param name: The name of this FeatureRefinement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def included_angle(self):
        """Gets the included_angle of this FeatureRefinement.  # noqa: E501


        :return: The included_angle of this FeatureRefinement.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._included_angle

    @included_angle.setter
    def included_angle(self, included_angle):
        """Sets the included_angle of this FeatureRefinement.


        :param included_angle: The included_angle of this FeatureRefinement.  # noqa: E501
        :type: DimensionalAngle
        """

        self._included_angle = included_angle

    @property
    def distance_refinement_levels(self):
        """Gets the distance_refinement_levels of this FeatureRefinement.  # noqa: E501

        <p>This dynamic table allows you to add refinements to the mesh associated with the features (e.g. edges) in a specific distance to the features. Therefore specify the distance in the left box and the associated refinement level on the right (the higher, the finer). The pair (0,0) would mean that a refinement with level 0 would be introduced directly at the features of the mesh.</p>  # noqa: E501

        :return: The distance_refinement_levels of this FeatureRefinement.  # noqa: E501
        :rtype: list[RefinementLevel]
        """
        return self._distance_refinement_levels

    @distance_refinement_levels.setter
    def distance_refinement_levels(self, distance_refinement_levels):
        """Sets the distance_refinement_levels of this FeatureRefinement.

        <p>This dynamic table allows you to add refinements to the mesh associated with the features (e.g. edges) in a specific distance to the features. Therefore specify the distance in the left box and the associated refinement level on the right (the higher, the finer). The pair (0,0) would mean that a refinement with level 0 would be introduced directly at the features of the mesh.</p>  # noqa: E501

        :param distance_refinement_levels: The distance_refinement_levels of this FeatureRefinement.  # noqa: E501
        :type: list[RefinementLevel]
        """

        self._distance_refinement_levels = distance_refinement_levels

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
        if not isinstance(other, FeatureRefinement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeatureRefinement):
            return True

        return self.to_dict() != other.to_dict()
