import random
def busca_binaria(inicio, fim, dados, buscado):
    while (inicio <= fim):
        meio = int((inicio + fim) / 2)
        if (buscado > dados[meio]):
            inicio = meio + 1
        elif (buscado < dados[meio]):
            fim = meio - 1
        else:
            return meio
    return -1

#Gerando 10 valores dentro de um intervalo de 0 até 9
dados = random.sample(range(10), 10)
dados.sort()
print(dados)

buscado = int(input('Digite o valor que deseja buscar: '))
achou = busca_binaria(0, len(dados), dados, buscado)

if (achou == -1):
    print('Valor não encontrado')
else:
    print('Valor encontrado na posição {}'.format(achou))