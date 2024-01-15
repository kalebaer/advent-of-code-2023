# assign each hand a score based on its strenght to be able to rank it
# calculate result
input = list(open('day07_test.in'))

values = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

winnings = []

for line in input:
    hand = line.split()[0]
    winning = 0
    cards = []
    for card in hand:
        if card not in cards:
            winning += values[card] ** hand.count(card) if hand.count(card) > 0 else 0
            cards.append(card)
    winnings.append(winning)

print(winnings)