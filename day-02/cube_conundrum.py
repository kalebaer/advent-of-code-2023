import math
import re

input_filename = 'day02.in'
test_input_filename = 'day02_test.in'

max_values = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def solution_part_one(input_filename):
    id_sum = 0
    with open(input_filename, 'r') as raw_input:
        input = raw_input.readlines()
    
    # Game
    for game in input:
        game_is_valid = True
        game_header = game.split(': ')[0]
        game_content = game.split(': ')[1]
        game_id = int(game_header.split()[1])

        # Draw
        draws = game_content.split('; ')
        for draw in draws:
            # Subdraw
            for subdraw in draw.split(', '):
                cube = subdraw.split(' ')
                cube_amount = int(cube[0])
                cube_color = cube[1].strip()
                if cube_amount > max_values[cube_color]:
                    game_is_valid = False
                    break
        if game_is_valid:
            id_sum += game_id
    return id_sum


def solution_part_two(input_filename):
    power_sum = 0
    with open(input_filename, 'r') as raw_input:
        input = raw_input.readlines()
    
    # Game
    for game in input:
        power = 0
        min_values = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        game_content = game.split(': ')[1]

        # Draw
        draws = game_content.split('; ')
        for draw in draws:
            # Subdraw
            for subdraw in draw.split(', '):
                cube = subdraw.split(' ')
                cube_amount = int(cube[0])
                cube_color = cube[1].strip()
                if cube_amount > min_values[cube_color]:
                    min_values[cube_color] = cube_amount
        power = min_values['red'] * min_values['blue'] * min_values['green']
        # print(power)
        power_sum += power
    return power_sum


# Test Part One
'''
test_value_one = solution_part_one(test_input_filename)
print(test_value_one)
if test_value_one == 8:
    print('Test Passed')
else:
    print('Test Failed')
'''

# Test Part Two
'''
test_value_two = solution_part_two(test_input_filename)
print(test_value_two)
if test_value_two == 2286:
    print('Test Passed')
else:
    print('Test Failed')
'''

# Solution Part One
print(solution_part_one(input_filename))

# Solution Part Two
print(solution_part_two(input_filename))


# Alternative Solution by u/4HbQ
def f(line):
    bag = {'r':0, 'g':0, 'b':0}
    for num, col in re.findall(r'(\d+) (\w)', line):
        bag[col] = max(bag[col], int(num))
    return math.prod(bag.values())

print(sum(map(f, open('day02.in'))))