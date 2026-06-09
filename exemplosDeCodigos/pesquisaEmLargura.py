from grafos import grafoM as GRAFO

# Criando uma FILA com todas as pessoas que devem ser verificadas
from collections import deque

filaDePesquisa = deque()

# Adicionando todos os meus amigos
filaDePesquisa += GRAFO['voce']

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'


while filaDePesquisa:
    pessoa = filaDePesquisa.popleft()
    verificadas = list()
    if not pessoa in verificadas:
        if pessoa_e_vendedor(pessoa):
            print(f"{pessoa} é um vendedor de Manga!")
            break
    else:
        filaDePesquisa += GRAFO[pessoa]
        verificadas.append(pessoa)
else:
    print("Não encontrei nenhum vendedor")