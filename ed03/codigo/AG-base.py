import random
import time
import pandas as pd

def inicializacao_aleatoria(n_pop, n_items):
    return [[random.randint(0, 1) for _ in range(n_items)] for _ in range(n_pop)]

def inicializacao_heuristica(n_pop, pesos, capacidade):
    populacao = []
    for _ in range(n_pop):
        ind = [0] * len(pesos)
        capacidade_restante = capacidade
        indices = sorted(range(len(pesos)), key=lambda i: pesos[i])  # itens mais leves primeiro
        for i in indices:
            if pesos[i] <= capacidade_restante:
                ind[i] = 1
                capacidade_restante -= pesos[i]
        populacao.append(ind)
    return populacao

# calcula o valor total da mochila (objetivo a ser maximizado)
def fitness(individuo, pesos, valores, capacidade):
    peso_total = sum(p * i for p, i in zip(pesos, individuo))
    valor_total = sum(v * i for v, i in zip(valores, individuo))
    return valor_total if peso_total <= capacidade else 0

# seleciona o melhor indivíduo de um subconjunto aleatório
def selecao_torneio(populacao, fitnesses, k=3):
    selecionados = random.sample(list(zip(populacao, fitnesses)), k)
    selecionados.sort(key=lambda x: x[1], reverse=True)
    return selecionados[0][0]


# para após um número fixo de gerações.
def criterio_parada_geracoes(atual, max_geracoes):
    return atual >= max_geracoes

# para se o melhor fitness não muda após várias gerações.
def criterio_parada_convergencia(fitnesses, geracoes_iguais, max_iguais):
    if len(set(fitnesses[-max_iguais:])) == 1:
        return True
    return False

def crossover_um_ponto(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    return pai1[:ponto] + pai2[ponto:], pai2[:ponto] + pai1[ponto:]

def crossover_dois_pontos(pai1, pai2):
    p1, p2 = sorted(random.sample(range(1, len(pai1)), 2))
    filho1 = pai1[:p1] + pai2[p1:p2] + pai1[p2:]
    filho2 = pai2[:p1] + pai1[p1:p2] + pai2[p2:]
    return filho1, filho2

def crossover_uniforme(pai1, pai2):
    filho1 = [random.choice([g1, g2]) for g1, g2 in zip(pai1, pai2)]
    filho2 = [random.choice([g1, g2]) for g1, g2 in zip(pai1, pai2)]
    return filho1, filho2

def mutacao(ind, taxa):
    return [gene if random.random() > taxa else 1 - gene for gene in ind]


def algoritmo_genetico(
    pesos, valores, capacidade, n_pop, max_geracoes,
    crossover_func, mutacao_taxa, init_func,
    criterio_parada_func=criterio_parada_geracoes, usar_convergencia=True, max_iguais=10
):
    n_items = len(pesos)
    populacao = init_func(n_pop, n_items) if init_func == inicializacao_aleatoria else init_func(n_pop, pesos, capacidade)
    historico_fitness = []
    geracao = 0
    geracoes_iguais = 0
    ultimo_melhor = None

    while True:
        fitnesses = [fitness(ind, pesos, valores, capacidade) for ind in populacao]
        melhor_fitness = max(fitnesses)
        historico_fitness.append(melhor_fitness)

        # Verifica convergência
        if ultimo_melhor is not None and melhor_fitness == ultimo_melhor:
            geracoes_iguais += 1
        else:
            geracoes_iguais = 0
        ultimo_melhor = melhor_fitness

        if usar_convergencia and geracoes_iguais >= max_iguais:
            print(f"Parou por convergência após {geracoes_iguais} gerações iguais.")
            break

        if not usar_convergencia and criterio_parada_func(geracao, max_geracoes):
            print(f"Parou após {geracao} gerações fixas.")
            break

        nova_populacao = []
        while len(nova_populacao) < n_pop:
            pai1 = selecao_torneio(populacao, fitnesses)
            pai2 = selecao_torneio(populacao, fitnesses)
            filho1, filho2 = crossover_func(pai1, pai2)
            nova_populacao.append(mutacao(filho1, mutacao_taxa))
            if len(nova_populacao) < n_pop:
                nova_populacao.append(mutacao(filho2, mutacao_taxa))

        populacao = nova_populacao
        geracao += 1

    fitnesses = [fitness(ind, pesos, valores, capacidade) for ind in populacao]
    melhor = max(zip(populacao, fitnesses), key=lambda x: x[1])
    return melhor, historico_fitness

# para ver os diferentes resultados substitui o nome dos arquivos
# cada vez que rodava o código, e as vezes mudava um parâmetro ou outro, quando se trata dos critérios de parada

df = pd.read_csv('ed03/codigo/mochilas/knapsack_9.csv')

# Separar as linhas com os dados dos itens (ignorando a linha da capacidade)
itens_df = df[df['Item'] != 'Capacidade da Mochila'].copy()

# Converter colunas para o tipo correto (caso estejam como string)
itens_df['Peso'] = itens_df['Peso'].astype(int)
itens_df['Valor'] = itens_df['Valor'].astype(int)

# Extrair pesos e valores
pesos = itens_df['Peso'].tolist()
valores = itens_df['Valor'].tolist()

# Extrair capacidade da mochila da última linha
capacidade = int(df[df['Item'] == 'Capacidade da Mochila']['Peso'].values[0])

print("Pesos:", pesos)
print("Valores:", valores)
print("Capacidade:", capacidade)

# Configurações possíveis
inits = [
    ('aleatoria', inicializacao_aleatoria),
    ('heuristica', inicializacao_heuristica)
]

crossovers = [
    ('um_ponto', crossover_um_ponto),
    ('dois_pontos', crossover_dois_pontos),
    ('uniforme', crossover_uniforme)
]

mutacoes = [0.02, 0.1, 0.3]
criterios = [
    ('convergencia', True),
    ('geracoes', False)
]

# Parâmetros fixos
n_pop = 50
max_geracoes = 100
max_iguais = 10

# Loop de testes
for nome_init, init_func in inits:
    for nome_cross, cross_func in crossovers:
        for mutacao_taxa in mutacoes:
            for nome_criterio, usar_convergencia in criterios:
                inicio = time.time()
                melhor_solucao, historico = algoritmo_genetico(
                    pesos=pesos,
                    valores=valores,
                    capacidade=capacidade,
                    n_pop=n_pop,
                    max_geracoes=max_geracoes,
                    crossover_func=cross_func,
                    mutacao_taxa=mutacao_taxa,
                    init_func=init_func,
                    usar_convergencia=usar_convergencia,
                    max_iguais=max_iguais
                )
                fim = time.time()
                tempo_execucao = fim - inicio

                print(f"--- Configuração: crossover={nome_cross}, init={nome_init}, mutacao={mutacao_taxa}, criterio={nome_criterio}")
                print(f"Melhor solução: {melhor_solucao[0]}")
                print(f"Valor total: {melhor_solucao[1]}")
                print(f"Tempo de execução: {tempo_execucao:.4f} segundos\n")