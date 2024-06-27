def calcula_fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calcula_fibonacci_recursivo(n-1) + calcula_fibonacci_recursivo(n-2)

print(calcula_fibonacci_recursivo(8))