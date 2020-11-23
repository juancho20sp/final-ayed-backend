import math

#Colors
WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'

VI = 0
VF = 1
W = 2


class GraphLD:
    def __init__(self,vertexes, arcs):
        self.V = {}
        for v in vertexes:
            self.V[v] = self.initialize_vertex()
        self.E = {}

        #Hay un espacio por cada vertice
        for v in self.V:
            self.E[v] = []

        for arc in arcs:
            self.E[arc[VI]].append((arc[VF], arc[W]))

    def initialize_vertex(self):
        return {
            'id': None,
            'color': WHITE,
            'distance': math.inf,
            'final_time': math.inf,
            'phi': None
        }

    def initialize_single_source(self, s):
        for v in self.V.keys():
            self.V[v] = self.initialize_vertex()
        self.V[s]['distance'] = 0

    def relax(self, arc):
        if self.V[arc[VF]]['distance'] > self.V[arc[VI]]['distance'] + arc[W]:
            self.V[arc[VF]]['distance'] = self.V[arc[VI]]['distance'] + arc[W]
            self.V[arc[VF]]['phi'] = arc[VI]

    def extract_min(self, visited):
        min, u = math.inf, None
        for v in self.V.keys():
            if v not in visited and min > self.V[v]['distance']:
                min, u = self.V[v]['distance'], v
        return u

    def dijkstra(self, s):
        self.initialize_single_source(s)
        visited = set()
        processedVertex = [ v for v in self.V.keys() ]
        while len(processedVertex) > 0:
            u = self.extract_min(visited)
            processedVertex.remove(u)
            visited = visited.union(set([u]))
            for arc in self.get_neighbours(u):
                self.relax((u, arc[VI], arc[VF]))

        for index in self.V.keys():
            self.V[index]['id'] = index

        return self.V

    def find_shortest_path(self, lista, distance, goal):
        if self.V[goal]['phi'] is None:
            lista.reverse()
            return lista, distance
        # Añadimos el elemento actual a la lista
        lista.append(goal)

        return self.find_shortest_path(lista, self.V[goal]['distance'], self.V[goal]['phi'])


    def print_current_state(self, result):
        for vertex in result.keys():
            print(vertex, result[vertex])

    def get_vertexes(self):
        return self.V

    def get_arcs(self):
        return self.E

    def get_neighbours(self, v):
        return self.E[v]

    def print_arcs(self):
        for v in self.E.keys():
            print(v, self.E[v])

    def get_arcs_as_triplets(self):
        arcs = []
        for key in self.E.keys():
            for rel in self.E[key] :
                arcs.append((key, rel[VI], rel[VF]))
        return arcs

    def bellman_ford(self, s):
        self.initialize_single_source(s)
        #Relax all arcs |V| - 1 times, assuming a dense graph
        for i in range(len(self.V.keys())-1):
            for arc in self.get_arcs_as_triplets():
                self.relax(arc)
        #Verify negative value cycles
        for arc in self.get_arcs_as_triplets():
            if self.V[arc[VF]]['distance'] > self.V[arc[VI]]['distance'] + arc[W]:
                return None
        return self.V

