def gerasucessores(estado_inicial):
        idx = estado_inicial.index(0) # retorna o indice aonde esta o 0
        linha, col = divmod(idx, 3) # converter o índice da lista (vetor 1D) para coordenadas
        sucessores = []
        movimentos = {
            'cima': (linha - 1, col),
            'baixo': (linha + 1, col),
            'esquerda': (linha, col - 1),
            'direita': (linha, col + 1),
        }
        
        # gera os possíveis estados seguintes ou seja os movimentos válidos que o 0 pode ir
        for movimento, (nl, nc) in movimentos.items():
            if 0 <= nl < 3 and 0 <= nc < 3:
                novo_idx = nl * 3 + nc
                novo_estado = estado_inicial[:]
                novo_estado[idx], novo_estado[novo_idx] = novo_estado[novo_idx], novo_estado[idx]
                sucessores.append(novo_estado)
        return sucessores