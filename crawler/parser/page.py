from bs4 import BeautifulSoup


class Page:
    def __init__(self, response):
        self.response = response
        self.__content = None
        self.__soup = None

    @property
    def _soup(self):
        if self.__soup:
            return self.__soup
        else:
            self.__soup = BeautifulSoup(self.response.text)
            # kill all script and style elements
            for script in self.__soup(["script", "style"]):
                script.extract()
            return self.__soup

    @property
    def content(self):
        if self.__content:
            return self.__content
        else:
            self.__content = self._soup.get_text()
            return self.__content
