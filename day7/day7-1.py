import os, itertools
fileDir = os.path.dirname(os.path.abspath(__file__))
opcodes = {'01': 3, '02': 3, '03': 1, '04': 1, '05': 2, '06': 2, '07': 3, '08': 3, '99': 0}

class Amplifier:
	def __init__(self):
		self.phase_set = False
		self.load_program()

	def load_program(self):
		with open(fileDir + "/input.txt") as file:
			line = file.readline()
			self.program = line.strip().split(",")

	def run(self, phase, other_input):
		output = -1
		i = 0

		while i < len(self.program):
			instr = self.program[i]
			opcode = instr[-2:] if len(instr) >= 2 else '0' + instr
			mode_1 = instr[-3] if len(instr) >= 3 else '0'
			mode_2 = instr[-4] if len(instr) >= 4 else '0'
			next_instr = True

			params = [int(self.program[i + j]) for j in range(1, opcodes[opcode] + 1)]

			if opcode in {'01', '02'}:
				x1 = int(self.program[params[0]]) if mode_1 == '0' else params[0]
				x2 = int(self.program[params[1]]) if mode_2 == '0' else params[1]
				self.program[params[2]] = str(x1 + x2) if opcode == '01' else str(x1 * x2)

			if opcode == '03':
				x = other_input if self.phase_set else phase
				self.phase_set = True
				self.program[params[0]] = str(x)

			if opcode == '04':
				output = int(self.program[params[0]]) if mode_1 == '0' else params[0]

			if opcode in {'05', '06'}:
				verify = int(self.program[params[0]]) if mode_1 == '0' else params[0]
				jump_to = int(self.program[params[1]]) if mode_2 == '0' else params[1]

				if (opcode == '05' and verify != 0) or (opcode == '06' and verify == 0):
					i = jump_to
					next_instr = False

			if opcode in {'07', '08'}:
				x1 = int(self.program[params[0]]) if mode_1 == '0' else params[0]
				x2 = int(self.program[params[1]]) if mode_2 == '0' else params[1]

				if (opcode == '07' and x1 < x2) or (opcode == '08' and x1 == x2):
					self.program[params[2]] = '1'
				else:
					self.program[params[2]] = '0'

			if opcode == '99':
				break

			if next_instr:
				i += 1 + opcodes[opcode]

		return output

def day7_1():
	phases = [0, 1, 2, 3, 4]
	permutations = itertools.permutations(phases)

	max_output = 0
	for sequence in permutations:
		amplifiers = [Amplifier() for i in range(5)]
		other_input = 0

		for i in range(5):
			other_input = amplifiers[i].run(sequence[i], other_input)

		max_output = max(max_output, other_input)

	return max_output

print(day7_1())