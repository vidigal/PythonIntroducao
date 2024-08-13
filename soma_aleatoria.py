from random import randint

lista = []

soma = 0
for i in range(10):
    numero_gerado = randint(0, 10)
    soma += numero_gerado
    lista.append(numero_gerado)


print(lista)
print(f'A soma é {soma}')