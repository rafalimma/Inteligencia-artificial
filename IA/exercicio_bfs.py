# Você tem um mapa 2D representado por uma matriz, onde:
# P é a posição do jogador suspeito (possível cheater).
# E são outros jogadores (potenciais alvos).
# # são montanhas ou obstáculos, que bloqueiam a visão e o caminho.
# . são espaços livres.
# Você quer usar BFS para verificar se o jogador P poderia ter visto o
# jogador E, considerando o caminho livre.

# “Existe um caminho livre (sem passar por montanhas) de P até algum jogador E?”

from collections import deque

grid = [
    ['P', '.', '.', '#', '.', '.', 'E'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.']
]

rows = len(grid)
cols = len(grid[0])

direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# busca em largura usa uma fila
fila = []

def valida_posicao(r, c):
    if c <= cols and r <= rows and grid[r][c] != '#':
        return True


def achar_objetivo(grid):
    start = goal = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "P":
                print('achou jogador')
                start = grid[r][c]
    return goal, start

def can_reach(grid, goal, start):
    queue = deque([start])
    visited = set()
    visited.add(start)

    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == "E":
            break
        for dr, dc in direcoes:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)
        if valida_posicao(nr, nc) and neighbor not in visited:
            ...

    ...


            

achar_objetivo(grid)
