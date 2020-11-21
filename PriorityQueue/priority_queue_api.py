from flask_restful import Resource, reqparse, abort
import sys
sys.path.append(".")
from PriorityQueue.priority_queue import PriorityQueue

# Configuramos los parámetros necesarios para crear una cola de prioridad
p_queue_args = reqparse.RequestParser()
p_queue_args.add_argument("names", type=str, help="The name of the person is required", required=True)
p_queue_args.add_argument("popularity", type=str, help="The popularity of the person is required", required=True)
p_queue_args.add_argument("times_spoken", type=str, help="The number of times this person have spoken with the goal is "
                                                         "required", required=True)

temp_priority_queue = []

class PriorityQueueApi(Resource):
    def __init__(self):
        # Instancia de la clase 'PriorityQueue'
        self._pq = None

        # Lista con las parejas
        self._data = []

    # Setters y getters
    @property
    def pq(self):
        '''
            Getter de la variable 'pq'
            :return: Variable 'pq'
        '''
        return self._pq

    @pq.setter
    def pq(self, pq):
        '''
        Setter de la variable 'pq'
        :param pq: Instancia de la clase "PriorityQueue"
        :return: None
        '''
        self._pq = pq

    @property
    def data(self):
        '''
            Getter de la variable 'data'
            :return: Variable 'data'
        '''
        return self._data

    @data.setter
    def data(self, data):
        '''
        Setter de la variable 'data'
        :param pq: Instancia de la clase "PriorityQueue"
        :return: None
        '''
        self._data = data

    def put(self):
        '''
        Función encargada de recibir los datos del Frontend.
        :return:
        '''
        # Verificamos que cumpla con los datos que necesitamos
        args = p_queue_args.parse_args()

        # Limpiamos los datos
        self.clean_data(args)

        # Creamos la lista de prioridad
        self.data = self.create_priority_queue(self.data)

        # Le damos formato al JSON de respuesta
        self.data = {
            "name": self.data[0][0],
            "score": self.data[0][1]
        }

        # Devolvemos la lista adecuada y el estado de éxito
        return self.data, 201

    def clean_data(self, args):
        '''
        Función encargada de tomar el JSON con los datos recibidos a través de la petición PUT
        al endpoint '/priority_queue' y devolver una lista de tuplas de la forma: (nombre, factor_de_importancia)
        :param args: Diccionario que contiene el JSON con los nombres, índices de popularidad y número de contactos con la
        persona objetivo en la última semana.
        :return: Lista de tuplas.
        '''

        # Tratamos los datos para poder agruparlos
        names = args['names'].split(",")

        popularity = list(map(int, args['popularity'].split(',')))

        times_spoken = list(map(int, args["times_spoken"].split(',')))

        # Verificamos que las listas tengan el mismo tamaño
        self.are_equal_length(names, popularity, times_spoken)

        # Creamos la lista de tuplas y calculamos el factor de importancia
        # Factor de importancia =(índice de importancia x número de contactos en la última semana)
        temp = []

        for i in range(len(names)):
            temp_list = [None, None]
            temp_list[0] = names[i]
            temp_list[1] = popularity[i]*times_spoken[i]

            temp.append(temp_list)

        # Guardamos la lista en la variable respectiva
        self.data = temp

    def are_equal_length(self, names, popularity, times_spoken):
        '''
        Esta función aborta del proceso en caso de no tener la misma cantidad de datos en las tres
        listas ingresadas como parámetro.
        :param names: Lista de nomrbes.
        :param popularity: Lista de índices de popularidad.
        :param times_spoken: Lista de contactos en la última semana.
        :return: None
        '''

        if len(names) != len(popularity) or len(names) != len(times_spoken) or len(popularity) != len(times_spoken):
            abort(411, message="Las listas no tienen el mismo tamaño, verifique los datos ingresados")

    def create_priority_queue(self, data):
        '''
        Esa función crea la cola de prioridad y devuelve el top 5 (si los har) de personas importantes,
        en caso de tener menos de 5 datos, devuelve los datos ingresados en orden decreciente.
        :param data: Lista donde cada elemento es una tupla de la forma (nombre, importancia).
        :return: Una lista organizada de acuerdo al factor de importancia (de mayor a menor).
        '''

        self.pq = PriorityQueue(data, 1)

        return self.pq.get_top()
