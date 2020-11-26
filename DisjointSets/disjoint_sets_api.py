from flask_restful import Resource, reqparse, abort
import sys
sys.path.append(".")
from DisjointSets.disjoint_sets import DisjointSets

# Configuramos los parámetros necesarios para revisar regiones conexas
disjoint_args = reqparse.RequestParser()
disjoint_args.add_argument("nodes", type=str, help="The list of nodes is required", required=True)
disjoint_args.add_argument("edges", type=str, help="The list of edges is required", required=True)

class DisjointSetsApi(Resource):
    def __init__(self):
        # Lista de nodos
        self._nodes = []

        # Lista con los arcos
        self._arcs = []

        # Información que se devolverá al frontend
        self._data = None

        # Instancia de la clase 'DisjointSets'
        self._dj = None

    # Setters y getters
    @property
    def nodes(self):
        '''
        Getter para la variable "nodes"
        :return: Variable "nodes"
        '''
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        '''
        Setter para la variable 'nodes'
        :param nodes: Lista de nodos presentes en el grafo.
        :return: None
        '''
        self._nodes = nodes

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

    def get(self):
        '''
        Función que devuelve la lista de arcos del árbol (si la hay) al hacer
        una petición GET al endpoint '/priority_queue'.
        :return: Un JSON con los arcos del grafo.
        '''

        return {"data": "Disjoint Sets API working..."}

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
            "related_regions": self.data,
        }

        return self.data, 201

    def clean_data(self, args):
        '''
            Esta función le da el formato adecuado a los datos recibidos y los guarda en las variables respectivas.
            :param args: JSON con los datos recibidos del frontend.
            :return: None
        '''
        # Guardamos la lista de nodos
        nodes = args['nodes']
        self.nodes = list(map(int, nodes.split(',')))


        # Preparamos los arcos
        arcs = args['edges'].split(',')
        self.arcs = [list(map(int, arc.split('-'))) for arc in arcs]

        # Verificamos que los nodos de los arcos estén dentro de la lista de nodos
        print(self.arcs)
        temp = []
        for el in self.arcs:
            temp.append(el[0])
            temp.append(el[1])

        temp = list(set(temp))
        print(temp)

        print(len(temp) > len(self.nodes))
        print(temp == self.nodes)

        # Creamos los conjuntos disjuntos y buscamos regiones conexas
        self.create_disjoint_sets()


    def create_disjoint_sets(self):
        # Creamos y guardamos la instancia de la clase 'Disjoint Sets'
        self.dj = DisjointSets(self.nodes)

        # Buscamos componentes conexas
        self.data = self.dj.connected_components(self.arcs)
