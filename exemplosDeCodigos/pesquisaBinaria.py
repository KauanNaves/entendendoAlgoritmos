# Algoritmo - PESQUISA BINÁRIA

def buscaBinaria(lista: list, item): # Retorna a posição do item procurado
    baixo = 0 # Começo da lista
    alto = len(lista) - 1 # Fim da lista

    while baixo <= alto:

        meio = (baixo + alto) // 2 # Meio da lista, arredondando para baixo
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
            alto = meio - 1
            continue

        else:
            baixo = meio + 1
            continue

        return None
    


MINHA_LISTA = [1, 3, 5, 7, 9]

print(buscaBinaria(MINHA_LISTA, 9)) # => 1
print()
print(buscaBinaria(MINHA_LISTA, -1)) # => None

