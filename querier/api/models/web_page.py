# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api.models.base_model_ import Model
from api import util


class WebPage(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, url: str=None, title: str=None):  # noqa: E501
        """WebPage - a model defined in Swagger

        :param url: The url of this WebPage.  # noqa: E501
        :type url: str
        :param title: The title of this WebPage.  # noqa: E501
        :type title: str
        """
        self.swagger_types = {
            'url': str,
            'title': str
        }

        self.attribute_map = {
            'url': 'url',
            'title': 'title'
        }
        self._url = url
        self._title = title

    @classmethod
    def from_dict(cls, dikt) -> 'WebPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WebPage of this WebPage.  # noqa: E501
        :rtype: WebPage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this WebPage.


        :return: The url of this WebPage.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this WebPage.


        :param url: The url of this WebPage.
        :type url: str
        """

        self._url = url

    @property
    def title(self) -> str:
        """Gets the title of this WebPage.


        :return: The title of this WebPage.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this WebPage.


        :param title: The title of this WebPage.
        :type title: str
        """

        self._title = title
