from lex import *
from parse import *
from emit import *
import sys

VERSION = "1.1d"


def main():
    print("Teeny Tiny Compiler v" + VERSION + "\n")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")

    filepath = sys.argv[1]
    filename = filepath.split(".")[0]
    outfile = filename + ".c"

    with open(filepath, "r") as inputFile:
        source = inputFile.read()

    print("Initializing components.")
    lexer = Lexer(source)
    emitter = Emitter(outfile)
    parser = Parser(lexer, emitter)

    print("Parsing " + str(inputFile.name) + ".")
    parser.program()
    print("Writing to " + emitter.fullPath + ".")
    emitter.writeFile()

    print("Compiling completed.")


main()
