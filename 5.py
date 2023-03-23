numeros = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(int, numeros.split()))

numeros.sort()

print("A lista ordenada em ordem crescente é:", numeros)