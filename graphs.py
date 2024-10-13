class Graph:
    def __init__(self, numnodes):
        self.numnodes = numnodes
        self. adjlist = [[] for i in range(numnodes)]
        print(self.adjlist)
    def addedge(self, node1, node2):
        self.adjlist[node1].append(node2)
        self.adjlist[node2].append(node1)
        print(self.adjlist)

graph = Graph(5)
graph.addedge(0, 1)
graph.addedge(0, 2)
graph.addedge(0, 3)
graph.addedge(3, 4)