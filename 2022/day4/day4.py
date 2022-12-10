import sys
sys.path.append("..")
from AoC_parser import *

def solve(part2=False):
    with open("input.txt") as file:
        overlap = 0
        for line in file:
            x = l_map(lambda x: x.split('-'),line.strip().split(","))
            r1 = [i for i in range(int(x[0][0]),int(x[0][1])+1)]
            r2 = [i for i in range(int(x[1][0]),int(x[1][1])+1)]
            if part2:
                if set(r1).intersection(set(r2)) != set():
                    overlap += 1
            else:
                if set(r1).issubset(set(r2)) or set(r2).issubset(r1):
                    overlap += 1
        return overlap

print(solve())
print(solve(part2=True))