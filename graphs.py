import queues
import stack
class Graph:
    def __init__(self, numnodes):
        self.numnodes = numnodes
        self. adjlist = [[] for i in range(numnodes)]
        #print(self.adjlist)
    def addedge(self, node1, node2):
        self.adjlist[node1].append(node2)
        self.adjlist[node2].append(node1)
        #print(self.adjlist)
    def bfs(self, source):
        visited = []
        q = queues.Queue(self.numnodes)
        q.enque(source)
        visited.append(source)
        while q.size() != 0:
            next = q.deque()
            for adj in self.adjlist[next]:
                if adj not in visited:
                    q.enque(adj)
                    visited.append(adj)
        print(visited)
    def dfs(self, source):
        visited = []
        s = stack.Stack(self.numnodes)
        s.push(source)
        while not s.isempty():
            next = s.pop()
            visited.append(next)
            print(visited)
            for adj in self.adjlist[next]:
                if adj not in visited:
                    s.push(adj)
            s.display()
        print(visited)

graph = Graph(5)
graph.addedge(0, 1)
graph.addedge(0, 2)
graph.addedge(0, 3)
graph.addedge(2, 3)
graph.addedge(2, 4)
graph.bfs(0)
graph.dfs(0)