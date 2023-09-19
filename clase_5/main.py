lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = ['m', 1, 's', 2]

print(lista1[3])
print(lista1[:3])

for i in range(len(lista1)):
    print(lista1[i])

def suma(a, b):
    return a + b

def multiplicacion(a, b):
    return sum([a for i in range(b)])

lista3 = [i+2 for i in range(10)]
print(lista3)
print(sum(lista3))

print(multiplicacion(2, 3))

