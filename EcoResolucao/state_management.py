# state_management.py

import random

# Função para normalizar o estado do ambiente, garantindo uma representação consistente com padding de 0
def normalize_state(state):
    max_len = max(len(row) for row in state)  # Encontrar o comprimento máximo das linhas
    normalized = []
    
    # Preencher as linhas menores com zeros para normalização
    for row in state:
        normalized_row = list(row) + [0] * (max_len - len(row))  # Preenche com 0
        normalized.append(tuple(normalized_row))  # Converte para tupla
    return tuple(normalized)

# Função para gerar o estado inicial aleatório, com robôs numerados de 1 a 5 e um espaço vazio (0)
def gerar_estado_inicial():
    valores = [1, 2, 3, 4, 5, 0]  # Representação dos robôs e espaço vazio
    random.shuffle(valores)  # Embaralha os valores para gerar um estado aleatório
    estado_inicial = [valores[:3], valores[3:]]  # Divide os valores em duas linhas
    return estado_inicial
