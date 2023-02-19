import sys

data: list = sys.stdin.readlines()

x: int = int(data[0])
y: int = int(data[1])

if x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
elif x > 0 and y > 0:
    print(1)
else:
    print(2)
