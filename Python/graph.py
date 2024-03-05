class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex in self.graph:
            print("vertex is already in graph")
        else:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
        else:
            print("vertex not in list")

    def delete_vertex(self, vertex):
        if vertex not in self.graph:
            print("vertex is not present in the graph ")
            return
        for i in self.graph[vertex]:
            self.graph[i].remove(vertex)
        del self.graph[vertex]

    def delete_edge(self, v1, v2):
        if v1 in self.graph[v2] and v2 in self.graph[v1]:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)
        else:
            print('vertex or edge not in graph')

    def dfs(self):
        visited = set()
        for start in self.graph:
            if start not in visited:
                self.dfs_recurse(start, visited)

    def dfs_recurse(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for i in self.graph[vertex]:
            if i not in visited:
                self.dfs_recurse(i,visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")

            for i in self.graph[v]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

    def __str__(self):
        return str(self.graph)


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(3)
graph.add_vertex(2)
graph.add_vertex(1)
graph.add_edge(0,3)
graph.add_edge(0,2)
graph.add_edge(0,1)
graph.add_edge(2,1)
print(graph)
# graph.delete_vertex(5)
# graph.delete_edge(5,4)
print(graph)
graph.dfs()
print()
graph.bfs(0)
print()
