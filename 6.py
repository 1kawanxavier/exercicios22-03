numeros = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(int, numeros.split()))

sort = sorted(numeros, reversed = True)

print("A lista ordenada em ordem crescente é:", numeros)