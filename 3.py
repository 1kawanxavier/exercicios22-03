#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.
numeros = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(int, numeros.split()))

maximo = max(numeros)
minimo = min(numeros)

print("O número máximo é:", maximo)
print("O número mínimo é:", minimo)
 