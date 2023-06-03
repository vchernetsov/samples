class SolverException(Exception):
    pass


class StopParsing(SolverException):
    pass


class StopLexerParser(StopParsing):
    pass
