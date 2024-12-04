import os
import re

dirname = os.path.dirname(__file__)
input_data = os.path.join(dirname, 'input.txt')

# find an X in the input
# scan the rest of the row forward for MAS
# scan the row backward for MAS
# scan the column down for MAS
# scan the column up for MAS
# scan down and right for MAS
# scan down and left for MAS
# scan up and right for MAS
# scan up and left for MAS

data = open(input_data)
lines = data.readlines()
lines = [line.strip() for line in lines]
target_string = 'XMAS'
# print(lines)
for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        for t, tletter in enumerate(target_string):
            if letter == tletter:

            if t == len(target_string) - 1:
                print(f"Found at {x},{y}")
