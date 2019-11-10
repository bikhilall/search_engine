import connexion
import six

from api.models.text_vector import TextVector  # noqa: E501
from api import util


def encode_post(body):  # noqa: E501
    """Returns a list of vectors.

    This will encode your list of texts to a list of vectors. # noqa: E501

    :param body: 
    :type body: List[]

    :rtype: List[TextVector]
    """
    return 'do some magic!'
