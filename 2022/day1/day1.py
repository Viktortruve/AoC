from collections import defaultdict
l = defaultdict(int)
i = 0

with open("input.txt") as file:
	for line in file:
		if line != '\n':
			l[i] += int(line)
		else:
			i += 1
	print(max(l.values()))
	print(sum([item[1] for item in sorted(l.items(), key = lambda x: x[1],reverse=True)[:3]]))

