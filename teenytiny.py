from lex import *
from parse import *


def main():
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], "r") as inputFile:
        source = inputFile.read()

    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program()
    print("Parsing completed.")


main()
