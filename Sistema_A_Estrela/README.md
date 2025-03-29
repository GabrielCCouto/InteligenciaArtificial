# Trabalho - Sistema A*

Classe Node:

    Representa um nó (cidade) no grafo.

    Atributos:

        name: Nome da cidade.

        parent: Nó pai (cidade anterior no caminho).

        distance: Custo acumulado do ponto inicial até o nó atual.

        heuristic: Custo estimado (distância reta) até o nó de destino.

        f: Soma do custo distance e da heuristic, usada para ordenar os nós no algoritmo A*.

Função romania_map():

    Define um grafo de cidades com as distâncias entre as cidades no Brasil (não é exatamente um mapa da Romênia).

    Cada cidade é conectada a outras, com as respectivas distâncias.

Função heuristic_cost():

    Fornece uma heurística simples para cada cidade (distância em linha reta até o destino).

    O valor da heurística foi predefinido para cada cidade, com base em um valor de aproximação.

Função a_star():

    Implementa o algoritmo A* para encontrar o caminho mais curto de uma cidade de partida até o destino.

    Usa duas listas:

        open_list: Lista de nós a serem explorados.

        closed_list: Lista de nós já explorados.

    Para cada cidade, calcula o custo total f(n) que é a soma do custo real (g(n)) e o custo estimado (h(n)).

    A função tenta explorar o caminho mais promissor (com o menor custo total).

Execução e Exibição do Caminho:

    O código usa a função a_star para encontrar o caminho entre as cidades 'Porto Alegre' e 'Rio de Janeiro'.

    O terminal é limpo antes de exibir os resultados.

    Se o caminho for encontrado, ele é impresso.