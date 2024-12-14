from z3 import Int, Solver
buttons = []
claw_machines = []
with open("day13.txt") as file:
    for line in file:
        l = line.strip() 
        if not l:
            continue
        l = l.split(":")        
        if 'Button' in line:
            nums = l[1].split(",")            
            if 'A' in line:
                buttons.append([3, int(nums[0][3:]), int(nums[1][3:])])
            else:
                buttons.append([1, int(nums[0][3:]), int(nums[1][3:])])
        else:
            sums = l[1].split(",")
            buttons.append([int(sums[0][3:])+10000000000000, int(sums[1][3:])+10000000000000])
            claw_machines.append(buttons)
            buttons  = []

token_cost = 0
for claw_machine in claw_machines:
    s = Solver()
    A,B  = Int("A"), Int("B")
    statement_1 = A*claw_machine[0][1] + B*claw_machine[1][1] == claw_machine[2][0]
    statement_2 = A*claw_machine[0][2] + B*claw_machine[1][2] == claw_machine[2][1]
    s.add([statement_1, statement_2])
    s.check()
    try:
        m = s.model()
        token_cost += int(str(m[A]))*3
        token_cost += int(str(m[B]))*1
    except:
        pass

print(token_cost)




