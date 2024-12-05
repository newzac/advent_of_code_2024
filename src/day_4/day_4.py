import os
import re

dirname = os.path.dirname(__file__)
input_data = os.path.join(dirname, 'input.txt')

data = open(input_data)
lines = data.readlines()
grid = [line.strip() for line in lines]
target_string = 'XMAS'
target_string_length = len(target_string)

max_depth  = len(grid) - 1
max_length = len(grid[0]) - 1


def find_all_in_line(line):
    reverse_target_string = target_string[::-1]
    matches = re.findall(r'XMAS', line)
    rematches = re.findall(r'SAMX', line)
    return len(matches) + len(rematches)

def gather_letters_down_right(x,y):
    letters = []
    ny = y
    nx = x
    while ny <= max_depth and nx <= max_length:
      letters.append(grid[ny][nx])
      nx += 1
      ny += 1
    len(letters)
    return ''.join(letters)

def gather_letters_up_right(x,y,letters=[]):
    letters = []
    ny = y
    nx = x
    while ny >= 0 and nx <= max_length:
      letters.append(grid[ny][nx])
      ny -= 1
      nx += 1
    
    len(letters)
    return ''.join(letters)

def check_string(string):
   return string == "MAS" or string == "SAM"

def find_mas():
    xmas_found = 0
    for y, line in enumerate(grid):
      if y == 0 or y == max_depth:
         continue
      else:
         potential_mas = [m.start() for m in re.finditer(r'A', line)]
         for a in potential_mas:
            if a == 0 or a == max_length:
               continue
            else:
              backslash_slash = f'{grid[y - 1][a - 1]}{grid[y][a]}{grid[y + 1][a + 1]}'
              forward_slash = f'{grid[y - 1][a + 1]}{grid[y][a]}{grid[y + 1][a - 1]}'
              if check_string(backslash_slash) == True and check_string(forward_slash) == True:
                xmas_found += 1

    return xmas_found
              



total = 0
for line in grid:
   total += find_all_in_line(line)
for i in range(max_length + 1):
   line = ''.join([item[i] for item in grid])
   total += find_all_in_line(line)

   dd = gather_letters_down_right(i, 0)
   total += find_all_in_line(dd)
   ur = gather_letters_up_right(i, max_depth)
   total += find_all_in_line(ur)
for i in range(1,max_depth + 1):
   dr = gather_letters_down_right(0, i)
   total += find_all_in_line(dr)
for i in range(1,max_depth):
   ur = gather_letters_up_right(0, i)
   total += find_all_in_line(ur)

print(f'Total XMAS: {total}')
print(f'Total X-MAS: {find_mas()}')

# for y, line in enumerate(lines):
#     for x, letter in enumerate(line):
#         for t, tletter in enumerate(target_string):
#             if 

#             if t == len(target_string) - 1:
#                 print(f"Found at {x},{y}")
