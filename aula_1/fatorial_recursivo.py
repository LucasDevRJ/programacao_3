def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        return n * fatorial(n-1)

x = fatorial(5)
print(x)