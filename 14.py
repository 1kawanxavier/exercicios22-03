# um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais baixo na lista.
numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = list(map(int, numeros.split()))

menor = segundo_menor = float('inf')

for numero in lista_numeros:
    if numero < menor:
        segundo_menor = menor
        menor = numero
    elif numero < segundo_menor and numero != menor:
        segundo_menor = numero

print("O segundo número mais baixo na lista é:", segundo_menor)
