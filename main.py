from Tokenizer import Tokenizer
from Parser import Parser


def show_codes(codes):
    for code in codes:
        print(code)
    print()


def repl():
    tokenizer = Tokenizer()
    parser = Parser()
    exp = ''

    while exp != 'end':
        exp = input('exp > ')
        tokenizer.clear()
        tokens = tokenizer.tokenize(exp)
        codes = parser.parse(tokens)
        show_codes(codes)


if __name__ == '__main__':
    repl()
