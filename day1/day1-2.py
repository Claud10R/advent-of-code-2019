import math, os
fileDir = os.path.dirname(os.path.abspath(__file__))

def calcFuel(x):
	newPeso = math.floor(x/3) - 2

	if newPeso <= 0:
		return 0

	return newPeso + calcFuel(newPeso)

def day1_2():
	cnt = 0
	with open(fileDir + '/input.txt') as file:
		for line in file:
			val = int(line)
			cnt += calcFuel(val)
	
	return cnt

print(day1_2())