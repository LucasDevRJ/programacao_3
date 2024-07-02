def mergeSort(dados):
  #Condiçao que indica se os dados ainda precisam ser divididos
  if len(dados) > 1:
    #divide recursivamente
    meio = len(dados)//2
    esquerda = dados[:meio]
    direita = dados[meio:]
    mergeSort(esquerda)
    mergeSort(direita)
    #intercala/mescla os dados
    i = j = k = 0
    while i<len(esquerda) and j<len(direita):
      if esquerda[i]<direita[j]:
        dados[k]=esquerda[i]
        i=i+1
      else:
        dados[k]=direita[j]
        j=j+1
      k=k+1
    while i<len(esquerda):
      dados[k]=esquerda[i]
      i=i+1
      k=k+1
    while j<len(direita):
      dados[k]=direita[j]
      j=j+1
      k=k+1


#Programa Principal
dados = [54, 26, 93, 17, 77, 31, 44, 55]
mergeSort(dados)
print(dados)