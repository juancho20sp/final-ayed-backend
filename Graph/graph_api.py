from flask_restful import Resource, reqparse, abort
import sys
sys.path.append(".")
from Graph.graph import Graph

# Configuramos los parámetros del necesarios para crear un grafo
graph_put_args = reqparse.RequestParser()
graph_put_args.add_argument("start", type=int, help="Start node is required", required=True)
graph_put_args.add_argument("goal", type=int, help="Goal node is required", required=True)
graph_put_args.add_argument("edges", type=str, help="Edges are required", required=True)

temp_graph = []


class GraphApi(Resource):
    def __init__(self):
        # Arcos
        self._arcs = []

        # Nodo inicial
        self._start = None

        # Nodo final
        self._goal = None

        # Instancia de la clase 'Graph'
        self._g_instance = None

        # Mensaje de respuesta al usuario
        self._data = None


    # Getters y setters
    @property
    def arcs(self):
        '''
        Getter de la variable 'arcs'.
        :return: La variable 'arcs'
        '''
        return self._arcs

    @arcs.setter
    def arcs(self, arcs):
        '''
            Setter de la variable 'arcs'.
            :return: None
        '''
        self._arcs = arcs

    @property
    def start(self):
        '''
            Getter de la variable 'start'.
            :return: La variable 'start'
        '''
        return self._start

    @start.setter
    def start(self, start):
        '''
            Setter de la variable 'start'.
            :return: None
        '''
        self._start = start

    @property
    def goal(self):
        '''
            Getter de la variable 'goal'.
            :return: La variable 'goal'
        '''
        return self._goal

    @goal.setter
    def goal(self, goal):
        '''
            Setter de la variable 'goal'.
            :return: None
        '''
        self._goal = goal

    @property
    def g_instance(self):
        '''
            Getter de la variable 'g_instance'.
            :return: La variable 'g_instance'
        '''
        return self._g_instance

    @g_instance.setter
    def g_instance(self, g_instance):
        '''
            Setter de la variable 'g_instance'.
            :return: None
        '''
        self._g_instance = g_instance

    @property
    def data(self):
        '''
            Getter de la variable 'data'.
            :return: La variable 'data'
        '''
        return self._data

    @data.setter
    def data(self, data):
        '''
            Setter de la variable 'data'.
            :return: None
        '''
        self._data = data

    def get(self):
        '''
        Función que devuelve la lista de arcos del árbol (si la hay) al hacer
        una petición GET al endpoint '/graph'.
        :return: Un JSON con los arcos del grafo.
        '''
        print("Self.arcs: {}".format(self.arcs))
        # Verificamos que los arcos no estén vacíos
        self.are_arcs_empty()

        return {"data": temp_graph}

    def put(self):
        '''
        Función encargada de recibir los datos necesarios para crear un grafo.
        Los recibe en formato JSON cuando se hace una petición PUT al endpoint.
        :return: Una tupla de la forma (num_personas_necesarias, [lista_de_personas_necesarias])
        '''
        # Verificamos que cumpla con los datos que necesitamos
        args = graph_put_args.parse_args()

        # Función encargada de tratar la entrada
        self.clean_data(args)

        # Iniciamos el grafo
        self.start_graph()

        # Le damos formato al JSON de respuesta
        self.data = {
            "distance": self.data[0],
            "nodes": self.data[1]
        }

        return self.data, 201

    def clean_data(self, args):
        # Guardamos el inicio y el objetivo
        self.start = args['start']
        self.goal = args['goal']

        # Separamos los arcos por parejas
        edges = args['edges'].split(',')

        # Separamos cada pareja
        edges = [tuple(map(int, edge.split('-'))) for edge in edges]

        # Guardamos los arcos en su variable respectiva
        self.arcs = edges

        # Modificamos la variable global
        for el in self.arcs:
            temp_graph.append(el)

    def delete(self):
        temp_graph.clear()
        return {"message": "Arcos borrados satisfactoriamente"}

    def are_arcs_empty(self):
        if len(temp_graph) == 0:
            abort(404, message="No se puede consultar un grafo sin nodos")

    def start_graph(self):
        self.g_instance = Graph(self.goal + 1)

        # Agregamos los arcos al grafo
        for pair in self.arcs:
            self.g_instance.add_edge(pair[0], pair[1])

        # Buscamos la cantidad de personas necesarias para llegar de 'start' a 'goal'
        self.data = self.g_instance.find_love(self.start, self.goal)
