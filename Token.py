unary_operator = ['-', '~']
comparison_operator = ['<', '>', '_EQUAL_', '_LE_', '_GE_', '_NE_']

# https://en.cppreference.com/w/c/language/operator_precedence
operator_priority = {
    '*': 3, '/': 3, '%': 3,
    '+': 4, '-': 4,
    '<': 6, '>': 6, '_LE_': 6, '_GE_': 6,
    '_EQUAL_': 7, '_NE_': 7,
    '&': 8,
    '^': 9,
    '|': 10
}

operator = unary_operator + list(operator_priority.keys())

unary_op_code = {
    '-': 'neg', '~': 'not'
}
operator_code = {
    '*': ['call Math.multiply 2'], '/': ['call Math.divide 2'], '%': ['call Math.modulo 2'],
    '+': ['add'], '-': ['sub'],
    '<': ['lt'], '>': ['gt'], '_LE_': ['gt', 'not'], '_GE_': ['lt', 'not'],
    '_EQUAL_': ['eq'], '_NE_': ['eq', 'not'],
    '&': ['and'],
    '^': ['xor'],
    '|': ['or'],
}


class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __str__(self):
        return '%15s:   %s' % (self.kind, self.value)

    def is_identifier(self):
        return self.kind == 'identifier'

    def is_unary_op(self):
        return self.value in unary_operator

    def is_constant(self):
        return self.kind == 'integerConstant'

    def is_term(self):
        return self.is_constant() or self.is_left_par() or self.is_right_par() or self.is_unary_op()

    def is_operator(self):
        return self.value in operator

    def is_left_par(self):
        return self.kind == 'symbol' and self.value == '('

    def is_right_par(self):
        return self.kind == 'symbol' and self.value == ')'

    def operator_code(self):
        if self.is_operator():
            return operator_code[self.value]
        return None

    def unary_code(self):
        if self.is_unary_op():
            return unary_op_code[self.value]
        return None

    def priority(self):
        if self.value in operator:
            return operator_priority[self.value]
        return None
