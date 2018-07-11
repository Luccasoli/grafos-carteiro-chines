import heapq 

def main():
    lista = []
    lista.append(100)
    lista.append(15)
    lista.append(200)
    lista.append(20)
    lista.append(2)
    lista.append(1)

    lista.append(2400)
    heapq.heapify(lista)
    for i in range(7):
        print(heapq.heappop(lista))





if __name__ == '__main__':
    main()