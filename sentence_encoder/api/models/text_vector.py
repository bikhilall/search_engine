# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api.models.base_model_ import Model
from api import util


class TextVector(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, text: str=None, vector: List[float]=None):  # noqa: E501
        """TextVector - a model defined in Swagger

        :param text: The text of this TextVector.  # noqa: E501
        :type text: str
        :param vector: The vector of this TextVector.  # noqa: E501
        :type vector: List[float]
        """
        self.swagger_types = {
            'text': str,
            'vector': List[float]
        }

        self.attribute_map = {
            'text': 'text',
            'vector': 'vector'
        }
        self._text = text
        self._vector = vector

    @classmethod
    def from_dict(cls, dikt) -> 'TextVector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextVector of this TextVector.  # noqa: E501
        :rtype: TextVector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self) -> str:
        """Gets the text of this TextVector.


        :return: The text of this TextVector.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this TextVector.


        :param text: The text of this TextVector.
        :type text: str
        """

        self._text = text

    @property
    def vector(self) -> List[float]:
        """Gets the vector of this TextVector.


        :return: The vector of this TextVector.
        :rtype: List[float]
        """
        return self._vector

    @vector.setter
    def vector(self, vector: List[float]):
        """Sets the vector of this TextVector.


        :param vector: The vector of this TextVector.
        :type vector: List[float]
        """

        self._vector = vector
