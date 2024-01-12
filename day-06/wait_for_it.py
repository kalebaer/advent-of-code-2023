import math

# Test Input
'''
test_times = [7, 15, 30]
test_distances = [9, 40, 200]
'''

# Input Part One
'''
times = [40, 81, 77, 72]
distances = [219, 1012, 1365, 1089]
'''

# Input Part Two
times = [40817772]
distances = [219101213651089]

records = []

for time, distance in list(zip(times, distances)):
    upper = (time + math.sqrt(time ** 2 - 4 * distance)) / 2
    lower = (time - math.sqrt(time ** 2 - 4 * distance)) / 2
    records.append(int(upper)-int(lower))

print(math.prod(records))