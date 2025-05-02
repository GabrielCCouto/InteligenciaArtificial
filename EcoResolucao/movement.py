# movement.py

# Função para encontrar a posição de um robô no estado
import random


def encontrar_posicao(robo, estado_normalizado):
    for r_idx, row in enumerate(estado_normalizado):
        try:
            return r_idx, row.index(robo)  # Retorna as coordenadas do robô
        except ValueError:
            pass
    return None  # Caso o robô não seja encontrado

# Função para tentar mover um robô em direção ao seu objetivo
def tentar_mover(estado, robo, objetivo_normalizado, restricoes):
    pos_atual = encontrar_posicao(robo, tuple(tuple(row) for row in estado))
    pos_objetivo = encontrar_posicao(robo, objetivo_normalizado)

    # Se o robô já está na posição desejada ou não pode ser movido, retorna o estado atual
    if pos_atual == pos_objetivo or pos_atual is None or pos_objetivo is None:
        return estado, None, restricoes

    r_atual, c_atual = pos_atual
    r_objetivo, c_objetivo = pos_objetivo

    # Lista de direções para mover o robô em direção ao objetivo
    direcoes = []
    if r_objetivo > r_atual:
        direcoes.append((1, 0))  # Move para baixo
    elif r_objetivo < r_atual:
        direcoes.append((-1, 0))  # Move para cima
    if c_objetivo > c_atual:
        direcoes.append((0, 1))  # Move para a direita
    elif c_objetivo < c_atual:
        direcoes.append((0, -1))  # Move para a esquerda

    # Embaralha as direções para tentar movimentos aleatórios
    random.shuffle(direcoes)

    for dr, dc in direcoes:
        nova_linha, nova_coluna = r_atual + dr, c_atual + dc
        if 0 <= nova_linha < len(estado) and 0 <= nova_coluna < len(estado[0]):
            if (robo, (nova_linha, nova_coluna)) not in restricoes:
                robo_ocupante = estado[nova_linha][nova_coluna]
                pos_ocupante_objetivo = encontrar_posicao(robo_ocupante, objetivo_normalizado)

                if robo_ocupante == 0:  # Se a célula estiver vazia
                    estado[r_atual][c_atual], estado[nova_linha][nova_coluna] = 0, robo
                    return estado, f"Robô {robo} move para a posição vazia ({nova_linha}, {nova_coluna}).", restricoes

    return estado, None, restricoes
