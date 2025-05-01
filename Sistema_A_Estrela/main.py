from graph import cidades # Importa as cidades - graph
from heuristics import *  # Importa todas as heurísticas
from astar import a_star # Importa lógica do A Estrela
from utils import clear_terminal, get_user_choice

# Dicionário para mapear destinos às suas respectivas funções heurísticas
heuristics_map = {
    "Rio de Janeiro": heuristic_destino_rj,
    "São Paulo": heuristic_destino_sp,
    "Belo Horizonte": heuristic_destino_bh,
    "Brasília": heuristic_destino_bsb,
    "Cuiabá": heuristic_destino_cuiaba,
    "Salvador": heuristic_destino_salvador,
    "Fortaleza": heuristic_destino_fortaleza,
    "Manaus": heuristic_destino_manaus,
    "Curitiba": heuristic_destino_curitiba,
    "Florianópolis": heuristic_destino_florianopolis,
    "Porto Alegre": heuristic_destino_porto_alegre
}

if __name__ == "__main__":
    graph = cidades()
    
    cities = {
        1: 'Porto Alegre', 2: 'Florianópolis', 3: 'Curitiba', 4: 'São Paulo', 5: 'Rio de Janeiro',
        6: 'Belo Horizonte', 7: 'Brasília', 8: 'Cuiabá', 9: 'Salvador', 10: 'Fortaleza', 11: 'Manaus'
    }
    
    clear_terminal()
    print("#### Algoritmo A* ####")
    
    start_point = get_user_choice(cities, "\n\nEscolha a cidade de origem:\n")
    available_destinations = {k: v for k, v in cities.items() if v != start_point}
    available_destinations = {i+1: v for i, (k, v) in enumerate(sorted(available_destinations.items(), key=lambda x: x[0]))}  # Reindexa começando de 1
    
    end_point = get_user_choice(available_destinations, "\n\nEscolha a cidade de destino:\n")
    
    # Seleciona a heurística correta automaticamente
    heuristic_function = heuristics_map.get(end_point, None)
    if heuristic_function is None:
        print("Nenhuma heurística definida para este destino. Verifique se a cidade está correta.")
        exit()

    path = a_star(graph, start_point, end_point, heuristic_function)
    
    clear_terminal()
    print("#### Algoritmo A* ####")
    print("\nOrigem:", start_point)
    print("Destino:", end_point)
    
    if path:
        print("\nCaminho encontrado:", path, "\n")
    else:
        print("\nO destino não está presente no grafo.\n")
