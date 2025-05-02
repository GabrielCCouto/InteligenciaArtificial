import matplotlib.pyplot as plt
from copy import deepcopy

# Estado objetivo
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def valid_pos(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def find_position(state, number):
    for i in range(3):
        for j in range(3):
            if state[i][j] == number:
                return (i, j)
    return None

class Agent:
    def __init__(self, number):
        self.number = number

    def goal_position(self):
        return find_position(GOAL_STATE, self.number)

    def current_position(self, state):
        return find_position(state, self.number)

    def in_correct_position(self, state):
        return self.current_position(state) == self.goal_position()

    def propose_move(self, state, empty_pos):
        cx, cy = self.current_position(state)
        gx, gy = self.goal_position()
        dx = gx - cx
        dy = gy - cy

        directions = []
        if dx < 0: directions.append('up')
        if dx > 0: directions.append('down')
        if dy < 0: directions.append('left')
        if dy > 0: directions.append('right')

        for direction in directions:
            dx, dy = MOVES[direction]
            nx, ny = cx + dx, cy + dy
            if valid_pos(nx, ny) and (nx, ny) == empty_pos:
                return direction
        return None

    def who_blocks_me(self, state, empty_pos):
        cx, cy = self.current_position(state)
        gx, gy = self.goal_position()
        dx = gx - cx
        dy = gy - cy

        directions = []
        if dx < 0: directions.append('up')
        if dx > 0: directions.append('down')
        if dy < 0: directions.append('left')
        if dy > 0: directions.append('right')

        for direction in directions:
            dx, dy = MOVES[direction]
            nx, ny = cx + dx, cy + dy
            if valid_pos(nx, ny) and (nx, ny) != empty_pos:
                blocker = state[nx][ny]
                if blocker != 0:
                    return blocker
        return None

    def possible_moves(self, state, empty_pos):
        cx, cy = self.current_position(state)
        moves = []
        for direction, (dx, dy) in MOVES.items():
            nx, ny = cx + dx, cy + dy
            if valid_pos(nx, ny) and (nx, ny) == empty_pos:
                moves.append(direction)
        return moves

def apply_move(state, agent, direction):
    dx, dy = MOVES[direction]
    cx, cy = agent.current_position(state)
    nx, ny = cx + dx, cy + dy
    state[cx][cy], state[nx][ny] = state[nx][ny], state[cx][cy]
    return state

def plot_state(state, step):
    fig, ax = plt.subplots()
    ax.set_title(f"Passo {step}")
    ax.axis('off')
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            ax.text(j, 2 - i, str(val) if val != 0 else "", ha='center', va='center',
                    fontsize=36, bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue'))

    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 2.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def eco_resolution_solver(initial_state, max_steps=100):
    state = deepcopy(initial_state)
    steps = 0

    while steps < max_steps and state != GOAL_STATE:
        agents = [Agent(n) for n in range(1, 9)]
        empty_pos = find_position(state, 0)
        moved = False
        aggression_occurred = False

        print(f"\n=== Passo {steps + 1} ===")

        for agent in agents:
            if agent.in_correct_position(state):
                print(f"✔ Agente {agent.number} está na posição correta.")
                continue

            direction = agent.propose_move(state, empty_pos)
            if direction:
                print(f"🔁 Agente {agent.number} move {direction}.")
                state = apply_move(state, agent, direction)
                moved = True
                break
            else:
                blocker_num = agent.who_blocks_me(state, empty_pos)
                if blocker_num:
                    print(f"❌ Agente {agent.number} está bloqueado por {blocker_num}.")
                    print(f"⚔ Agente {agent.number} agride {blocker_num}.")
                    aggression_occurred = True

                    # Cooperação mínima: o agente bloqueador tenta sair do caminho
                    blocker_agent = Agent(blocker_num)
                    blocker_moves = blocker_agent.possible_moves(state, empty_pos)
                    if blocker_moves:
                        direction = blocker_moves[0]
                        print(f"🤝 Agente {blocker_num} coopera e move {direction} para sair do caminho.")
                        state = apply_move(state, blocker_agent, direction)
                        moved = True
                        break
                else:
                    print(f"🚫 Agente {agent.number} não pode se mover nem está bloqueado diretamente.")

        if not moved and not aggression_occurred:
            print("⚠ Nenhum agente pôde se mover. Encerrando.")
            break

        steps += 1
        plot_state(state, steps)

    print("\n🏁 Estado final:")
    for row in state:
        print(row)
    return state

# Estado inicial
initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

eco_resolution_solver(initial_state)