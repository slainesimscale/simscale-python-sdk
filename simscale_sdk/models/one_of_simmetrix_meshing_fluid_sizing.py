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


class OneOfSimmetrixMeshingFluidSizing(object):
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
        'fineness': 'float',
        'maximum_edge_length': 'DimensionalLength',
        'minimum_edge_length': 'DimensionalLength',
        'chordal_error': 'float',
        'min_curv_ref': 'float',
        'gradation_rate': 'float',
        'prox_ref_factor': 'float',
        'min_prox_size': 'DimensionalLength',
        'small_feature_tol': 'float',
        'layer_adjustment_behaviour': 'str',
        'layer_height_gradation_rate': 'float',
        'surf_skewness': 'float',
        'vol_len_ratio': 'float'
    }

    attribute_map = {
        'type': 'type',
        'fineness': 'fineness',
        'maximum_edge_length': 'maximumEdgeLength',
        'minimum_edge_length': 'minimumEdgeLength',
        'chordal_error': 'chordalError',
        'min_curv_ref': 'minCurvRef',
        'gradation_rate': 'gradationRate',
        'prox_ref_factor': 'proxRefFactor',
        'min_prox_size': 'minProxSize',
        'small_feature_tol': 'smallFeatureTol',
        'layer_adjustment_behaviour': 'layerAdjustmentBehaviour',
        'layer_height_gradation_rate': 'layerHeightGradationRate',
        'surf_skewness': 'surfSkewness',
        'vol_len_ratio': 'volLenRatio'
    }

    discriminator_value_class_map = {
        'AUTOMATIC_V9': 'AutomaticMeshSizingSimmetrix',
        'MANUAL': 'ManualMeshSizingSimmetrix',
        'DEBUG': 'DebugMeshSizingSimmetrix'
    }

    def __init__(self, type='DEBUG', fineness=None, maximum_edge_length=None, minimum_edge_length=None, chordal_error=None, min_curv_ref=None, gradation_rate=None, prox_ref_factor=None, min_prox_size=None, small_feature_tol=None, layer_adjustment_behaviour=None, layer_height_gradation_rate=None, surf_skewness=None, vol_len_ratio=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSimmetrixMeshingFluidSizing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._fineness = None
        self._maximum_edge_length = None
        self._minimum_edge_length = None
        self._chordal_error = None
        self._min_curv_ref = None
        self._gradation_rate = None
        self._prox_ref_factor = None
        self._min_prox_size = None
        self._small_feature_tol = None
        self._layer_adjustment_behaviour = None
        self._layer_height_gradation_rate = None
        self._surf_skewness = None
        self._vol_len_ratio = None
        self.discriminator = 'type'

        self.type = type
        if fineness is not None:
            self.fineness = fineness
        if maximum_edge_length is not None:
            self.maximum_edge_length = maximum_edge_length
        if minimum_edge_length is not None:
            self.minimum_edge_length = minimum_edge_length
        if chordal_error is not None:
            self.chordal_error = chordal_error
        if min_curv_ref is not None:
            self.min_curv_ref = min_curv_ref
        if gradation_rate is not None:
            self.gradation_rate = gradation_rate
        if prox_ref_factor is not None:
            self.prox_ref_factor = prox_ref_factor
        if min_prox_size is not None:
            self.min_prox_size = min_prox_size
        if small_feature_tol is not None:
            self.small_feature_tol = small_feature_tol
        if layer_adjustment_behaviour is not None:
            self.layer_adjustment_behaviour = layer_adjustment_behaviour
        if layer_height_gradation_rate is not None:
            self.layer_height_gradation_rate = layer_height_gradation_rate
        if surf_skewness is not None:
            self.surf_skewness = surf_skewness
        if vol_len_ratio is not None:
            self.vol_len_ratio = vol_len_ratio

    @property
    def type(self):
        """Gets the type of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The type of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSimmetrixMeshingFluidSizing.


        :param type: The type of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fineness(self):
        """Gets the fineness of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501

        <p>Adjust the overall mesh sizing from coarse (value: 0) to fine (10).</p>  # noqa: E501

        :return: The fineness of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._fineness

    @fineness.setter
    def fineness(self, fineness):
        """Sets the fineness of this OneOfSimmetrixMeshingFluidSizing.

        <p>Adjust the overall mesh sizing from coarse (value: 0) to fine (10).</p>  # noqa: E501

        :param fineness: The fineness of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                fineness is not None and fineness > 10):  # noqa: E501
            raise ValueError("Invalid value for `fineness`, must be a value less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fineness is not None and fineness < 0):  # noqa: E501
            raise ValueError("Invalid value for `fineness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fineness = fineness

    @property
    def maximum_edge_length(self):
        """Gets the maximum_edge_length of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The maximum_edge_length of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._maximum_edge_length

    @maximum_edge_length.setter
    def maximum_edge_length(self, maximum_edge_length):
        """Sets the maximum_edge_length of this OneOfSimmetrixMeshingFluidSizing.


        :param maximum_edge_length: The maximum_edge_length of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: DimensionalLength
        """

        self._maximum_edge_length = maximum_edge_length

    @property
    def minimum_edge_length(self):
        """Gets the minimum_edge_length of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The minimum_edge_length of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._minimum_edge_length

    @minimum_edge_length.setter
    def minimum_edge_length(self, minimum_edge_length):
        """Sets the minimum_edge_length of this OneOfSimmetrixMeshingFluidSizing.


        :param minimum_edge_length: The minimum_edge_length of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: DimensionalLength
        """

        self._minimum_edge_length = minimum_edge_length

    @property
    def chordal_error(self):
        """Gets the chordal_error of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The chordal_error of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._chordal_error

    @chordal_error.setter
    def chordal_error(self, chordal_error):
        """Sets the chordal_error of this OneOfSimmetrixMeshingFluidSizing.


        :param chordal_error: The chordal_error of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                chordal_error is not None and chordal_error > 0.5):  # noqa: E501
            raise ValueError("Invalid value for `chordal_error`, must be a value less than or equal to `0.5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                chordal_error is not None and chordal_error < 0):  # noqa: E501
            raise ValueError("Invalid value for `chordal_error`, must be a value greater than or equal to `0`")  # noqa: E501

        self._chordal_error = chordal_error

    @property
    def min_curv_ref(self):
        """Gets the min_curv_ref of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The min_curv_ref of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._min_curv_ref

    @min_curv_ref.setter
    def min_curv_ref(self, min_curv_ref):
        """Sets the min_curv_ref of this OneOfSimmetrixMeshingFluidSizing.


        :param min_curv_ref: The min_curv_ref of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                min_curv_ref is not None and min_curv_ref < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_curv_ref`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_curv_ref = min_curv_ref

    @property
    def gradation_rate(self):
        """Gets the gradation_rate of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The gradation_rate of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._gradation_rate

    @gradation_rate.setter
    def gradation_rate(self, gradation_rate):
        """Sets the gradation_rate of this OneOfSimmetrixMeshingFluidSizing.


        :param gradation_rate: The gradation_rate of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                gradation_rate is not None and gradation_rate < 0):  # noqa: E501
            raise ValueError("Invalid value for `gradation_rate`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gradation_rate = gradation_rate

    @property
    def prox_ref_factor(self):
        """Gets the prox_ref_factor of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The prox_ref_factor of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._prox_ref_factor

    @prox_ref_factor.setter
    def prox_ref_factor(self, prox_ref_factor):
        """Sets the prox_ref_factor of this OneOfSimmetrixMeshingFluidSizing.


        :param prox_ref_factor: The prox_ref_factor of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                prox_ref_factor is not None and prox_ref_factor > 4):  # noqa: E501
            raise ValueError("Invalid value for `prox_ref_factor`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                prox_ref_factor is not None and prox_ref_factor < 0):  # noqa: E501
            raise ValueError("Invalid value for `prox_ref_factor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prox_ref_factor = prox_ref_factor

    @property
    def min_prox_size(self):
        """Gets the min_prox_size of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The min_prox_size of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._min_prox_size

    @min_prox_size.setter
    def min_prox_size(self, min_prox_size):
        """Sets the min_prox_size of this OneOfSimmetrixMeshingFluidSizing.


        :param min_prox_size: The min_prox_size of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: DimensionalLength
        """

        self._min_prox_size = min_prox_size

    @property
    def small_feature_tol(self):
        """Gets the small_feature_tol of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The small_feature_tol of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._small_feature_tol

    @small_feature_tol.setter
    def small_feature_tol(self, small_feature_tol):
        """Sets the small_feature_tol of this OneOfSimmetrixMeshingFluidSizing.


        :param small_feature_tol: The small_feature_tol of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                small_feature_tol is not None and small_feature_tol < 0):  # noqa: E501
            raise ValueError("Invalid value for `small_feature_tol`, must be a value greater than or equal to `0`")  # noqa: E501

        self._small_feature_tol = small_feature_tol

    @property
    def layer_adjustment_behaviour(self):
        """Gets the layer_adjustment_behaviour of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The layer_adjustment_behaviour of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: str
        """
        return self._layer_adjustment_behaviour

    @layer_adjustment_behaviour.setter
    def layer_adjustment_behaviour(self, layer_adjustment_behaviour):
        """Sets the layer_adjustment_behaviour of this OneOfSimmetrixMeshingFluidSizing.


        :param layer_adjustment_behaviour: The layer_adjustment_behaviour of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: str
        """
        allowed_values = ["SHRINKING", "TRIMMING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and layer_adjustment_behaviour not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `layer_adjustment_behaviour` ({0}), must be one of {1}"  # noqa: E501
                .format(layer_adjustment_behaviour, allowed_values)
            )

        self._layer_adjustment_behaviour = layer_adjustment_behaviour

    @property
    def layer_height_gradation_rate(self):
        """Gets the layer_height_gradation_rate of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The layer_height_gradation_rate of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._layer_height_gradation_rate

    @layer_height_gradation_rate.setter
    def layer_height_gradation_rate(self, layer_height_gradation_rate):
        """Sets the layer_height_gradation_rate of this OneOfSimmetrixMeshingFluidSizing.


        :param layer_height_gradation_rate: The layer_height_gradation_rate of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                layer_height_gradation_rate is not None and layer_height_gradation_rate < 0):  # noqa: E501
            raise ValueError("Invalid value for `layer_height_gradation_rate`, must be a value greater than or equal to `0`")  # noqa: E501

        self._layer_height_gradation_rate = layer_height_gradation_rate

    @property
    def surf_skewness(self):
        """Gets the surf_skewness of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The surf_skewness of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._surf_skewness

    @surf_skewness.setter
    def surf_skewness(self, surf_skewness):
        """Sets the surf_skewness of this OneOfSimmetrixMeshingFluidSizing.


        :param surf_skewness: The surf_skewness of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                surf_skewness is not None and surf_skewness < 0):  # noqa: E501
            raise ValueError("Invalid value for `surf_skewness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._surf_skewness = surf_skewness

    @property
    def vol_len_ratio(self):
        """Gets the vol_len_ratio of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501


        :return: The vol_len_ratio of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :rtype: float
        """
        return self._vol_len_ratio

    @vol_len_ratio.setter
    def vol_len_ratio(self, vol_len_ratio):
        """Sets the vol_len_ratio of this OneOfSimmetrixMeshingFluidSizing.


        :param vol_len_ratio: The vol_len_ratio of this OneOfSimmetrixMeshingFluidSizing.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                vol_len_ratio is not None and vol_len_ratio < 0):  # noqa: E501
            raise ValueError("Invalid value for `vol_len_ratio`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vol_len_ratio = vol_len_ratio

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, OneOfSimmetrixMeshingFluidSizing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSimmetrixMeshingFluidSizing):
            return True

        return self.to_dict() != other.to_dict()
