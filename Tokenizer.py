from Token import Token


token_type = {
    'class': 'keyword',
    'constructor': 'keyword',
    'function': 'keyword',
    'method': 'keyword',
    'field': 'keyword',
    'static': 'keyword',
    'var': 'keyword',
    'int': 'keyword',
    'char': 'keyword',
    'boolean': 'keyword',
    'void': 'keyword',
    'true': 'keyword',
    'false': 'keyword',
    'null': 'keyword',
    'this': 'keyword',
    'if': 'keyword',
    'elif': 'keyword',
    'else': 'keyword',
    'while': 'keyword',
    'return': 'keyword',
    '{': 'symbol',
    '}': 'symbol',
    '(': 'symbol',
    ')': 'symbol',
    '[': 'symbol',
    ']': 'symbol',
    '.': 'symbol',
    ',': 'symbol',
    ';': 'symbol',
    '+': 'symbol',
    '-': 'symbol',
    '*': 'symbol',
    '/': 'symbol',
    '&': 'symbol',
    '|': 'symbol',
    '^': 'symbol',
    '<': 'symbol',
    '>': 'symbol',
    '=': 'symbol',
    '~': 'symbol',
    '%': 'symbol',
    '_GE_': 'symbol',
    '_LE_': 'symbol',
    '_NE_': 'symbol',
    '_DEC_': 'symbol',
    '_INC_': 'symbol',
    '_LSHIFT_': 'symbol',
    '_RSHIFT_': 'symbol',
    '_EQUAL_': 'symbol',
    '"': 'quote',
}
space_tokens = [
    '(', ')', '[', ']', '{', '}', ';', '"', ',', '.', '~', '+', '-', '*', '/', '<', '>', '=',
    '_LE_', '_GE_', '_NE_'
]
long_operators = {
    '==': '_EQUAL_', '<=': '_LE_', '>=': '_GE_', '!=': '_NE_'
}


class Tokenizer:
    def __init__(self):
        self.tokens = []

    def tokenize(self, line):
        tokens = self.line2tokens(line)
        self.tokens.extend(tokens)
        return self.tokens

    def clear(self):
        self.tokens = []

    def line2tokens(self, line):
        tokens = []
        #
        # long length operator
        #
        for op in long_operators:
            line = line.replace(op, long_operators[op])
        #
        # add space around operators
        #
        for token in space_tokens:
            line = line.replace(token, ' ' + token + ' ')
        #
        # split line into tokens
        #
        divided_line = line.strip().split()
        #
        # work with token
        #
        for item in divided_line:
            if item in token_type:
                # special token
                token_kind = token_type[item]
            else:
                if item.isdigit():
                    # integer constant
                    token_kind = 'integerConstant'
                else:
                    token_kind = 'identifier'
            token = Token(token_kind, item)
            tokens.append(token)
        return tokens
