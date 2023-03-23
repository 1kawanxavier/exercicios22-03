#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.

numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = list(map(int, numeros.split()))

repetidos = []
unicos = set()

for numero in lista_numeros:
    if numero not in unicos:
        unicos.add(numero)
    else:
        repetidos.append(numero)

repetidos = list(set(repetidos))

print("Os números que se repetem são:", repetidos)
