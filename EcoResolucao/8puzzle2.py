import matplotlib.pyplot as plt
import numpy as np

class Puzzle8:
    def __init__(self, start_state):
        self.start_state = start_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Estado objetivo
        self.size = 3  # Tabuleiro 3x3
        self.visited = set()  # Para evitar ciclos
        self.visited.add(tuple(map(tuple, self.start_state)))  # Marca o estado inicial como visitado
        self.empty_pos = self.find_empty_pos(start_state)  # Posição do '0' (vazio)

    def find_empty_pos(self, state):
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return i, j
        return None

    def is_goal_state(self, state):
        return state == self.goal_state

    def get_valid_moves(self, empty_pos):
        x, y = empty_pos
        moves = []
        if x > 0:  # Para cima
            moves.append((-1, 0))
        if x < self.size - 1:  # Para baixo
            moves.append((1, 0))
        if y > 0:  # Para a esquerda
            moves.append((0, -1))
        if y < self.size - 1:  # Para a direita
            moves.append((0, 1))
        return moves

    def apply_move(self, state, move):
        x, y = self.find_empty_pos(state)
        new_state = [row[:] for row in state]  # Cria uma cópia do estado
        dx, dy = move
        new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
        return new_state

    def eco_resolution(self):
        print("Estado inicial:")
        self.print_state(self.start_state)
        
        queue = [(self.start_state, [])]  # A fila agora mantém o estado e o histórico de movimentos
        iteration = 0
        while queue:
            state, history = queue.pop(0)
            empty_pos = self.find_empty_pos(state)
            iteration += 1
            
            # Exibe o tabuleiro com matplotlib
            print(f"\nIteração {iteration}:")
            self.visualize_state(state)

            # Verificando se é o estado objetivo
            if self.is_goal_state(state):
                print("Solução encontrada!")
                self.print_solution(history + [state])
                break

            # Explora todos os movimentos válidos
            valid_moves = self.get_valid_moves(empty_pos)
            for move in valid_moves:
                new_state = self.apply_move(state, move)
                state_tuple = tuple(map(tuple, new_state))  # Converter para tupla para verificar no 'visited'

                # Verifica se o estado já foi visitado
                if state_tuple not in self.visited:
                    self.visited.add(state_tuple)
                    queue.append((new_state, history + [state]))  # Adiciona o novo estado à fila

    def print_state(self, state):
        for row in state:
            print(row)
        print()

    def visualize_state(self, state):
        # Visualização do estado atual do tabuleiro
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xticks(np.arange(self.size + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.size + 1) - 0.5, minor=True)
        ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

        # Desenha as células com os números
        for i in range(self.size):
            for j in range(self.size):
                num = state[i][j]
                # Ajustando a cor para destacar o "0" e mostrar a posição dos outros números
                ax.add_patch(plt.Rectangle((j, i), 1, 1, color='lightblue' if num != 0 else 'white', lw=2))
                ax.text(j + 0.5, i + 0.5, str(num), ha='center', va='center', fontsize=24, color='black' if num != 0 else 'black')
        
        ax.set_xticks([])
        ax.set_yticks([])
        plt.title("Tabuleiro - Iteração")
        plt.show()

    def print_solution(self, solution_history):
        print("\nSolução final:")
        for idx, state in enumerate(solution_history):
            print(f"Passo {idx}:")
            self.print_state(state)

# Estado inicial do tabuleiro 8-puzzle
start_state = [
    [8, 6, 3],
    [4, 5, 2],
    [7, 1, 0]
]

# Criando o objeto Puzzle8 e chamando o método eco_resolution
puzzle = Puzzle8(start_state)
puzzle.eco_resolution()
