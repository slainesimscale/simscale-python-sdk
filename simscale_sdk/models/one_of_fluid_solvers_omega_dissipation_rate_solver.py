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


class OneOfFluidSolversOmegaDissipationRateSolver(object):
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
        'absolute_tolerance': 'float',
        'relative_tolerance': 'float',
        'preconditioner': 'OneOfPBICGSolverPreconditioner',
        'smoother': 'str',
        'num_sweeps': 'int'
    }

    attribute_map = {
        'type': 'type',
        'absolute_tolerance': 'absoluteTolerance',
        'relative_tolerance': 'relativeTolerance',
        'preconditioner': 'preconditioner',
        'smoother': 'smoother',
        'num_sweeps': 'numSweeps'
    }

    discriminator_value_class_map = {
        'PBICG': 'PBICGSolver',
        'SMOOTH': 'SmoothSolver'
    }

    def __init__(self, type='SMOOTH', absolute_tolerance=None, relative_tolerance=None, preconditioner=None, smoother=None, num_sweeps=None, local_vars_configuration=None):  # noqa: E501
        """OneOfFluidSolversOmegaDissipationRateSolver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._absolute_tolerance = None
        self._relative_tolerance = None
        self._preconditioner = None
        self._smoother = None
        self._num_sweeps = None
        self.discriminator = 'type'

        self.type = type
        if absolute_tolerance is not None:
            self.absolute_tolerance = absolute_tolerance
        if relative_tolerance is not None:
            self.relative_tolerance = relative_tolerance
        if preconditioner is not None:
            self.preconditioner = preconditioner
        if smoother is not None:
            self.smoother = smoother
        if num_sweeps is not None:
            self.num_sweeps = num_sweeps

    @property
    def type(self):
        """Gets the type of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501

        Schema name: SmoothSolver  # noqa: E501

        :return: The type of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfFluidSolversOmegaDissipationRateSolver.

        Schema name: SmoothSolver  # noqa: E501

        :param type: The type of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def absolute_tolerance(self):
        """Gets the absolute_tolerance of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501

        <p>Define the absolute tolerance for the residual. The convergence process will be stopped as soon as the residual falls below the absolute tolerance.</p>  # noqa: E501

        :return: The absolute_tolerance of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :rtype: float
        """
        return self._absolute_tolerance

    @absolute_tolerance.setter
    def absolute_tolerance(self, absolute_tolerance):
        """Sets the absolute_tolerance of this OneOfFluidSolversOmegaDissipationRateSolver.

        <p>Define the absolute tolerance for the residual. The convergence process will be stopped as soon as the residual falls below the absolute tolerance.</p>  # noqa: E501

        :param absolute_tolerance: The absolute_tolerance of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                absolute_tolerance is not None and absolute_tolerance > 1):  # noqa: E501
            raise ValueError("Invalid value for `absolute_tolerance`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                absolute_tolerance is not None and absolute_tolerance < 0):  # noqa: E501
            raise ValueError("Invalid value for `absolute_tolerance`, must be a value greater than or equal to `0`")  # noqa: E501

        self._absolute_tolerance = absolute_tolerance

    @property
    def relative_tolerance(self):
        """Gets the relative_tolerance of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501

        <p>Choose the relative tolerance for the residual. The convergence process will be stopped as soon as the ratio of current to initial residual falls below the relative tolerance.</p>  # noqa: E501

        :return: The relative_tolerance of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :rtype: float
        """
        return self._relative_tolerance

    @relative_tolerance.setter
    def relative_tolerance(self, relative_tolerance):
        """Sets the relative_tolerance of this OneOfFluidSolversOmegaDissipationRateSolver.

        <p>Choose the relative tolerance for the residual. The convergence process will be stopped as soon as the ratio of current to initial residual falls below the relative tolerance.</p>  # noqa: E501

        :param relative_tolerance: The relative_tolerance of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                relative_tolerance is not None and relative_tolerance > 1):  # noqa: E501
            raise ValueError("Invalid value for `relative_tolerance`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relative_tolerance is not None and relative_tolerance < 0):  # noqa: E501
            raise ValueError("Invalid value for `relative_tolerance`, must be a value greater than or equal to `0`")  # noqa: E501

        self._relative_tolerance = relative_tolerance

    @property
    def preconditioner(self):
        """Gets the preconditioner of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501


        :return: The preconditioner of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :rtype: OneOfPBICGSolverPreconditioner
        """
        return self._preconditioner

    @preconditioner.setter
    def preconditioner(self, preconditioner):
        """Sets the preconditioner of this OneOfFluidSolversOmegaDissipationRateSolver.


        :param preconditioner: The preconditioner of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :type: OneOfPBICGSolverPreconditioner
        """

        self._preconditioner = preconditioner

    @property
    def smoother(self):
        """Gets the smoother of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501

        <p>Choose a smoother for your solver.</p>  # noqa: E501

        :return: The smoother of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :rtype: str
        """
        return self._smoother

    @smoother.setter
    def smoother(self, smoother):
        """Sets the smoother of this OneOfFluidSolversOmegaDissipationRateSolver.

        <p>Choose a smoother for your solver.</p>  # noqa: E501

        :param smoother: The smoother of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :type: str
        """
        allowed_values = ["GAUSSSEIDEL", "SYMGAUSSSEIDEL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and smoother not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `smoother` ({0}), must be one of {1}"  # noqa: E501
                .format(smoother, allowed_values)
            )

        self._smoother = smoother

    @property
    def num_sweeps(self):
        """Gets the num_sweeps of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501

        <p>Define the numbers of sweeps.</p>  # noqa: E501

        :return: The num_sweeps of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :rtype: int
        """
        return self._num_sweeps

    @num_sweeps.setter
    def num_sweeps(self, num_sweeps):
        """Sets the num_sweeps of this OneOfFluidSolversOmegaDissipationRateSolver.

        <p>Define the numbers of sweeps.</p>  # noqa: E501

        :param num_sweeps: The num_sweeps of this OneOfFluidSolversOmegaDissipationRateSolver.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_sweeps is not None and num_sweeps < 1):  # noqa: E501
            raise ValueError("Invalid value for `num_sweeps`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_sweeps = num_sweeps

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
        if not isinstance(other, OneOfFluidSolversOmegaDissipationRateSolver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfFluidSolversOmegaDissipationRateSolver):
            return True

        return self.to_dict() != other.to_dict()
