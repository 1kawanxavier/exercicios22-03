nomes = input("Digite uma lista de nomes separados por espaço: ")

nomes = nomes.split()

mais_longo = max(nomes, key=len)
mais_curto = min(nomes, key=len)


print("O nome mais longo é:", mais_longo)
print("O nome mais curto é:", mais_curto)