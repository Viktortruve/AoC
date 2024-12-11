#from functools import cache
#from iteration_utilities import deepflatten
from collections import defaultdict
s = "0 5601550 3914 852 50706 68 6 645371"
arr = [int(item) for item in s.split()]
cached = defaultdict(int)
for item in arr:
    cached[item] = 1
for _ in range(75):
    new_stones = defaultdict(int)
    for stone, n in cached.items():
        str_number = str(stone)
        if stone == 0:
            new_stones[1] += n
        elif len(str_number) % 2 == 0:
            num_1 = int(str_number[:len(str_number) // 2])
            num_2 = int(str_number[len(str_number) // 2:])
            new_stones[num_1] += n
            new_stones[num_2] += n
        else:
            new_stones[stone*2024] += n
    cached = new_stones

print(sum(cached.values()))
