import sys

data: list = sys.stdin.readlines()

n1: int = data[0].split()[0]
n2: int = data[0].split()[1]

if n1 > n2:
    print(1)
else:
    print(0)
