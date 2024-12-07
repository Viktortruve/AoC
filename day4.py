import numpy as np
def isValidPos(i, j, n, m):
 
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

def parse_matrix():
	l = []
	with open("day4.txt") as file:
		for line in file:
			x = []
			for ele in line:
				x.append(ele.strip())
			l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
	return np.array(l)

m = parse_matrix()

def right_xmas(i,j):
    try_coords = [(i+1,j), (i+2,j), (i+3,j), (i+4,j)]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
        return 0    
    return int(m[i+1][j] + m[i+2][j] + m[i+3][j] + m[i+4][j] == "XMAS")

def left_xmas(i,j):
    try_coords = [(i-1,j), (i-2,j), (i-3,j), (i-4,j)]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
        return 0    
    return int(m[i-1][j] + m[i-2][j] + m[i-3][j] + m[i-4][j] == "XMAS")

def down_xmas(i,j):
    try_coords = [(i,j+1), (i,j+2), (i,j+3),]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
        return 0    
    return int(m[i][j+1] + m[i][j+2] + m[i][j+3] + m[i][j+4] == "XMAS")

def up_xmas(i,j):
    try_coords = [(i,j-1), (i,j-2), (i,j-3)]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
        return 0    
    return int(m[i][j-1] + m[i][j-1] + m[i][j-2] + m[i][j-3] == "XMAS")

def diag1_xmas(i,j):
    try_coords = [(i+1,j+1), (i+2,j+2), (i+3,j+3)]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
        return 0
    return int(m[i][j] + m[i+1][j+1] + m[i+2][j+2] + m[i+3][j+3] == "XMAS")

def diag2_xmas(i,j):
    try_coords = [(i-1,j-1), (i-2,j-2), (i-3,j-3)]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
        return 0
    return int(m[i][j] + m[i-1][j-1] + m[i-2][j-2] + m[i-3][j-3] == "XMAS")

def diag3_xmas(i,j):
    try_coords = [(i+1,j-1), (i+2,j-2), (i+3,j-3)]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
        return 0
    return int(m[i][j] + m[i+1][j-1] + m[i+2][j-2] + m[i+3][j-3] == "XMAS")

def diag4_xmas(i,j):
    try_coords = [(i-1,j+1), (i-2,j+2), (i-3,j+3)]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
        return 0
    return int(m[i][j] + m[i-1][j+1] + m[i-2][j+2] + m[i-3][j+3] == "XMAS")

def xmas(i,j):
    return up_xmas(i,j) + down_xmas(i,j) + left_xmas(i,j) + right_xmas(i,j) +  diag1_xmas(i,j) + diag2_xmas(i,j) + diag3_xmas(i,j) + diag4_xmas(i,j)

def x_mas(i,j):
    try_coords = [(i+1,j+1), (i-1,j-1), (i+1,j-1),(i-1,j+1)]
    if not all([isValidPos(a,b,len(m),len(m[0])) for a,b in try_coords]):
         return 0 
    cond1 = m[i-1][j-1] == "M" and m[i+1][j-1] == "M" and m[i-1][j+1] == "S" and m[i+1][j+1] == "S"
    cond2 = m[i-1][j-1] == "S" and m[i+1][j-1] == "S" and m[i-1][j+1] == "M" and m[i+1][j+1] == "M"
    cond3 = m[i-1][j-1] == "M" and m[i+1][j-1] == "S" and m[i-1][j+1] == "M" and m[i+1][j+1] == "S"
    cond4 = m[i-1][j-1] == "S" and m[i+1][j-1] == "M" and m[i-1][j+1] == "S" and m[i+1][j+1] == "M"
    return cond1 or cond2 or cond3 or cond4
xmas_counter = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] != "A":
             continue
        xmas_counter += int(x_mas(i,j))

print(xmas_counter)
MMSS
SSMM
MSMS
SMSM
