import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
from collections import defaultdict
import math
import os
from matplotlib import pyplot as plt
def computeGCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd
    
monkeys = defaultdict(list)
monkey_test = {
0: {"Divisor": 0, "True": 0, "False": 0, "Op": 0} ,
1: {"Divisor": 0, "True": 0, "False": 0, "Op": 0} ,
2: {"Divisor": 0, "True": 0, "False": 0, "Op": 0} ,
3: {"Divisor": 0, "True": 0, "False": 0, "Op": 0} ,
4: {"Divisor": 0, "True": 0, "False": 0, "Op": 0} ,
5: {"Divisor": 0, "True": 0, "False": 0, "Op": 0} ,
6: {"Divisor": 0, "True": 0, "False": 0, "Op": 0} ,
7: {"Divisor": 0, "True": 0, "False": 0, "Op": 0} 
}



with open("input.txt") as file:
    for line in file:
        s = line.strip().split(" ")
        if "Monkey" in s:
            m_index = int(s[1][0])
            continue
        if "items:" in s:
            monkeys[m_index] = [int(item.replace(',','')) for item in s[2:]]
        if "Operation:" in s:
            monkey_test[m_index]["Op"] = s[4:]
        if "Test:" in s:
            monkey_test[m_index]["Divisor"] = int(s[3])
        if "true:" in s:
            monkey_test[m_index]["True"] = int(s[5])
        if "false:" in s:
            monkey_test[m_index]["False"] = int(s[5])
    
mod_sum = math.prod( [item['Divisor'] for item in monkey_test.values()])

def solve(i,part2=False):
    inspected = defaultdict(int)
    for _ in range(0,i):
        for m in range(len(monkeys)):
            items = monkeys[m]
            divisor = monkey_test[m]["Divisor"]
            false = monkey_test[m]["False"]
            true = monkey_test[m]["True"]
            op = monkey_test[m]["Op"]
            for old in items:
                inspected[m] += 1
                val = eval(str(old) +  str(op[0]) + str(try_int(str(op[1]))))
                val = val % mod_sum if part2 else math.floor(val/3)
                if val % divisor == 0:
                    monkeys[true].append(val)
                else:
                    monkeys[false].append(val)
            monkeys[m] = []
    return math.prod(sorted(inspected.values(),reverse=True)[0:2])


print(solve(20))
print(solve(10000,part2=True))


