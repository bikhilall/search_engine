import logging
from configparser import ConfigParser


class Config():
    """ This a singleton to load app config """
    instance = None

    def __new__(cls, *args, **kwargs):
        """ __new__ is Always a class method. """
        if not cls.instance:
            cls.instance = ConfigParser(*args, **kwargs)
            logging.debug('Config instance is built.')
        return cls.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


if __name__ == "__main__":
    config = Config()
    config = Config()
