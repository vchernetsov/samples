class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data
# Print the Tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))      



exit()













from lexer import Lexer
import tokens as Tokens
from tree import *
from enum import Enum, auto
from decimal import Decimal


class NodeType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()


class Node:
    left = None
    rigth = None

    def __init__(self, value=None):
        if value is not None:
            self.value = Decimal(value)

    def __repr__(self):

        return f'{self.node_type.name}'

class NumberNode(Node):
    node_type = NodeType.NUMBER


class PlusNode(Node):
    node_type = NodeType.PLUS


class MinusNode(Node):
    node_type = NodeType.MINUS


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        stack = []
        tree = Node()
        while self.tokens:
            token = self.tokens.pop()

            if isinstance(token, Tokens.NumberToken):
                node = NumberNode(value=token.value)
                stack.append(node)
            if isinstance(token, Tokens.PlusToken):
                node = PlusNode()
                node.left


            print (node, stack)



#            if isinstance(token, Tokens.PlusToken):
#                current_node = NumberNode(token)



#            if isinstance(token, Tokens.PlusToken):
#                node = PlusNode()
#                node.children.append(self.parse())
#            elif isinstance(token, Tokens.MinusToken):
#                node = MinusNodeNode()
#                node.children.append(self.parse())
#            elif isinstance(token, Tokens.NumberToken):
#                node = NumberNode(token)
#            self.tree.children.append(node)




#        return
#        stack = []
#        root = None
#        for char in input_string:
#            print (char, stack)
#            if char == '(':
#                node = Node('')
#                if stack:
#                    stack[-1].children.append(node)
#                stack.append(node)
#            elif char == ')':
#                if stack:
#                    stack.pop()
#            else:
#                if stack:
#                    stack[-1].value += char
#                else:
#                    root = Node(char)
#        print (stack)
#        return root





















#        token = tokens.pop(0)

#        if isinstance(token, Tokens.PlusToken):
#            node = PlusNode()
#            node.children.append(self.parse())
#        elif isinstance(token, Tokens.MinusToken):
#            node = MinusNodeNode()
#            node.children.append(self.parse())
#        elif isinstance(token, Tokens.NumberToken):
#            node = NumberNode(token)
#        self.tree.children.append(node)


query = '1 + 2' #  * (6 - 4) / 2'
lexer = Lexer(text=query)
tokens = list(lexer.parse())
print ('Tokens', tokens)
parser = Parser(tokens)
tree = parser.parse()
print (tree)


#parser = Parser(tokens=list(tokens))
#tree = parser.parse()
#print (tree)











## Пример использования
#expression = "3 + (4 * 2) - (6 / 3)"
#tokens = list(expression.replace('(', ' ( ').replace(')', ' ) ').split())
#print (tokens)
#tree = parse_expression(tokens)
#print_tree(tree)







#        return
#        stack = []
#        root = None
#        for char in input_string:
#            print (char, stack)
#            if char == '(':
#                node = Node('')
#                if stack:
#                    stack[-1].children.append(node)
#                stack.append(node)
#            elif char == ')':
#                if stack:
#                    stack.pop()
#            else:
#                if stack:
#                    stack[-1].value += char
#                else:
#                    root = Node(char)
#        print (stack)
#        return root

#def print_tree(node, depth=0):
#    if node:
#        print('  ' * depth + node.value)
#        for child in node.children:
#            print_tree(child, depth + 1)

## Пример использования:
#input_string = "(A(B(C))(D))"
#tree = parse_string(input_string)

#print_tree(tree)

