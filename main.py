cont = 0
n_max = 10

def factorial_it(n):
    global cont
    total = 1
    for i in range(n, 1, -1):
        total = total * i
    return total

for i in range(n_max):
    factorial_it(i)
print(cont)

cont = 0

def factorial_rec(n):
    global cont
    cont +=1
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_rec(n-1)
for i in range(8):

    print(f'{i}! = {factorial_rec(i)}')


