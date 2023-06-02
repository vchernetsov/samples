import re
from abc import ABC, abstractmethod
from decimal import Decimal


class SyntaxError(Exception):
    pass

class NoLexemError(SyntaxError):
    pass


class BaseLexem(ABC):

    particle = None
    text = None
    value = None

    def __init__(self, text):
        self.text = text
        self.value = self.coerce()

    @staticmethod
    def detect(particle):
        for detector, cls in DETECTORS.items():
            match = re.match(detector, particle)
            if match:
                instance = cls(text=match[0])
                return instance

    @abstractmethod
    def coerce(self, particle):
        pass

    def __str__(self):
        return f'Lexem: <{self.value}>'

class Number(BaseLexem):
    def coerce(self):
        return Decimal(self.text)


DETECTORS = {
    r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)': Number,
}



class Lexer:

    def __init__(self, text):
        self.text = text

    @property
    def tokens(self):
        position = 0
        while True:
            particle = self.text[position:]
            lexem = BaseLexem.detect(particle)
            if lexem:
                print (position, lexem)

                position += len(lexem.text)
                continue

            # update index
            position += 1
            # and leave the loop when done
            if position >= len(self.text):
                break


query = '-1 + 20 - 3.4'

lexer = Lexer(query)

lexer.tokens
