import csv
from collections import deque
from buscas.busca_largura import busca_largura
from buscas.busca_profundidade import busca_profundidade
from buscas.busca_gulosa import busca_gulosa
from buscas.algoritmoA import busca_a_estrela
import time

def ler_estado_inicial_csv(caminho):
    with open(caminho, 'r') as file:
        numeros = csv.reader(file)
        next(numeros)  # pular cabeçalho
        # converte cada linha para int
        return [[int(n) for n in linha] for linha in numeros]

estados= ler_estado_inicial_csv("ed02-puzzle8.csv")
objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print('realizando busca em largura')
for i, estado_inicial in enumerate(estados, start=1):
    print(f" Resolvendo estado {i}: {estado_inicial}")
    tempo_inicio = time.time()
    solucao, memoria = busca_largura(estado_inicial, objetivo)
    tempo_fim = time.time()
    if solucao:
        print(f"Solucao encontrada em {len(solucao)-1} movimentos. Tempo: {tempo_fim - tempo_inicio:.4f} segundos.")
        print(f"Memoria usada: {memoria / 1024:.2f} KB")
    else:
        print(f"Sem solução encontrada. Tempo: {tempo_fim - tempo_inicio:.4f} segundos")

tempo_total_fim = time.time()
print()
print('realizando busca em profundidade..')
for i, estado_inicial in enumerate(estados, start=1):
    print(f" Resolvendo estado {i}: {estado_inicial}")
    tempo_inicio = time.time()
    solucao, memoria = busca_profundidade(estado_inicial, objetivo)
    tempo_fim = time.time()
    if solucao:
        print(f"Solucao encontrada em {len(solucao)-1} movimentos. Tempo: {tempo_fim - tempo_inicio:.4f} segundos.")
        print(f"Memoria usada: {memoria / 1024:.2f} KB")
    else:
        print(f"Sem solução encontrada. Tempo: {tempo_fim - tempo_inicio:.4f} segundos.")
    
print()
print('realizando busca gulosa..')
for i, estado_inicial in enumerate(estados, start=1):
    print(f" Resolvendo estado {i}: {estado_inicial}")
    tempo_inicio = time.time()
    solucao, memoria = busca_gulosa(estado_inicial, objetivo)
    tempo_fim = time.time()
    if solucao:
        print(f"Gulosa: movimentos = {len(solucao)-1}, tempo = {tempo_fim - tempo_inicio:.4f}s, memoria = {memoria / 1024:.2f} KB")
    else:
        print(f"Sem solução encontrada. Tempo: {tempo_fim - tempo_inicio:.4f} segundos.")
    
print()
print('realizando busca Algoritmo A*..')
for i, estado_inicial in enumerate(estados, start=1):
    print(f" Resolvendo estado {i}: {estado_inicial}")
    tempo_inicio = time.time()
    solucao, memoria = busca_a_estrela(estado_inicial, objetivo)
    tempo_fim = time.time()
    if solucao:
        print(f"Algoritmo A*: movimentos = {len(solucao)-1}, tempo = {tempo_fim - tempo_inicio:.4f}s, memoria = {memoria / 1024:.2f} KB")
    else:
        print(f"Sem solução encontrada. Tempo: {tempo_fim - tempo_inicio:.4f} segundos.")