from api.models.web_page import WebPage  # noqa: E501


def query(body):
    return WebPage(url='test_url', title='test_title')
