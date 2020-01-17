import math
import os
fileDir = os.path.dirname(os.path.abspath(__file__))


def day1_1():
	cnt = 0
	with open(fileDir + '/input.txt') as file:
		for line in file:
			val = int(line)
			cnt += math.floor(val/3) - 2
	
	return cnt


print(day1_1())
