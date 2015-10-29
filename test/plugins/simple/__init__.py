from pyglins import BasePlugin


class SimplePlug(BasePlugin):
    def __init__(self):
        self.name = 'Simple'

    def run(self):
        print('Running the Simple plugin')

