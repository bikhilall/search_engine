"""
https://tfhub.dev/google/nnlm-en-dim128/2?tf-hub-format=compressed
"""
import os
import tensorflow_hub as hub

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(FILE_PATH, 'model')

embed = hub.load("https://tfhub.dev/google/nnlm-en-dim128/2")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
print(embeddings)