import matplotlib.pyplot as plt
import random
import copy

# Objetivo fixo
objetivo = [1, 2, 3]

# Lista de combinações possíveis (excluindo o objetivo)
estados_possiveis = [
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]

# Mostrar menu de opções
print("Escolha uma combinação inicial para testar:")
for i, estado in enumerate(estados_possiveis):
    print(f"{i + 1}: {estado}")

# Obter escolha do usuário
while True:
    try:
        escolha = int(input("Digite o número da combinação desejada (1 a 5): "))
        if 1 <= escolha <= 5:
            estado_inicial = estados_possiveis[escolha - 1]
            break
        else:
            print("Escolha inválida. Digite um número de 1 a 5.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

# Funções auxiliares
def encontrar_posicao(robo, lista):
    return lista.index(robo)

def robo_nome(r):
    return f"Robô {r}"

def desenhar_estado(estado, titulo="Estado", descricao=""):
    fig, ax = plt.subplots(figsize=(6, 1.5))
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 1)
    ax.axis('off')

    cores = {
        1: 'lightskyblue',
        2: 'lightgreen',
        3: 'salmon'
    }

    for i, robo in enumerate(estado):
        ax.add_patch(plt.Rectangle((i, 0.25), 1, 0.5, edgecolor='black', facecolor=cores[robo]))
        ax.text(i + 0.5, 0.55, f"Robô {robo}", ha='center', va='center', fontsize=10, weight='bold')

    plt.title(f"{titulo}\n{descricao}", fontsize=9)
    plt.tight_layout()
    plt.show()

# Mostrar objetivo
desenhar_estado(objetivo, titulo="Objetivo Final", descricao="Robôs devem estar nesta ordem")

# Mostrar estado inicial escolhido
desenhar_estado(estado_inicial, titulo="Estado Inicial Escolhido", descricao=str(estado_inicial))

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

print(f"\n=== ESTADO INICIAL ESCOLHIDO ===\n{estado_inicial}\n")
print("=== INÍCIO DA SIMULAÇÃO ===")
print(" - ".join(map(str, estado)))

while estado != objetivo:
    passo += 1
    print(f"\npasso {passo}")
    for robo in [1, 2, 3]:  # Ordem sempre começando do Robô 1
        estado, log_texto, restricoes = tentar_mover(estado, robo, restricoes)
        if log_texto:
            print(" - ".join(map(str, estado)))
            print(log_texto)
            desenhar_estado(estado, titulo=f'Passo {passo}', descricao=log_texto)
            break  # Apenas 1 robô age por passo

print("\nObjetivo final alcançado!")