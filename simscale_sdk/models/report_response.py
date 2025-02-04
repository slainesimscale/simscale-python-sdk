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


class ReportResponse(object):
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
        'report_id': 'str',
        'name': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'status': 'Status',
        'result_ids': 'list[str]',
        'report_properties': 'object',
        'failure_reason': 'LogEntry',
        'download': 'object'
    }

    attribute_map = {
        'report_id': 'reportId',
        'name': 'name',
        'description': 'description',
        'created_at': 'createdAt',
        'started_at': 'startedAt',
        'finished_at': 'finishedAt',
        'status': 'status',
        'result_ids': 'resultIds',
        'report_properties': 'reportProperties',
        'failure_reason': 'failureReason',
        'download': 'download'
    }

    def __init__(self, report_id=None, name=None, description=None, created_at=None, started_at=None, finished_at=None, status=None, result_ids=None, report_properties=None, failure_reason=None, download=None, local_vars_configuration=None):  # noqa: E501
        """ReportResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._report_id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._started_at = None
        self._finished_at = None
        self._status = None
        self._result_ids = None
        self._report_properties = None
        self._failure_reason = None
        self._download = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if status is not None:
            self.status = status
        if result_ids is not None:
            self.result_ids = result_ids
        if report_properties is not None:
            self.report_properties = report_properties
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if download is not None:
            self.download = download

    @property
    def report_id(self):
        """Gets the report_id of this ReportResponse.  # noqa: E501

        The ID of the report.  # noqa: E501

        :return: The report_id of this ReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this ReportResponse.

        The ID of the report.  # noqa: E501

        :param report_id: The report_id of this ReportResponse.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def name(self):
        """Gets the name of this ReportResponse.  # noqa: E501

        The name of the report.  # noqa: E501

        :return: The name of this ReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportResponse.

        The name of the report.  # noqa: E501

        :param name: The name of this ReportResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ReportResponse.  # noqa: E501

        The description of the report.  # noqa: E501

        :return: The description of this ReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportResponse.

        The description of the report.  # noqa: E501

        :param description: The description of this ReportResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this ReportResponse.  # noqa: E501

        The time the report was created.  # noqa: E501

        :return: The created_at of this ReportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReportResponse.

        The time the report was created.  # noqa: E501

        :param created_at: The created_at of this ReportResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def started_at(self):
        """Gets the started_at of this ReportResponse.  # noqa: E501

        The time the report was started.  # noqa: E501

        :return: The started_at of this ReportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this ReportResponse.

        The time the report was started.  # noqa: E501

        :param started_at: The started_at of this ReportResponse.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this ReportResponse.  # noqa: E501

        The time the report was finished.  # noqa: E501

        :return: The finished_at of this ReportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this ReportResponse.

        The time the report was finished.  # noqa: E501

        :param finished_at: The finished_at of this ReportResponse.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def status(self):
        """Gets the status of this ReportResponse.  # noqa: E501


        :return: The status of this ReportResponse.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReportResponse.


        :param status: The status of this ReportResponse.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def result_ids(self):
        """Gets the result_ids of this ReportResponse.  # noqa: E501

        The resultIds the report has been created for.  # noqa: E501

        :return: The result_ids of this ReportResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._result_ids

    @result_ids.setter
    def result_ids(self, result_ids):
        """Sets the result_ids of this ReportResponse.

        The resultIds the report has been created for.  # noqa: E501

        :param result_ids: The result_ids of this ReportResponse.  # noqa: E501
        :type: list[str]
        """

        self._result_ids = result_ids

    @property
    def report_properties(self):
        """Gets the report_properties of this ReportResponse.  # noqa: E501

        Note: This object is replaced at runtime with the actual report model schema which is fetched from reporting service.   # noqa: E501

        :return: The report_properties of this ReportResponse.  # noqa: E501
        :rtype: object
        """
        return self._report_properties

    @report_properties.setter
    def report_properties(self, report_properties):
        """Sets the report_properties of this ReportResponse.

        Note: This object is replaced at runtime with the actual report model schema which is fetched from reporting service.   # noqa: E501

        :param report_properties: The report_properties of this ReportResponse.  # noqa: E501
        :type: object
        """

        self._report_properties = report_properties

    @property
    def failure_reason(self):
        """Gets the failure_reason of this ReportResponse.  # noqa: E501


        :return: The failure_reason of this ReportResponse.  # noqa: E501
        :rtype: LogEntry
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this ReportResponse.


        :param failure_reason: The failure_reason of this ReportResponse.  # noqa: E501
        :type: LogEntry
        """

        self._failure_reason = failure_reason

    @property
    def download(self):
        """Gets the download of this ReportResponse.  # noqa: E501

        Note: This object is replaced at runtime with the actual report model schema which is fetched from reporting service.   # noqa: E501

        :return: The download of this ReportResponse.  # noqa: E501
        :rtype: object
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this ReportResponse.

        Note: This object is replaced at runtime with the actual report model schema which is fetched from reporting service.   # noqa: E501

        :param download: The download of this ReportResponse.  # noqa: E501
        :type: object
        """

        self._download = download

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
        if not isinstance(other, ReportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportResponse):
            return True

        return self.to_dict() != other.to_dict()
