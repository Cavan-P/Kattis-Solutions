import sys

data = sys.stdin.readlines()

n = int(data[0].split()[0])
vals = data[1].split()
total = 0

for i in range(0, n):
    if int(vals[i]) < 0:
        total += 1
        
print(total)
