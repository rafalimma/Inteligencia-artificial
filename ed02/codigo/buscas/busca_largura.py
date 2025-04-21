from collections import deque
import tracemalloc
from utils.sucessors import gerasucessores

def busca_largura(estado_inicial, objetivo):
    tracemalloc.start()

    fila = deque()
    fila.append((estado_inicial, []))  # estado + caminho até aqui
    visitados = set()

    while fila:
        estado, caminho = fila.popleft()
        estado_tupla = tuple(estado)

        if estado_tupla in visitados:
            continue

        visitados.add(estado_tupla)

        if estado == objetivo:
            mem_atual, mem_pico = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return caminho + [estado], mem_pico

        for sucessor in gerasucessores(estado):
            fila.append((sucessor, caminho + [estado]))

    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return None, mem_pico

