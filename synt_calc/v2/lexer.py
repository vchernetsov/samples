import re
from contextlib import suppress
from tokens import *
from exceptions import StopLexerParser


class Lexer:
    """
        Class performing lexical analisys by splittion of incoming text to lexem tokens.
        text - incoming text for the reference
        position - current parser position

        Usage:
            >>> query = ' -1 - 2 + 20 - 5'
            >>> lexer = Lexer(text=query)
            >>> for token in list(lexer.parse()):
            >>>     print (token)
            OP:NO_ACTION
            OP:MINUS
            NUMBER:1
            OP:NO_ACTION
            OP:MINUS
            OP:NO_ACTION
            NUMBER:2
            OP:NO_ACTION
            OP:PLUS
            OP:NO_ACTION
            NUMBER:20
            OP:NO_ACTION
            OP:MINUS
            OP:NO_ACTION
            NUMBER:5
    """
    text = None
    position = 0

    def __init__(self, text):
        self.text = text

    def _shift(self, offset=1):
        """Method increases current position by 1"""
        self.position += offset
        if self.position >= len(self.text) + 1:
            self.position = 0

    @property
    def particle(self):
        return self.text[self.position:]

    def detect(self):
        """Method returns lexem token"""
        for pattern, cls in QUALIFIERS.items():
            match = re.match(pattern, self.particle)
            if match:
                instance = cls(value=match[0])
                self._shift(offset=len(instance.value))
                return instance
        raise StopLexerParser()

    def parse(self):
        """Main parsing generator method."""
        while True:
            try:
                yield self.detect()
            except StopLexerParser:
                break
