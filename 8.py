#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são maiores do que 10.

numeros = input("Digite uma lista de números separados por espaço: ")


numeros = list(map(int, numeros.split()))


maior = [num for num in numeros if num > 10]


print("Os números maiores do que 10 são:", maior)
