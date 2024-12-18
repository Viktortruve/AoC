from collections import defaultdict
import more_itertools
from z3 import *
registers = {}
with open("day17.txt") as file:
    for line in file:
        if not line.strip():
            continue
        line = line.strip()
        l = line.split(":")
        if "Register" in line:
            registers[l[0].split()[1]] = int(l[1].strip())
            continue
        instructions = [int(item) for item in l[1].strip().split(",")]

operand_to_register = {
    4: "A",
    5: "B",
    6: "C"
}

def adv(n):
    v = operand_to_register.get(n)
    if v:
        n = registers[v]
    registers["A"] //= 2**n
    symbolic_operations.append(f"A = A >> {v if v else n}")


def bxl(n):
    registers["B"] ^= n
    symbolic_operations.append(f"B = B ^ {n} ")
def bst(n):
    v = operand_to_register.get(n)
    if v:
        n = registers[v]
    registers["B"] = n % 8
    symbolic_operations.append(f"B = {v if v else n} % 8 ")

def jnz(n):
    global instruction_pointer
    if registers["A"] != 0:
        instruction_pointer = n
    else:
        instruction_pointer += 2        
def bxc(n):
    registers["B"] ^= registers["C"]        
    symbolic_operations.append(f"B = B ^ C ")

def out(n):
    global symbols
    global symbolic_operations
    v = operand_to_register.get(n)
    if v:
        n = registers[v]
    n = n % 8
    symbols.append(copy.deepcopy(symbolic_operations))
    symbolic_operations = []
    return str(n)

def bdv(n):
    v = operand_to_register.get(n)
    if v:
        n = registers[v]
    registers["B"] = registers['A'] // 2**n

    symbolic_operations.append(f"B = A >> {v if v else n}")

def cdv(n):
    v = operand_to_register.get(n)
    if v:
        n = registers[v]
    
    registers["C"] = registers['A'] // 2**n
    symbolic_operations.append(f"C = A >> {v if v else n}")


program = "".join([str(item) for item in instructions])
program_out = ""
instruction_pointer = 0
symbolic_operations = []
symbols = []
registers["A"] = 109685364335840
while(True):
    if instruction_pointer >= len(instructions):
        break
    opcode, operand = instructions[instruction_pointer], instructions[instruction_pointer+1]
    if opcode == 0:
        adv(operand)
        instruction_pointer += 2

    elif opcode == 1:
        bxl(operand)
        instruction_pointer += 2

    elif opcode == 2:
        bst(operand)
        instruction_pointer += 2

    elif opcode == 3:   
        jnz(operand) 
    
    elif opcode == 4:
        bxc(operand)
        instruction_pointer += 2        

    elif opcode == 5:
        outp = out(operand)
        program_out += outp
        instruction_pointer += 2

    elif opcode == 6:
        bdv(operand)
        instruction_pointer += 2

    elif opcode == 7:
        cdv(operand)
        instruction_pointer += 2

print(",".join(program_out))
Bs = []
As = []
from z3 import *
def evaluate_operations(operations, A, B_expr=None, C_expr=None):
    for operation in operations:
        lhs, rhs = operation.split('=', 1)
        lhs = lhs.strip()
        rhs = rhs.strip()

        rhs_expr = parse_expression(rhs, A, B_expr, C_expr)

        if lhs == 'B':
            B_expr = rhs_expr
        elif lhs == 'C':
            C_expr = rhs_expr
        elif lhs == 'A':
            A = rhs_expr 

    return A, B_expr, C_expr

def parse_expression(rhs, A, B_expr, C_expr):
    if B_expr is not None:
        rhs = rhs.replace('B', 'B_expr')  
        rhs = rhs.replace('C', 'C_expr')  
    rhs = rhs.replace('/ 2**', ' >> ')  

    return eval(rhs, {"A": A, "B_expr": B_expr, "C_expr": C_expr})

A = BitVec('A', 64)
B_expr = None
C_expr = None
s = Optimize()
s.add(A < 109685330781408)
for symbol, c in zip(symbols,program):
    A, B_expr, C_expr = evaluate_operations(symbol, A, B_expr, C_expr)
    s.add(B_expr % 8 == c)
s.minimize(A)
s.check()
print(s.model())

