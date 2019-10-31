"""
Google Universal Sentence Encoder Lite -- Multilingual Universal Sentence Encoder for Semantic Retrieval

To download the library:
https://tfhub.dev/google/universal-sentence-encoder-lite/2?tf-hub-format=compressed
MODEL_PATH = https://tfhub.dev/google/universal-sentence-encoder-lite/2
"""
import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import sentencepiece as spm
from encoders import Base

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(FILE_PATH, 'model')


class Gusel(Base):
    def __init__(self, model_path= MODEL_PATH):
        self.model_path = model_path

    def sent_to_hash(self, sent: str):
        return self.messages_to_vec([sent])


    def process_to_IDs_in_sparse_format(self, sp, sentences):
        # An utility method that processes sentences with the sentence piece processor
        # 'sp' and returns the results in tf.SparseTensor-similar format:
        # (values, indices, dense_shape)
        ids = [sp.EncodeAsIds(x) for x in sentences]
        max_len = max(len(x) for x in ids)
        dense_shape = (len(ids), max_len)
        values = [item for sublist in ids for item in sublist]
        indices = [[row, col] for row in range(len(ids)) for col in range(len(ids[row]))]
        return (values, indices, dense_shape)

    def messages_to_vec(self, messages):
        module = hub.Module(MODEL_PATH)

        input_placeholder = tf.sparse_placeholder(tf.int64, shape=[None, None])
        encodings = module(
            inputs=dict(
                values=input_placeholder.values,
                indices=input_placeholder.indices,
                dense_shape=input_placeholder.dense_shape))

        with tf.Session() as sess:
            spm_path = sess.run(module(signature="spm_path"))

        sp = spm.SentencePieceProcessor()
        sp.Load(spm_path)
        print("SentencePiece model loaded at {}.".format(spm_path))

        values, indices, dense_shape = self.process_to_IDs_in_sparse_format(sp, messages)

        # Reduce logging output.
        tf.logging.set_verbosity(tf.logging.ERROR)

        with tf.Session() as session:
            session.run([tf.global_variables_initializer(), tf.tables_initializer()])
            message_embeddings = session.run(
                encodings,
                feed_dict={input_placeholder.values: values,
                           input_placeholder.indices: indices,
                           input_placeholder.dense_shape: dense_shape})

            for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
                print("Message: {}".format(messages[i]))
                print("Embedding size: {}".format(len(message_embedding)))
                message_embedding_snippet = ", ".join(
                    (str(x) for x in message_embedding[:3]))
                print("Embedding: [{}, ...]\n".format(message_embedding_snippet))

        return message_embeddings
        # The following are example embedding output of 512 dimensions per sentence
        # Embedding for: The quick brown fox jumps over the lazy dog.
        # [0.0560572519898, 0.0534118898213, -0.0112254749984, ...]
        # Embedding for: I am a sentence for which I would like to get its embedding.
        # [-0.0343746766448, -0.0529498048127, 0.0469399243593, ...]


if __name__ == '__main__':
    gusel = Gusel()
    embedings = gusel.messages_to_vec(["I am fat.", "I am very fat.", "I am not fat", "I am thin"])

    corr = np.inner(embedings, embedings)
    print(corr)


