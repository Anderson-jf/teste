# 10. Dicionário com listas
# Crie um dicionário onde a chave seja o nome de um aluno e o valor seja uma lista
# de notas. Implemente uma função para calcular a média de cada aluno.

aluno = {
    "anderson": [10, 10, 10, 10],
    "joao": [6, 7, 8, 9],
    "welson": [9, 9, 9, 9]
}

for nome, notas in aluno.items():
    soma = 0
    for nota in notas:
        soma += nota
        media = soma // len(notas)
    print(f"{nome} --> {media}")