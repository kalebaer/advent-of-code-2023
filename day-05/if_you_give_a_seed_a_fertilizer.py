from functools import reduce

'''
# Part One

def create_map(lst):
    return [[int(k) for k in i.strip().split()] for i in lst]

def check_map(source, map):
    for o in map:
        if source is not None and o is not None and len(o) > 1:
            if o[1] <= source and source <= (o[1] + o[-1]):
                return o[0] + (source - o[1])
    return source

seeds = [
    1848591090,
    462385043,
    2611025720,
    154883670,
    1508373603,
    11536371,
    3692308424,
    16905163,
    1203540561,
    280364121,
    3755585679,
    337861951,
    93589727,
    738327409,
    3421539474,
    257441906,
    3119409201,
    243224070,
    50985980,
    7961058
]

maps = [
    create_map(list(open('seed_to_soil.in'))),
    create_map(list(open('soil_to_fertilizer.in'))),
    create_map(list(open('fertilizer_to_water.in'))),
    create_map(list(open('water_to_light.in'))),
    create_map(list(open('light_to_temperature.in'))),
    create_map(list(open('temperature_to_humidity.in'))),
    create_map(list(open('humidity_to_location.in')))
]

def check_location(seed):
    location = seed
    for map in maps:
        location = check_map(location, map)
    return location

locations = []

for seed in seeds:
    locations.append(check_location(seed))

print(min(locations))
'''

# Part Two
# Solution by u/4HbQ


seeds, *mappings = open('day05.in').read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))

def lookup(inputs, mapping):
    # loops through seeds and length of seed ranges
    for start, length in inputs:
        while length > 0:
            # loops through maps (seed to soil, soil to fertilizer, etc.)
            for m in mapping.split('\n')[1:]:
                dst, src, len = map(int, m.split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else: yield (start, length); break

print(*[min(reduce(lookup, mappings, s))[0] for s in [
    zip(seeds, [1] * len(seeds)),
    zip(seeds[0::2], seeds[1::2])]])