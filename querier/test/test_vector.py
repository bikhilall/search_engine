import unittest
from search_engine_core.db.models import Pages as DbPage
from lib.vector import find_similar_pages


class VectorTest(unittest.TestCase):

    def test_find_similar_page(self):
        pages = [
            DbPage(url='page1', vector=[1, 2, 3]),
            DbPage(url='page2', vector=[1, 2, 3]),
            DbPage(url='page3', vector=[1, -2, 3]),
            DbPage(url='page4', vector=[0, 0, 0]),
            DbPage(url='page5', vector=[1, 1, 3])
        ]
        similar_pages = find_similar_pages(vector=[1, 2, 3], pages=pages)


if __name__ == '__main__':
    unittest.main()
