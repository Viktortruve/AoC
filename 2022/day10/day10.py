import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
from collections import defaultdict
import math
from PIL import Image
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'/opt/homebrew/bin/tesseract'
pytesseract.tesseract_cmd = path_to_tesseract

X = 1
cycle = 1
relevant_cycles = [20,60,100,140,180,220]
rc_vals = []

with open("input.txt") as file:
    for line in file:
        s = line.strip().split()
        op = s[0]
        if cycle in relevant_cycles:
            rc_vals.append(X*cycle)
        cycle += 1
        if len(s) > 1:
            if cycle in relevant_cycles:
                rc_vals.append(X*cycle)
            cycle += 1
            X += int(s[1])
print(sum(rc_vals))

cycle = 0 
X = 1
ls = [40,80,120,160,200,400]
m = np.empty([6,40],dtype=str) 
offset = 0
with open("input.txt") as file:
    for line in file:
        s = line.strip().split()
        sprite_positions = [(offset,X-1),(offset,X),(offset,X+1)]
        m[offset][cycle] = "#" if (offset,cycle) in sprite_positions else "."
        cycle += 1
        
        if cycle in ls:
            cycle = 0
            offset += 1

        if len(s) > 1:
            m[offset][cycle] = "#" if (offset,cycle) in sprite_positions else "."
            cycle += 1
            if cycle in ls:
                offset += 1
                cycle = 0

            X += int(s[1])
    
    for item in m:
        print("".join(item))



