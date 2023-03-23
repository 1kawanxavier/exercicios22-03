#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista.
numeros = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(int, numeros.split()))

soma = 0

for num in numeros:
    
    if num % 2 != 0:
        soma += num

print("A soma dos números ímpares na lista é:", soma)
