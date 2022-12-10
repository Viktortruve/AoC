import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
import string
from collections import defaultdict
stacks = [["bs"],
["C","Q","B"],
    ["Z","W","Q","R"],
    ["V","L","R","M","B"],
    ["W","T","V","H","Z","C"],
    ["G","V","N","B","H","Z","D"],
    ["Q","V","F","J","C","P","N","H"],
    ["S","Z","W","R","T","G","D"],
    ["P","Z","W","B","N","M","G","C"],
    ["P","F","Q","W","M","B","J","N"]
]

#stacks = [["bs"],["N","Z"],["D","C","M"],["P"]]

with open("input.txt") as file:
    for line in file:
        if "move" not in line:
            continue
        s = line.strip().split()
        splits = int(s[1])
        n1 = int(s[3])
        n2 = int(s[5])
        to_move = stacks[n1][:splits]
        stacks[n2] = to_move + stacks[n2]
        stacks[n1] = stacks[n1][splits:]
        print(stacks)
        print()
    del stacks[0]
    print(stacks)
    print("".join([item[0] for item in stacks]))
