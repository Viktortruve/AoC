l = []
with open ("day2.txt") as file:
    for line in file:
        l.append([int(item) for item in line.strip().split()])
safe = 0
for silly_list in l:
    list_combinations = []
    passes = 0

    for j in range(len(silly_list)):
        list_combinations.append([silly_list[i] for i in range(len(silly_list)) if i != j])
    list_combinations += [item[::-1] for item in list_combinations]

    for combination in list_combinations:
        diff = combination[1] - combination[0]
        increasing = diff <= 3 and diff >= 1
        if increasing:
            for i in range(1, len(combination)-1):
                val = combination[i+1] - combination[i]
                if val > 3 or val < 1:
                    break     
                if i == len(combination)-2:
                    passes += 1
        else:
            continue
    if passes:
        safe += 1
print(safe)
            
        
        