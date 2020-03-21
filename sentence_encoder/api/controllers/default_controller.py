from api.models.text_vector import TextVector  # noqa: E501
from encoders import Gusel

encoder = Gusel()

def encode(body):
    results = encoder.encode(body)
    text_vectors = [TextVector(text=r['text'], vector=r['vector']) for r in results]

    return text_vectors
