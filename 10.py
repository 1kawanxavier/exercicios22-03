#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista com os números duplicados removidos.
numeros = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(int, numeros.split()))

numeros_unicos = list(set(numeros))

print("A lista com os números duplicados removidos é:", numeros_unicos)
