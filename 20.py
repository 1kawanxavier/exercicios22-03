palavras = input("Digite uma lista de palavras separadas por espaço: ")
lista_palavras = palavras.split()

palavras_impares = []

for palavra in lista_palavras:
    if len(palavra) % 2 != 0:
        palavras_impares.append(palavra)

print(f"As palavras com número ímpar de letras são:", palavras_impares)
