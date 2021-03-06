def checkNumber(x):
	currVal = ''
	cnt = 0
	for i in range(len(x)):
		if x[i] == currVal:
			cnt += 1
		else:
			currVal = x[i]
			if cnt == 2:
				return True
			else:
				cnt = 1

	if cnt == 2:
		return True
	return False


def day4_1():
	minN = 138307
	maxN = 654504
	count = 0

	for i in range(1,7):
		for j in range(i,10):
			for k in range(j,10):
				for l in range(k,10):
					for m in range(l,10):
						for n in range(m,10):
							x = "{0}{1}{2}{3}{4}{5}".format(i,j,k,l,m,n)

							if minN <= int(x) <= maxN and checkNumber(x):
								count -= -1

	return count

print(day4_1())