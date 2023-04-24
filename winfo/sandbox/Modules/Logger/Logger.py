import os
import logging
from config import Config

class Logger:
    def __init__(self, name=__name__, level=logging.DEBUG, filename='myapp.log'):
        self.config = Config()
        self.log_dir = self.config.config.get("log_dir")
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.handler = logging.FileHandler(os.path.join(self.log_dir, filename))
        self.handler.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.name = self.logger.name
        self.run = print('Starting logger...')

    def set_name(self, name):
        self.logger.name = name
        self.name = name
        return self

    def log(self, message, level=logging.DEBUG, *args, **kwargs):
        self.logger.log(level, message, *args, **kwargs)

    def setup(self, directory=None, filename=None):
        print('Starting Logger...')
        if __name__ == '__main__':
            print('This file is being run directly.')
        else:
            self.set_name()
        print('Done!')
