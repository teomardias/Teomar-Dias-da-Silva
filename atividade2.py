def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_menor = i
        print('Menor numeração de contêiner', lista[indice_menor])
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
                print('Menor numeração de contêiner identificado: ')
                print(lista[indice_menor])
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    return lista

numeros = [64, 25, 12, 22, 11]
print('Fileira Oiginal: ', numeros)

ordenada = selection_sort(numeros)
print('Fileira ordenada: ', ordenada) 