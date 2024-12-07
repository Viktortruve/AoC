from pprint import pprint
def fix(updates):
    xs = []
    for instr in updates:
        rules_with_instr_before = [item[0] for item in page_rules if item[1] == instr]
        xs.append((rules_with_instr_before, [instr]))
    apa = sorted(xs, key= lambda x: len(x[0]))
    return [item[1][0] for item in apa]
def ok(updates):
    bools = []
    for instr in updates:
        rules_with_instr_after = [item[1] for item in page_rules if item[0] == instr]
        rules_with_instr_after = [item for item in rules_with_instr_after if item in updates]
        rules_with_instr_before = [item[0] for item in page_rules if item[1] == instr]
        rules_with_instr_before = [item for item in rules_with_instr_before if item in updates]
        all_before_ok = all([updates.index(instr) > updates.index(item) for item in rules_with_instr_before])
        all_after_ok = all([updates.index(instr) < updates.index(item) for item in rules_with_instr_after])
        bools.append(all_after_ok and all_before_ok)
        #print(all_before_ok, all_after_ok)
    return all(bools)

page_rules = []
list_of_updates = []

with open("day5.txt") as file:
    for line in file:
        if '|' in line:
            a,b = line.split('|')
            page_rules.append((int(a),int(b)))
        elif "," in line:
            page = line.split(',')
            list_of_updates.append([int(item) for item in page])
        else: 
            continue
s1 = 0
s2 = 0
for i, updates in enumerate(list_of_updates):
    if ok(updates):
        s1 += updates[len(updates)//2]
    else:
        fixed = fix(updates)
        s2 += fixed[len(fixed)//2]
print(s1)
print(s2)