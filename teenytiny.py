from lex import *
from parse import *

VERSION = "1.0"


def main():
    print("Teeny Tiny Compiler v" + VERSION + "\n")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], "r") as inputFile:
        source = inputFile.read()

    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program()
    print("\nParsing completed.")


main()
