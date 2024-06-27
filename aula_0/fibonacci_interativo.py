def calcula_fibonacci(fibonacci):
    if fibonacci == 0:
        return 0
    elif fibonacci == 1 or fibonacci == 2:
        return 1
    else:
        numero_atual = 1
        numero_anterior = 0
        troca = 0
        i = 1
        while i < fibonacci:
            troca = numero_anterior
            numero_anterior = numero_atual
            numero_atual += troca
            i += 1
        return numero_atual

print(calcula_fibonacci(8))