import math
from graph import Graph
from digraph import DiGraph

class WeightedGraph(Graph):
    def __init__(self):
        super().__init__()
        self.weights = {}

    def add_edge(self, u, v, weight):
        self.edges[u].append(v)
        self.nodes.update([u, v])
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight

    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        del self.weights[(u, v)]
        del self.weights[(v, u)]

    def floyd_warshall(self):
        distance = {u: {v: math.inf for v in self.nodes} for u in self.nodes}
        for u in self.nodes:
            distance[u][u] = 0
        for u, v in self.weights:
            distance[u][v] = self.weights[(u, v)]
        for k in self.nodes:
            for i in self.nodes:
                for j in self.nodes:
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        return distance

class WeightedDiGraph(DiGraph):
    def __init__(self):
        super().__init__()
        self.weights = {}

    def add_edge(self, u, v, weight):
        self.edges[u].append(v)
        self.nodes.update([u, v])
        self.weights[(u, v)] = weight

    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        del self.weights[(u, v)]

    def floyd_warshall(self):
        distance = {u: {v: math.inf for v in self.nodes} for u in self.nodes}
        for u in self.nodes:
            distance[u][u] = 0
        for u, v in self.weights:
            distance[u][v] = self.weights[(u, v)]
        for k in self.nodes:
            for i in self.nodes:
                for j in self.nodes:
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        return distance
        for u in self.nodes:
            distance[u][u] = 0
        for u, v in self.weights:
            distance[u][v] = self.weights[(u, v)]
        for k in self.nodes:
            for i in self.nodes:
                for j in self.nodes:
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        return distance

if __name__ == '__main__':
    # Example usage
    print("OUTPUT-1")
    print("For undirected graph")
    graph1 = WeightedGraph()
    graph1.add_edge('A', 'B', 5)
    graph1.add_edge('B', 'C', 2)
    graph1.add_edge('C', 'D', 3)
    graph1.add_edge('C', 'E', 4)
    graph1.add_edge('E', 'B', 2)
    print(graph1.floyd_warshall())
    print("\n")
    print("For directed graph")
    graph2 = WeightedDiGraph()
    graph2.add_edge('A', 'B', 3)
    graph2.add_edge('B', 'C', 4)
    graph2.add_edge('C', 'D', 2)
    graph2.add_edge('C', 'E', 4)
    graph2.add_edge('E', 'B', 1)
    print(graph2.floyd_warshall())
    print("\n")
    print("OUTPUT-2")
    print("For undirected graph")
    graph3 = WeightedGraph()
    graph3.add_edge('A', 'C', 3)
    graph3.add_edge('D', 'B', 5)
    graph3.add_edge('E', 'A', 2)
    graph3.add_edge('D', 'C', 3)
    print(graph3.floyd_warshall())
    print("\n")
    print("For directed graph")
    graph4 = WeightedDiGraph()
    graph4.add_edge('A', 'C', 4)
    graph4.add_edge('D', 'B', 5)
    graph4.add_edge('E', 'A', 1)
    graph4.add_edge('D', 'C', 3)
    print(graph4.floyd_warshall())
