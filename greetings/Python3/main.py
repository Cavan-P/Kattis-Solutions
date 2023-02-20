import sys
import re

data: list = sys.stdin.readlines()[0].split()[0]

e = re.findall('e', data)

print('h' + 'e'*len(e)*2 + 'y')
