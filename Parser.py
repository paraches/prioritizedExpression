LOWEST_PRIORITY = 20


class Parser:
    def __init__(self):
        self.tokens = []
        self.token_index = 0
        self.error = False
        self.codes = []

    def get_token(self):
        if len(self.tokens) > self.token_index:
            token = self.tokens[self.token_index]
            self.token_index += 1
            return token
        else:
            return None

    def code_write(self, command, args):
        s = '%s %s' % (command, args)
        self.codes.append(s)

    def error_message(self, locate, required, actual):
        print('In %s, %s is expected but %s come.' % (locate, required, actual))
        self.error = True

    def parse(self, tokens=None):
        self.tokens = tokens
        self.token_index = 0
        self.error = False
        self.codes = []

        token = self.get_token()
        self.do_expression(token, LOWEST_PRIORITY)
        return self.codes

    def do_expression(self, token, priority):
        if not token.is_term():
            self.error_message('Expression', 'Term', token)
            return token

        token = self.do_term(token, priority)

        while token.is_operator() and token.priority() < priority:
            opcodes = token.operator_code()
            new_priority = token.priority()

            token = self.get_token()
            if not token.is_term():
                self.error_message('Expression', 'Term', token)
                return token
            token = self.do_expression(token, new_priority)

            for opcode in opcodes:
                self.code_write('arithmetic', (opcode,))

        return token

    def do_term(self, token, priority):
        #
        #   integer constant
        #
        if token.kind == 'integerConstant':
            term_value = token.value
            self.code_write('push', ('constant', term_value, 'int'))
            token = self.get_token()
        #
        #   ( expression )
        #
        elif token.is_left_par():
            token = self.get_token()
            token = self.do_expression(token, LOWEST_PRIORITY)
            if not token.is_right_par():
                self.error_message('term left_par', ')', token)
                return token
            token = self.get_token()
        #
        #   unary operator
        #   ~, -
        #
        elif token.is_unary_op():
            op = token

            token = self.get_token()
            if not token.is_term():
                self.error_message('term unaryOp', 'term', token)
                return token
            token = self.do_term(token, priority)

            self.code_write('arithmetic', (op.unary_code(),))

            return token
        else:
            self.error_message('term', 'term', token)

        return token
