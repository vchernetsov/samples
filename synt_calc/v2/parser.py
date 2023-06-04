from lexer import Lexer
from tree import *


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        root = Node()
        for token in self.tokens:
            print (token)



#query = ' -1 - 2 + 20 - 5 * (6 * 5 / (2 * 3))'
#lexer = Lexer(text=query)
#for token in list(lexer.parse()):
#    print (token)







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

