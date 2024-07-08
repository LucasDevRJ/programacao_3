class Estado:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None


class Estados:
    def __init__(self):
        self.head = None

    def inserir_no_inicio(self, sigla, nome):
        novo_estado = Estado(sigla, nome)
        novo_estado.proximo = self.head
        self.head = novo_estado

    def __str__(self):
        estados = []
        atual = self.head
        while atual:
            estados.append(atual.sigla)
            atual = atual.proximo
        estados.append("None")
        return " -> ".join(estados)


class TabelaHashEstados:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [Estados() for _ in range(tamanho)]

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            char1, char2 = sigla[0], sigla[1]
            return (ord(char1) + ord(char2)) % 10

    def adicionar(self, sigla, estado):
        posicao = self.funcao_hash(sigla)
        self.tabela[posicao].inserir_no_inicio(sigla, estado)

    def exibir(self):
        for i in range(self.tamanho):
            print(f"{i}: {self.tabela[i]}")


# Estados e siglas
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
    ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
    ("SE", "Sergipe"), ("TO", "Tocantins")
]

# Estado fictício
estado_ficticio = ("LL", "Lucas Lima")

# Inicialização da tabela hash
tabela_hash = TabelaHashEstados()

# Impressão da tabela hash vazia
print("Tabela Hash vazia:")
tabela_hash.exibir()
print("\n")

# Inserção dos estados na tabela hash
for sigla, nome in estados:
    tabela_hash.adicionar(sigla, nome)

# Impressão da tabela hash após inserir os 26 estados e o Distrito Federal
print("Tabela Hash após inserir os 26 estados e o Distrito Federal:")
tabela_hash.exibir()
print("\n")

# Inserção do estado fictício
tabela_hash.adicionar(estado_ficticio[0], estado_ficticio[1])

# Impressão da tabela hash após inserir o estado fictício
print("Tabela Hash após inserir os 26 estados, o Distrito Federal e o estado fictício:")
tabela_hash.exibir()
print("\n")
