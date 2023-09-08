# user definded exception
# raise & assestion
#raise TypeError("execption raised by rasie keyword")
#assert - works based on condition
# a=5
# assert a!=5, "Assertion error raised based on condtion"

import os

print(os.getcwd())
print(os.listdir())
os.remove("file1.txt")
print(os.listdir())