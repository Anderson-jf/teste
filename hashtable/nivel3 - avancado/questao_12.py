# 12. Detectar anagramas

# Dada uma lista de palavras, agrupe palavras que são anagramas entre si usando
# um dicionário.    

def ordenar(lista):
   n = len(lista)
   for i in range(1, n):
       j = i
       while j > 0:
           if lista[j-1] < lista[j]:
               aux = lista[j-1]
               lista[j-1] = lista[j]
               lista[j] = aux
           j-=1
   return lista

lista = ['amor', 'arara', 'joao']

anagramas = {}

for palavra in lista:
    letras = list(palavra)
    palavra_normal = ''.join(letras)
    palavra_ordenada = ''.join(ordenar(palavra_normal))
    if palavra_ordenada in anagramas:
        anagramas[palavra_ordenada].append(palavra)
    else:
        anagramas[palavra_ordenada] = [palavra]    

for grupo in anagramas.values():
    if len(grupo) > 1:
        print(grupo)