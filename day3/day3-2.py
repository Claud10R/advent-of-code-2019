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

def countStepsToVertex(wire, limit):
	#Given wire's representation as a vector of its vertices' coordinates
	#This function computes the numbers of steps required to reach the latest vertex
	#before the intersection (sum of all the movements)
	steps = 0

	for i in range(limit):
		prevV = wire[i]
		nextV = wire[i+1]

		if prevV[0] == nextV[0]:
			movement = 1
		else:
			movement = 0

		steps += abs(prevV[movement] - nextV[movement])

	return steps

def countSteps(intersection, w1, w2):
	#Given the intersection, represented as (x,y,[i,j]), where i and j are
	#the indices at which the intersection happens during w1 and w2's movements
	#This function computes the total cost (number of steps) required to reach
	#the intersection
	i,j = intersection[2]

	total = countStepsToVertex(w1,i) + countStepsToVertex(w2,j)
	
	c1 = abs(w1[i][0] - intersection[0]) + abs(w1[i][1] - intersection[1])
	c2 = abs(w2[j][0] - intersection[0]) + abs(w2[j][1] - intersection[1]) 

	return c1 + c2 + total

def findMinSteps(ints, w1, w2):
	first = ints[0]
	minSteps = countSteps(first,w1,w2)

	for intersection in ints[1:]:
		minSteps = min(minSteps,countSteps(intersection,w1,w2))

	return minSteps

def day3_2():
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
					pos_int = [r1[1],r2[1],[j,i]]
					if (r2[2] <= pos_int[0] <= r2[3]) and (r1[2] <= pos_int[1] <= r1[3]):
						ints.append(pos_int)
				else:
					#Case R2:x, R1:y
					pos_int = [r2[1],r1[1],[j,i]]
					if (r1[2] <= pos_int[0] <= r1[3]) and (r2[2] <= pos_int[1] <= r2[3]):
						ints.append(pos_int)

	return findMinSteps(ints,w1,w2)

print(day3_2())