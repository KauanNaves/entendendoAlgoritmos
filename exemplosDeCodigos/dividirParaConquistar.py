# Técnica DC - Dividir para Conquistar

"""
    Seguir esses dois passos:
    1 - Descubra o caso-base, ou seja, o caso mais simples possível
    2 - Divida ou Diminua o seu problema até que se torne o caso-base
"""

### *** ALGORITMO DE EUCLIDS *** ###

listaTeste = [2, 4, 6]
# Soma Recursiva de arrays
def somaRecursiva(lista: list) -> int:
    # Caso-base
    if len(lista) == 0:
        return 0
    else:

        return lista.pop(0) + somaRecursiva(lista)
    
print(f"Soma recursiva: array: {listaTeste}")
print(f"Resultado: {somaRecursiva(listaTeste)}")
print()


listaTeste2 = [1, 5, 4, 2, 6, 8, 9]
# Contagem de itens recursivamente
def contagemRecursiva(lista: list) -> int:
    # Caso-base
    if lista == []:
        return 0
    else:
        lista.pop()
        return 1 + contagemRecursiva(lista)
    
print(f"Contagem recursiva: array: {listaTeste2}")
print(f"Resultado: {contagemRecursiva(listaTeste2)}")
print()

listaTeste3 = [1, 32, 3224, 2, 54, 2, 100]
def encontrandoMaior(lista: list) -> int:
    # Caso-base 
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    
    # Caso-recursivo
    sub_maximo = encontrandoMaior(lista[1:])
    return lista[0] if lista[0] > sub_maximo else sub_maximo

print(f"Encontrando maior: {listaTeste3}")
print(f"Resultado: {encontrandoMaior(listaTeste3)}")
