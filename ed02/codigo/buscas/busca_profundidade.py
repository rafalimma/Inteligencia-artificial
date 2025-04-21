from collections import deque
from utils.sucessors import gerasucessores
import tracemalloc

def busca_profundidade(estado_inicial, objetivo, limite_profundidade=30):
    tracemalloc.start()
    pilha = [(estado_inicial, [])]  # (estado atual, caminho até ele)
    visitados = set()

    while pilha:
        estado, caminho = pilha.pop()
        estado_tupla = tuple(estado)

        if estado_tupla in visitados:
            continue

        visitados.add(estado_tupla)

        if estado == objetivo:
            mem_atual, mem_pico = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return caminho + [estado], mem_pico

        if len(caminho) >= limite_profundidade:
            continue  # evitar loops infinitos e estados muito profundos

        for sucessor in gerasucessores(estado):
            pilha.append((sucessor, caminho + [estado]))
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return None, mem_pico  # se não encontrar