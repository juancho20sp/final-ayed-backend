import math


class PriorityQueue:
    def test(self):
        print("Priority Queue working!")

    def __init__(self, A, property_check=0):
        self.heap = Heap(A, property_check)

    def push(self, element):
        self.heap.insert(element)

    def pop(self):
        element = self.heap.get_root()
        self.heap.delete(element)
        return element

    def __len__(self):
        return len(self.heap)


class Heap:
    def __init__(self, A, property_check = 0):

        print("Heap working!")

        self.property_check = property_check
        self.elements = []
        for e in A:
            self.insert(e)

    def get_elements(self):
        return self.elements

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*(i + 1)

    def height(self):
        return math.floor(math.log(len(self.elements),2)) + 1

    def parent(self, i):
        return (i-1)//2 if i % 2 != 0 else (i//2 - 1)

    def build_max_heapify(self):
        for i in range(len(self.elements)//2, -1, -1):
            self.max_heapify(i)

    def get_root(self):
        return self.elements[0]

    def insert(self, e):
        self.elements.append(e)
        self.build_max_heapify()

    def delete(self, key):
        self.elements.remove(key)
        self.build_max_heapify()

    def update(self, old_key, new_key):
        self.delete(old_key)
        self.insert(new_key)

    def max_heapify(self, root):
        left, right, largest = self.left(root), self.right(root), root
        if left < len(self.elements) and self.elements[root][self.property_check] < self.elements[left][self.property_check]:
            largest = left
        if right < len(self.elements) and self.elements[largest][self.property_check] < self.elements[right][self.property_check]:
            largest = right
        if largest != root:
            self.elements[largest], self.elements[root] = self.elements[root], self.elements[largest]
            self.max_heapify(largest)

    def __len__(self):
        return len(self.elements)