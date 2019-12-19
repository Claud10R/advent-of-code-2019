import os
fileDir = os.path.dirname(os.path.abspath(__file__))

class Graph:
	def __init__(self):
		self.vertices = {}

	def __str__(self):
		string = ""

		for label, vertex in self.vertices.items():
			string += label + ", edges: " + str(vertex.adjacents) + "\n"

		return string

	def add_vertex(self, label):
		v = Vertex(label)
		self.vertices[label] = v

	def get_vertex(self, label):
		if label in self.vertices.keys():
			return self.vertices[label]
		else:
			return None

	def add_edge(self,v1,v2,w=1):
		if v1 not in self.vertices:
			self.add_vertex(v1)

		if v2 not in self.vertices:
			self.add_vertex(v2)

		self.vertices[v1].add_neighbour(v2,w)
		self.vertices[v2].add_neighbour(v1,w)

class Vertex:
	def __init__(self, label):
		self.label = label
		self.adjacents = {}

	def add_neighbour(self, dest, weight):
		self.adjacents[dest] = weight

	def get_neighbours(self):
		return self.adjacents

	def get_edge(self, dest):
		if dest in self.adjacents.keys():
			return self.adjacents[dest]
		else:
			return None

def get_closest(unvisited, distances):
	closest = None
	closest_w = float('inf')

	for i in range(len(unvisited)):
		node = unvisited[i]
		if node.label in distances and distances[node.label] < closest_w:
			closest_w = distances[node.label]
			closest = node

	return closest

def dijkstra(graph, source, dest):
	distances = {source: 0}
	unvisited = [v for _label,v in graph.vertices.items()]

	while len(unvisited) > 0:
		closest = get_closest(unvisited, distances)
		unvisited.remove(closest)

		for n in closest.get_neighbours():
			node = graph.vertices[n]
			if node in unvisited:
				new_distance = distances[closest.label] + closest.get_edge(n)
				if n not in distances or distances[n] > new_distance:
					distances[n] = new_distance

	return distances[dest] - 2

def day6_2():
	g = Graph()

	with open(fileDir + "/input.txt") as file:
		for line in file:
			center = line.strip()[:3]
			orbitand = line.strip()[-3:]

			g.add_edge(center, orbitand)

	v1 = "SAN"
	v2 = "YOU"
	print("Distance (orbital changes) between {0} and {1}: {2}".format(v1,v2,dijkstra(g,v1,v2)))

day6_2()