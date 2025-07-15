# 11. Implementar uma hashtable simples
# Sem usar o tipo dict , implemente uma estrutura básica de tabela hash com
# inserção e busca simples.

lista = [None, None, None, None]

opcao = input("Escolha uma opção: ")
while opcao != 3:
    print("1 - Inserir ")
    print("2 - Buscar ")
    print("3 - Sair ")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        chave = input("Chave: ")
        valor = input("Valor: ")
        indice = len(chave) % len(lista)
        lista[indice] = (chave, valor)
    elif opcao == 2:
        chave = input("Digite a chave: ")
        indice = len(chave) % len(lista)
        if lista[indice] != None:
            if lista[indice][chave] == chave:
                print(f"{chave} encontrada.")
            else:
                print(f"{chave} não encontrada.")        
        else:
            print(f"{chave} não encontrada.")
