import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "helloworld/juan")

'''
Para grafos

response = requests.put(BASE + "priority_queue", {
    "start": 0,
    "goal": 4,
    "edges": "0-1,0-2,0-3,3-4"
})
'''

'''
Para colas de prioridad


print(response.json())
'''

response = requests.put(BASE + "graph", {
    "start": 0,
    "goal": 4,
    "edges": "0-1,0-2,0-3,3-4"
})
print(response.json())

input()

response = requests.put(BASE + "priority_queue", {
    "names": "Melissa,Juan,Ernesto,Andres,Javier,Vanessa,Mariana,Pedro,Luz",
    "popularity": "90,87,10,24,37,65,70,14,93",
    "times_spoken": "15,30,5,1,55,19,25,173,47"
})

print(response.json())
# Put





#response = requests.put(BASE + "video/1",  {"likes": 10, "name": "Juan", "views": 150})
#print(response.json())

#input()

#response = requests.get(BASE + "video/100")
#print(response.json())