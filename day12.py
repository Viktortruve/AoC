import numpy as np
import math
import itertools
from matplotlib import pyplot as plt
from shapely.geometry import box, Polygon
from shapely.ops import unary_union

def parse_matrix():
    l = []
    with open("day12.txt") as file:
        for line in file:
            x = []
            for ele in line:
                x.append(ele.strip())
            
            l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
    return np.array(l, dtype=object)

def outside_matrix(curr, m):
    return (curr[0] < 0 or curr[0] >= len(m)) or (curr[1] < 0 or curr[1] >= len(m))

diagonals = [
    [-0.5,0.5],
    [0.5,0.5],
    [0.5,-0.5],
    [-0.5,0.5],
    ]

directions = [
    [0,1],
    [1,0],		
    [0,-1],
    [-1,0]
]
def map_region(m, cord, l):
    ns = map(lambda x: (cord[0]+x[0], cord[1]+x[1]),directions)
    ns = filter(lambda x: not outside_matrix(x,m) and x not in l, ns)
    ns = list(filter(lambda x: m[x] == m[cord], ns))
    if not ns:
            return l
    else:
        for n in ns:
            l.add(n)
            l.update(map_region(m, n, l))
    return l

def perimeter(region, m):
    perimeter = 0
    for cord in region:
        neighbors = list(map(lambda x: (cord[0]+x[0], cord[1]+x[1]),directions))
        neighbors_on_border = [item for item in neighbors if item[0] == -1 or item[0] == len(m) or item[1] == -1 or item[1] == len(m)]
        neighbors_inside_matrix = list(filter(lambda x: not outside_matrix(x,m), neighbors))
        neighbors_inside_matrix = list(filter(lambda x: m[x] != m[cord], neighbors_inside_matrix))
        perimeter_points = set(neighbors_inside_matrix + neighbors_on_border)
        perimeter += len(perimeter_points)
    return perimeter	

def price_p1(region, m):
    r_perimeter = perimeter(region, m)
    price = r_perimeter*len(region)
    return price

import matplotlib.pyplot as plt

def merge_lines(lines):
    horizontal_lines = {}
    vertical_lines = {}

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2: 
            x = x1
            y_min, y_max = sorted([y1, y2])
            if x in vertical_lines:
                vertical_lines[x].append((y_min, y_max))
            else:
                vertical_lines[x] = [(y_min, y_max)]
        elif y1 == y2: 
            y = y1
            x_min, x_max = sorted([x1, x2])
            if y in horizontal_lines:
                horizontal_lines[y].append((x_min, x_max))
            else:
                horizontal_lines[y] = [(x_min, x_max)]

    def merge_intervals(intervals):
        intervals.sort()
        merged = [intervals[0]]
        for current in intervals[1:]:
            prev = merged[-1]
            if current[0] <= prev[1]:  
                merged[-1] = (prev[0], max(prev[1], current[1]))
            else:
                merged.append(current)
        return merged

    full_horizontal_lines = [(x_min, y, x_max, y) for y, intervals in horizontal_lines.items() for x_min, x_max in merge_intervals(intervals)]
    full_vertical_lines = [(x, y_min, x, y_max) for x, intervals in vertical_lines.items() for y_min, y_max in merge_intervals(intervals)]

    return full_horizontal_lines + full_vertical_lines

def convert_to_lines(bboxes):
    shapely_boxes = [box(x_min, y_min, x_max, y_max) for x_min, y_min, x_max, y_max in bboxes]
    merged_polygon = unary_union(shapely_boxes)
    exterior_coords = list(merged_polygon.exterior.coords)
    lines = [(exterior_coords[i], exterior_coords[i + 1]) for i in range(len(exterior_coords) - 1)]
    full_lines = merge_lines(lines) 
    return full_lines

def reconstruct_ordered_points(segments):
    edges = [((x1, y1), (x2, y2)) for x1, y1, x2, y2 in segments]

    ordered_points = [edges[0][0]]  
    current_point = edges[0][1]    
    edges.pop(0)                   

    while edges:
        for edge in edges:
            if edge[0] == current_point:
                ordered_points.append(edge[0])
                current_point = edge[1]
                edges.remove(edge)
                break
            elif edge[1] == current_point:
                ordered_points.append(edge[1])
                current_point = edge[0]
                edges.remove(edge)
                break

    ordered_points.append(ordered_points[0])

    return ordered_points

def sides(region):
    region = [(x,y*-1) for (y,x) in region]
    bboxes = []
    for cord in region:
        corners = list(map(lambda x: (cord[0]+x[0], cord[1]+x[1]),diagonals))
        min_x = min([item[0] for item in corners])
        min_y = min([item[1] for item in corners])
        max_x = max([item[0] for item in corners])
        max_y = max([item[1] for item in corners])
        bboxes.append([min_x, min_y, max_x, max_y])
    lines = convert_to_lines(bboxes)
    ordered_points = reconstruct_ordered_points(lines)
    polygon = Polygon(ordered_points)
    return polygon

def plot_polygon(polygon, title="Shapely Polygon"):

    exterior_coords = polygon.exterior.coords
    interiors = [interior.coords for interior in polygon.interiors]

    x, y = zip(*exterior_coords)
    plt.plot(x, y, label="Exterior", color="blue")

    for interior_coords in interiors:
        x, y = zip(*interior_coords)
        plt.plot(x, y, label="Interior (Hole)", color="red")

    plt.fill(*zip(*exterior_coords), alpha=0.2, color="blue", label="Polygon Area")
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def lines_to_polygon(lines):
    edges = [((line[0], line[1]), (line[2], line[3])) for line in lines]
    
    ordered_points = [edges[0][0]] 
    current_point = edges[0][1]   

    while len(edges) > 0:
        ordered_points.append(current_point)
        edges = [edge for edge in edges if edge != (ordered_points[-2], current_point)]
        next_edges = [edge for edge in edges if edge[0] == current_point]
        current_edge = next_edges[0]
        edges.remove(current_edge)
        current_point = current_edge[1]

    return Polygon(ordered_points)

def price_p2(regions):
    polys = []
    s = 0
    for region in regions:
        p = sides(region)
        polys.append(p)
    for region, poly in zip(regions,polys):
        other_polys = [item for item in polys if item != poly]
        overlapping_polys = [item for item in other_polys if poly.contains(item)]
        holes = [list(item.exterior.coords) for item in overlapping_polys]

        masked_polygon = Polygon(shell=list(poly.exterior.coords), holes=holes)
        shell_edges = len(masked_polygon.exterior.coords) - 1
        
        holes_edges = sum(len(interior.coords) - 1 for interior in masked_polygon.interiors)
        total_edges = shell_edges + holes_edges
        s += total_edges*len(region)
    return s

m = parse_matrix()
regions = set()
for col in range(len(m)):
        for row in range(len(m)):
                s = set()
                s.add((col, row))
                region = map_region(m, (col,row), s)
                regions.add(frozenset(region))
print(sum(map(lambda x: price_p1(x,m), regions)))
print(price_p2(regions))
