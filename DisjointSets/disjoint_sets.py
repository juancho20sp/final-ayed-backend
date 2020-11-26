class DisjointSets:

    def __init__(self, lista_nodos):
        #sets = [x for x in range(A + 1)]
        self.sets = [set([x]) for x in lista_nodos]

    def get_sets(self):
        return self.sets

    def find_set(self, x):
        for si in self.sets:
            if x in si:
                return si
        return None

    def make_set(self, x):
        if self.find_set(x) is None:
            self.sets.append(set([x]))
            return self.sets[len(self.sets)-1]
        return self.find_set(x)

    def union(self, x, y):
        s1 = self.find_set(x)
        s2 = self.find_set(y)

        if s1 is None:
            s1 = self.make_set(x)
        if s2 is None:
            s2 = self.make_set(y)
        if s1 != s2:
            s3 = s1.union(s2)
            self.sets.remove(s1)
            self.sets.remove(s2)
            self.sets.append(s3)

    def connected_components(self, Arcs):
        for e in Arcs:
            self.union(e[0], e[1])

        result = []
        for si in self.sets:
            result.append(si)
        return result

