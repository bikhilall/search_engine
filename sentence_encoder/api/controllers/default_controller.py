from api.models.text_vector import TextVector  # noqa: E501
from encoders import Gusel


def encode(body):
    encoder = Gusel()
    results = encoder.encode(body)
    text_vectors = [TextVector(text=r['text'], vector=r['vector']) for r in results]

    return text_vectors
