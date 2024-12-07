from collections import defaultdict
import itertools
ls = []
with open("day7.txt") as file:
    for line in file:
        s = line.strip().split(':')
        ls.append((int(s[0]), [int(item) for item in s[1].split()]))

total = 0
for k,v in ls:
    solvable_ways = 0
    operator_shuffles = itertools.product("*+|", repeat=len(v)-1)
    for shuffle in operator_shuffles:
        val = v[0]
        for i in range(1, len(v)):
            if shuffle[i-1] == "+":
                val += v[i]
            elif shuffle[i-1] == "*":
                val*= v[i]
            elif shuffle[i-1] == "|":
                val = int(str(val) + str(v[i]))  
        if val == k:
            total += val
            break
print(total)
# too high 4225351764413
# too low 4122618555677