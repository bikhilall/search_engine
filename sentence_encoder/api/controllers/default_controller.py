from api.models.text_vector import TextVector  # noqa: E501
from api.singleton import SingletonDecorator
from encoders import Gusel

global encoder
encoder = SingletonDecorator(Gusel)()


def encode(body):
    results = encoder.encode(body)
    text_vectors = [TextVector(text=r['text'], vector=r['vector']) for r in results]

    return text_vectors


def health():
    return (True, 200)
