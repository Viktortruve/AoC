import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
from collections import defaultdict

paths = {}
sizes = {}
path = "/"

def size(dir):
    if sizes.get(dir) is not None:
        return sizes[dir]
    else: 
        return sum(map(size,paths[dir]))

with open("input.txt") as file:
    for line in file:
        s = line.strip().split(" ")
        if '$' in s:
            if 'ls' in s:
                continue
            if 'cd' in s:
                if '..' in s:
                    curr_folder = path.split('/')
                    curr_folder = curr_folder[:-2]
                    curr_folder = "/".join(curr_folder)
                    curr_folder += "/"
                    path = curr_folder

                elif '/' in s:
                    path = "/"
                
                else:
                    if path == "/":
                        path += s[2] + "/"

                    else:
                        path = path + s[2] + "/"

    
        if 'dir' in s or any([item for item in s if item.isnumeric()]):
            if paths.get(path) is None:
                paths[path] = []
            paths[path].append(path+s[1]+"/")
            if s[0].isnumeric():
                sizes[path+s[1]+"/"] = int(s[0])

    directories = {}
    for k,v in paths.items():
        c = sum(map(size,v))
        directories[k] = c
    
    
    used = directories['/']
    pprint(sum([item[1] for item in sorted(directories.items(), key = lambda x: x[1]) if item[1] <= 100000]))
    needed_space = 30000000-(70000000-used)
    print(l_filter(lambda x: x[1] >= needed_space, sorted(directories.items(), key = lambda x: x[1]))[0][1])

