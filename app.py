from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

import sys
sys.path.append(".")

# Importamos los archivos que necesitamos
from Graph.graph_api import GraphApi
from PriorityQueue.priority_queue_api import PriorityQueueApi

from disjoint_sets import DisjointSets

# Creamos la aplicación
app = Flask(__name__)
api = Api(app)


# Generamos el endpoint para la funcionalidad de grafos
api.add_resource(GraphApi, "/graph")

# Generamos el endpoint para la funcionalidad de cola de prioridad
api.add_resource(PriorityQueueApi, "/priority_queue")


# Configuramos los parámetros necesarios para revisar regiones conexas
disjoint_args = reqparse.RequestParser()
disjoint_args.add_argument("final_node", type=int, help="The number of nodes is required", required=True)
disjoint_args.add_argument("edges", type=str, help="The list of edges is required", required=True)


class DisjointSetsApi(Resource):
    def __init__(self):
        # Cantidad de nodos
        self._final_node = 0

        # Lista con los arcos
        self._arcs = []

        # Información que se devolverá al frontend
        self._data = None

        # Instancia de la clase 'DisjointSets'
        self._dj = None

    # Setters y getters
    @property
    def final_node(self):
        '''
        Getter para la variable "nodes"
        :return: Variable "nodes"
        '''
        return self._final_node

    @final_node.setter
    def final_node(self, nodes):
        '''
        Setter para la variable nodes
        :param nodes: Cantidad de nodos presentes en el grafo
        :return: None
        '''
        self._final_node = nodes

    @property
    def data(self):
        '''
        Getter para la variable 'data'
        :return: Variable 'data'
        '''
        return self._data

    @data.setter
    def data(self, data):
        '''
        Setter para la variable data
        :param data: Información que viajará al frontend
        :return: None
        '''
        self._data = data

    @property
    def arcs(self):
        '''
        Getter para la variable 'arcs'
        :return: Variable 'arcs'
        '''
        return self._arcs

    @arcs.setter
    def arcs(self, arcs):
        '''
        Setter para la variable 'arcs'
        :param arcs: Una lista de listas, de la forma: [[nodo_inicio, nodo_final]]
        :return: None
        '''
        self._arcs = arcs

    @property
    def dj(self):
        '''
        Getter para la variable 'dj'
        :return: La variable 'dj'
        '''
        return self._dj

    @dj.setter
    def dj(self, dj):
        '''
        Setter para la variable 'dj'
        :param dj: Una instancia de la clase DisjointSets
        :return: None
        '''
        self._dj = dj

    def put(self):
        '''
        Función encargada de recibir los datos del Frontend.
        :return: Un JSON con la respuesta obtenida de procesar los datos.
        '''
        # Verificamos que cumpla con los datos que necesitamos
        args = disjoint_args.parse_args()

        # Limpiamos los datos
        self.clean_data(args)

        # Preparamos el JSON para devolverlo al frontend
        self.data = [list(el) for el in self.data]

        self.data = {
            "num_nodes": self.final_node + 1,
            "final_node": self.final_node,
            "related_regions": self.data,
            "num_related_regions": len(self.data)
        }

        return self.data, 201

    def clean_data(self, args):
        # Guardamos el total de nodos
        self.final_node = args['final_node']

        # Preparamos los arcos
        arcs = args['edges'].split(',')
        self.arcs = [list(map(int, arc.split('-'))) for arc in arcs]

        print(self.arcs)

        # Creamos los conjuntos disjuntos y buscamos regiones conexas
        self.create_disjoint_sets()


    def create_disjoint_sets(self):
        # Creamos y guardamos la instancia de la clase 'Disjoint Sets'
        self.dj = DisjointSets(self.final_node)

        # Buscamos componentes conexas
        self.data = self.dj.connected_components(self.arcs)
        print(self.data)






# Generamos el endpoint para la funcionalidad de cola de prioridad
api.add_resource(DisjointSetsApi, "/sets")

