#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por 3.
numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = list(map(int, numeros.split()))

divisiveis_por_3 = []

for numero in lista_numeros:
    if numero % 3 == 0:
        divisiveis_por_3.append(numero)

print("Os números divisíveis por 3 são:", divisiveis_por_3)
