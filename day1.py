
l1 = []
l2 = []
with open("input.txt") as file:
    for line in file:
      a,b = line.strip().split()
      l1.append(int(a))
      l2.append(int(b))
l1 = sorted(l1)
l2 = sorted(l2)
print(sum([abs(x1-x2) for (x1,x2) in zip (l1,l2)]))
from collections import Counter
c = Counter(l2)
print(sum([c[item]*item for item in l1]))
