import heapq # Manipular lista
import os # Limpar terminal

class Node:
    def __init__(self, name, parent=None, distance=0):
        """
        Classe que representa um nó no grafo.

        Args:
            name (str): Nome do nó.
            parent (Node, optional): Nó pai. Defaults to None.
            distance (int, optional): Custo do ponto inicial ao ponto atual. Defaults to 0.
        """
        self.name = name
        self.parent = parent
        self.distance = distance  # custo do ponto inicial ao ponto atual
        self.heuristic = 0  # custo estimado do ponto atual ao ponto de destino
        self.f = 0  # soma dos custos e heurística

    def __eq__(self, other):
        """
        Quando utilizado o operador de igualdade entre dois objetos.

        Verifica se dois nós são iguais.

        Args:
            other (Node): Outro nó a ser comparado.

        Returns:
            bool: True se os nós são iguais, False caso contrário.
        """
        return self.name == other.name

    def __lt__(self, other):
        """
        Quando utilizado o operador de menor ou menor ou igual entre dois objetos.

        Verifica se o custo total deste nó é menor que o custo total de outro nó.

        Args:
            other (Node): Outro nó a ser comparado.

        Returns:
            bool: True se o custo total deste nó é menor, False caso contrário.
        """
        return self.f < other.f

def romania_map():
    """
    Define o mapa da Romênia com as conexões entre as cidades e as distâncias.

    Returns:
        dict: Um dicionário representando o grafo.
    """
    graph = {
        'Manaus': {'Fortaleza': 2384,'Cuiabá': 1453},
        'Fortaleza': {'Manaus': 2384, 'Brasília': 1600, 'Salvador': 1028},
        'Cuiabá': {'Rio de Janeiro': 1576,'Manaus': 1453, 'Belo Horizonte': 1373},
        'Brasília': {'Fortaleza': 1600, 'Belo Horizonte': 600},
        'Salvador': {'São Paulo': 1454, 'Fortaleza': 1028},
        'Belo Horizonte': {'Cuiabá': 1373, 'Brasília': 600, 'São Paulo': 490, 'Rio de Janeiro': 340},
        'Rio de Janeiro': {'Cuiabá': 1576, 'Curitiba': 676,'Belo Horizonte': 340},
        'São Paulo': {'Salvador': 1454,'Belo Horizonte': 490, 'Curitiba': 339, },
        'Curitiba': {'Rio de Janeiro': 676, 'São Paulo': 339, 'Florianópolis': 251},
        'Florianópolis': {'Porto Alegre':376,'Curitiba': 251},
        'Porto Alegre': {'São Paulo': 852, 'Florianópolis': 376}
    }
    return graph

def heuristic_cost(node_name):
    """
    Define uma heurística simples de distância em linha reta (aproximada).

    Args:
        node_name (str): Nome do nó atual.

    Returns:
        int: Heurística estimada do ponto atual ao ponto de destino.
    """
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
    """
    Executa o algoritmo A* para encontrar o caminho mais curto de um nó inicial para um nó de destino em um grafo.

    Args:
        graph (dict): O grafo que representa o mapa.
        start (str): O nó inicial.
        goal (str): O nó de destino.

    Returns:
        list: O caminho mais curto do nó inicial ao nó de destino.
    """
    # Verifica se o nó de destino está presente no grafo
    if goal not in graph:
        return None
    
    # Inicializa os nós de início e fim
    start_node = Node(start)
    goal_node = Node(goal)

    # Inicializa as listas aberta e fechada
    open_list = []
    closed_list = []

    # Adiciona o nó de início à lista aberta
    heapq.heappush(open_list, (start_node.f, start_node))

    # Loop principal do algoritmo A*
    while open_list:
        # Obtém o nó atual da lista aberta
        current_node = heapq.heappop(open_list)[1]

        # Adiciona o nó atual à lista fechada
        closed_list.append(current_node)

        # Verifica se alcançamos o nó de destino
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Retorna o caminho do fim ao início

        # Gera os nós filhos
        children = []
        for neighbor, distance in graph[current_node.name].items():
            # Define o vizinho de current_node como nó filho
            child_node = Node(neighbor, current_node, distance)
            # Cálculo do custo real (g(n)), somasse o custo do nó atual ao custo da aresta que leva ao nó filho
            child_node.distance = current_node.distance + distance
            # Cálculo do custo heurístico (h(n)), retorna uma heurística simples de distância em linha reta do nó atual ao nó destino
            child_node.heuristic = heuristic_cost(neighbor)
            # Cálculo do custo total (f(n)), é calculando somando os dois valores anteriores, g(n) e h(n)
            child_node.f = child_node.distance + child_node.heuristic # f(n) = g(n) + h(n)
            children.append(child_node)

        # Loop através dos nós filhos
        for child in children:
            # Verifica se o filho está na lista fechada
            if any(child == closed_node for closed_node in closed_list):
                continue

            # Verifica se o filho está na lista aberta e se é melhor que o existente
            for open_node in open_list:
                if child == open_node[1] and child.f > open_node[1].f:
                    break
            else:
                # Adiciona o filho à lista aberta
                heapq.heappush(open_list, (child.f, child))
                
# Exemplo de uso
if __name__ == "__main__":
    # Define o mapa da Romênia
    graph = romania_map()
    
    # Define o ponto de partida e o ponto de chegada
    start_point = 'Porto Alegre'
    end_point = 'Rio de Janeiro'
    
    # Executa o algoritmo A* para encontrar o caminho
    path = a_star(graph, start_point, end_point)

    # Limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Imprimir informações iniciais
    print("-| Algoritmo A* |-")
    print("\nOrigem:", start_point)
    print("Destino:", end_point)
    
    # Verifica se foi encontrado um caminho
    if path:
        print("\nCaminho encontrado:", path, "\n")
    else:
        print("\nO destino não está presente no grafo.\n")