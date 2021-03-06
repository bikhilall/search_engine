# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api.models.base_model_ import Model
from api.models.web_page import WebPage  # noqa: F401,E501
from api import util


class ListOfWebPages(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """ListOfWebPages - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ListOfWebPages':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListOfWebPages of this ListOfWebPages.  # noqa: E501
        :rtype: ListOfWebPages
        """
        return util.deserialize_model(dikt, cls)
