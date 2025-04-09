# Trabalho - Sistema A*

📁 astar.py
Função: Implementa o algoritmo A* propriamente dito.

Define a classe Node, que representa cada cidade durante a busca.

A função a_star(graph, start, goal, heuristic_func) realiza a busca do melhor caminho do ponto de origem (start) ao destino (goal), utilizando a heurística (heuristic_func) e os pesos do grafo.

Usa uma open_list (lista de nós a explorar) e uma closed_list (nós já explorados), com heapq para garantir a ordenação pelo custo total f = custo real + heurística.

📁 graph.py
Função: Define o grafo com as distâncias entre as cidades conectadas.

A função cidades() retorna um dicionário onde cada chave é uma cidade e os valores são dicionários com cidades vizinhas e distâncias (custos) diretas.

📁 heuristics.py
Função: Contém as funções heurísticas para cada cidade como destino.

Cada função (heuristic_destino_<cidade>) retorna uma estimativa da distância de qualquer cidade para uma cidade específica (usada como destino).

Essas heurísticas são pré-definidas com base em alguma estimativa (como distância em linha reta, por exemplo).

📁 main.py
Função: É o ponto de entrada do programa.

Gerencia a interação com o usuário:

Pergunta a cidade de origem e destino.

Seleciona automaticamente a heurística correspondente ao destino.

Executa o algoritmo A* e exibe o caminho encontrado.

Usa funções auxiliares de utils.py para limpar a tela e obter escolhas do usuário.

📁 utils.py
Função: Contém funções utilitárias auxiliares.

clear_terminal(): limpa o terminal para melhor apresentação.

get_user_choice(options, prompt): mostra opções numeradas ao usuário e valida a entrada, retornando a cidade selecionada.