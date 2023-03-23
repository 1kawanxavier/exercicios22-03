#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são menores do que 5.
numeros = input("Digite uma lista de números separados por espaço: ")


numeros = list(map(int, numeros.split()))


menor = [num for num in numeros if num < 5]


print("Os números menores do que 5 são:", menor)
