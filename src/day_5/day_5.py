import os
import re
import math

dirname = os.path.dirname(__file__)
input_data = os.path.join(dirname, 'input.txt')

data = open(input_data)
lines = data.readlines()
lines = [line.strip() for line in lines]

instructions = dict()
updates = []

for line in lines:
    if "|" in line:
        i = line.split('|')
        if i[0] in instructions:
            instructions[i[0]].append(i[1])
        else:
            instructions[i[0]] = [i[1]]
        
    elif "," in line:
        updates.append(line.split(','))

def is_page_in_correct_location(source_page, target_page, update):
    if source_page in instructions and target_page in instructions[source_page]:
        return False
    else:
        return True

def check_correct_order_of_updates(updates: list):
    middle_page_total = 0
    incorrect_updates = []
    for update in updates:
        correct_order = True
        for n, page in enumerate(update):
            for i in range(n + 1):
                if not is_page_in_correct_location(page, update[i], update):
                    correct_order = False
                    incorrect_updates.append(update)
                    break
            if correct_order == False:
                break
        if correct_order == True:
            middle = math.floor(len(update)/2)
            middle_page_total += int(update[middle])
    return middle_page_total, incorrect_updates

total, incorrect_updates = check_correct_order_of_updates(updates)

print(f'Number of incorrect updates: {len(incorrect)}')
print(f'Middle page total {total}')

def swap_locations(l1, l2, update):
    page_1 = update[l1]
    page_2 = update[l2]
    update.insert(l2, page_1)
    del update[l2 + 1]
    update.insert(l1, page_2)
    del update[l1 + 1]

corrected_middle_page_total = 0
for update in incorrect_updates:
    page_location_updates = 1
    while page_location_updates > 0:
        page_location_updates = 0
        for n, page in enumerate(update):
            if n != len(update) - 1 and not is_page_in_correct_location(update[n + 1], page, update):
                swap_locations(n, n + 1, update)
                page_location_updates += 1

corrected_total, incorrect = check_correct_order_of_updates(incorrect_updates)

print(f'Remaining incorrect updates: {len(incorrect)}')
print(f'Corrected middle page total {corrected_total}')

