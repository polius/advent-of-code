import re

def simulate(program, reg_a, reg_b, reg_c):
    pointer = 0
    output = []
    while pointer < len(program):
        opcode, opvalue_literal = program[pointer:pointer + 2]
        opvalue = reg_a if opvalue_literal == 4 else reg_b if opvalue_literal == 5 else reg_c if opvalue_literal == 6 else opvalue_literal

        match opcode:
            case 0:
                reg_a = reg_a // (2 ** opvalue)
            case 1:
                reg_b = reg_b ^ opvalue_literal
            case 2:
                reg_b = opvalue % 8
            case 3:
                pointer = opvalue_literal - 2 if reg_a != 0 else pointer
            case 4:
                reg_b = reg_b ^ reg_c
            case 5:
                output.append(opvalue % 8)
            case 6:
                reg_b = reg_a // (2 ** opvalue)
            case 7:
                reg_c = reg_a // (2 ** opvalue)

        pointer += 2

    return output

with open("input.txt") as fopen:
    file = fopen.read().strip()

program = list(map(int, re.search(r"Program: (.*)", file).group(1).split(',')))
solutions = {0}

for i in reversed(range(0, len(program))):
    expected_instruction = program[i]

    for a in solutions.copy():
        solutions.remove(a)
        a *= 8

        for a_modifier in range(8):
            reg_a = a + a_modifier
            reg_b = 0
            reg_c = 0
            output = simulate(program, reg_a, reg_b, reg_c)

            if output and output[0] == expected_instruction:
                solutions.add(reg_a)

print(min(solutions))