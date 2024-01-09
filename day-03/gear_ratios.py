# solution by u/4HbQ

# import math and regular expression module
import math as m
import re

# convert input file into a list
board = list(open('day03.in'))

# create empty dictionary to store found characters
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

# iterate over each row in the board list using the enumerate() function 
# to get both the index (r) and the row itself (row)
for r, row in enumerate(board):
    # find all occurrences of one or more digits (\d+) in the current row
    for n in re.finditer(r'\d+', row):
        # for each match found, create a set called edge that represents the neighboring cells
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        # if one of the neighboring cells contains a character, 
        # the integer value of the digits is appended to the chars dictionary
        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

# calculate sums for part 1 and part 2
print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))