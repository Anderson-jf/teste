# 6. Contador de frequências
# Dado um texto, conte a frequência de cada palavra usando um dicionário.

texto = 'treinar biceps biceps e costas e triceps triceps e biceps'
texto_separado = texto.split()

frequencia = {}

for item in texto_separado:
    if item not in frequencia:
        frequencia[item] = 1
    else:
        frequencia[item] += 1

print(frequencia)