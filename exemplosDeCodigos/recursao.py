# Contando de N a 1 de forma recursiva

def contagemRecursiva(n: int):
    print(n)

    # Caso-base
    if n <= 1:
        return
    
    #Caso-recursivo
    else:
        contagemRecursiva(n-1)

contagemRecursiva(10)
print()


# Fatorial usando recursão
def fatorialRecursivo(n: int):
    # Caso-base
    if n == 1:
        return 1
    
    # Caso-recursivo
    else:
        return n * fatorialRecursivo(n-1)
    

# N-ésimo termo de Fibonacci
def nesimoTermoDeFibonacci(n: int): # Retorna o N-ésimo termo da sequência de fibonacci
    # Casos-base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Caso-recursivo
    else:
        return nesimoTermoDeFibonacci(n-1) + nesimoTermoDeFibonacci(n-2)
    
print("N-ésimo termo de Fibonacci")
print(nesimoTermoDeFibonacci(10))
print()


# Potenciação recursiva
def potenciacaoRecursiva(a: int, n: int):
    if a == 0 or n == 0:
        return 1
    if n == 1:
        return a
    
    else:
        return a * potenciacaoRecursiva(a, n-1)
    
print("Potenciação Recursiva:")
print(potenciacaoRecursiva(2, 3))