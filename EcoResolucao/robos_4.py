import matplotlib.pyplot as plt
import random
import copy

# Objetivo fixo
objetivo = [1, 2, 3, 4]

# Estado inicial aleatório (diferente do objetivo)
while True:
    estado_inicial = random.sample(objetivo, len(objetivo))
    if estado_inicial != objetivo:
        break

# Funções auxiliares
def encontrar_posicao(robo, lista):
    return lista.index(robo)

def robo_nome(r):
    return f"Robô {r}"

def desenhar_estado(estado, titulo="Estado", descricao=""):
    fig, ax = plt.subplots(figsize=(8, 1.5))
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 1)
    ax.axis('off')

    cores = {
        1: 'lightskyblue',
        2: 'lightgreen',
        3: 'salmon',
        4: 'khaki'
    }

    for i, robo in enumerate(estado):
        ax.add_patch(plt.Rectangle((i, 0.25), 1, 0.5, edgecolor='black', facecolor=cores[robo]))
        ax.text(i + 0.5, 0.55, f"Robô {robo}", ha='center', va='center', fontsize=10, weight='bold')

    plt.title(f"{titulo}\n{descricao}", fontsize=9)
    plt.tight_layout()
    plt.show()

# Mostrar objetivo e estado inicial
desenhar_estado(objetivo, titulo="Objetivo Final", descricao="Robôs devem estar nesta ordem")
desenhar_estado(estado_inicial, titulo="Estado Inicial Aleatório", descricao=str(estado_inicial))

# Simulação principal
estado = copy.deepcopy(estado_inicial)
restricoes = {}
passo = 0

def tentar_mover(estado, robo, restricoes):
    pos_atual = encontrar_posicao(robo, estado)
    pos_objetivo = encontrar_posicao(robo, objetivo)

    if pos_atual == pos_objetivo:
        return estado, None, restricoes  # Não há movimentação

    direcao = 1 if pos_objetivo > pos_atual else -1
    nova_posicao = pos_atual + direcao

    if nova_posicao < 0 or nova_posicao >= len(estado):
        return estado, None, restricoes

    robo_ocupante = estado[nova_posicao]

    if (robo, nova_posicao) in restricoes:
        return estado, None, restricoes

    # Agressão
    estado[pos_atual], estado[nova_posicao] = estado[nova_posicao], estado[pos_atual]

    # Aplicar restrição ao agredido: ele não pode voltar para onde foi retirado
    restricoes[(robo_ocupante, pos_atual)] = True

    # Checar satisfação após a movimentação
    satisfeito_robo = "satisfeito" if encontrar_posicao(robo, estado) == encontrar_posicao(robo, objetivo) else "não satisfeito"
    satisfeito_agredido = "satisfeito" if encontrar_posicao(robo_ocupante, estado) == encontrar_posicao(robo_ocupante, objetivo) else "não satisfeito"

    log = (
        f"{robo_nome(robo)} agride {robo_nome(robo_ocupante)}\n"
        f"Restrição aplicada: {robo_nome(robo_ocupante)} não pode ocupar a posição {pos_objetivo}.\n"
        f"{robo_nome(robo)} {satisfeito_robo}, {robo_nome(robo_ocupante)} {satisfeito_agredido}."
    )
    return estado, log, restricoes

print(f"\n=== ESTADO INICIAL ALEATÓRIO ===\n{estado_inicial}\n")
print("=== INÍCIO DA SIMULAÇÃO ===")
print(" - ".join(map(str, estado)))

while estado != objetivo:
    passo += 1
    print(f"\npasso {passo}")
    for robo in [1, 2, 3, 4]:  # Ordem dos robôs
        estado, log_texto, restricoes = tentar_mover(estado, robo, restricoes)
        if log_texto:
            print(" - ".join(map(str, estado)))
            print(log_texto)
            desenhar_estado(estado, titulo=f'Passo {passo}', descricao=log_texto)
            break  # Apenas 1 robô age por passo

#print("\nObjetivo final alcançado!")

# Ao final, mostrar visualmente o objetivo alcançado
desenhar_estado(estado, titulo="Objetivo Final Alcançado!", descricao="Todos os robôs estão satisfeitos.")