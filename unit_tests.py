import unittest
import sys
sys.path.append(".")
from Graph.graph import Graph
from PriorityQueue.priority_queue import PriorityQueue
from DisjointSets.disjoint_sets import DisjointSets
from Djikstra.djikstra import GraphLD

class TestStringMethods(unittest.TestCase):
    def test_find_love(self):
        '''
        Función encargada de probar la función find love.
        :return:
        '''
        # Primer test
        start, goal = 0, 4
        arcs = [(0, 1), (0, 2), (0, 3), (3, 4)]

        g = Graph(goal + 1)
        for arc in arcs:
            g.add_edge(arc[0], arc[1])
        self.assertEqual(g.find_love(start, goal), (2, ['3', '4']))

        # Segundo test
        start, goal = 0, 9
        arcs = [(0, 1), (0, 2), (0, 3), (1, 5), (2, 4), (3, 7), (4, 9), (5, 6), (7, 8), (6, 9), (8, 9)]

        g = Graph(goal + 1)
        for arc in arcs:
            g.add_edge(arc[0], arc[1])
        self.assertEqual(g.find_love(start, goal), (3, ['2', '4', '9']))


        # Tercer test
        start, goal = 0, 4
        arcs = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4)]

        g = Graph(goal + 1)
        for arc in arcs:
            g.add_edge(arc[0], arc[1])
        self.assertEqual(g.find_love(start, goal), (2, ['2', '4']))

    def test_priority_queue(self):
        '''
        Función encargada de probar la cola de prioridad
        :return:
        '''
        # Primer test
        data = [['Melissa', 1350], ['Juan', 2610], ['Ernesto', 50], ['Andres', 24], ['Javier', 2035], ['Vanessa', 1235], ['Mariana', 1750], ['Pedro', 2422], ['Luz', 4371]]
        pq = PriorityQueue(data, 1)
        self.assertEqual(pq.get_top(), [['Luz', 4371], ['Juan', 2610], ['Pedro', 2422], ['Javier', 2035], ['Mariana', 1750]])

        # Segundo test
        data = [['Juan', 150], ['Luis', 104], ['Maria', 11]]
        pq = PriorityQueue(data, 1)
        self.assertEqual(pq.get_top(), [['Juan', 150], ['Luis', 104], ['Maria', 11]])

        # Tercer test
        data = [['Juan', 150]]
        pq = PriorityQueue(data, 1)
        self.assertEqual(pq.get_top(), [['Juan', 150]])

    def test_related_regions(self):
        '''
            Función encargada de probar la cola de prioridad
            :return:
        '''
        # Primer test
        nodes = 9
        arcs = [[0, 1], [0, 2], [1, 2], [4, 5], [4, 6], [5, 6], [7, 8], [7, 9], [8, 9]]

        dj = DisjointSets(nodes)
        self.assertEqual(dj.connected_components(arcs), [{3}, {0, 1, 2}, {4, 5, 6}, {8, 9, 7}])

        # Segundo test
        nodes = 4
        arcs = []

        dj = DisjointSets(nodes)
        self.assertEqual(dj.connected_components(arcs), [{0}, {1}, {2}, {3}, {4}])

        # Tercer test
        nodes = 1
        arcs = []

        dj = DisjointSets(nodes)
        self.assertEqual(dj.connected_components(arcs), [{0}, {1}])

    def test_djikstra_shortest_path(self):
        '''
        Función encargada de probar la funcionalidad de camino mínimo de djikstra
        :return:
        '''

        # Primer test
        vertex = [0, 1, 2, 3, 4]
        arcs = [[0, 1, 16], [0, 2, 2], [0, 3, 1], [1, 4, 1], [2, 4, 0], [3, 4, 3]]

        dj = GraphLD(vertex, arcs)
        dj.dijkstra(0)
        self.assertEqual(dj.find_shortest_path([], 0, 4), ([2, 4], 2))

        # Segundo test
        vertex = [0, 1, 2, 3, 4]
        arcs = [[0, 1, 1], [0, 2, 10], [1, 3, 2], [2, 3, 10], [3, 4, 3]]
        dj = GraphLD(vertex, arcs)
        dj.dijkstra(0)
        self.assertEqual(dj.find_shortest_path([], 0, 4), ([1, 3, 4], 1))

        # Segundo test
        vertex = [0, 1, 2, 3, 4, 5]
        arcs = [[0, 1, 2], [1, 2, 2], [2, 5, 2], [5, 4, 2], [4, 3, 2]]
        dj = GraphLD(vertex, arcs)
        dj.dijkstra(0)
        self.assertEqual(dj.find_shortest_path([], 0, 3), ([1, 2, 5, 4, 3], 2))


if __name__ == '__main__':
    unittest.main()