# 5. Itere sobre o dicionário
# Imprima todos os nomes e idades do dicionário usando um loop.

pessoas = {
    "anderson": 21,
    "joao": 20,
    "welson": 21
}

for nome, idade in pessoas.items():
    print(f"{nome} --> {idade}")