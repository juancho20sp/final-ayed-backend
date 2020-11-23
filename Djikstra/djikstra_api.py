from flask_restful import Resource, reqparse, abort
import sys
sys.path.append(".")

from Djikstra.djikstra import GraphLD

# Configuramos los parámetros necesarios para revisar regiones conexas
djikstra_args = reqparse.RequestParser()
djikstra_args.add_argument("start", type=int, help="The start node is required", required=True)
djikstra_args.add_argument("goal", type=int, help="The goal node is required", required=True)
djikstra_args.add_argument("edges", type=str, help="The list of edges is required", required=True)

class DjikstraApi(Resource):
    def __init__(self):
        # Nodo de inicio
        self._start = None

        # Nodo objetivo
        self._goal = None

        # Cantidad de nodos
        self._nodes = None

        # Lista de arcos
        self._arcs = []

        # Información que se devolverá al frontend
        self._data = None

        # Instancia de la clase 'GraphLD'
        self._dj = None

    # Setters y getters
    @property
    def start(self):
        '''
        Getter para la variable 'start'
        :return: Variable 'start'
        '''
        return self._start

    @start.setter
    def start(self, start):
        '''
        Setter para la variable 'start'
        :param start: Nodo de inicio de la búsqueda al aplicar el algoritmo de Djikstra
        :return: None
        '''
        self._start = start

    @property
    def goal(self):
        '''
        Getter para la variable 'goal'
        :return: Variable 'goal'
        '''
        return self._goal

    @goal.setter
    def goal(self, goal):
        '''
        Setter para la variable 'goal'
        :param start: Nodo de objetivo al aplicar el algoritmo de Djikstra
        :return: None
        '''
        self._goal = goal

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
        :param start: Lista con los arcos
        :return: None
        '''
        self._arcs = arcs

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
        :param dj: Una instancia de la clase GraphLD
        :return: None
        '''
        self._dj = dj

    @property
    def nodes(self):
        '''
        Getter para la variable 'nodes'
        :return: La variable 'nodes'
        '''
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        '''
        Setter para la variable 'nodes'
        :param nodes: Una instancia de la clase GraphLD
        :return: None
        '''
        self._nodes = nodes


    def get(self):
        '''
        Función que verifica el funcionamiento del endpoint al hacer
        una petición GET al endpoint '/djikstra'.
        :return: Un JSON con un mensaje de prueba.
        '''

        return {"data": "Djikstra API working..."}

    def put(self):
        '''
        Función encargada de recibir los datos del Frontend.
        :return: Una tupla de la forma ([ruta...], costo), decribiendo los nodos a seguir para llegar al
        objetivo y el costo de este movimiento (de acuerdo al peso del grafo).
        '''

        # Verificamos que cumpla con los datos que necesitamos
        args = djikstra_args.parse_args()

        # Limpiamos los datos
        self.clean_data(args)

        # Preparamos el JSON para devolverlo al frontend
        self.data = {
            "route": self.data[0],
            "cost": self.data[1]
        }

        return self.data, 201

    def clean_data(self, args):
        '''
        Esta función le da el formato adecuado a los datos recibidos y los guarda en las variables respectivas.
        :param args: JSON con los datos recibidos del frontend.
        :return: None
        '''

        # Guardamos el nodo inicial
        self.start = args['start']

        # Guardamos el nodo objetivo
        self.goal = args['goal']

        # Preparamos los arcos
        arcs = args['edges'].split(',')
        self.arcs = [list(map(int, arc.split('-'))) for arc in arcs]

        # Encontramos los nodos presentes en el grafo
        n = []
        for arc in self.arcs:
            n.append(arc[0])
            n.append(arc[1])

        # Guardamos la cantidad de nodos
        self.nodes = list(set(n))

        # Creamos la instancia de la clase y buscamos el camino más corto
        self.find_shortest_path()

    def find_shortest_path(self):
        '''
        Esta función se encarga de comunicarse con la clase 'GraphLD' y ejecutar el algoritmo de
        Djikstra con los datos obtenidos del frontend.
        :return:
        '''
        # Creamos la instancia de la clase
        self.dj = GraphLD(self.nodes, self.arcs)

        # Ejecutamos el algoritmo de Djikstra iniciando desde 'start'
        self.dj.dijkstra(self.start)

        # Guardamos la respuesta del algoritmo
        self.data = self.dj.find_shortest_path([], 0, self.goal)
