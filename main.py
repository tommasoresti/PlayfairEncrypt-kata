import sys
from cipher import SimpleCipher

if len(sys.argv) != 2:
    print("No input string")
    exit()

print(SimpleCipher.encode(sys.argv[1]))

