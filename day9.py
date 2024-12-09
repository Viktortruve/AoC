import itertools
program = open("day9.txt").read()
blocks = [(i,program[item]) for i,item in enumerate(range(0,len(program),2))]
free_spaces = [program[i] for i in range(1, len(program),2)] + [0]
def unwrap(blocks, free_spaces):
    s = []
    for block,free_space in zip(blocks,free_spaces):
        for _ in range(int(block[1])):
            s.append(str(block[0]))
        for _ in range(int(free_space)):
            s.append(".")
    return s

def move(s):
    i = 1
    while not all([item == "." for item in s[s.index('.'):]]):
        space = s.index(".")
        s[space] = s[-i]
        del s[-i]
        s.append(".")
        i += 1
    return s

def move_part2(s, files):
    for file in files[::-1]:
        f = []
        for _ in range(int(file[1])):
            f.append(str(file[0]))
        file_length = len(f)
        index = s.index(str(file[0]))
        j = 0
        c = 0
        while(j < index):
            if s[j] == ".":
                if not c:
                    candidate = j
                c += 1
            else:
                c = 0
            if c >= file_length:
                s[candidate:candidate+file_length] = f
                s[index:index+file_length] = ["." for _ in range(file_length)]
                break
            j += 1
    return s

unwrapped = unwrap(blocks, free_spaces)
moved = move(unwrapped)
moved = [item for item in moved if item != "."]
print(sum([i*int(item) for i,item in enumerate(moved)]))
moved = move_part2(unwrapped, blocks)
print(sum([i*int(item) if item != "." else 0 for i,item in enumerate(moved) if item]))

# 90835814297 too low 
# 86224312106

# part 2
# 6447597218597 too high