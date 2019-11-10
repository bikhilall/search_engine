# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_encode_post(self):
        """Test case for encode_post

        Returns a list of vectors.
        """
        request_body = ['request_body_example']
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/encode',
            method='POST',
            headers=headers,
            data=json.dumps(request_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
