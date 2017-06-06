from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.res = 0
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, u, visited, par):
        print(u)
        visited[u] = True
        for ver in self.graph[u]:
            if(visited[ver]==False):
                return self.DFSUtil(ver,visited,u)
            else:
                if(par!=ver):
                    self.res = 1
                    print("Cycle exists at " + str(ver))
        return res            
        
    def DFS(self,u):
        visited = [False]*len(self.graph)
        for ver in self.graph[u]:
            if(visited[ver]==False):
                return self.DFSUtil(ver,visited,-1)
        return 0

    
g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,1)

if(g.DFS(1)):
    print("Cycle Exists")
