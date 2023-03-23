#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule a média dos números na lista.

numeros = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(int, numeros.split()))

resultado = sum(numeros) / len(numeros)

print(resultado)