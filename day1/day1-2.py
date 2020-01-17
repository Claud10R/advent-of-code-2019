import math
import os
fileDir = os.path.dirname(os.path.abspath(__file__))


def calc_fuel(x):
	new_peso = math.floor(x/3) - 2

	if new_peso <= 0:
		return 0

	return new_peso + calc_fuel(new_peso)


def day1_2():
	cnt = 0
	with open(fileDir + '/input.txt') as file:
		for line in file:
			val = int(line)
			cnt += calc_fuel(val)
	
	return cnt


print(day1_2())