import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "helloworld/juan")

# Put
response = requests.get(BASE + "graph")
print(response.json())

input()

response = requests.put(BASE + "graph", {
    "start": 0,
    "goal": 4,
    "edges": "0-1,0-2,0-3,3-4"
})
print(response.json())

input()

response = requests.get(BASE + "graph")
print(response.json())

input()

response = requests.delete(BASE + "graph")
print(response.json())

input()

response = requests.get(BASE + "graph")
print(response.json())


#response = requests.put(BASE + "video/1",  {"likes": 10, "name": "Juan", "views": 150})
#print(response.json())

#input()

#response = requests.get(BASE + "video/100")
#print(response.json())