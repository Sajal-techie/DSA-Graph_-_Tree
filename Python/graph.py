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

    ## to search through all vertex without starting value

    # def dfs(self):
    #     visited = set()
    #     for start in self.graph:
    #         if start not in visited:
    #             self.dfs_recurse(start, visited)
    #
    # def dfs_recurse(self, vertex, visited):
    #     visited.add(vertex)
    #     print(vertex, end=" ")
    #     for i in self.graph[vertex]:
    #         if i not in visited:
    #             self.dfs_recurse(i,visited)

    def dfs(self, node, visited=set()):
        if node not in self.graph:
            print("node not in graph")
            return
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for i in self.graph[node]:
                self.dfs(i, visited)

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
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')
# graph.delete_vertex('A')
graph.delete_edge('A','B')
print('dfs')
graph.dfs("A")
print('\nbfs')
graph.bfs("A")