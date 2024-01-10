import re

scratchcards = list(open('day04.in'))
test = list(open('day04_test.in'))


def solution_part_one(scratchcards):
    total_points = 0
    for card in scratchcards:
        points = 0
        content = re.split(r'[:|]', card)
        winning_numbers = [int(number) for number in content[1].strip().split()]
        numbers = [int(number) for number in content[-1].strip().split()]
        for number in numbers:
            if number in winning_numbers:
                points = 1 if points == 0 else points * 2
        total_points += points
    return total_points


def solution_part_two(scratchcards):
    card_amounts = {card_number: 1 for card_number in range(len(scratchcards))}
    for index, card in enumerate(scratchcards):
        n = 0
        content = re.split(r'[:|]', card)
        winning_numbers = [int(number) for number in content[1].strip().split()]
        numbers = [int(number) for number in content[-1].strip().split()]
        for number in numbers:
            if number in winning_numbers:
                n += 1
        for i in range(1, n+1):
            if index + i + 1 <= len(scratchcards):
                card_amounts[index + i] += card_amounts[index]
    return sum(card_amounts.values())


# print(solution_part_one(test))
print(solution_part_one(scratchcards))

# print(solution_part_two(test))
print(solution_part_two(scratchcards))



# Alternative Solution by u/4HbQ

p1 = [0.5]*len(scratchcards)
p2 = [1.0]*len(scratchcards)

for i, line in enumerate(scratchcards):
    w, h = map(str.split, line.split('|'))

    for j in range(len(set(w) & set(h))):
        p1[i] *= 2
        p2[i+j+1] += p2[i]

for p in p1, p2: print(sum(map(int, p)))