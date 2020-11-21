from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# Importamos los archivos que necesitamos
import sys
sys.path.append(".")
from graph import Graph


# Creamos la aplicación
app = Flask(__name__)
api = Api(app)

# Configuramos los parámetros del necesarios para crear un grafo
graph_put_args = reqparse.RequestParser()
graph_put_args.add_argument("start", type=int, help="Start node is required", required=True)
graph_put_args.add_argument("goal", type=int, help="Goal node is required", required=True)
graph_put_args.add_argument("edges", type=str, help="Edges are required", required=True)

temp = []
class GraphApi(Resource):
    def __init__(self):
        # Arcos
        self.arcs = []

        # Nodo inicial
        self.start = None

        # Nodo final
        self.goal = None

        # Instancia de la clase 'Graph'
        self.g = None

        # Mensaje de respuesta al usuario
        self.data = None

    def get(self):
        print("Self.arcs: {}".format(self.arcs))
        # Verificamos que los arcos no estén vacíos
        self.are_arcs_empty()

        return {"data": temp or "GraphAPI Working..."}

    def put(self):
        # Verificamos que cumpla con los datos que necesitamos
        args = graph_put_args.parse_args()

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
            temp.append(el)

        # Iniciamos el grafo
        self.start_graph()

        return self.data, 201

    def delete(self):
        temp.clear()
        return {"message": "Arcos borrados satisfactoriamente"}

    def are_arcs_empty(self):
        if len(temp) == 0:
            abort(404, message="No se puede consultar un grafo sin nodos")

    def start_graph(self):
        self.g = Graph(self.goal + 1)

        # Agregamos los arcos al grafo
        for pair in self.arcs:
            self.g.add_edge(pair[0], pair[1])

        # Buscamos la cantidad de personas necesarias para llegar de 'start' a 'goal'
        self.data = self.g.find_love(self.start, self.goal)




api.add_resource(GraphApi, "/graph")