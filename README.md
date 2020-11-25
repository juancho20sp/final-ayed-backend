# Backend AYED

## What is this?

This is a repository for all the files used to create a backend with flask in order to connect our functions with a simple JavaScript web application. This project was deployed to [Heroku](https://dashboard.heroku.com/) and the URL is: https://obscure-sierra-80708.herokuapp.com/.


## Getting Started

For implementing this library you will need to have Python installed in your computer.

### Prerequisites
To use this library you will need to have Python installed in your computer, at least the version 3.7. <br/>
You can check your Python version typing on cmd:

```
python --version
```

### Installing
- Clone this git repository into your computer.
- Start coding!

```
# In your root folder:

git clone https://github.com/juancho20sp/final-ayed-backend.git

```
### Using the Virtual Environment
**Activate**:
``` python
cd venv/Scripts
activate
```

Deactivate:
``` python
cd venv/Scripts
deactivate
```

Install requirements:
- With the **venv** activated: 

``` python
pip install -r requirements.txt
```

## API
### PUT REQUESTS
- [/graph](https://obscure-sierra-80708.herokuapp.com/graph) : Here you will find the functionallity based on the BFS algorythm for graphs. The JSON structure of a PUT request to this endpoint should look like this:
```javascript
{
    // Start node for BFS
    "start": 0,
    
    // Goal node for BFS
    "goal": 4,
    
    // List of edges (from-to)
    "edges": "0-1,0-2,0-3,3-4"
}
```
- The server response for [/graph](https://obscure-sierra-80708.herokuapp.com/graph)  will be a JSON with this structure:
```javascript
{
    // The distance (node count) between 'start' and 'goal'
    "distance": 2,
    
    // The path from 'start' to 'goal'
    "nodes": [2, 4]
}
```
- [/priority_queue](https://obscure-sierra-80708.herokuapp.com/priority_queue): Here you will find the functionallity based on a _priority queue_ and a _binary heap_. The JSON structure of a PUT request to this endpoint should look like this:
```javascript
{
    // The name of each person
    "names": "Melissa,Juan,Ernesto,Andres,Javier,Vanessa,Mariana,Pedro,Luz",
    
    // The popularity of each person
    "popularity": "90,87,10,24,37,65,70,14,93",
    
    // The number of times this person have spoken with our goal.
    "times_spoken": "15,30,5,1,55,19,25,173,47"
    
    // Note that the data is ordered by index, so popularity[0] and times_spoken[0] correspond to names[0]
}
``` 

- The server response for  [/priority_queue](https://obscure-sierra-80708.herokuapp.com/priority_queue)  will be a JSON with this structure:
```javascript
{
    // An array with the data of the mos important people in the list
    data: [{'name': 'Luz', 'score': 4371}, {'name': 'Juan', 'score': 2610}, {'name': 'Pedro', 'score': 2422}]
}
```
- [/sets](https://obscure-sierra-80708.herokuapp.com/sets): Here you will find the functionallity based on _disjoint sets_. The JSON structure of a PUT request to this endpoint should look like this:
```javascript
{
    // The range of nodes, i.e: 0 - 9 (inclusive)
    "final_node": 9,
    
    // List of connections between nodes (from-to)
    "edges": "0-1,0-2,1-2,4-5,4-6,5-6,7-8,7-9,8-9"
}
``` 

- The server response for [/sets](https://obscure-sierra-80708.herokuapp.com/sets) will be a JSON with this structure:
```javascript
{
    // Number of nodes in the graph
    "num_nodes": 10,
    
    // Last analyzed node
    "final_node": 9,
    
    // List of related regions (each related region is an array)
    "related_regions": [1, [2,3,4], [5,6,7,8,9]],
    
    // Length of 'related_regions' array
    "num_related_regions": 3
}
```
- [/djikstra](https://obscure-sierra-80708.herokuapp.com/djikstra): Here you will find the functionallity based on the _Djikstra algorythm_. The JSON structure of a PUT request to this endpoint should look like this:
```javascript
{
    // Start node for Djikstra's algorythm
    "start": 0,
    
    // Goal node form Djikstra's algorythm
    "goal": 4,
    
    // List of connections (from-to-cost)
    "edges": "0-1-16,0-2-2,0-3-1,1-4-1,2-4-0,3-4-3"
}
``` 
- The server response for  [/djikstra](https://obscure-sierra-80708.herokuapp.com/djikstra) will be a JSON with this structure:
```javascript
{
    // Array with the order in which nodes should be visited
    "route": [1,3,5,6],
    
    // Cost of 'route'
    "cost": 11
}
```

## Built With

* [Python 3.8](https://www.python.org/) - As the main programming language and *Flask* as microframework.



## Author

* **Juan David Murillo** - [Github](https://github.com/juancho20sp) | [Twitter](https://twitter.com/juancho20sp)<br/>
* **Diego Fernando Ruiz** -<br/>
Students at: [Escuela Colombiana de Ingeniería Julio Garavito](https://www.escuelaing.edu.co/es/) <br/>
2020 



## License

This is an *open source* project.

### Thanks for checking out!
