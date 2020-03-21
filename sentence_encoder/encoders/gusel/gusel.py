"""
Google Universal Sentence Encoder Lite -- Multilingual Universal Sentence Encoder for Semantic Retrieval

To download the library:
https://tfhub.dev/google/universal-sentence-encoder-lite/2?tf-hub-format=compressed
MODEL_PATH = https://tfhub.dev/google/universal-sentence-encoder-lite/2
"""
import os
import logging
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import sentencepiece as spm
from typing import List
from encoders import Base

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(FILE_PATH, 'model')


class Gusel(Base):
    def __init__(self, model_path=MODEL_PATH):
        # Reduce logging output.
        tf.logging.set_verbosity(tf.logging.ERROR)
        self._model_path = model_path
        self.module = hub.Module(self._model_path)
        self._graph = tf.get_default_graph()
        self.build_sp()
        self._input_placeholder = tf.sparse_placeholder(tf.int64, shape=[None, None])
        self._encodings = self.module(
            inputs=dict(
                values=self._input_placeholder.values,
                indices=self._input_placeholder.indices,
                dense_shape=self._input_placeholder.dense_shape
            )
        )

    def encode(self, sentences: List[str]) -> List[float]:
        embeddings = self.text_to_vec(sentences)
        results = []
        for i, text in enumerate(sentences):
            results.append(
                {
                    "text": text,
                    "vector": [round(x, 4) for x in embeddings[i].astype(float)]
                }
            )
        return results

    def process_to_IDs_in_sparse_format(self, sentences):
        # An utility method that processes sentences with the sentence piece processor
        # 'sp' and returns the results in tf.SparseTensor-similar format:
        # (values, indices, dense_shape)
        ids = [self._sp.EncodeAsIds(x) for x in sentences]
        max_len = max(len(x) for x in ids)
        dense_shape = (len(ids), max_len)
        values = [item for sublist in ids for item in sublist]
        indices = [[row, col] for row in range(len(ids)) for col in range(len(ids[row]))]
        return (values, indices, dense_shape)

    def build_sp(self):
        with tf.Session() as sess:
            spm_path = sess.run(self.module(signature="spm_path"))

        sp = spm.SentencePieceProcessor()
        sp.Load(spm_path)
        logging.info("SentencePiece model loaded at {}.".format(spm_path))
        self._sp = sp

    def text_to_vec(self, texts):
        with self._graph.as_default():
            with tf.Session() as session:
                session.run([tf.global_variables_initializer(), tf.tables_initializer()])
                values, indices, dense_shape = self.process_to_IDs_in_sparse_format(texts)
                message_embeddings = session.run(
                    self._encodings,
                    feed_dict={
                        self._input_placeholder.values: values,
                        self._input_placeholder.indices: indices,
                        self._input_placeholder.dense_shape: dense_shape
                    }
                )

        return message_embeddings


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    gusel = Gusel()
    test_cases = [
        "best places to visit at Bellevue",
        "Best places to visit in Bellevue are: My home, Your place, and stores",
        "Here is a list of must go places in Bellevue: school, bus station, and Amin's place",
        "best travel destinations in Bellevue",
        "Here is a list of best places to see in Bellevue washington",
        "Find what to do today, this weekend, or in November. We have reviews of the best places to see in Bellevue. Visit top-rated & must-see attractions.",

        "Square mall is the best place to visit in Bellevue",
        "did you know that square mall is the best place to visit in Bellevue?",
        "This article is not about the best places in Bellevue",

        "Bellevue is big and best",
        "Best foods to eat in bellevue",
        "I created the best search engine",
        "best places to visit in Iran",
        "where is the best place to visit in China?",
        "Best places to visit in China are: great wall, he's home, and alibaba",

        "Bellevue is a city in Washington state, across Lake Washington from Seattle. Downtown Park has a large lawn, gardens and a waterfall. Nearby, the Bellevue Arts Museum features craft and design exhibitions, plus a sculpture garden. The Bellevue Botanical Garden highlights Pacific Northwest plants, and includes woodlands and wetlands. KidsQuest Children’s Museum has interactive science, tech and art exhibitions.",
        'Bellevue is bordered by the cities of Kirkland to the north and Redmond to the northeast along the Overlake and Crossroads neighborhoods.',
        'Bellevue, WA: What you need to know. Separated from Seattle by Lake Washington, but just a 25-minute drive away, the city of Bellevue offers residents with a small-town vibe and a large assortment of entertainment options',

        "Access a wide and ever-growing collection of extensions and plugins created by the developers and companies that form the Kubernetes community.",
        "A conformant Kubernetes service allows you to take full advantage of these community offerings and add capabilities such as security, monitoring, management.",
        "Define complex containerized applications and deploy them globally across a cluster of servers—or even multiple clusters—as Kubernetes optimizes resources according to your desired state.",
        "With built-in auto-scaler, Kubernetes can easily scale your application horizontally while automatically monitoring and maintaining container health."
        "Iran is an Islamic republic on the Persian (Arabian) Gulf with historical sites dating to the Persian Empire.",
        "Extensive marble ruins mark Persepolis, the empire’s capital founded by Darius I in the 6th century B.C.",
        "Laptop",
        "I have the best car ever",
        "give me some food"
    ]

    embeddings = [gusel.text_to_vec([t]) for t in test_cases]
    from matplotlib import pyplot

    for i, embeding1 in enumerate(embeddings):
        distance = np.linalg.norm(embeddings[0] - embeding1)
        print(distance, "---------", test_cases[i])

        pyplot.plot(embeding1)

    pyplot.show()
