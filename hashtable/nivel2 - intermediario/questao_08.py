# 8. Filtragem de dados
# Dado um dicionário de produtos e seus preços, crie um novo dicionário contendo
# apenas os produtos com preço acima de R$ 50.

produtos = {
    "bolacha": 500,
    "pipoca": 40,
    "pastel": 600
}

novo_dicionario = {}

for produto, preco in produtos.items():
    if preco > 50:
        novo_dicionario[produto] = preco

print(f"Produtos com preços maiores que 50:")
print(f"{novo_dicionario}")