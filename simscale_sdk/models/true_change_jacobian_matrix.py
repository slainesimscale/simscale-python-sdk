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


class TrueChangeJacobianMatrix(object):
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
        'threshold_time_step_value': 'float',
        'matrix_reactualization_iteration': 'int',
        'max_newton_iterations': 'int'
    }

    attribute_map = {
        'type': 'type',
        'threshold_time_step_value': 'thresholdTimeStepValue',
        'matrix_reactualization_iteration': 'matrixReactualizationIteration',
        'max_newton_iterations': 'maxNewtonIterations'
    }

    def __init__(self, type='TRUE', threshold_time_step_value=None, matrix_reactualization_iteration=None, max_newton_iterations=None, local_vars_configuration=None):  # noqa: E501
        """TrueChangeJacobianMatrix - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._threshold_time_step_value = None
        self._matrix_reactualization_iteration = None
        self._max_newton_iterations = None
        self.discriminator = None

        self.type = type
        if threshold_time_step_value is not None:
            self.threshold_time_step_value = threshold_time_step_value
        if matrix_reactualization_iteration is not None:
            self.matrix_reactualization_iteration = matrix_reactualization_iteration
        if max_newton_iterations is not None:
            self.max_newton_iterations = max_newton_iterations

    @property
    def type(self):
        """Gets the type of this TrueChangeJacobianMatrix.  # noqa: E501

        <p>Choose if the Jacobian matrix should automatically change from tangent stiffnes matrix to elastic matrix if the time increment is falling below a given threshold. On the assumption that below a given time increment value the nonlinearities are not evolving within the time step one can strongly save computation time by switching to the elastic matrix.</p>  Schema name: TrueChangeJacobianMatrix  # noqa: E501

        :return: The type of this TrueChangeJacobianMatrix.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TrueChangeJacobianMatrix.

        <p>Choose if the Jacobian matrix should automatically change from tangent stiffnes matrix to elastic matrix if the time increment is falling below a given threshold. On the assumption that below a given time increment value the nonlinearities are not evolving within the time step one can strongly save computation time by switching to the elastic matrix.</p>  Schema name: TrueChangeJacobianMatrix  # noqa: E501

        :param type: The type of this TrueChangeJacobianMatrix.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def threshold_time_step_value(self):
        """Gets the threshold_time_step_value of this TrueChangeJacobianMatrix.  # noqa: E501

        <p>Set the threshold value of the Jacobian matrix changing. If the time increment is lower than this value the elastic matrix is used.</p>  # noqa: E501

        :return: The threshold_time_step_value of this TrueChangeJacobianMatrix.  # noqa: E501
        :rtype: float
        """
        return self._threshold_time_step_value

    @threshold_time_step_value.setter
    def threshold_time_step_value(self, threshold_time_step_value):
        """Sets the threshold_time_step_value of this TrueChangeJacobianMatrix.

        <p>Set the threshold value of the Jacobian matrix changing. If the time increment is lower than this value the elastic matrix is used.</p>  # noqa: E501

        :param threshold_time_step_value: The threshold_time_step_value of this TrueChangeJacobianMatrix.  # noqa: E501
        :type: float
        """

        self._threshold_time_step_value = threshold_time_step_value

    @property
    def matrix_reactualization_iteration(self):
        """Gets the matrix_reactualization_iteration of this TrueChangeJacobianMatrix.  # noqa: E501

        <p>Set how often the elastic stiffness matrix should be recomputed. If this parameter is set to 10, the elastic matrix is recomputed every 10th iteration within a given time step. If it is set to 0, the elastic stiffness matrix is not updated within any time step.</p>  # noqa: E501

        :return: The matrix_reactualization_iteration of this TrueChangeJacobianMatrix.  # noqa: E501
        :rtype: int
        """
        return self._matrix_reactualization_iteration

    @matrix_reactualization_iteration.setter
    def matrix_reactualization_iteration(self, matrix_reactualization_iteration):
        """Sets the matrix_reactualization_iteration of this TrueChangeJacobianMatrix.

        <p>Set how often the elastic stiffness matrix should be recomputed. If this parameter is set to 10, the elastic matrix is recomputed every 10th iteration within a given time step. If it is set to 0, the elastic stiffness matrix is not updated within any time step.</p>  # noqa: E501

        :param matrix_reactualization_iteration: The matrix_reactualization_iteration of this TrueChangeJacobianMatrix.  # noqa: E501
        :type: int
        """

        self._matrix_reactualization_iteration = matrix_reactualization_iteration

    @property
    def max_newton_iterations(self):
        """Gets the max_newton_iterations of this TrueChangeJacobianMatrix.  # noqa: E501

        <p>Maximum number of allowed Newton iterations per time increment. If this value is reached the simulation is considered non-converging. If an automatic time stepping is activated the time increment is reduced in order to reach convergence.</p>  # noqa: E501

        :return: The max_newton_iterations of this TrueChangeJacobianMatrix.  # noqa: E501
        :rtype: int
        """
        return self._max_newton_iterations

    @max_newton_iterations.setter
    def max_newton_iterations(self, max_newton_iterations):
        """Sets the max_newton_iterations of this TrueChangeJacobianMatrix.

        <p>Maximum number of allowed Newton iterations per time increment. If this value is reached the simulation is considered non-converging. If an automatic time stepping is activated the time increment is reduced in order to reach convergence.</p>  # noqa: E501

        :param max_newton_iterations: The max_newton_iterations of this TrueChangeJacobianMatrix.  # noqa: E501
        :type: int
        """

        self._max_newton_iterations = max_newton_iterations

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
        if not isinstance(other, TrueChangeJacobianMatrix):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrueChangeJacobianMatrix):
            return True

        return self.to_dict() != other.to_dict()
