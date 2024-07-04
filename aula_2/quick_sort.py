#Versão clássica
def quickSort(dados,inicio,fim):
  if inicio < fim:
    posicao_de_particionamento = partition(dados,inicio,fim)
    quickSort(dados,inicio,posicao_de_particionamento - 1)
    quickSort(dados,posicao_de_particionamento + 1,fim)

def partition(dados,inicio,fim):
  pivo = dados[inicio]
  esq = inicio + 1
  dir = fim
  flag = False
  while not flag:
    while esq <= dir and dados[esq] <= pivo:
      esq = esq + 1
    while dir >= esq and dados[dir] >= pivo:
      dir = dir -1
    if dir < esq:
      flag = True
    else:
      temp = dados[esq]
      dados[esq] = dados[dir]
      dados[dir] = temp
  temp = dados[inicio]
  dados[inicio] = dados[dir]
  dados[dir] = temp
  return dir

#Programa Principal
dados = [50,25,92,16,76,30,43,54,19]
quickSort(dados,0,len(dados)-1)
print(dados)