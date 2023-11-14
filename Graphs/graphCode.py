import sys

class Graph:

    class Vertex:
        def __init__(self, vertex_id):
            self.id = vertex_id
            self.adjacent_vertices = {}

        def is_neighbour(self, vertex):
            return vertex in self.adjacent_vertices

        def add_neighbour(self, vertex_id, weight=0):
            if not self.is_neighbour(vertex_id):
                self.adjacent_vertices[vertex_id] = weight

        def list_neighbours(self):
            return list(self.adjacent_vertices.keys())

        def edge_cost(self, vertex_id):
            return self.adjacent_vertices.get(vertex_id, sys.maxsize)

    def __init__(self):
        self.vertex_count = 0
        self.adjacency_list = {}

    def get_vertex_count(self):
        return self.vertex_count

    def add_vertex(self, vertex_id):
        if vertex_id not in self.adjacency_list:
            self.vertex_count += 1
            new_vertex = self.Vertex(vertex_id)
            self.adjacency_list[vertex_id] = new_vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.adjacency_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.add_vertex(to_vertex)

        self.adjacency_list[from_vertex].add_neighbour(to_vertex, weight)
        self.adjacency_list[to_vertex].add_neighbour(from_vertex, weight)

    def get_edge_cost(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list:
            return self.adjacency_list[from_vertex].edge_cost(to_vertex)

    def get_vertex_list(self):
        if self.vertex_count != 0:
            return list(self.adjacency_list.keys())

    def get_neighbour_list(self, vertex_id):
        return self.adjacency_list[vertex_id].list_neighbours()

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.get_vertex_list():
            return None
        for node in self.get_neighbour_list(start):
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.get_vertex_list():
            return None
        paths = []
        for node in self.get_neighbour_list(start):
            if node not in path:
                new_path = self.find_all_paths(node, end, path)
                for new_way in new_path:
                    paths.append(new_way)
        
        return paths

    def display_paths(self, paths):
        indices = [i for i in range(len(paths)) if paths[i] == paths[0]]        
        routes = []
        for idx in range(len(indices) - 1):
            routes.append(paths[indices[idx]:indices[idx + 1]])
        
        routes.append(paths[indices[-1]:])
        return routes


def test_empty_graph():
    g1 = Graph()
    assert g1.get_vertex_count() == 0

def test_graph():
    g1 = Graph()
    g1.add_vertex('A')
    g1.add_vertex('C')
    g1.add_vertex('B')    
    g1.add_vertex('D')
    g1.add_vertex('E')
    
    g1.add_edge('A', 'C', 20)    
    g1.add_edge('A', 'B', 10)
    g1.add_edge('A', 'D', 20)    
    g1.add_edge('C', 'B', 20)
    g1.add_edge('C', 'E', 20)

    paths = g1.find_all_paths('E', 'D')
    print(g1.display_paths(paths))

test_empty_graph()
test_graph()
