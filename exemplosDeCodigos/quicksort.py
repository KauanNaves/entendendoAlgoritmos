# Implementação de QuickSort

listaTeste = [
    1, 2, 5, 5, 6, 8, 8, 1, 25, 1, 32, 65, 98
]

def quicksort(lista: list) -> list:
    # Caso-base
    if len(lista) < 2:
        return lista
    
    # Caso-recursivo
    pivo = lista[0]
    menores = [i for i in lista[1:] if i <= pivo]
    maiores = [i for i in lista[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(f"Algoritmo de ordenação QuickSort: array: {listaTeste}")
print(f"Resultado: {quicksort(listaTeste)}")