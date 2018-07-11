from Graph import Graph


# 0 2 3 4
# 2 0 5 6
# 3 5 0 7
# 4 6 7 0
def main():
    g = Graph()

    # Lê uma matriz e transforma em uma lista de adjacências
    n = int(input('Digite o tamanho da matriz: '))
    inicio = 1
    for i in range(n):
        linha = input().split(' ')
        linha = [int(aux) for aux in linha] 
        for j, value in enumerate(linha):
            if(j >= inicio):
                g.addEdge(i, [j, value])
                g.addEdge(j, [i, value])

        inicio += 1

    print(g.graph)

if __name__ == '__main__':
    main()
