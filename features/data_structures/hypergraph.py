class Hypergraph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.incidence_matrix = np.zeros((len(vertices), len(edges)))

    def add_vertex(self, vertex):
        # adds a vertex to the hypergraph
        pass

    def add_edge(self, edge):
        # adds an edge to the hypergraph
        pass

    def get_incidence_matrix(self):
        # returns the incidence matrix of the hypergraph
        pass
