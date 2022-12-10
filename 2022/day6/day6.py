import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
from collections import defaultdict



def solve(offset):
    l = open("input.txt").read().strip()
    for i in range(0,len(l)-offset):
        if len(set(l[i:i+offset])) == offset:
            return i+offset

print(solve(4))
print(solve(14))