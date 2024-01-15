# Solution by u/4HbQ
# Commented for (my own) better understanding

def eval(line):
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', face))
    # Creates a list with the highest count of each card in the hand
    # example:
        # hand: C89AA
            # 089AA -> [2, 2, 1, 1, 1] (max and is therefore chosen)
            # C09AA -> [2, 2, 1, 1, 1] (max)
            # C80AA -> [2, 2, 1, 1, 1] (max)
            # C890A -> [1, 1, 1, 1, 1]
            # C89A0 -> [1, 1, 1, 1, 1]
        # best: [2, 2, 1, 1, 1]
    best = max(type(hand.replace('0', r)) for r in hand)
    return best, hand, int(bid)

# Counts number of card occurrences in a hand 
# and sorts them in descending order
def type(hand):
    return sorted(map(hand.count, hand), reverse=True)

for face in 'ABCDE', 'A0CDE':
    print(sum(rank * bid for rank, (*_, bid) in
        enumerate(sorted(map(eval, open('day07.in'))), start=1)))
