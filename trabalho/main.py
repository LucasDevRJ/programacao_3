class Main:
    def __init__(self):
        self.lista = ListaDePacientes()

    def exibe_menu(self):
        while True:
            print()
            print('1 - Adicionar paciente a fila')
            print('2 - Mostrar pacientes na fila')
            print('3 - Chamar paciente')
            print('4 - Sair')
            opcao = int(input('Digite a sua opção: '))

            if opcao == 1:
                self.lista.inserir()
            elif opcao == 2:
                self.lista.mostrar()
            elif opcao == 3:
                self.lista.chamar()
            elif opcao == 4:
                break
            else:
                print("Opção inválida! Tente novamente.")


class ListaDePacientes:
    def __init__(self):
        self.pacientes = []

    def inserir(self):
        cor = input('Digite a cor do cartão (A/V): ')
        if cor == 'A':
            numero = int(input('Informe o número do cartão: '))
            if numero < 201:
                print("Número inválido. Deve ser maior ou igual a 1.")
                return
        elif cor == 'V':
            numero = int(input('Informe o número do cartão: '))
            if numero < 1:
                print("Número inválido. Deve ser maior ou igual a 201.")
                return
        else:
            print("Cor inválida. Use 'A' para amarelo e 'V' para vermelho.")
            return

        paciente = Paciente(cor, numero)
        self.adicionar(paciente)

    def adicionar(self, paciente):
        if paciente.cor == 'V':
            # Adiciona pacientes com cartão 'A' antes dos pacientes com cartão 'V'
            pos = next((i for i, p in enumerate(self.pacientes) if p.cor == 'V'), len(self.pacientes))
            self.pacientes.insert(pos, paciente)
        else:
            # Adiciona pacientes com cartão 'V' ao final da lista
            self.pacientes.append(paciente)

        print(f'Paciente de cor {paciente.cor} e número {paciente.numero} foi adicionado com sucesso.')

    def inserirSemPrioridade(self, paciente):
        self.pacientes.append(paciente)
        print(f'Paciente de cor {paciente.cor} e número {paciente.numero} foi adicionado com sucesso.')

    def inserirComPrioridade(self, paciente):
        numero_pacientes = len(self.pacientes)
        if numero_pacientes == 0:
            self.pacientes.append(paciente)
            print(f'Paciente de cor {paciente.cor} e número {paciente.numero} foi adicionado com sucesso.')
            return

        for i in range(1, numero_pacientes):
            if self.pacientes[i - 1].cor == 'A':
                self.pacientes.insert(i, paciente)
                print(
                    f'Paciente de cor {paciente.cor} e número {paciente.numero} foi adicionado com sucesso na posição {i}.')
                return

        # Se nenhum paciente com cor 'A' for encontrado, adicionar no final
        self.pacientes.append(paciente)
        print(f'Paciente de cor {paciente.cor} e número {paciente.numero} foi adicionado com sucesso no final da fila.')


    def mostrar(self):
        if not self.pacientes:
            print("Nenhum paciente na fila.")
        else:
            # Separar pacientes com cartão 'A' e 'V'
            pacientes_a = [p for p in self.pacientes if p.cor == 'A']
            pacientes_v = [p for p in self.pacientes if p.cor == 'V']

            # Ordenar cada lista de pacientes
            pacientes_a.sort(key=lambda p: p.numero)
            pacientes_v.sort(key=lambda p: p.numero)

            print("Lista ->", end=" ")
            for paciente in pacientes_a + pacientes_v:
                print(f'[{paciente.cor}, {paciente.numero}]', end=" ")
            print()  # Para finalizar a linha após a lista de pacientes

    print()
    def chamar(self):
        if not self.pacientes:
            print("Nenhum paciente na fila para chamar.")
            return

        # Encontra o paciente com cor 'A' e menor número
        indice_prioritario = -1
        menor_numero = float('inf')

        for i, paciente in enumerate(self.pacientes):
            if paciente.cor == 'A' and paciente.numero < menor_numero:
                menor_numero = paciente.numero
                indice_prioritario = i

        # Se encontrou um paciente prioritário (cor 'A' com menor número)
        if indice_prioritario != -1:
            paciente = self.pacientes.pop(indice_prioritario)
            print(f'Atendendo o paciente com o cartão cor {paciente.cor} e número {paciente.numero}')
            return

        # Se não há pacientes com cor 'A', encontrar o paciente com cor 'V' e menor número
        indice_prioritario = -1
        menor_numero = float('inf')

        for i, paciente in enumerate(self.pacientes):
            if paciente.cor == 'V' and paciente.numero < menor_numero:
                menor_numero = paciente.numero
                indice_prioritario = i

        # Atende o paciente com cor 'V' e menor número
        if indice_prioritario != -1:
            paciente = self.pacientes.pop(indice_prioritario)
            print(f'Atendendo o paciente com o cartão cor {paciente.cor} e número {paciente.numero}')


class Paciente:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero


if __name__ == "__main__":
    principal = Main()
    principal.exibe_menu()
