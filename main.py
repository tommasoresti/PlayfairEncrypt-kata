import sys
from cipher import Cipher

if len(sys.argv) != 2:
    print("No input string")
    exit()

print(Cipher().encode(sys.argv[1]))

