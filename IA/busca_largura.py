from collections import deque

# Representação do mapa
grid = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', 'G']
]

fila = []

rows = len(grid) # tamanho de linha
cols = len(grid[0]) # tamanho de coluna

direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(r, c):
    # verifica se a posição no grid pode ser viditada
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

# Busca  a posição de 'S' (inicio) e 'G' (objetivo)
start = goal = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            print('achou a posição do inicio')
            start = (r, c)
        elif grid[r][c] == 'G':
            print('achou a posição do objetivo')
            goal = (r, c)
        
# busca em largura
def bfs(start, goal):
    # definimos uma fila colocando o ponto de partida
    queue = deque([start])
    # guarda os nós ja visitados
    visited = set()
    visited.add(start)
    # guarda de onde veio cada posição
    # ajuda a reconstruir o caminho do objetivo até o inicio ao final da busca
    parent = {start: None}

    #enquanto estiver posições na fila
    while queue:
        # remove o primeiro item da fila e armazena como current
        current = queue.popleft()
        if current == goal:
            break
        # loop por cada direção possível
        for dr, dc in direcoes:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)

            if is_valid(nr, nc) and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    # reconstruindo o caminho
    path = []
    if goal in parent:
        node = goal
        while node: