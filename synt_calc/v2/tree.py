from decimal import Decimal
from dataclasses import dataclass
from tokens import *

class Node:

    def __init__(self, children=None):
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        self.children.append(node)

    @staticmethod
    def create(token):
        if isinstance(token, NumberToken):
            return NumberNode(token.value)
        elif isinstance(token, PlusToken):
            return AddNode
        elif isinstance(token, MinusToken):
            return SubstractNode
        elif isinstance(token, MultiplyToken):
            return MultiplyNode
        elif isinstance(token, DivideToken):
            return DivideNode
        raise SyntaxError(token)


@dataclass
class NumberNode(Node):
    result: Decimal

    def __str__(self):
        return self.result


@dataclass
class OperationNode(Node):
    left: Decimal
    rigth: Decimal


class AddNode(OperationNode):

    def __str__(self):
        return f'{self.left}+{self.rigth}'


class SubstractNode(OperationNode):
    def __str__(self):
        return f'{self.left}-{self.rigth}'

class PrimaryNode(OperationNode):
    pass

class MultiplyNode(PrimaryNode):
    def __str__(self):
        return f'{self.left}*{self.rigth}'


class DivideNode(PrimaryNode):
    def __str__(self):
        return f'{self.left}/{self.rigth}'
