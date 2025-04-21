import tracemalloc
import heapq
from utils.sucessors import gerasucessores
from utils.heuristica_m import heuristica_manhattan

import heapq
import tracemalloc

def busca_a_estrela(estado_inicial, objetivo):
    tracemalloc.start()

    fila = []
    heapq.heappush(fila, (0, estado_inicial, []))  # (f, estado, caminho)
    visitados = set()

    while fila:
        f, estado, caminho = heapq.heappop(fila)
        estado_tupla = tuple(estado)

        if estado_tupla in visitados:
            continue
        visitados.add(estado_tupla)

        if estado == objetivo:
            mem_atual, mem_pico = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return caminho + [estado], mem_pico

        for sucessor in gerasucessores(estado):
            g = len(caminho) + 1
            h = heuristica_manhattan(sucessor, objetivo)
            f_n = g + h
            heapq.heappush(fila, (f_n, sucessor, caminho + [estado]))

    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return None, mem_pico