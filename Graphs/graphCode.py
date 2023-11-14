import sys

class Graph:

	# Class to represent individual Vertex
	# Design consists of vertexID and a
	# dictionary to store neighbours info of that vertex
	class _Vertex:
		def __init__(self, vID):
			self.id = vID
			self.adjacentVertex = {}

		def _isNeighbour(self, vertex):
			return vertex in self.adjacentVertex

		def _addNeighbour(self, id, wt = 0):
			if not self._isNeighbour(id):
				self.adjacentVertex[id] = wt

		def _listNeighbours(self):
			return self.adjacentVertex.keys()

		def _edgeCost(self, id):
			if self._isNeighbour(id):
				return self.adjacentVertex[id]
			else:
				return sys.maxsize

	def __init__(self):
		self.vertex_count = 0
		self.adjacency_list = {}

	def getVertexCount(self):
		return self.vertex_count

	def addVertex(self, vid):
		if not vid in self.adjacency_list:
			self.vertex_count += 1
			new_vertex = self._Vertex(vid)
			self.adjacency_list[vid] = new_vertex

	def addEdge(self, frm, to, wt = 0):
		if not frm in self.adjacency_list:
			self.addVertex(frm)
		if not to in self.adjacency_list:
			self.addVertex(to)

		self.adjacency_list[frm]._addNeighbour(to, wt)
		self.adjacency_list[to]._addNeighbour(frm, wt)	# Not for Directed graph

	def getEdgeCost(self, frm, to):
		if frm in self.adjacency_list and to in self.adjacency_list:
			return self.adjacency_list[frm]._edgeCost(to)

	def getVertexList(self):
		if self.vertex_count != 0:
			return (list(self.adjacency_list.keys()))

	def getNeighbourList(self, vid):
		return (list(self.adjacency_list[vid]._listNeighbours()))

	# Returns only first discoverd path
	def findPath(self, start, end, path=[]):
		path = path + [start]
		if start == end:
			return path
		if not start in self.getVertexList():
			return None
		for node in self.getNeighbourList(start):
			if not node in path:
				new_path = self.findPath(node, end, path)
				if new_path:
					return new_path
		return None

	# Returns all existing path (not in a required format)
	# Use displayPaths() to get paths in a proper way
	def findAllPaths(self, start, end, path=[]):
		path = path + [start]
		if start == end:
			return path
		if not start in self.getVertexList():
			return None
		paths = []
		for node in self.getNeighbourList(start):
			if not node in path:
				new_path = self.findAllPaths(node, end, path)
				for new_way in new_path:
					paths.append(new_way)
		
		return paths

	def displayPaths(self, paths):
		indicies = [ i for i in range(len(paths)) if paths[i] == paths[0]]		
		routes = []
		for idx in range(len(indicies)):
			if indicies[idx] != indicies[-1]: # to exclude the last value in list indicies
				routes.append(paths[indicies[idx]:indicies[idx+1]])
	
		routes.append(paths[indicies[-1]:]) # last value from indicies is added outside loop
		
		return routes


def testemptyGraph():
	g1 = Graph()
	assert (g1.getVertexCount() == 0)

def testGraph():
	g1 = Graph()
	g1.addVertex('A')
	g1.addVertex('C')
	g1.addVertex('B')	
	g1.addVertex('D')
	g1.addVertex('E')
	
	g1.addEdge('A', 'C', 20)	
	g1.addEdge('A', 'B', 10)
	g1.addEdge('A', 'D', 20)	
	g1.addEdge('C', 'B', 20)
	g1.addEdge('C', 'E', 20)

	#assert (g1.getVertexCount() == 3)
	#assert (g1.getEdgeCost(1,2) == 10)
	#print(g1.getNeighbourList(2))
	#print(g1.getVertexList())
	paths = g1.findAllPaths('E', 'D')
	print(g1.displayPaths(paths))

testemptyGraph()
testGraph()
