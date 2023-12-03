import collections
from graph import Graph

class DiGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.nodes.update([u, v])

    def remove_edge(self, u, v):
        self.edges[u].remove(v)

    def predecessors(self, u):
        return [v for v in self.nodes if u in self.edges[v]]

    def successors(self, u):
        return self.edges[u]

    def reverse(self):
        reversed_graph = DiGraph()
        for u in self.nodes:
            for v in self.edges[u]:
                reversed_graph.add_edge(v, u)
        return reversed_graph

    def strongly_connected_components(self):
        stack = [u for u in self.nodes]
        low = {}
        idx = {}
        idx_counter = [0]
        result = []

        def tarjan(u):
            low[u] = idx[u] = idx_counter[0]
            idx_counter[0] += 1
            stack.append(u)
            for v in self.edges[u]:
                if v not in idx:
                    tarjan(v)
                    low[u] = min(low[u], low[v])
                elif v in stack:
                    low[u] = min(low[u], idx[v])
            if low[u] == idx[u]:
                component = []
                while stack[-1] != u:
                    component.append(stack.pop())
                component.append(stack.pop())
                result.append(component)

        for u in self.nodes:
            if u not in idx:
                tarjan(u)
        return result
        return result

if __name__ == '__main__':
    # Example usage
    graph1 = DiGraph()
    print("OUTPUT-1")
    graph1.add_edge('A', 'B')
    graph1.add_edge('B', 'C')
    graph1.add_edge('C', 'D')
    graph1.add_edge('C', 'E')
    graph1.add_edge('E', 'B')
    print("graph predecessors: ")
    print(graph1.predecessors('B'))
    print("graph successors: ")
    print(graph1.successors('B'))
    reversed_graph = graph1.reverse()
    print("Reversed graph predecessors: ")
    print(reversed_graph.predecessors('B'))
    print("Reversed graph successors: ")
    print(reversed_graph.successors('B'))
    print("Strongly Connected components: ")
    print(graph1.strongly_connected_components())

    graph = DiGraph()
    print("OUTPUT-2")
    graph.add_edge('A', 'C')
    graph.add_edge('D', 'B')
    graph.add_edge('E', 'A')
    graph.add_edge('D', 'C')
    print("graph predecessors: ")
    print(graph.predecessors('A'))
    print("graph successors: ")
    print(graph.successors('A'))
    reversed_graph = graph.reverse()
    print("Reversed graph predecessors: ")
    print(reversed_graph.predecessors('A'))
    print("Reversed graph successors: ")
    print(reversed_graph.successors('A'))
    print("Strongly Connected components: ")
    print(graph.strongly_connected_components())