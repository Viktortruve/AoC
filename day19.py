designs = []
from functools import cache
with open("day19.txt") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if "," in line:
            towels = line.split(", ")
        else:
            designs.append(line)
@cache
def works(design, towel):
    if "".join(towel) == design:
        return 1
    else:
        if not design.startswith("".join(towel)):
            return 0
        return sum(map(lambda x: works(design, towel+x), towels))
ok_designs = 0

for i, design in enumerate(designs):
    passing_designs = towels
    passing_designs = [item for item in passing_designs if design.startswith("".join(item))]
    for towel in passing_designs:
        ok_designs += works(design, towel)

print(ok_designs)
