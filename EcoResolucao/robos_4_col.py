import matplotlib.pyplot as plt
import random
import time  # Para controlar o tempo entre os passos

# Novo objetivo fixo
objetivo = [[1, 2, 3], [4, 5]]

# Gerar estado inicial aleatório com os robôs 1 a 5 e um espaço vazio (0)
valores = [1, 2, 3, 4, 5, 0]
random.shuffle(valores)
estado_inicial = [valores[:3], valores[3:]]

# Normalizar para uma representação consistente (tupla de tuplas com padding de 0)
def normalize_state(state):
    max_len = max(len(row) for row in state)
    normalized = []
    for row in state:
        normalized_row = list(row) + [0] * (max_len - len(row))
        normalized.append(tuple(normalized_row))
    return tuple(normalized)

def robo_nome(r):
    return f"Robô {r}" if r != 0 else "Espaço vazio"

objetivo_normalizado = normalize_state(objetivo)
estado_inicial_normalizado = normalize_state(estado_inicial)
n_cols = len(objetivo_normalizado[0])
n_rows = len(objetivo_normalizado)

def encontrar_posicao(robo, estado_normalizado):
    for r_idx, row in enumerate(estado_normalizado):
        try:
            return r_idx, row.index(robo)
        except ValueError:
            pass
    return None

def desenhar_estado(estado_normalizado, titulo="Estado", descricao=""):
    fig, ax = plt.subplots(figsize=(n_cols * 4, 4))
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.axis('off')

    cores = {
        1: 'lightskyblue',
        2: 'lightgreen',
        3: 'salmon',
        4: 'khaki',
        5: 'gold'
    }

    for r_idx, row in enumerate(estado_normalizado):
        for c_idx, robo in enumerate(row):
            if robo != 0:
                ax.add_patch(plt.Rectangle((c_idx, n_rows - 1 - r_idx), 1, 0.8, edgecolor='black', facecolor=cores.get(robo, 'lightgray')))
                ax.text(c_idx + 0.5, n_rows - 0.6 - r_idx, f"Robô {robo}", ha='center', va='center', fontsize=14, weight='bold')

    plt.title(f"{titulo}\n{descricao}", fontsize=14)
    plt.tight_layout()
    plt.show()

print(f"=== OBJETIVO ===\n{[[val for val in row if val != 0] for row in objetivo]}")
desenhar_estado(objetivo_normalizado, titulo="Objetivo Final Esperado", descricao="Configuração final desejada")
time.sleep(0.1)

# Mostrar objetivo e estado inicial ANTES de iniciar a simulação
print(f"\n=== ESTADO INICIAL ===\n{[[val for val in row if val != 0] for row in estado_inicial]}")
desenhar_estado(estado_inicial_normalizado, titulo="Estado Inicial", descricao="Estado aleatório inicial")
time.sleep(0.1)

print("=== INÍCIO DA SIMULAÇÃO ===")
print(" - ".join([" ".join(map(str, row)) for row in [[val for val in r if val != 0] for r in estado_inicial_normalizado]]))

estado = list(map(list, estado_inicial_normalizado))  # estado mutável
restricoes = {}
passo = 0

def tentar_mover(estado, robo, objetivo_normalizado, restricoes):
    pos_atual = encontrar_posicao(robo, tuple(tuple(row) for row in estado))
    pos_objetivo = encontrar_posicao(robo, objetivo_normalizado)

    if pos_atual == pos_objetivo or pos_atual is None or pos_objetivo is None:
        return estado, None, restricoes

    r_atual, c_atual = pos_atual
    r_objetivo, c_objetivo = pos_objetivo

    direcoes = []
    if r_objetivo > r_atual:
        direcoes.append((1, 0))
    elif r_objetivo < r_atual:
        direcoes.append((-1, 0))
    if c_objetivo > c_atual:
        direcoes.append((0, 1))
    elif c_objetivo < c_atual:
        direcoes.append((0, -1))

    random.shuffle(direcoes)

    for dr, dc in direcoes:
        nova_linha, nova_coluna = r_atual + dr, c_atual + dc
        if 0 <= nova_linha < n_rows and 0 <= nova_coluna < n_cols:
            if (robo, (nova_linha, nova_coluna)) not in restricoes:
                robo_ocupante = estado[nova_linha][nova_coluna]
                pos_ocupante_objetivo = encontrar_posicao(robo_ocupante, objetivo_normalizado)

                if robo_ocupante == 0:
                    estado[r_atual][c_atual], estado[nova_linha][nova_coluna] = 0, robo
                    return estado, f"{robo_nome(robo)} move para a posição vazia ({nova_linha}, {nova_coluna}).", restricoes

                if encontrar_posicao(robo_ocupante, tuple(tuple(row) for row in estado)) != pos_ocupante_objetivo:
                    estado[r_atual][c_atual], estado[nova_linha][nova_coluna] = robo_ocupante, robo
                    restricoes[(robo_ocupante, (r_atual, c_atual))] = True
                    restricoes[(robo_ocupante, pos_objetivo)] = True

                    satisfeito_robo = "satisfeito" if encontrar_posicao(robo, tuple(tuple(row) for row in estado)) == pos_objetivo else "não satisfeito"
                    satisfeito_agredido = "satisfeito" if encontrar_posicao(robo_ocupante, objetivo_normalizado) == encontrar_posicao(robo_ocupante, tuple(tuple(row) for row in estado)) else "não satisfeito"

                    log = (
                        f"{robo_nome(robo)} agride {robo_nome(robo_ocupante)} na posição ({nova_linha}, {nova_coluna}).\n"
                        f"Restrições aplicadas a {robo_nome(robo_ocupante)}:\n"
                        #f" - Não pode ocupar a posição ({nova_linha},{nova_coluna})\n"
                        f" - Não pode ocupar a posição do {robo_nome(robo)} em {pos_objetivo}\n"
                        f"{robo_nome(robo)} {satisfeito_robo}, {robo_nome(robo_ocupante)} {satisfeito_agredido}."
                    )
                    return estado, log, restricoes

    return estado, None, restricoes

while normalize_state(estado) != objetivo_normalizado:
    passo += 1
    print(f"\npasso {passo}")
    houve_movimento = False

    robos_nao_satisfeitos = []
    estado_atual_normalizado = normalize_state(estado)
    for robo_val in sorted([item for sublist in estado_inicial for item in sublist if item != 0]):
        if encontrar_posicao(robo_val, estado_atual_normalizado) != encontrar_posicao(robo_val, objetivo_normalizado):
            robos_nao_satisfeitos.append(robo_val)

    for robo in robos_nao_satisfeitos:
        estado, log_texto, restricoes = tentar_mover(estado, robo, objetivo_normalizado, restricoes)
        if log_texto:
            print(" - ".join([" ".join(map(str, row)) for row in [[val for val in r if val != 0] for r in estado]]))
            print(log_texto)
            desenhar_estado(tuple(tuple(row) for row in estado), titulo=f'Passo {passo}', descricao=log_texto)
            houve_movimento = True
            break

    if not houve_movimento:
        print("\nImpasse detectado. Nenhum robô não satisfeito conseguiu se mover.")
        break
    if passo > 500:
        print("\nLimite máximo de passos atingido. A simulação será encerrada.")
        break

    time.sleep(0.1)  # Pequena pausa entre passos

if normalize_state(estado) == objetivo_normalizado:
    print("\nObjetivo final alcançado!")
    desenhar_estado(normalize_state(estado), titulo="Objetivo Final Alcançado!", descricao="Todos os robôs estão satisfeitos.")
else:
    print("\nSimulação encerrada sem alcançar o objetivo.")