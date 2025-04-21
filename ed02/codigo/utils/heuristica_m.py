def heuristica_manhattan(estado, objetivo):
    distancia = 0
    for i, valor in enumerate(estado):
        if valor == 0:
            continue  # ignorar o espaço em branco
        pos_atual = i
        pos_objetivo = objetivo.index(valor)
        linha_atual, col_atual = divmod(pos_atual, 3)
        linha_objetivo, col_objetivo = divmod(pos_objetivo, 3)
        distancia += abs(linha_atual - linha_objetivo) + abs(col_atual - col_objetivo)
    return distancia