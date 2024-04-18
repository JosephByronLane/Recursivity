fib_max = 30
cont = 0

def fibonacci_iter(n):
    global cont
    cont +=1
    fib = 0
    fib_1 = 1
    fib_2 = 0

    for i in range(1, n+1):
        fib_2 = fib_1
        fib_1 = fib
        fib = fib_1 + fib_2
    return fib
serie =[]
for i in range(fib_max):
    serie.append(fibonacci_iter(i))

print(serie)
print(f'iterativa 100')
cont = 0

def fibonacci_rec(n):
    global cont
    cont += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)



serie =[]
for i in range(fib_max):
    serie.append(fibonacci_rec(i))

print(serie)
print(f'recursiva 3001041072413792166451')
