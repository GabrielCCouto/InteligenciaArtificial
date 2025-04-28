import matplotlib.pyplot as plt
import numpy as np
import time
from collections import deque

# Corrigido: movimentos corretos
MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Função para encontrar a posição do zero (espaço vazio)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Gerar novos estados possíveis
def generate_states(state):
    x, y = find_zero(state)
    new_states = []

    for move, (dx, dy) in MOVES.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            new_states.append((move, new_state))

    return new_states

# Resolver usando BFS
def solve(initial_state, goal_state):
    queue = deque()
    visited = set()

    queue.append((initial_state, []))
    visited.add(str(initial_state))

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for move, new_state in generate_states(current_state):
            if str(new_state) not in visited:
                visited.add(str(new_state))
                queue.append((new_state, path + [move]))

    return None

# Atualizar o estado movendo
def move_tile(state, move):
    x, y = find_zero(state)
    dx, dy = MOVES[move]
    nx, ny = x + dx, y + dy
    if 0 <= nx < 3 and 0 <= ny < 3:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
        return new_state
    return state

# Comparar posição atual com posição no objetivo
def find_piece_position(state, piece):
    for i in range(3):
        for j in range(3):
            if state[i][j] == piece:
                return i, j
    return None

# Detectar motivo do movimento
def detect_reason(prev_state, move, goal_state):
    x0, y0 = find_zero(prev_state)
    dx, dy = MOVES[move]
    px, py = x0 + dx, y0 + dy
    moved_piece = prev_state[px][py]

    # Onde deveria estar
    goal_pos = find_piece_position(goal_state, moved_piece)
    current_pos = (px, py)

    if current_pos == goal_pos:
        return moved_piece, 'normal'

    # Verificando se é pulo/agressão
    if abs(x0 - px) + abs(y0 - py) > 1:
        return moved_piece, 'aggression'

    # Senão é porque está bloqueando
    return moved_piece, 'blocked'

# Função para plotar o tabuleiro com cores
def plot_state(state, highlight_piece=None, reason=None, move=None, before_move=True):
    plt.clf()
    grid = np.array(state)

    # Grid branco
    plt.imshow(np.ones_like(grid), cmap="gray", vmin=0, vmax=1)

    for i in range(3):
        for j in range(3):
            val = grid[i][j]
            if val != 0:
                if highlight_piece and val == highlight_piece:
                    # Cores baseadas na razão
                    if reason == 'normal':
                        color = 'green'
                    elif reason == 'blocked':
                        color = 'yellow'
                    elif reason == 'aggression':
                        color = 'red'
                else:
                    color = 'black'
                plt.text(j, i, str(val), ha='center', va='center', fontsize=24, color=color)

    plt.xticks([])
    plt.yticks([])
    plt.grid(which='both')
    if move:
        plt.title(f"{'Antes' if before_move else 'Depois'} do movimento: {move}\n({reason})")
    else:
        plt.title("Estado Inicial")
    plt.pause(0.8)

# --- Configurações de execução ---

# Estados iniciais
initial = [
    [1, 3, 6],
    [5, 2, 4],
    [7, 0, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Resolver
solution = solve(initial, goal)

# Plotar o processo
if solution:
    print("Movimentos para resolver:", solution)

    plt.figure(figsize=(5, 5))

    current_state = initial
    plot_state(current_state)
    time.sleep(1)

    for move in solution:
        # Antes de mover
        moved_piece, reason = detect_reason(current_state, move, goal)
        plot_state(current_state, highlight_piece=moved_piece, reason=reason, move=move, before_move=True)
        time.sleep(0.8)

        # Agora sim move
        current_state = move_tile(current_state, move)

        # Mostrar o novo estado depois do movimento
        plot_state(current_state, move=move, before_move=False)
        time.sleep(0.8)

    plt.show()
else:
    print("Não há solução.")
