import os
fileDir = os.path.dirname(os.path.abspath(__file__))

opcodes = {'01': 3, '02': 3, '03': 1, '04': 1, '05': 2, '06': 2, '07': 3, '08': 3, '99': 0}

def day5_2():
	instructions = []

	with open(fileDir + "/input.txt") as file:
		line = file.readline()
		instructions = line.split(",")
		
	i = 0
	while i < len(instructions):
		instr = instructions[i]
		opcode = instr[-2:] if len(instr) >= 2 else '0' + instr
		mode_1 = instr[-3] if len(instr) >= 3 else '0'
		mode_2 = instr[-4] if len(instr) >= 4 else '0'
		next_instr = True
		assert opcode in opcodes

		if opcode in {'01','02'}:
			if mode_1 == '0':
				x1 = int(instructions[int(instructions[i+1])])
			else:
				x1 = int(instructions[i+1])

			if mode_2 == '0':
				x2 = int(instructions[int(instructions[i+2])])
			else:
				x2 = int(instructions[i+2])

			if opcode == '01':
				instructions[int(instructions[i+3])] = str(x1 + x2)
			else:
				instructions[int(instructions[i+3])] = str(x1 * x2)

		if opcode == '03':
			x = input("Enter a new input: ")
			pos = int(instructions[i+1])
			instructions[pos] = str(x)

		if opcode == '04':
			if mode_1 == '0':
				output = instructions[int(instructions[i+1])]
			else:
				output = instructions[i+1]
			print("Output:",output)

		if opcode in {'05','06'}:
			if mode_1 == '0':
				verify = int(instructions[int(instructions[i+1])])
			else:
				verify = int(instructions[i+1])

			if mode_2 == '0':
				jump_to = int(instructions[int(instructions[i+2])])
			else:
				jump_to = int(instructions[i+2])

			if (opcode == '05' and verify != 0) or (opcode == '06' and verify == 0):
				i = int(jump_to)
				next_instr = False

		if opcode in {'07','08'}:
			if mode_1 == '0':
				x1 = int(instructions[int(instructions[i+1])])
			else:
				x1 = int(instructions[i+1])

			if mode_2 == '0':
				x2 = int(instructions[int(instructions[i+2])])
			else:
				x2 = int(instructions[i+2])

			if (opcode == '07' and x1 < x2) or (opcode == '08' and x1 == x2):
				instructions[int(instructions[i+3])] = '1'
			else:
				instructions[int(instructions[i+3])] = '0'

		if opcode == '99':
			print("Halt")
			break

		if next_instr:
			i += 1 + opcodes[opcode]

day5_2()