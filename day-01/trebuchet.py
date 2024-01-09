import re
import timeit

digits_to_int = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
input_filename = 'day01.in'

# Original Solution
def original_solution(input_filename, digit_conversion_dictionary):
    total_sum = 0

    with open (input_filename, 'r') as day01_input:
        input = day01_input.readlines()
    for line in input:
        digit_list = []
        i = 0
        for element in line:
            if (element in digit_conversion_dictionary.keys()):
                digit_list.append(digit_conversion_dictionary[element])
            if (i < len(line)-3):
                if line[i:i+3] in digit_conversion_dictionary.keys():
                    digit_list.append(digit_conversion_dictionary[line[i:i+3]])
            if (i < len(line)-4):
                if line[i:i+4] in digit_conversion_dictionary.keys():
                    digit_list.append(digit_conversion_dictionary[line[i:i+4]])
            if (i < len(line)-5):
                if line[i:i+5] in digit_conversion_dictionary.keys():
                    digit_list.append(digit_conversion_dictionary[line[i:i+5]])
            i += 1
        line_value = 10 * digit_list[0] + digit_list[-1]
        total_sum += line_value
    return total_sum


# Original Solution Improved by ChatGPT
def improved_solution(input_filename, digit_conversion_dictionary):
    total_sum = 0

    with open(input_filename, 'r') as input_file:
        for line in input_file.readlines():
            digit_list = []

            for i in range(len(line)):
                if line[i] in digit_conversion_dictionary:
                    digit_list.append(digit_conversion_dictionary[line[i]])
                for j in range(3, 6):  # Check for 3 to 5 characters
                    if line[i:i+j] in digit_conversion_dictionary:
                        digit_list.append(digit_conversion_dictionary[line[i:i+j]])

            line_value = 10 * digit_list[0] + digit_list[-1]
            total_sum += line_value

    return total_sum


# Alternative Solution by u/81reap
def alternative_solution(input_filename, digit_conversion_dictionary):
    total_sum = 0

    # Read File
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()

    for line in lines:
        digits = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))", line)
        parsed_digits = [digit_conversion_dictionary[num] for num in digits]
        number = str(parsed_digits[0]) + str(parsed_digits[-1])
        #print(line, parsed_digits, number)
        total_sum = total_sum + int(number)

    return total_sum

solutions = [original_solution, improved_solution, alternative_solution]
execution_times = []

for solution in solutions:
    timed_solution = lambda: solution(input_filename, digits_to_int)
    execution_time = round((timeit.timeit(timed_solution, number=10) / 10), 2)
    execution_times.append(execution_time)

print("Solutions:")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}: {solution(input_filename, digits_to_int)} | Execution time: {execution_times[i]}s")

# Verify equivalence
print(f'Solutions produce same output: {all(solution(input_filename, digits_to_int) == solutions[0](input_filename, digits_to_int) for solution in solutions)}')
