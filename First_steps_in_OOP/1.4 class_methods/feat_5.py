class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        print (" ".join (map (str, filter (lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1], self.data))))


graph_1 = Graph ()
graph_1.set_data ([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw ()

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        a, b = self.LIMIT_Y
        print(*filter(lambda x: a <= x <= b, self.data))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


class Graph:

    LIMIT_Y = range(0, 11)

    def set_data(self, data):
        self.data = [k for k in data if k in Graph.LIMIT_Y]


    def draw(self):
        print(*self.data)

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()