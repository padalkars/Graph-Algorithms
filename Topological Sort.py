from collections import defaultdict

class Graph():

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.stack = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topSortUtil(self, u):
        f = 0  
        self.visited.add(u)
        for ver in self.graph[u]:
            if ver not in self.visited:
                self.topSortUtil(ver)
        
        for ver in self.graph[u]:
              
            if ver in self.visited:
                continue
            else:
                f = 1
                break
        if(f==0):
            self.stack.append(u)
            
g = Graph()
g.addEdge('A','B')
g.addEdge('A','D')
g.addEdge('A','C')
g.addEdge('C','D')
#g.addEdge('D','E')

g.topSortUtil('A')
g.stack.reverse()
for ele in g.stack:
    print(ele)

g2 = Graph()
g2.addEdge('A','B')
g2.addEdge('A','D')
g2.addEdge('A','C')
g2.addEdge('C','D')
g2.addEdge('e','g')
g2.addEdge('e','f')
g2.addEdge('e','q')

g2.topSortUtil('A')
g2.stack.reverse()
for ele in g.stack:
    print(ele)        
           
            
                
