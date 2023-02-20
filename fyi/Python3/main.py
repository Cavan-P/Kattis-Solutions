import sys

data = sys.stdin.readlines()[0].split()[0]


if data[0] == '5' and data[1] == '5' and data[2] == '5':
    print(1)
else:
    print(0)


