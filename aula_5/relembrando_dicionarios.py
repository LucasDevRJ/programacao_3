#Cria o dicionário
caderno = dict()

#atribui dados ao dicionário
caderno['kiwi'] = 3.12
caderno['abacaxi'] = 1.97
caderno['banana'] = 2.65
caderno['uva'] = 6.99

#imprime o dicionário mapeado: chaves:valores
print(caderno)
#imprime somente o valor da chave banana
print(caderno['banana'])

#imprime todas a chaves
for fruta in caderno.keys():
    print(fruta)
