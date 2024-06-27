# Fatorial interativo

def fatorial_interativo(n):
    fat = 1
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return fat
    else:
        for i in range(1, n + 1):
            fat *= i
        return fat

print(fatorial_interativo(5))  # resultado = 120
