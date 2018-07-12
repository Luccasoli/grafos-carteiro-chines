from collections import defaultdict
import heapq

# Classe que representa um grafo como lista de adjacência
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

    def rmvEdge(self, u, v):
        for vertice in self.graph[u]:
            if(vertice[0] == v):
                self.graph[u].discard(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        #print(v)
        for i in self.graph[v]:
            if(not visited[i[0]]):
                self.DFSUtil(i[0], visited)

    def DFS(self, v):
        visited = [False] * (self.graph_size + 1)
        self.DFSUtil(v, visited)
        return visited

    def BFS(self, v):
        visited = [False] * (self.graph_size + 1)
        queue = []

        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.pop(0)
            for i in self.graph[v]:
                if(not visited[i[0]]):
                    print(i[0])
                    queue.append(i[0])
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

    def isConnected(self, v):
        visited = self.DFS(v)
        num_v_visitados = 0
        for i in range(len(visited)):
            num_v_visitados += 1
        return self.graph_size == num_v_visitados

    def euleriano(self):
        for v in self.graph:
            vertice = self.graph[v]
            if (len(vertice) - 1) % 2 != 0:
                return False
            else:
                return True

    def numVertex(self):
        return len(self.graph)

    def isValidNextEdge(self, v, u):
        if (len(self.graph[v]) == 1):
            return True

        custo = u[1]
        u = u[0]

        visited = [False] * self.numVertex()
        c1 = self.DFSCount(v, visited)

        self.rmvEdge(u, v)
        self.rmvEdge(v, u)

        visited = [False] * self.numVertex()
        c2 = self.DFSCount(v, visited)

        self.addEdge(v, (u, custo))
        self.addEdge(u, (v, custo))

        return c2 <= c1

    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True

        for i in self.graph[v]:
            if (visited[0] == False):
                count += self.DFSCount(i, visited)
        return count

    def numEdges(self):
        m = 0

        for v in self.graph:
            vertice = self.graph[v]
            m += len(vertice)
        return m

    def fleury(self, v):
        ciclo = [v]
        custo = 0

        while(self.numEdges() != 0):
            for u in self.graph[v]:
                if (self.isValidNextEdge(v, u)):
                    ciclo.append(u[0])
                    custo += u[1]
                    self.rmvEdge(u, v)
                    self.rmvEdge(v, u)
                    v = u
                    break
        return ciclo, custo

