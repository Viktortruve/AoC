import numpy as np
import itertools
l = []
instructions = []
with open("day15.txt") as file:
    for line in file:
        if not line:
            continue
        line = line.strip()
        if "#" in line or "O" in line or "@" in line or "." in line:
            x = []
            for ele in line:
                e = ele.strip()
                if e == "@":
                    x.append(e)
                    x.append(".")
                elif e == "O":
                    x.append("[")
                    x.append("]")

                else:
                    x.append(e)
                    x.append(e)
            l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
        else:
            instructions += [item for item in line]

m = np.array(l, dtype=object)
direction_map = {
    "^": [-1,0],
    ">": [0,1],
    "v": [1,0],
    "<": [0,-1]
}

print('\n'.join(map(''.join, m)))
def aligned_boxes(pos, instr, m, b):
    directions = [
        direction_map[instr],
    ]
    
    new_boxes = []
    new_boxes_left = [
        [(pos[0][0] + d[0], pos[0][1] + d[1]), "["] for d in directions
        if m[pos[0][0] + d[0]][pos[0][1] + d[1]] == "["
    ]
    new_boxes_right = [
        [(pos[0][0] + d[0], pos[0][1] + d[1]), "]"] for d in directions
        if m[pos[0][0] + d[0]][pos[0][1] + d[1]] == "]"
    ]
    
    new_boxes += [ [(box[0][0], box[0][1] + 1), "]"] for box in new_boxes_left ]
    new_boxes += [ [(box[0][0], box[0][1] - 1), "["] for box in new_boxes_right ]

    
    new_boxes += new_boxes_left
    new_boxes += new_boxes_right
    old_boxes = [item for item in b]
    new_boxes = [item for item in new_boxes if item not in old_boxes]
    if not new_boxes:
        return b
    result = []
    for new_pos in new_boxes:
        b.append(new_pos)
        result.extend(aligned_boxes(new_pos, instr, m, b))
        b.pop()
    return result

robot = np.argwhere(m=="@")[0]
for instr in instructions:
    next_c = [robot[0] + direction_map[instr][0], robot[1] + direction_map[instr][1]]
    next_val = m[next_c[0]][next_c[1]]
    if next_val == "#":
        continue
    elif next_val in [ "[" , "]" ]:
        if next_val == "[":
            neighbor_box = [(next_c[0], next_c[1]+1), ']' ]
        else:
            neighbor_box = [(next_c[0], next_c[1]-1), '[' ]
        this_box = [tuple(next_c), next_val]
        boxes = aligned_boxes(this_box, instr, m, [this_box, neighbor_box])
        boxes += aligned_boxes(neighbor_box, instr, m, [this_box, neighbor_box])
        boxes = [list(x) for x in set(tuple(x) for x in boxes)]
        boxes = sorted(boxes, key = lambda p: (p[0][1] - robot[1])**2 + (p[0][0] - robot[0])**2)
        boxes = boxes[::-1]
        if boxes:          
            if not any([m[item[0][0]+direction_map[instr][0]][item[0][1]+direction_map[instr][1]] == "#" for item in boxes]):
                for box in boxes:
                    m[box[0][0]+direction_map[instr][0]][box[0][1]+direction_map[instr][1]] = box[1]
                    m[box[0][0]][box[0][1]] = "."
                m[robot[0]][robot[1]] = "."
                robot = next_c
                m[next_c[0]][next_c[1]] = "@"

    else:
        m[robot[0]][robot[1]] = "."
        robot = next_c
        m[next_c[0]][next_c[1]] = "@"

left_halfs = np.argwhere(m=="[")
print('\n'.join(map(''.join, m)))

print(sum(map(lambda x: 100*x[0]+x[1], left_halfs)))


# too high 1462499
# too low 1416435