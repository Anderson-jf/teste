# 9. Mesclar dois dicionários
# Dado dois dicionários com dados de alunos (nome e nota), una os dois, somando as
# notas dos alunos repetidos.

alunos1 = {
    "anderson": 10,
    "joao": 6 
}
alunos2 = {
    "camilo": 10,
    "welson": 9,
    "anderson": 10
}

alunos_mesclados = {}

for nome, nota in alunos1.items():
    alunos_mesclados[nome] = nota

for nome, nota in alunos2.items():
    if nome not in alunos_mesclados:
        alunos_mesclados[nome] = nota
    else:
        alunos_mesclados[nome] += nota

print(f"{alunos_mesclados}")