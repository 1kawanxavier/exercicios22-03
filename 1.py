#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.

listas = input("Digite uma lista de números separados por espaço: ")

listas = list(map(int, listas.split()))

print("Os numeros pares da lista são: ")

for lista in listas:
    if lista % 2 == 0:
        print(lista)

