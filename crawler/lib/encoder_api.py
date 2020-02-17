import os
from typing import List
import requests


class EncoderApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def _get(self, url, params, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    def encode(self, text: str) -> List[float]:
        res = self._get(url=self.base_url)
        return res.json()


def encode(text: str) -> List[float]:
    encoder_api = EncoderApi(base_url=os.environ['ENCODER_API_BASE_URL'])
    return encoder_api.encode(text)
