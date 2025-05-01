import heapq  # Importa o módulo heapq, que fornece uma fila de prioridade baseada em heap (mínimo).

# Define a classe Node, que representa cada nó (estado) no grafo
class Node:
    def __init__(self, name, parent=None, distance=0):
        self.name = name              # Nome do nó (pode ser uma string ou outro identificador)
        self.parent = parent          # Referência ao nó pai, para reconstruir o caminho ao final
        self.distance = distance      # Custo acumulado do início até este nó
        self.heuristic = 0            # Heurística estimada do nó atual até o destino
        self.f = 0                    # f(n) = g(n) + h(n), custo total estimado (distância + heurística)

    def __eq__(self, other):
        return self.name == other.name  # Dois nós são considerados iguais se tiverem o mesmo nome

    def __lt__(self, other):
        return self.f < other.f  # Permite comparação entre nós com base no valor f, necessário para o heap

# Função principal do algoritmo A* (A-estrela)
def a_star(graph, start, goal, heuristic_func):
    if goal not in graph:  # Verifica se o objetivo está no grafo; se não estiver, retorna None
        return None
    
    start_node = Node(start)  # Cria o nó inicial
    goal_node = Node(goal)    # Cria o nó objetivo

    open_list = []            # Lista de nós a serem explorados (fronteira)
    closed_list = []          # Lista de nós já explorados

    heapq.heappush(open_list, (start_node.f, start_node))  # Adiciona o nó inicial à fila de prioridade

    # Loop principal: continua enquanto houver nós na open_list
    while open_list:
        current_node = heapq.heappop(open_list)[1]  # Remove o nó com menor f da fila
        closed_list.append(current_node)            # Adiciona o nó à lista de visitados

        if current_node == goal_node:  # Verifica se o objetivo foi alcançado
            path = []
            while current_node:        # Reconstrói o caminho a partir do objetivo até o início
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]          # Retorna o caminho na ordem correta (do início ao fim)

        children = []  # Lista para armazenar os vizinhos (filhos) do nó atual
        for neighbor, distance in graph[current_node.name].items():  # Itera sobre os vizinhos do nó atual
            child_node = Node(neighbor, current_node, distance)         # Cria um novo nó filho
            child_node.distance = current_node.distance + distance      # Atualiza a distância acumulada
            child_node.heuristic = heuristic_func(neighbor)             # Calcula a heurística para o vizinho
            child_node.f = child_node.distance + child_node.heuristic   # Calcula o custo total estimado
            children.append(child_node)                                 # Adiciona o filho à lista de filhos

        # Para cada filho gerado, verifica se ele já foi visitado ou está na open_list com menor custo
        for child in children:
            if any(child == closed_node for closed_node in closed_list):  # Ignora se já foi explorado
                continue

            for open_node in open_list:
                if child == open_node[1] and child.f > open_node[1].f:  # Ignora se já está na open_list com menor f
                    break
            else:
                heapq.heappush(open_list, (child.f, child))  # Adiciona à open_list se for promissor
    
    return None  # Retorna None se não houver caminho possível até o objetivo