#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por um número fornecido pelo usuário.

numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = list(map(int, numeros.split()))

divisor = int(input("Digite o número pelo qual deseja dividir: "))

divisiveis = []

for numero in lista_numeros:
    if numero % divisor == 0:
        divisiveis.append(numero)

print(f"Os números divisíveis por {divisor} são:", divisiveis)
