from Graph import Graph


# 3 4 2 3 0 1 1
def main():
    g = Graph()

    g.addEdge(2, 5)
    g.addEdge(2, 4)
    g.addEdge(2, 1)
    g.addEdge(4, 3)

    # g.rmEdge(1, 2)
    print("Seu grafo:\n{}".format(g.graph))
    print("DFS:")
    g.DFS(2)
    print("BFS:")
    g.BFS(2)


if __name__ == '__main__':
    main()
