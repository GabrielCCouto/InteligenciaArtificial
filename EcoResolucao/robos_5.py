import matplotlib.pyplot as plt
import itertools
import random
import copy

# Objetivo fixo
objetivo = [1, 2, 3, 4, 5]

# Gerar todas as permutações diferentes do objetivo
todas_combinacoes = list(itertools.permutations([1, 2, 3, 4, 5]))
estados_possiveis = [list(c) for c in todas_combinacoes if list(c) != objetivo]

# Escolher aleatoriamente uma combinação inicial
estado_inicial = random.choice(estados_possiveis)

# Funções auxiliares
def encontrar_posicao(robo, lista):
    return lista.index(robo)

def robo_nome(r):
    return f"Robô {r}"

def desenhar_estado(estado, titulo="Estado", descricao=""):
    fig, ax = plt.subplots(figsize=(9, 1.5))
    ax.set_xlim(0, len(estado))
    ax.set_ylim(0, 1)
    ax.axis('off')

    cores = {
        1: 'lightskyblue',
        2: 'lightgreen',
        3: 'salmon',
        4: 'khaki',
        5: 'orchid'
    }

    for i, robo in enumerate(estado):
        ax.add_patch(plt.Rectangle((i, 0.25), 1, 0.5, edgecolor='black', facecolor=cores.get(robo, 'gray')))
        ax.text(i + 0.5, 0.55, f"Robô {robo}", ha='center', va='center', fontsize=10, weight='bold')

    plt.title(f"{titulo}\n{descricao}", fontsize=9)
    plt.tight_layout()
    plt.show()

# Mostrar estados
desenhar_estado(objetivo, titulo="Objetivo Final", descricao="Robôs devem estar nesta ordem")
desenhar_estado(estado_inicial, titulo="Estado Inicial Aleatório", descricao=str(estado_inicial))

# Simulação principal
estado = copy.deepcopy(estado_inicial)
restricoes = {}
passo = 0
robos_satisfeitos = set()
max_passos = 100  # Limite de segurança

def tentar_mover(estado, robo, restricoes):
    pos_atual = encontrar_posicao(robo, estado)
    pos_objetivo = encontrar_posicao(robo, objetivo)

    if pos_atual == pos_objetivo:
        return estado, None, restricoes

    direcao = 1 if pos_objetivo > pos_atual else -1
    nova_posicao = pos_atual + direcao

    if nova_posicao < 0 or nova_posicao >= len(estado):
        return estado, None, restricoes

    robo_ocupante = estado[nova_posicao]

    if (robo, nova_posicao) in restricoes:
        return estado, None, restricoes

    estado[pos_atual], estado[nova_posicao] = estado[nova_posicao], estado[pos_atual]
    restricoes[(robo_ocupante, pos_atual)] = True

    satisfeito_robo = "satisfeito" if encontrar_posicao(robo, estado) == encontrar_posicao(robo, objetivo) else "não satisfeito"
    satisfeito_agredido = "satisfeito" if encontrar_posicao(robo_ocupante, estado) == encontrar_posicao(robo_ocupante, objetivo) else "não satisfeito"

    log = (
        f"{robo_nome(robo)} agride {robo_nome(robo_ocupante)}\n"
        f"Restrição aplicada: {robo_nome(robo_ocupante)} não pode ocupar a posição {pos_objetivo}.\n"
        f"{robo_nome(robo)} {satisfeito_robo}, {robo_nome(robo_ocupante)} {satisfeito_agredido}."
    )
    return estado, log, restricoes

print(f"\n=== ESTADO INICIAL ALEATÓRIO ===\n{estado_inicial}")
print("=== INÍCIO DA SIMULAÇÃO ===")
print(" - ".join(map(str, estado)))

while estado != objetivo and passo < max_passos:
    passo += 1
    progresso = False
    print(f"\nPasso {passo}")

    # Tentar mover os robôs na ordem de 1 a 5, mas só mover o próximo robô se o anterior estiver satisfeito
    for robo in range(1, 6):
        if robo in robos_satisfeitos:
            continue  # Pular robôs já satisfeitos

        estado, log_texto, restricoes = tentar_mover(estado, robo, restricoes)

        if log_texto:
            progresso = True
            print(" - ".join(map(str, estado)))
            print(log_texto)
            desenhar_estado(estado, titulo=f'Passo {passo}', descricao=log_texto)
            break  # Apenas 1 ação por passo

    # Atualizar robôs satisfeitos após o passo
    for r in range(1, 6):
        if encontrar_posicao(r, estado) == encontrar_posicao(r, objetivo):
            robos_satisfeitos.add(r)

    if not progresso:
        print("\n⚠️ Nenhum robô conseguiu se mover neste passo. Encerrando para evitar loop infinito.")
        break

if estado == objetivo:
    print("\n✅ Objetivo final alcançado!")
else:
    print("\n⛔ Objetivo não alcançado. Algo impediu o progresso.")