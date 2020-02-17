from bs4 import BeautifulSoup


class Page:
    def __init__(self, response):
        self.response = response
        self._content = None
        self._soup = None

    @property
    def url(self):
        return self.response.url

    @property
    def title(self):
        return self.soup.title.string

    @property
    def soup(self):
        if self._soup:
            return self._soup
        else:
            self._soup = BeautifulSoup(self.response.text)
            # kill all script and style elements
            for script in self._soup(["script", "style"]):
                script.extract()
            return self._soup

    @property
    def content(self):
        if self._content:
            return self._content
        else:
            self._content = self.soup.get_text()
            return self._content
