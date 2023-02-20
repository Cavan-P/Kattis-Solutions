import sys

data: list = sys.stdin.readlines()[0].split()

print(int(data[0])*int(data[1])*int(data[2]))
