# Implementando grafos

grafo = dict()

grafo['voce'] = ['alice', 'bob', 'claire']

# Grafo Maior
grafoM = dict()

# Não importa a ordem em que adicionamos os pares chave/valor
grafoM['voce'] = ['alice', 'bob', 'claire']
grafoM['alice'] = ['peggy']
grafoM['bob'] = ['peggy', 'anuj']
grafoM['claire'] = ['jonny', 'thom']
grafoM['anuj'] = []
grafoM['peggy'] = []
grafoM['jonny'] = []
grafoM['thom'] = []

# Grafo Direcionado x Grafo Não Direcionado
'''
    Direcionado:
        (Ross) -----> (Rachel)
        (Ross) <----- (Rachel)
    
    Não Direcionado:
        (Ross) ------ (Rachel)

    Ambos os gráficos são iguais
'''
