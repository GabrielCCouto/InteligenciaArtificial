import heapq  # Manipular lista
import os  # Limpar terminal

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Node:
    def __init__(self, name, parent=None, distance=0):
        self.name = name
        self.parent = parent
        self.distance = distance  # custo do ponto inicial ao ponto atual
        self.heuristic = 0  # custo estimado do ponto atual ao ponto de destino
        self.f = 0  # soma dos custos e heurística

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.f < other.f

def romania_map():
    return {
        'Manaus': {'Fortaleza': 2384, 'Cuiabá': 1453},
        'Fortaleza': {'Manaus': 2384, 'Brasília': 1600, 'Salvador': 1028},
        'Cuiabá': {'Rio de Janeiro': 1576, 'Manaus': 1453, 'Belo Horizonte': 1373},
        'Brasília': {'Fortaleza': 1600, 'Belo Horizonte': 600},
        'Salvador': {'São Paulo': 1454, 'Fortaleza': 1028},
        'Belo Horizonte': {'Cuiabá': 1373, 'Brasília': 600, 'São Paulo': 490, 'Rio de Janeiro': 340},
        'Rio de Janeiro': {'Cuiabá': 1576, 'Curitiba': 676, 'Belo Horizonte': 340},
        'São Paulo': {'Salvador': 1454, 'Belo Horizonte': 490, 'Curitiba': 339},
        'Curitiba': {'Rio de Janeiro': 676, 'São Paulo': 339, 'Florianópolis': 251},
        'Florianópolis': {'Porto Alegre': 376, 'Curitiba': 251},
        'Porto Alegre': {'São Paulo': 852, 'Florianópolis': 376},
    }

def heuristic_cost(node_name):
    heuristic_values = {
        'Porto Alegre': 1124,
        'Florianópolis': 748,
        'Curitiba': 676,
        'São Paulo': 357,
        'Rio de Janeiro': 0,
        'Belo Horizonte': 340,
        'Brasília': 933,
        'Cuiabá': 1576,
        'Salvador': 1210,
        'Fortaleza': 2190,
        'Manaus': 2849,
    }
    return heuristic_values[node_name]

def a_star(graph, start, goal):
    if goal not in graph:
        return None
    
    start_node = Node(start)
    goal_node = Node(goal)

    open_list = []
    closed_list = []

    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        current_node = heapq.heappop(open_list)[1]
        closed_list.append(current_node)

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        children = []
        for neighbor, distance in graph[current_node.name].items():
            child_node = Node(neighbor, current_node, distance)
            child_node.distance = current_node.distance + distance
            child_node.heuristic = heuristic_cost(neighbor)
            child_node.f = child_node.distance + child_node.heuristic
            children.append(child_node)

        for child in children:
            if any(child == closed_node for closed_node in closed_list):
                continue

            for open_node in open_list:
                if child == open_node[1] and child.f > open_node[1].f:
                    break
            else:
                heapq.heappush(open_list, (child.f, child))

def get_user_choice(options, prompt):
    while True:
        print(prompt)
        sorted_options = sorted(options.items())  # Ordena pelo número da opção
        for key, value in sorted_options:
            print(f"{key} - {value}")
        try:
            choice = int(input("Escolha uma opção: "))
            if choice in options:
                return options[choice]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    graph = romania_map()
    cities = {
        1: 'Porto Alegre', 2: 'Florianópolis', 3: 'Curitiba', 4: 'São Paulo', 5: 'Rio de Janeiro',
        6: 'Belo Horizonte', 7: 'Brasília', 8: 'Cuiabá', 9: 'Salvador', 10: 'Fortaleza', 11: 'Manaus'
    }
    
    clear_terminal()
    print("-| Algoritmo A* |-")
    start_point = get_user_choice(cities, "Escolha a cidade de origem:")
    available_destinations = {k: v for k, v in cities.items() if v != start_point}
    available_destinations = {i+1: v for i, (k, v) in enumerate(sorted(available_destinations.items(), key=lambda x: x[0]))}  # Reindexa começando de 1
    end_point = get_user_choice(available_destinations, "Escolha a cidade de destino:")
    
    path = a_star(graph, start_point, end_point)
    
    clear_terminal()
    print("-| Algoritmo A* |-")
    print("\nOrigem:", start_point)
    print("Destino:", end_point)
    
    if path:
        print("\nCaminho encontrado:", path, "\n")
    else:
        print("\nO destino não está presente no grafo.\n")