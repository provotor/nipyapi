# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.19.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StackTraceElement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'method_name': 'str',
        'file_name': 'str',
        'line_number': 'int',
        'class_name': 'str',
        'native_method': 'bool'
    }

    attribute_map = {
        'method_name': 'methodName',
        'file_name': 'fileName',
        'line_number': 'lineNumber',
        'class_name': 'className',
        'native_method': 'nativeMethod'
    }

    def __init__(self, method_name=None, file_name=None, line_number=None, class_name=None, native_method=None):
        """
        StackTraceElement - a model defined in Swagger
        """

        self._method_name = None
        self._file_name = None
        self._line_number = None
        self._class_name = None
        self._native_method = None

        if method_name is not None:
          self.method_name = method_name
        if file_name is not None:
          self.file_name = file_name
        if line_number is not None:
          self.line_number = line_number
        if class_name is not None:
          self.class_name = class_name
        if native_method is not None:
          self.native_method = native_method

    @property
    def method_name(self):
        """
        Gets the method_name of this StackTraceElement.

        :return: The method_name of this StackTraceElement.
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """
        Sets the method_name of this StackTraceElement.

        :param method_name: The method_name of this StackTraceElement.
        :type: str
        """

        self._method_name = method_name

    @property
    def file_name(self):
        """
        Gets the file_name of this StackTraceElement.

        :return: The file_name of this StackTraceElement.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this StackTraceElement.

        :param file_name: The file_name of this StackTraceElement.
        :type: str
        """

        self._file_name = file_name

    @property
    def line_number(self):
        """
        Gets the line_number of this StackTraceElement.

        :return: The line_number of this StackTraceElement.
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """
        Sets the line_number of this StackTraceElement.

        :param line_number: The line_number of this StackTraceElement.
        :type: int
        """

        self._line_number = line_number

    @property
    def class_name(self):
        """
        Gets the class_name of this StackTraceElement.

        :return: The class_name of this StackTraceElement.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """
        Sets the class_name of this StackTraceElement.

        :param class_name: The class_name of this StackTraceElement.
        :type: str
        """

        self._class_name = class_name

    @property
    def native_method(self):
        """
        Gets the native_method of this StackTraceElement.

        :return: The native_method of this StackTraceElement.
        :rtype: bool
        """
        return self._native_method

    @native_method.setter
    def native_method(self, native_method):
        """
        Sets the native_method of this StackTraceElement.

        :param native_method: The native_method of this StackTraceElement.
        :type: bool
        """

        self._native_method = native_method

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, StackTraceElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
