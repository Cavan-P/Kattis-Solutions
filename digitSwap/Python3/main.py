import sys

data = sys.stdin.readlines()[0].split()[0]

print(''.join(reversed([*data])))
