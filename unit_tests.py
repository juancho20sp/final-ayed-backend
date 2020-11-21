import unittest
import sys
sys.path.append(".")
from graph import Graph

class TestStringMethods(unittest.TestCase):
    def test_find_love(self):
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


if __name__ == '__main__':
    unittest.main()