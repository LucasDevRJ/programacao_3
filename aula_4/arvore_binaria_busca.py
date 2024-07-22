class BST:
    def __init__(self, dado=None):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def inserir(self, dado):
        if (self.dado == None):
            self.dado = dado
        else:
            if (dado < self.dado):
                if (self.esquerda): #self.esquerda == None:
                    self.esquerda.inserir(dado)
                else:
                    self.esquerda = BST(dado)
            else:
                if(self.direita): #self.direita == None:
                    self.direita.inserir(dado)
                else:
                    self.direita = BST(dado)

    def emOrdem(self, lst):
        if (self.esquerda):
            self.esquerda.emOrdem(lst)
        lst.append(self.dado) #root
        if (self.direita):
            self.direita.emOrdem(lst)
        return lst

    def preOrdem(self, lst):
        lst.append(self.dado) #root
        if (self.esquerda):
            self.esquerda.preOrdem(lst)
        if (self.direita):
            self.direita.preOrdem(lst)
        return lst

    def posOrdem(self, lst):
        if (self.esquerda):
            self.esquerda.posOrdem(lst)
        if (self.direita):
            self.direita.posOrdem(lst)
        lst.append(self.dado) #root
        return lst

    def emNivel(self):
        nodoAtual = self
        lst = []
        fila = []
        fila.insert(0,nodoAtual)
        while(len(fila) > 0):
            nodoAtual = fila.pop()
            lst.append(nodoAtual.dado)
            if(nodoAtual.esquerda):
                fila.insert(0,nodoAtual.esquerda)
            if(nodoAtual.direita):
                fila.insert(0,nodoAtual.direita)

        return lst

Teste = BST()

Teste.inserir(7)
Teste.inserir(4)
Teste.inserir(9)
Teste.inserir(0)
Teste.inserir(5)
Teste.inserir(8)
Teste.inserir(13)

#          7
#        /  \
#      /     \
#     4        9
#    / \      /  \
#   0   5    8    13

print('Em ordem: ', Teste.emOrdem([]))
print('Em pré-ordem: ', Teste.preOrdem([]))
print('Em pós-ordem: ', Teste.posOrdem([]))

print('Em nível: ', Teste.emNivel())