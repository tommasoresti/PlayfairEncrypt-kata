import sys
from cipher import Cipher

if len(sys.argv) != 2:
    print("No input string")
    exit()

print(Cipher().run(sys.argv[1]))

