import math

# Colores que puede tomar cada grafo
WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'


class Graph:
    def __init__(self, v):
        self.v = v
        self.goal = v

        # Definimos los atributos de los vértices
        self.vertices = {}

        # Inicializamos cada vertice
        self.reset_vertex(v)

        self.matrix = [[0 for i in range(v)] for j in range(v)]
        self.visited = [False] * self.v

    def reset_vertex(self, v):
        # Inicializamos cada vértice
        for i in range(v):
            self.vertices[i] = self.initialize_vertex(i)

    def initialize_vertex(self, value):
        return {
            'value': value,
            'color': WHITE,
            'distance': math.inf,
            'phi': None
        }

    def get_neighbours(self, index):
        neighbours = []
        for i in range(self.v):
            if self.matrix[i][index] == 1:
                neighbours.append(i)

        return neighbours

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def print_all_vertex(self):
        for key in self.vertices.keys():
            print(self.vertices[key])

    def add_edge(self, start, end):
        # Suponiendo un grafo NO dirigido
        self.matrix[start][end] = 1
        self.matrix[end][start] = 1

    def DFS(self, start):
        for v in self.vertices.keys():
            self.vertices[v]['color'] = WHITE
            self.vertices[v]['phi'] = None

        time = 0

        for v in self.vertices.keys():
            if self.vertices[v]['color'] == WHITE:
                self.DFS_VISIT(v, time)

        return self.vertices

    def DFS_VISIT(self, u, time):
        time = time + 1
        self.vertices[u]['distance'] = time
        self.vertices[u]['color'] = GRAY

        for n in self.get_neighbours(u):
            if self.vertices[n]['color'] == WHITE:
                self.vertices[n]['phi'] = u
                time = self.DFS_VISIT(n, time)

        self.vertices[u]['color'] = BLACK
        time = time + 1
        self.vertices[u]['final_time'] = time
        return time

    def BFS(self, start):
        for v_index in self.vertices.keys():
            if v_index == start:
                self.vertices[v_index]['color'] = GRAY
                self.vertices[v_index]['distance'] = 0

        # Definimos la cola que tendrá los nodos pendientes por evaluar
        queue = [start]


        # Mientras hayan elementos en la cola, buscamos por anchura en cada uno de ellos
        while queue:
            # Tomamos el nodo actual
            actual = queue[0]

            # Tomamos las propiedades del nodo actual
            actual_obj = self.vertices[actual]

            # Sacamos al nodo actual de la cola
            del queue[0]

            for n in self.get_neighbours(actual):
                n_obj = self.vertices[n]

                # Si el nodo no ha sido visitado -> Color blanco
                if n_obj['color'] == WHITE:
                    self.vertices[n]['color'] = GRAY
                    self.vertices[n]['distance'] = actual_obj['distance'] + 1
                    self.vertices[n]['phi'] = actual

                    # Agregamos el vecino a la cola
                    queue.append(n)

            self.vertices[actual]['color'] = BLACK

        return self.vertices

    def get_route(self, start, goal, steps = []):
        if self.vertices[goal]['value'] == start:
            return steps

        steps.append(self.vertices[goal]['value'])

        return self.get_route(start, self.vertices[goal]['phi'], steps)


    def find_love(self, start, goal):
        self.BFS(start)

        res = self.get_route(start, goal)
        res.reverse()

        for idx in range(len(res)):
            if res[idx] == goal and idx + 1 != len(res):
                res = res[:idx + 1]
                break


        res = list(map(str, res))
        return len(res), res
