from flask import Flask
from flask_restful import Api

# Importamos los archivos que necesitamos
import sys
sys.path.append(".")
#from graph import Graph
from Graph.graph_api import GraphApi
from PriorityQueue.priority_queue_api import PriorityQueueApi
#from priority_queue import PriorityQueue

# Creamos la aplicación
app = Flask(__name__)
api = Api(app)


# Generamos el endpoint para la funcionalidad de grafos
api.add_resource(GraphApi, "/graph")

# Generamos el endpoint para la funcionalidad de cola de prioridad
api.add_resource(PriorityQueueApi, "/priority_queue")