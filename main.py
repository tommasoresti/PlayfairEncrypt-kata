import sys
from lib.cipher import SimpleCipher


def print_usages():
    print("Usage:")
    print("\tTo encode: main.py -e <message>")
    print("\tTo decode: main.py -d <message>")


if len(sys.argv) != 3:
    print("Wrong arguments")
    print_usages()
    exit()

commands = {
    "-e": SimpleCipher.encode,
    "-d": SimpleCipher.decode
}

if sys.argv[1] not in commands:
    print("Command not found:" + sys.argv[1])
    print_usages()

print(commands[sys.argv[1]](sys.argv[2]))

