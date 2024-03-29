import os
from typing import List
import requests


class EncoderApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def _get(self, sub_url, params=None, **kwargs):
        return requests.get(url=self.base_url + sub_url, params=params, **kwargs)

    def _post(self, sub_url, data=None, json=None, **kwargs):
        return requests.post(url=self.base_url + sub_url, data=data, json=json, **kwargs)

    def encode(self, texts: List[str]) -> List[List[float]]:
        """
        encode a list of texts into vectors
        :param texts: list of texts
        :return: list of vectors
        """
        res = self._post(sub_url='/encode', json=texts)
        return res.json()


def encode(text: str) -> List[float]:
    """
    encode a text into vector
    """
    encoder_api = EncoderApi(base_url=os.environ['ENCODER_API_BASE_URL'])
    return encoder_api.encode([text])[0]['vector']