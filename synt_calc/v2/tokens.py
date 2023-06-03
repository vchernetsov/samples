class Token:
    """Basic token class"""

    def __init__(self, value=None):
        if value is not None:
            self.value = value


class Syntax(Token):
    """Syntax token class"""


class OpenBracket(Syntax):
    """Open Bracket token class"""

    def __str__(self):
        return f'SYN:OPEN_BRACKET'


class CloseBracket(Syntax):
    """Close Bracket token class"""

    def __str__(self):
        return f'SYN:CLOSE_BRACKET'


class Number(Token):
    """Number token class"""

    def __str__(self):
        return f'NUMBER:{self.value}'


class Constant(Number):
    """Constant token class"""


class PI(Constant):
    """PI token class"""

    def __str__(self):
        return f'CONST:PI'


class EPS(Constant):
    """Epsilon token class"""

    def __str__(self):
        return f'CONST:EPS'


class Operator(Token):
    """Operator token class"""


class Plus(Operator):
    """Plus token class"""

    def __str__(self):
        return f'OP:PLUS'


class Minus(Operator):
    """Minus token class"""

    def __str__(self):
        return f'OP:MINUS'


class Multiply(Operator):
    """Multiply token class"""

    def __str__(self):
        return f'OP:MULTIPLY'


class Divide(Operator):
    """Divide token class"""

    def __str__(self):
        return f'OP:DIVIDE'


class Nop(Token):
    """Ignored token class"""

    def __str__(self):
        return f'OP:NO_ACTION'


QUALIFIERS = {
    r'^([0-9]+([.][0-9]*)?|[.][0-9]+)': Number,
    r'^PI': PI,
    r'^EPS': EPS,
    r'^\+': Plus,
    r'^\-': Minus,
    r'^\*': Multiply,
    r'^\/': Divide,
    r'^\(': OpenBracket,
    r'^\)': CloseBracket,
    r'^\s': Nop,
}
