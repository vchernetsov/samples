import re
from abc import ABC, abstractmethod
from decimal import Decimal


class SyntaxError(Exception):
    pass

class NoLexemError(SyntaxError):
    pass


class BaseLexem(ABC):

    particle = None
    lexem = None
    value = None

    def __init__(self, lexem):
        self.lexem = lexem
        self.value = self.coerce()

    @staticmethod
    def detect(particle):
        for detector, cls in DETECTORS.items():
            match = re.match(detector, particle)
            if match:
                instance = cls(lexem=match[0])
                return instance

    @abstractmethod
    def coerce(self, particle):
        pass

    def __str__(self):
        return f'Lexem: <{self.value}>'

class Number(BaseLexem):
    def coerce(self):
        return Decimal(self.lexem)


DETECTORS = {
    r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)': Number,
}



class Lexer:

    def __init__(self, text):
        self.text = text

    @property
    def tokens(self):
        for pos, _ in enumerate(self.text):
            particle = self.text[pos:]
            lexem = BaseLexem.detect(particle)
            print (lexem)

query = '-1 + 20 - 3.4'

lexer = Lexer(query)

lexer.tokens
