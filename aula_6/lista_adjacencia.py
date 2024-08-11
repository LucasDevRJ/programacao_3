#implementação com lista de adjacência
class Vertice:
    def __init__(self, n):
      self.nome = n
      self.vizinhos = list()

    def addVizinho(self, v):
      if v not in self.vizinhos:
          self.vizinhos.append(v)
          self.vizinhos.sort()

class Grafo:
    vertices = {}

    def addVertice(self, vertice):
        #Verifique se o objeto é de fato um objeto de vértice e se ele ainda não existe
        if isinstance(vertice, Vertice) and vertice.nome not in self.vertices:
            #adiciona o vértice no dicionario
            self.vertices[vertice.nome] = vertice
            return True
        else:
            return False

    def addAresta(self, u, v):
        #verifica se ambos vertices de fato existe para criar a aresta
        if u in self.vertices and v in self.vertices:
            for key, valor in self.vertices.items():
                #adiciona um na lista de vizinhos do outro
                if key == u:
                    valor.addVizinho(v)
                if key == v:
                    valor.addVizinho(u)
            return True
        else:
            return False

    #Imprime a lsita de adjacências
    def printGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].vizinhos))

G = Grafo()
G.addVertice(Vertice('A'))
G.addVertice(Vertice('B'))
for i in range(ord('A'), ord('G')):
    G.addVertice(Vertice(chr(i)))

arestas = ['AB','AD','BC','CD','CE','CF']
for aresta in arestas:
    G.addAresta(aresta[:1], aresta[1:])

G.printGrafo()