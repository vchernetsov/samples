"""
The very primitive parser. First approach to the problem.

"""


from decimal import Decimal

query = '1 + 20 + 34.5 - 5.6'


def parse(query):
    tokens = tokenize(query)
#    tokens = numberize(tokens)
    return tokens


def tokenize(query):
    idx = 0
    while True:
        token = []
        for x in query[idx:]:
            # detect whitespace
            if x == ' ':
                # and do nothing
                break

            # detect sum
            if x == '+':
                yield lambda x, y: x + y
                break

            # detect minus
            if x == '-':
                yield lambda x, y: x - y
                break

            # detect number
            try:
                int(x)
                token.append(x)
                idx += 1
                continue
            except:
                if x == '.':
                    idx += 1
                    token.append(x)
                    continue
        # update index
        idx += 1
        if token:
            yield token
        # and leave the loop when done
        if idx >= len(query):
            break


def numberize(tokens):
    for token in tokens:
        try:
            yield Decimal(''.join(token))
        except:
            yield token

def calculate(tokens):
    tokens = list(tokens)
    idx = 0
    result = 0
    while True:
        token = tokens[idx]
        if isinstance(token, Decimal):
            try:
                action = tokens[idx + 1]
                another = tokens[idx + 2]
                result += action(token, another)
                idx += 2
            except IndexError:
                pass

        # update index
        idx += 1
        # and leave the loop when done
        if idx >= len(tokens):
            return result

tokens = parse(query)
print (list(tokens))
calculated = calculate(tokens)
print (f'result of {query} is: {calculated}')
