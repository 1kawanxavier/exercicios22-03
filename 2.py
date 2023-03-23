#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a".

palavras = input("Digite uma lista de palavras separadas por espaço: ")

palavras = palavras.split()
print("As palavras que começam com a letra 'a' são: ")
for palavra in palavras:
    if palavra.startswith("a") or palavra.startswith("A"):
        print(palavra)
 