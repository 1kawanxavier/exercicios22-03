#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, crie uma nova lista que contenha apenas os nomes que contêm a letra "e".
nomes = input("Digite uma lista de nomes separados por espaço: ")
lista_nomes = nomes.split()

nomes_com_e = []

for nome in lista_nomes:
    if "e" in nome:
        nomes_com_e.append(nome)

print("Os nomes que contêm a letra 'e' são:", nomes_com_e)
