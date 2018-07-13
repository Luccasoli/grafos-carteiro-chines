from Graph import Graph
from time import time

'''
15
0 6 6 5 1000 7 1000 4 3 5 5 2 9 1 6
6 0 2 9 8 9 1000 1000 7 1000 1 8 1000 1 7
6 2 0 7 1000 4 2 4 2 1000 4 1000 1000 1000 1000
5 9 7 0 8 1000 9 8 1000 1000 1000 1000 1000 1000 1
1000 8 1000 8 0 2 1000 1000 3 5 1 1000 6 3 7
7 9 4 1000 2 0 5 7 6 1000 1000 3 7 6 1000
1000 1000 2 9 1000 5 0 6 1000 4 7 1000 1000 2 1000
4 1000 4 8 1000 7 6 0 5 3 1 8 9 1000 1
3 7 2 1000 3 6 1000 5 0 6 1000 5 1000 8 6
5 1000 1000 1000 5 1000 4 3 6 0 8 1000 8 9 1000
5 1 4 1000 1 1000 7 1 1000 8 0 5 4 2 3
2 8 1000 1000 1000 3 1000 8 5 1000 5 0 4 1 1000
9 1000 1000 1000 6 7 1000 9 1000 8 4 4 0 7 1000
1 1 1000 1000 3 6 2 1000 8 9 2 1 7 0 7
6 7 1000 1 7 1000 1000 1 6 1000 3 1000 1000 7 0
'''

'''
5
0 5 1000 9 1
5 0 2 1000 1000
1000 2 0 6 1000
9 1000 6 0 2
1 1000 1000 2 0
'''

'''
8
0 8 1000 1000 1000 1000 1000 1000
8 0 1000 4 1000 9 1000 1000
1000 1000 0 1000 1 1000 1000 1000
1000 4 1000 0 1000 6 1000 1000
1000 1000 1 1000 0 1000 1000
1000 9 1000 6 1000 0 3 1000
1000 1000 1000 1000 1000 3 0 1000
1000 1000 1000 1000 1000 1000 1000 0
'''


def print_matrix(g):
    for vertice in g.graph.items():
        print(vertice)


def readMatriz():
    g = Graph()
    with open('matriz.txt') as arquivo:
        for j, linha in enumerate(arquivo):
            l = linha.split(' ')
            l = [int(aux) for aux in l]
            index = 0
            for i, value in enumerate(l):
                if((i >= index) and (value != 1000)):
                    g.addEdge(j, (i, value))
                    g.addEdge(i, (j, value))
                    g.peso += value/2

            index += 1
    return g


def main():

    g = readMatriz()
    g.DFS(0)
    print("Vértices de grau impar: ", g.impares)

    odds_v = Graph()  # Grafo dos vértices de grau ímpar

    for i in g.impares:  # Construindo o grafo com os vértices de grau ímpar, a partir dos menores custos encontrado pelo algoritmo de dijkstra
        linha = g.dijkstra(i)
        for j in g.impares:
            odds_v.addEdge(i, (j, linha[j]))

    print("\nMenores caminhos entre os vértices de grau ímpar:")
    print_matrix(odds_v)

    g.addEdge(3, (7, 2))
    g.addEdge(4, (10, 1))
    g.addEdge(6, (13, 2))
    g.peso += 2 + 1 + 2

    print("\nGrafo com as arestas duplicadas:")
    print_matrix(g)

    print("Peso total: ", int(g.peso))

    if(not g.isConnected(0)):
        print('E morreu')
        exit()

    if(g.euleriano()):
        ciclo, custo = g.fleury(0)
        print(ciclo)
        print(custo)
        print('Topzero')
    else:
        print('Flopou')


if __name__ == '__main__':
    t = time()
    main()
    t = (time() - t) / 1000
    print('Tempo de execução: {}ms'.format(t))
