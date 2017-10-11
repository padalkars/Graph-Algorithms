from collections import defaultdict

class graph:
	
	def __init__(self, vertex):
		self.graph = defaultdict(list)
		self.V = vertex + 1
		self.vertices = []

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.vertices.append(u)
		self.vertices.append(v)
		
	def topSort(self,u):
		
		visited = [False] * (self.V)
		stack = []
		for ver in self.vertices:
			if(visited[ver]==True):
				continue
			
			self.topSortUtil(ver,visited,stack)
		return stack

	def topSortUtil(self,u,visited,stack):
			
		visited[u] = True
		for ver in self.graph[u]:
			if(visited[ver]==True):
				continue
			self.topSortUtil(ver,visited,stack)
		stack.append(u)				
	
g = graph(7)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(2,5)
g.addEdge(4,6)
g.addEdge(5,6)
g.addEdge(6,7)
s = g.topSort(1)
l = len(s)

for i in range(l):
	print(s[l-i-1])

	
