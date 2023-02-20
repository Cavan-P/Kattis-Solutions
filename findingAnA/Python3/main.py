import sys

data = sys.stdin.readlines()[0].split()[0]

for i in range(0, len(data)):
    if data[i] == 'a':
        print(data[i:])
        break
