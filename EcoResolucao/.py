import matplotlib.pyplot as plt
import time
from collections import deque


# Representação:
# 'V' -> Sapo verde
# 'M' -> Sapo marrom
# '_' -> Espaço vazio

# Gerar todos os estados possíveis a partir de um estado atual
def generate_states(state):
    states = []
    for i in range(len(state)):
        if state[i] == 'V':
            # Verde pode andar para direita
            if i + 1 < len(state) and state[i + 1] == '_':
                new_state = state.copy()
                new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                states.append(('move', i, i + 1, new_state))
            elif i + 2 < len(state) and state[i + 2] == '_':
                new_state = state.copy()
                new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                states.append(('jump', i, i + 2, new_state))

        elif state[i] == 'M':
            # Marrom pode andar para esquerda
            if i - 1 >= 0 and state[i - 1] == '_':
                new_state = state.copy()
                new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                states.append(('move', i, i - 1, new_state))
            elif i - 2 >= 0 and state[i - 2] == '_':
                new_state = state.copy()
                new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                states.append(('jump', i, i - 2, new_state))
    return states


# Resolver o problema usando BFS
def solve(initial_state, goal_state):
    queue = deque()
    visited = set()

    queue.append((initial_state, []))
    visited.add(tuple(initial_state))

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for action, from_idx, to_idx, new_state in generate_states(current_state):
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                queue.append((new_state, path + [(action, from_idx, to_idx, new_state)]))

    return None


# Função para plotar o estado atual
def plot_state(state, move_description=None):
    plt.clf()
    colors = {'V': 'green', 'M': 'brown', '_': 'lightblue'}
    for idx, val in enumerate(state):
        plt.scatter(idx, 0, color=colors[val], s=1000)
        if val != '_':
            plt.text(idx, 0, val, ha='center', va='center', fontsize=20, color='white')
    plt.xticks(range(len(state)))
    plt.yticks([])
    plt.xlim(-1, len(state))
    plt.ylim(-1, 1)
    if move_description:
        plt.title(move_description)
    plt.pause(0.7)


# Definindo estados
initial_state = ['V', 'V', 'V', '_', 'M', 'M', 'M']
goal_state = ['M', 'M', 'M', '_', 'V', 'V', 'V']

# Resolver
solution = solve(initial_state, goal_state)

# Plotar
if solution:
    plt.figure(figsize=(10, 2))
    current_state = initial_state.copy()
    plot_state(current_state, "Estado Inicial")
    time.sleep(0.1)
    for action, from_idx, to_idx, new_state in solution:
        move_text = f"{action.upper()}: {current_state[from_idx]} de {from_idx} -> {to_idx}"
        plot_state(new_state, move_text)
        current_state = new_state
        time.sleep(0.1)
    plt.show()
else:
    print("Não há solução encontrada.")
