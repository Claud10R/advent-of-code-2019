import os
fileDir = os.path.dirname(os.path.abspath(__file__))

class Tree:
	def __init__(self, label, depth = 0):
		self.label = label
		self.depth = depth
		self.children = []

	def __str__(self):
		return self.label

	def __repr__(self):
		return self.label

	def addChild(self, node):
		self.children.append(node)
		curr_lvl = [node]
		sub_lvl = []
		new_depth = 1

		while True:
			if len(curr_lvl) == 0:
				if len(sub_lvl) == 0:
					return

				new_depth += 1
				curr_lvl = sub_lvl.copy()
				sub_lvl = []

			curr_node = curr_lvl[0]
			curr_lvl = curr_lvl[1:]
			curr_node.depth = self.depth + new_depth

			for child in curr_node.children:
				sub_lvl.append(child)


	def print(self):
		print("{0}, children: {1}".format(self.label, self.children))

	def visit(self):
		to_visit = [self]

		for node in to_visit:
			node.print()
			for child in node.children:
				to_visit.append(child)

	def getDescendant(self, label):
		to_visit = [self]

		for node in to_visit:
			if node.label == label:
				return node
			for child in node.children:
				to_visit.append(child)

	def getRoot(self):
		return self.label

	def countOrbits(self):
		to_visit = [self]
		counter = 0

		for node in to_visit:
			counter += node.depth
			for child in node.children:
				to_visit.append(child)

		print("Total orbits:",counter)

def day6_1():
	trees = []

	with open(fileDir + "/input.txt") as file:
		for line in file:
			center = line.strip()[:3]
			orbitand = line.strip()[-3:]

			low_tree = Tree(orbitand)
			for tree in trees:
				if orbitand == tree.getRoot():
					low_tree = tree
					trees.remove(tree)
					break

			flag = True
			for tree in trees:
				node = tree.getDescendant(center)
				if node is not None:
					node.addChild(low_tree)
					flag = False
					break

			if flag:
				up_tree = Tree(center)
				up_tree.addChild(low_tree)
				trees.append(up_tree)

	assert len(trees) == 1
	trees[0].visit()
	trees[0].countOrbits()

day6_1()