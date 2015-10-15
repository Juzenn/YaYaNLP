from yaya import config
from yaya.collection.dict import DoubleArrayTrie, CoreDict
from yaya.collection.hmm import HMMMatrix
from yaya.common.nr import NRPattern
from yaya.const import TAG_PEOPLE
from yaya.utility.singleton import singleton

__author__ = 'tony'


@singleton
class PersonDict:
    def __init__(self):
        self.trie = DoubleArrayTrie.load(config.PERSON_DICT_NAME)
        self.matrix = HMMMatrix.load(config.PERSON_TR_PATH)

PERSON_WORD_ID, PERSON_ATTRIBUTE = CoreDict().trie.get(TAG_PEOPLE)

@singleton
class NRPatternDict:
    def __init__(self):
        self.trie = DoubleArrayTrie()
        NRPattern.sort()
        self.trie.build(key=NRPattern)