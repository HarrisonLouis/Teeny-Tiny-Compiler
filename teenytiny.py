from lex import *
from parse import *
from emit import *
import sys

VERSION = "1.1"


def main():
    print("Teeny Tiny Compiler v" + VERSION + "\n")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], "r") as inputFile:
        source = inputFile.read()

    print("Initializing components.")
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    print("Parsing " + str(inputFile.name) + ".")
    parser.program()
    print("Writing to " + emitter.fullPath + ".")
    emitter.writeFile()

    print("Compiling completed.")


main()
