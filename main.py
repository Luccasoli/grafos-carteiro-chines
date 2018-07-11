from Graph import Graph


# 0 2 3 4
# 2 0 5 6
# 3 5 0 7
# 4 6 7 0

'''
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
def main():
    g = Graph()

    # Lê uma matriz e transforma em uma lista de adjacências
    n = int(input('Digite o tamanho da matriz: '))
    inicio = 1
    for i in range(n):
        linha = input().split(' ')
        linha = [int(aux) for aux in linha] 
        for j, value in enumerate(linha):
            if(j >= inicio and value != 1000):
                g.addEdge(i, [j, value])
                g.addEdge(j, [i, value])

        inicio += 1

    print(g.graph)

if __name__ == '__main__':
    main()
