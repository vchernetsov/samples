from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    OPEN_PARENTHESIS = auto()
    CLOSE_PARENTHESIS = auto()
    WHITESPACE = auto()


@dataclass
class Token:
    value: any
    novalue = True

    def __repr__(self):
        if self.novalue:
            return self.token_type.name

        value = ''
        if self.value is not None:
            value = self.value
        token_type = self.token_type
        return f'{self.token_type.name}: {value}'


class NumberToken(Token):
    token_type = TokenType.NUMBER
    novalue = False


class PlusToken(Token):
    token_type = TokenType.PLUS


class MinusToken(Token):
    token_type = TokenType.MINUS


class MultiplyToken(Token):
    token_type = TokenType.MULTIPLY


class DivideToken(Token):
    token_type = TokenType.DIVIDE


class OpenParenthesisToken(Token):
    token_type = TokenType.OPEN_PARENTHESIS


class CloseParenthesisToken(Token):
    token_type = TokenType.CLOSE_PARENTHESIS


class WhitespaceToken(Token):
    token_type = TokenType.WHITESPACE


QUALIFIERS = {
    r'^([0-9]+([.][0-9]*)?|[.][0-9]+)': NumberToken,
    r'^\+': PlusToken,
    r'^\-': MinusToken,
    r'^\*': MultiplyToken,
    r'^\/': DivideToken,
    r'^\(': OpenParenthesisToken,
    r'^\)': CloseParenthesisToken,
    r'^\s': WhitespaceToken,
}
