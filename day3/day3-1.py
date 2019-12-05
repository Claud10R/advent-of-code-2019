import os
fileDir = os.path.dirname(os.path.abspath(__file__))

def readWire(line):
	#Wires are represented as vectors of their vertices' coordinates

	vec = [[0,0]]
	x,y = 0,0

	splitted = line.split(",")
	for instr in splitted:
		assert instr[0] in {'R','L','U','D'}
		mov = int(instr[1:])

		if instr[0] == 'R':
			x += mov

		if instr[0] == 'L':
			x -= mov

		if instr[0] == 'U':
			y += mov

		if instr[0] == 'D':
			y -= mov

		vec.append([x,y])

	return vec

def getSegment(p1,p2):
	#A wire moving from its vertex P1 to its vertex P2 draws a segment
	#Since the wire can only go N,S,E or W, only one coordinate changes for every movement
	#Then, a segment can be represented as the equation of the straight line
	#passing through the two points AND lower and upper bounds on the "free" coordinate
	#E.G.: P1 = (4,5), P2 = (12,5)
	#Straight line equation: y = 5
	#Limitations on the other coordinate: 4 <= x <= 12
	#Representation: ['y', 5, 4, 12]

	assert p1[0] == p2[0] or p1[1] == p2[1]

	if p1[0] == p2[0]:
		return ['x', p1[0], min(p1[1],p2[1]), max(p1[1],p2[1])]
	else:
		return ['y', p1[1], min(p1[0],p2[0]), max(p1[0],p2[0])]

def findClosestDistance(ints):
	#Given the list of all the intersections between the two wires
	#Using Manhattan Distance to compute the distance between a point and the origin (0,0)
	#Is the same as summing the absolute values of the two coordinates of the intersection

	first = ints[0]
	minDistance = abs(first[0]) + abs(first[1])
	
	for x in ints[1:]:
		minDistance = min(minDistance,abs(x[0])+abs(x[1]))

	return minDistance


def day3_1():
	ints = w1 = w2 = []

	with open(fileDir + '/input.txt') as file:
		line = file.readline()
		w1 = readWire(line)

		line = file.readline()
		w2 = readWire(line)

	for i in range(len(w2)-1):
		p1 = w2[i]
		p2 = w2[i+1]
		r1 = getSegment(p1,p2)

		for j in range(len(w1)-1):
			q1 = w1[j]
			q2 = w1[j+1]
			r2 = getSegment(q1,q2)

			if r1[0] != r2[0] and not (r1[1] == r2[1] == 0):
				
				if r1[0] == 'x':
					#Case R1:x, R2:y
					pos_int = [r1[1],r2[1]]
					if (r2[2] <= pos_int[0] <= r2[3]) and (r1[2] <= pos_int[1] <= r1[3]):
						ints.append(pos_int)
				else:
					#Case R2:x, R1:y
					pos_int = [r2[1],r1[1]]
					if (r1[2] <= pos_int[0] <= r1[3]) and (r2[2] <= pos_int[1] <= r2[3]):
						ints.append(pos_int)

	return findClosestDistance(ints)

print(day3_1())