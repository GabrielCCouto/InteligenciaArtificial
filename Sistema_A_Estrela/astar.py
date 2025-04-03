import heapq

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

def a_star(graph, start, goal, heuristic_func):
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
            child_node.heuristic = heuristic_func(neighbor)
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
    
    return None
