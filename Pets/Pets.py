from Pets.Collie import Collie
from Pets.JackRussell import JackRussell
from Pets.GoldenRetriever import GoldenRetriever

class Pets:
    def __init__(self):
        self.collie = Collie('Apollo', 2)
        self.jack_russell =JackRussell('Jack', 1)
        self.golden_retriever = GoldenRetriever('Sabrina', 4)

    def pets_info(self):
        self.collie.info()
        self.jack_russell.info()
        self.golden_retriever.info()

