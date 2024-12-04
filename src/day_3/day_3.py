import os
import re

dirname = os.path.dirname(__file__)
input_data = os.path.join(dirname, 'input.txt')

data = open(input_data)
mulls = []
total = 0
for line in data:
    mulls.append(re.findall(r'(do\(\))|mul\((\d+)\,(\d+)\)|(don\'t\(\))', line))

doing = True

def mul(a, b, do):
    if doing == True:
        return int(a) * int(b)
    else:
        return 0

for list in mulls:
    for do,a,b,dont in list:
        if do == 'do()':
            doing = True
        if a != '' and b != '':
            m = mul(a, b, do)
            total += m
        if dont == "don't()":
            doing = False

print(f'Total: {total}')