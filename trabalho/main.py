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
        numero = int(input('Informe o número do cartão: '))
        paciente = Paciente(cor, numero)
        if cor == 'V':
            if numero < 1:
                print('Os números do cartão V iniciam em 1!')
                self.inserir()
            else:
                self.inserirSemPrioridade(paciente)
        elif cor == 'A':
            if numero < 201:
                print('Os números do cartão A iniciam em 201!')
                self.inserir()
            else:
                self.inserirComPrioridade(paciente)

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
            print("Lista -> ", end="")
            for paciente in self.pacientes:
                print(f'[{paciente.cor}, {paciente.numero}] ', end="")

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
