from collections import defaultdict
import heapq

# Classe que representa um gráfico como lista de adjacência
class Graph:
    def __init__(self):
        # Define o valor list() como padrão dos atributos do dicionário
        self.graph = defaultdict(set)
        # Útil pra criação de listas de marcação de vértices, listas que
        # são necessárias nos algoritmos de DFS e BFS
        self.graph_size = 0

    def addEdge(self, u, v):
        self.graph[u].add(v)
        temp = max(u, v[0])
        if(temp > self.graph_size):
            self.graph_size = temp

    def rmEdge(self, u, v):
        self.graph.discard(u, v)
        self.graph_size -= 1

    def DFSUtil(self, v, visited):
        print(v)
        visited[v] = True

        for i in self.graph[v]:
            if(not visited[i[0]]):
                self.DFSUtil(i[0], visited)

    def DFS(self, v):
        visited = [False] * (self.graph_size + 1)
        self.DFSUtil(v, visited)

    def BFS(self, v):
        visited = [False] * (self.graph_size + 1)
        queue = []

        queue.add(v)
        visited[v] = True

        while queue:
            v = queue.discard(0)

            print(v)

            for i in self.graph[v]:
                if(not visited[i[0]]):
                    queue.add(i[0])
                    visited[i[0]] = True

    def dijkstra(self, x):
        distance = [1000] * (self.graph_size + 1) # distâncias a partir do vértice x
        visited = [False] * (self.graph_size + 1) # vértices já verificados (índices)
        pq = [] 
        heapq.heapify(pq) 
       
        distance[x] = 0
        heapq.heappush(pq, (0, x))

        while(len(pq) > 0):
            aux = heapq.heappop(pq)
            a = aux[1]

            if(visited[a]):
                continue
            visited[a] = True

            for u in self.graph[a]:
                b = u[0]
                w = u[1]

                if(distance[a] + w < distance[b]):
                    distance[b] = distance[a] + w
                    heapq.heappush(pq, (distance[b], b))
        return distance
