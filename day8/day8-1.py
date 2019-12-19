import os
fileDir = os.path.dirname(os.path.abspath(__file__))

def count_digit(layer,digit):
	occurrences = len([x for x in layer if x == digit])
	return occurrences

def day8_1(width, height):
	with open(fileDir + "/input.txt") as file:
		line = file.readline().strip()
		chars = [int(char) for char in line]

	dim_layer = width * height
	min_zeros = float('inf')
	min_layer = []
	i = 0
	while i < len(chars):
		curr_layer = chars[i : i + dim_layer]
		curr_zeros = count_digit(curr_layer, 0)

		if curr_zeros < min_zeros:
			min_layer = curr_layer
			min_zeros = curr_zeros

		i += dim_layer

	n_ones = count_digit(min_layer,1)
	n_twos = count_digit(min_layer,2)
	return n_ones * n_twos

print(day8_1(25,6))