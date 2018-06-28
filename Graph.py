from collections import defaultdict


# Classe que representa um gráfico como lista de adjacência
class Graph:
    def __init__(self):
        # Define o valor list() como padrão dos atributos do dicionário
        self.graph = defaultdict(list)
        # Útil pra criação de listas de marcação de vértices, listas que
        # são necessárias nos algoritmos de DFS e BFS
        self.graph_size = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        temp = max(u, v)
        if(temp > self.graph_size):
            self.graph_size = temp

    def rmEdge(self, u, v):
        self.graph.pop(u, v)
        self.graph_size -= 1

    def DFSUtil(self, v, visited):
        visited[v] = True

        print(v)

        for i in self.graph[v]:
            if(not visited[i]):
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * (self.graph_size + 1)
        self.DFSUtil(v, visited)

    def BFS(self, v):
        visited = [False] * (self.graph_size + 1)
        queue = []

        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.pop(0)

            print(v)

            for i in self.graph[v]:
                if(not visited[i]):
                    queue.append(i)
                    visited[i] = True
