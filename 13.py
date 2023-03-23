#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais alto na lista.
numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = list(map(int, numeros.split()))

maior = segundo_maior = float('-inf')

for numero in lista_numeros:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
        segundo_maior = numero

print("O segundo número mais alto na lista é:", segundo_maior)
