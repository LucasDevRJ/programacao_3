#Fatorial recursivo
def fatorial_interativo(n):
    fat = 1
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return fat
    else:
        return n * fatorial_interativo(n-1)

print(fatorial_interativo(5))  # resultado = 120