def bubble_sort(dados):
    tamanho = len(dados)
    for v in range(0, tamanho, 1):
        for i in range(0, tamanho-1, 1):
            if dados[i] > dados[i+1]:
                auxiliar = dados[i]
                dados[i] = dados[i+1]
                dados[i+1] = auxiliar

dados = [5, 4, 2, 1, 8]
bubble_sort(dados)
print(dados)