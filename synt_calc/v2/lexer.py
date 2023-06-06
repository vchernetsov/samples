import re
import tokens
from exceptions import StopLexerParser


class Lexer:
    """
        Class performing lexical analisys by splittion of incoming text to lexem tokens.
        text - incoming text for the reference
        position - current parser position

        Usage:
        >>> query = '1 + 2 * (6 - 4) / 2'
        >>> lexer = Lexer(text=query)
        >>> tokens = lexer.parse()
        >>> print (list(tokens))
        [NUMBER: 1, PLUS, NUMBER: 2, MULTIPLY, OPEN_PARENTHESIS, NUMBER: 6, MINUS, NUMBER: 4, CLOSE_PARENTHESIS, DIVIDE, NUMBER: 2]
    """
    text = None
    position = 0

    def __init__(self, text):
        self.text = text

    def forward(self, offset=1):
        """Method increases current position by 1"""
        self.position += offset

    @property
    def particle(self):
        return self.text[self.position:]

    def detect(self):
        """Method returns lexem token"""
        for pattern, cls in tokens.QUALIFIERS.items():
            match = re.match(pattern, self.particle)
            if match:
                token = cls(value=match[0])
                self.forward(offset=len(token.value))
                return token
        # humans count from 1
        position = self.position + 1
        raise StopLexerParser(f'can not match symbol: {self.particle[:1]}, pos {position}')

    def parse(self, whitespace=False):
        """Main parsing generator method."""
        while self.position < len(self.text):
            token = self.detect()
            # ignore whitespaced tokens
            if not whitespace and isinstance(token, tokens.WhitespaceToken):
                continue
            yield token
