# 7. Inverta um dicionário
# Dado um dicionário {chave: valor} , crie um novo dicionário {valor: chave}.

pessoas = {
    "anderson": 21,
    "joao": 20,
    "welson": 21
}

novo_dicionario = {}

for chave, valor in pessoas.items():
    if valor not in novo_dicionario:
        # novo_dicionario[chave] = valor
        novo_dicionario[valor] = [chave]
    else:
        novo_dicionario[valor] += [chave]
    
print(f"{novo_dicionario}")