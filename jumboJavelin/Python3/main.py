import sys

data: list = sys.stdin.readlines()

n: int = int(data[0])

lengths: list = data[:0] + data[1:]

total: int = 0

for i in range(0, n):
    total += int(lengths[i])-1
    
print(total + 1)
