from enum import Enum
from abs import ABS

class Lexem(ABS):
    @abstractmethod
    def is(self, particle):
        pass



class Number(Lexem):
#    type = 


class LexemFactory:

    @classmethod
    def factory(cls, particle):
        for x in 






class Lexer:

    position = None

    def __init__(self, text):
        self.text = text

    @property
    def enumerated(self):
        for idx, char in enumerate(self.text):
            yield (idx, char)

    @property
    def tokens(self):
        for x in self.enumerated:
            print (x)

query = '1 + 20 + 34.5 - 5.6 + 2 - 1'

lexer = Lexer(query)

lexer.tokens
