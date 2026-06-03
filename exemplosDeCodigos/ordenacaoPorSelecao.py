MINHA_LISTA = [
    156, 141, 35, 94, 88, 61, 111,
]

MINHA_LISTA2 = [
    156, 141, 35, 94, 88, 61, 111,
]
MINHA_LISTA3 = [
    156, 141, 35, 94, 88, 61, 111,
]
# Ordenação por seleção criando novas listas
# Ordenacao do menor para o maior
def buscarMenor(lista: list) -> int:
    menor = lista[0]
    menorIndice = 0

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menorIndice = i
        
    return menorIndice


def ordenacaoPorSelecao_Crescente(lista: list) -> list:
    listaOrdenada = list()

    for i in range(len(lista)):
        menor = buscarMenor(lista=lista)
        listaOrdenada.append(lista.pop(menor))

    return listaOrdenada

    

# Ordenando do maior para o menor
def buscarMaior(lista: list) -> int:
    maior = lista[0]
    maiorIndice = 0

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            maiorIndice = i
    return maiorIndice


def ordenacaoPorSelecao_Decrescente(lista: list) -> list:
    listaOrdenada2 = list()

    for i in range(len(lista)):
        maior = buscarMaior(lista)
        listaOrdenada2.append(lista.pop(maior))
    return listaOrdenada2

print("Ordenação Crescente")
print(ordenacaoPorSelecao_Crescente(MINHA_LISTA))
print()

print("Ordenação Decrescente")
print(ordenacaoPorSelecao_Decrescente(MINHA_LISTA2))
print()

print()
print()
print()

#Ordenação por seleção alterando a lista original
def ordenacaoPorSelecao(lista: list):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j] < lista[i]:
                lista[j], lista[i] = lista[i], lista[j]

print(f"Lista original: \n{MINHA_LISTA3}")
ordenacaoPorSelecao(MINHA_LISTA3)
print()

print(f"Lista ordenada: \n{MINHA_LISTA3}")
