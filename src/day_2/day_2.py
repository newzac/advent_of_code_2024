import os
import re

dirname = os.path.dirname(__file__)
input_data = os.path.join(dirname, 'input.txt')

data = open(input_data)
reports = []
for report in data:
    cd = re.sub('\n', '', report)
    ra = cd.split(' ')
    reports.append(ra)

def get_current_direction(current_level, previous_level):
    if previous_level == None:
        return None
    elif int(current_level) > int(previous_level):
        return 'increasing'
    elif int(current_level) < int(previous_level):
        return 'decreasing'
    elif int(current_level) == int(previous_level):
        return 'neither'

def is_safe_direction(current_direction, previous_direction):
    if previous_direction == None:
        return True
    if current_direction == 'neither':
        return False
    if current_direction == previous_direction:
        return True
    else:
        return False
def is_safe_difference(current_level, previous_level):
    if previous_level == None:
        return True
    else:
        return 1 <= abs(int(current_level) - int(previous_level)) <= 3

def check_report(report):
    previous_level = None
    previous_direction = None
    safe = None
    for level in report:
        if previous_level == None and previous_direction == None:
            previous_level = level
            safe = True
            continue
        current_direction = get_current_direction(level, previous_level)
        safe_direction = is_safe_direction(current_direction, previous_direction)
        safe_difference = is_safe_difference(level, previous_level)
        if not safe_difference:
            safe = False
            break
            print(f'Non-safe difference: {level} - {previous_level} = {abs(int(level) - int(previous_level))}')

        elif not safe_direction:
            safe = False
            break
            print(f'Non-safe direction: current: {current_direction} previous: {previous_direction}')
        elif safe_difference and safe_direction:
            safe = True
            previous_level = level
            previous_direction = current_direction
        else:
            safe = False
            break
    return safe

num_safe_reports = 0
for report in reports:
    is_safe_report = check_report(report)
    if is_safe_report:
        num_safe_reports += 1
    else:
        for i, level in enumerate(report):
            new_report = report.copy()
            del new_report[i]
            is_new_report_safe = check_report(new_report)
            if is_new_report_safe:
                num_safe_reports += 1
                break
print(f'Total Safe Reports: {num_safe_reports}')
