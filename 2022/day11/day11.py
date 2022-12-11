import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
from collections import defaultdict
import math
import os
    
monkeys = defaultdict(dict)

with open("input.txt") as file:
    for line in file:
        s = line.strip().split(" ")
        if "Monkey" in s:
            m_index = int(s[1][0])
            continue
        if "items:" in s:
            monkeys[m_index]["items"] = [int(item.replace(',','')) for item in s[2:]]
        if "Operation:" in s:
            monkeys[m_index]["Op"] = s[4:]
        if "Test:" in s:
            monkeys[m_index]["Divisor"] = int(s[3])
        if "true:" in s:
            monkeys[m_index]["True"] = int(s[5])
        if "false:" in s:
            monkeys[m_index]["False"] = int(s[5])
    
mod_sum = math.prod( [item['Divisor'] for item in monkeys.values()])

def solve(i,part2=False):
    inspected = defaultdict(int)
    for _ in range(0,i):
        for m in range(len(monkeys)):
            items = monkeys[m]["items"]
            divisor = monkeys[m]["Divisor"]
            false = monkeys[m]["False"]
            true = monkeys[m]["True"]
            op = monkeys[m]["Op"]
            for old in items:
                inspected[m] += 1
                val = eval(str(old) + op[0] +  op[1])
                val = val % mod_sum if part2 else math.floor(val/3)
                if not val % divisor:
                    monkeys[true]["items"].append(val)
                else:
                    monkeys[false]["items"].append(val)
            monkeys[m]["items"] = []
    return math.prod(sorted(inspected.values(),reverse=True)[0:2])


print(solve(20))
print(solve(10000,part2=True))


