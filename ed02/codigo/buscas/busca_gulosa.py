from collections import deque
import tracemalloc
import heapq
from utils.sucessors import gerasucessores
from utils.heuristica_m import heuristica_manhattan

def busca_gulosa(estado_inicial, objetivo):
    tracemalloc.start()

    fila = []
    h = heuristica_manhattan(estado_inicial, objetivo)
    heapq.heappush(fila, (h, estado_inicial, []))
    visitados = set()

    while fila:
        _, estado, caminho = heapq.heappop(fila)
        estado_tupla = tuple(estado)

        if estado_tupla in visitados:
            continue
        visitados.add(estado_tupla)

        if estado == objetivo:
            mem_atual, mem_pico = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return caminho + [estado], mem_pico

        for sucessor in gerasucessores(estado):
            h = heuristica_manhattan(sucessor, objetivo)
            heapq.heappush(fila, (h, sucessor, caminho + [estado]))

    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return None, mem_pico