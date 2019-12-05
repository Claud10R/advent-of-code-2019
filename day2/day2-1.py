import os
fileDir = os.path.dirname(os.path.abspath(__file__))

def day2_1():
	vector = []

	with open(fileDir + '/input.txt') as file:
		line = file.readline()
		splitted = line.split(",")
		for val in splitted:
			vector.append(int(val))

	vector[1] = 12
	vector[2] = 2

	for i in range(0, len(vector)-4, 4):
		opcode = vector[i]
		assert opcode in {1,2,99}
		
		if opcode == 99:
			break		
		
		pos1 = vector[i+1]
		v1 = vector[pos1]

		pos2 = vector[i+2]
		v2 = vector[pos2]
		
		output = vector[i+3]

		if opcode == 1:
			vector[output] = v1+v2

		if opcode == 2:
			vector[output] = v1*v2

	return vector[0]

print(day2_1())