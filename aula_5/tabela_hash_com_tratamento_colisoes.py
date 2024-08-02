#Tentativa linear
from aula_5.tabela_hash import hashFuncSigla


def tentativaLinear(k, n, pos, tabelaHash):
  tentativa = pos
  while (tabelaHash[tentativa] != None):
    tentativa += 1
    if tentativa == n:
      tentativa = 0
    if tentativa == pos:
      tentativa = -1
      break
  return tentativa

#Tentativa linear
def tentativaLinear(k, n, pos, tabelaHash):
  tentativa = pos
  while (tabelaHash[tentativa] != None):
    tentativa += 1
    if tentativa == n:
      tentativa = 0
    if tentativa == pos:
      tentativa = -1
      break
  return tentativa

#Tentativa linear Remover
def tentativaLinearDel(k, n, pos, tabelaHash):
  tentativa = pos
  while (tabelaHash[tentativa] != k):
    tentativa += 1
    if tentativa == n:
      tentativa = 0
    if tentativa == pos:
      tentativa = -1
      break
  return tentativa

#Programa principal
n = 10
tabelaHash = [None] * n

while True:
  print('1 - Inserir na tabela hash')
  print('2 - Remover na tabela hash')
  print('3 - Listar a tabela hash')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))
  if op == 1:
    chave = input('Digite a sigla de um estado: ')
    pos = hashFuncSigla(chave, n)
    if tabelaHash[pos] == None:
        tabelaHash[pos] = chave
    else: #Colisão!
        pos = tentativaLinear(chave, n, pos, tabelaHash)
        if pos != -1:
          tabelaHash[pos] = chave
        else:
          print('Tabela hash cheia. Impossível inserir!')
  elif op == 2:
    chave = input('Digite o que deseja remover: ')
    pos = hashFuncSigla(chave, n)
    if tabelaHash[pos] == chave:
        tabelaHash[pos] = None
    else: #Colisão
        pos = tentativaLinearDel(chave, n, pos, tabelaHash)
        if pos != -1:
          tabelaHash[pos] = None
        else:
            print('Valor não localizado para a remoção!')
  elif op == 3:
      print(tabelaHash)
  elif op == 4:
    print('Encerrando...')
    break
  else:
    print("Selecione outra opção!\n")