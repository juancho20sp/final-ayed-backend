import requests

BASE = "http://127.0.0.1:5000/"
#BASE = "https://obscure-sierra-80708.herokuapp.com/"
#response = requests.get(BASE + "helloworld/juan")

'''
Para grafos

response = requests.put(BASE + "graph", {
    "start": 0,
    "goal": 4,
    "edges": "0-1,0-2,0-3,3-4"
})

print(response.json())
'''

'''
Para colas de prioridad

response = requests.put(BASE + "priority_queue", {
    "names": "Melissa,Juan,Ernesto,Andres,Javier,Vanessa,Mariana,Pedro,Luz",
    "popularity": "90,87,10,24,37,65,70,14,93",
    "times_spoken": "15,30,5,1,55,19,25,173,47"
})
print(response.json())
'''

'''
Para conjuntos disjuntos

response = requests.put(BASE + "sets", {
    "final_node": 9,
    "edges": "0-1,0-2,1-2,4-5,4-6,5-6,7-8,7-9,8-9"
})

print(response.json())
'''

'''
Para Djikstra
response = requests.put(BASE + "djikstra", {
    "start": 0,
    "goal": 4,
    "edges": "0-1,0-2,0-3,3-4"
})

print(response.json())

'''
response = requests.put(BASE + "graph", {
    "start": 0,
    "goal": 4,
    "edges": "0-1,0-2,0-3,3-4"
})

print(response.json())

response = requests.put(BASE + "priority_queue", {
    "names": "Melissa,Juan,Ernesto,Andres,Javier,Vanessa,Mariana,Pedro,Luz",
    "popularity": "90,87,10,24,37,65,70,14,93",
    "times_spoken": "15,30,5,1,55,19,25,173,47"
})
print(response.json())

response = requests.put(BASE + "sets", {
    "nodes": "0,1,2,3,4,5,6,7,8,9",
    "edges": "0-1,0-2,1-2,4-5,4-6,5-6,7-8,7-9,8-9,11-12,11-13,14-14"
})

print(response.json())

response = requests.put(BASE + "djikstra", {
    "start": 0,
    "goal": 2,
    "edges": "0-1-1,1-2-2"
})

print(response.json())








#response = requests.put(BASE + "video/1",  {"likes": 10, "name": "Juan", "views": 150})
#print(response.json())

#input()

#response = requests.get(BASE + "video/100")
#print(response.json())