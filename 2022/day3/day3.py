import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
import string

al = [item for item in string.ascii_lowercase+string.ascii_uppercase]
ns = [i for i in range(1,53)]
z = dict(list(zip(al,ns)))
print(sum(l_map(lambda x: z[list(set(x[0:int(len(x)/2)]).intersection(set(x[int(len(x)/2):])))[0]],parse_file_by_separator('\n'))))
print(sum(l_map(lambda x: z[list(set(x[0]).intersection(set(x[1])).intersection(set(x[2])))[0]],read_file_in_chunks(3))))
