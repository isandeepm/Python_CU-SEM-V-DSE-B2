import collections
class Graph:
    def __init__(self):
        self.edges = collections.defaultdict(list)
        self.nodes = set()

    def read_edge_list(self, edge_list_file):
        with open(edge_list_file, 'r') as f:
            for line in f:
                u, v = map(int, line.strip().split())
                self.add_edge(u, v)

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)
        self.nodes.update([u, v])

    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        self.edges[v].remove(u)

    def add_node(self, u):
        self.nodes.add(u)

    def remove_node(self, u):
        self.nodes.remove(u)
        for v in self.edges[u]:
            self.edges[v].remove(u)
        del self.edges[u]

    def print_nodes(self):
        print(self.nodes)

    def print_edges(self):
        print(self.edges)

    def degree_distribution(self):
        degrees = [len(v) for v in self.edges.values()]
        return collections.Counter(degrees)

    def clustering_coefficient(self):
        total_coefficient = 0
        for u in self.nodes:
            neighbors = set(self.edges[u])
            num_neighbors = len(neighbors)
            if num_neighbors < 2:
                continue
            num_edges = 0
            for v in neighbors:
                num_edges += u in self.edges[v]
            total_coefficient += num_edges / (num_neighbors * (num_neighbors - 1))
        return total_coefficient / len(self.nodes)

    def connected_components(self):
        visited = set()
        components = []
        for u in self.nodes:
            if u not in visited:
                component = self._dfs(u, visited)
                components.append(component)
        return components

    def _dfs(self, u, visited):
        component = []
        stack = [u]
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                component.append(v)
                stack.extend(self.edges[v])
        return component

    def shortest_path(self, u, v):
        if u not in self.nodes or v not in self.nodes:
            return None
        queue = [(u, [u])]
        while queue:
            node, path = queue.pop(0)
            if node == v:
                return path
            for neighbor in self.edges[node]:
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))
        return None


if __name__ == '__main__':
    obj1 = Graph()
    print("OUTPUT-1")
    obj1.read_edge_list('edge_list_file1.txt')
    print("Nodes")
    obj1.print_nodes()
    print("Edges")
    obj1.print_edges()
    print("Degree Distribution: ", obj1.degree_distribution())
    print("Clustering Coefficient: ", obj1.clustering_coefficient())
    print("Connected components: ", obj1.connected_components())
    print("Shortest path: ", obj1.shortest_path(2, 4))
    obj1.add_edge(2, 4)
    obj1.remove_edge(1, 3)
    print("New Nodes")
    obj1.print_nodes()
    print("New Edges")
    obj1.print_edges()
    print("Shortest path: ", obj1.shortest_path(3, 1))
    obj2 = Graph()
    print("OUTPUT-2")
    obj2.read_edge_list('edge_list_file2.txt')
    print("Nodes")
    obj2.print_nodes()
    print("Edges")
    obj2.print_edges()
    print("Degree Distribution: ", obj2.degree_distribution())
    obj1 = Graph()
    print("OUTPUT-1")
    obj1.read_edge_list('edge_list_file1.txt')
    print("Nodes")
    obj1.print_nodes()
    print("Edges")
    obj1.print_edges()
    print("Degree Distribution: ", obj1.degree_distribution())
    print("Clustering Coefficient: ", obj1.clustering_coefficient())
    print("Connected components: ", obj1.connected_components())
    print("Shortest path: ", obj1.shortest_path(2, 4))
    obj1.add_edge(2, 4)
    obj1.remove_edge(1, 3)
    print("New Nodes")
    obj1.print_nodes()
    print("New Edges")
    obj1.print_edges()
    print("Shortest path: ", obj1.shortest_path(3, 1))
    obj2 = Graph()
    print("OUTPUT-2")
    obj2.read_edge_list('edge_list_file2.txt')
    print("Nodes")
    obj2.print_nodes()
    print("Edges")
    obj2.print_edges()
    print("Degree Distribution: ", obj2.degree_distribution())
    print("Clustering Coefficient: ", obj2.clustering_coefficient())
    print("Connected components: ", obj2.connected_components())
    print("Shortest path: ", obj2.shortest_path(3, 5))
    obj2.add_edge(4, 5)
    obj2.remove_edge(3, 4)
    print("New Nodes")
    obj2.print_nodes()
    print("New Edges")
    obj2.print_edges()
    print("Shortest path: ", obj2.shortest_path(4, 1))