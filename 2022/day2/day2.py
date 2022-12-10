l = []
with open("input.txt") as file:
	for line in file:
		l.append(line.strip().split())

m = {"A": "Rock", "X": "Rock",
	"B": "Paper", "Y": "Paper",
	"C": "Scissor", "Z": "Scissor"
	}
points = {"Rock": 1, "Paper": 2, "Scissor": 3}
beats = {"Rock": "Scissor", "Scissor": "Paper","Paper": "Rock"}
beaten_by = {v: k for k, v in beats.items()}


def play(ele):
	a,b = (m[ele[0]],m[ele[1]])
	if beats[a] == b:
		return points[b]
	if a == b:
		return points[b] + 3 
	if beaten_by[a] == b:
		return points[b] + 6

def play_rigged(ele):
	a,b = (m[ele[0]],m[ele[1]])
	if ele[1] == "X":
		b = beats[a]
	elif ele[1] == "Y":
		b = a 
	else:
		b = beaten_by [a]

	if beats[a] == b:
		return points[b]
	if a == b:
		return points[b] + 3 
	if beaten_by[a] == b:
		return points[b] + 6

print(sum(map(play,l)))
print(sum(map(play_rigged,l)))