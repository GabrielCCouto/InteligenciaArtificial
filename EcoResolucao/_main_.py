# main.py

import time
from state_management import normalize_state, gerar_estado_inicial
from movement import tentar_mover, encontrar_posicao
from drawing import desenhar_estado

# Definição do objetivo
objetivo = [[1, 2, 3], [4, 5]]

# Gerar o estado inicial aleatório
estado_inicial = gerar_estado_inicial()

# Normalizar o objetivo e estado inicial
objetivo_normalizado = normalize_state(objetivo)
estado_inicial_normalizado = normalize_state(estado_inicial)

# Exibir o objetivo e o estado inicial antes de iniciar a simulação
print(f"=== OBJETIVO ===\n{[[val for val in row if val != 0] for row in objetivo]}")
desenhar_estado(objetivo_normalizado, titulo="Objetivo Final Esperado", descricao="Configuração final desejada")
time.sleep(0.1)

print(f"\n=== ESTADO INICIAL ===\n{[[val for val in row if val != 0] for row in estado_inicial]}")
desenhar_estado(estado_inicial_normalizado, titulo="Estado Inicial", descricao="Estado aleatório inicial")
time.sleep(0.1)

print("=== INÍCIO DA SIMULAÇÃO ===")

# Variáveis de controle da simulação
estado = list(map(list, estado_inicial_normalizado))
restricoes = {}
passo = 0

# Inicia a simulação
while normalize_state(estado) != objetivo_normalizado:
    passo += 1
    print(f"\npasso {passo}")
    houve_movimento = False

    robos_nao_satisfeitos = []
    estado_atual_normalizado = normalize_state(estado)
    
    # Verifica os robôs não satisfeitos e tenta movê-los
    for robo_val in sorted([item for sublist in estado_inicial for item in sublist if item != 0]):
        if encontrar_posicao(robo_val, estado_atual_normalizado) != encontrar_posicao(robo_val, objetivo_normalizado):
            robos_nao_satisfeitos.append(robo_val)

    for robo in robos_nao_satisfeitos:
        estado, log_texto, restricoes = tentar_mover(estado, robo, objetivo_normalizado, restricoes)
        if log_texto:
            print(" - ".join([" ".join(map(str, row)) for row in [[val for val in r if val != 0] for r in estado]]))
            print(log_texto)
            desenhar_estado(tuple(tuple(row) for row in estado), titulo=f'Passo {passo}', descricao=log_texto)
            houve_movimento = True
            break

    # Caso nenhum robô se mova
    if not houve_movimento:
        print("\nImpasse detectado. Nenhum robô não satisfeito conseguiu se mover.")
        break
    if passo > 500:
        print("\nLimite máximo de passos atingido. A simulação será encerrada.")
        break

    time.sleep(0.1)  # Pausa entre os passos

# Resultado da simulação
if normalize_state(estado) == objetivo_normalizado:
    print("\nObjetivo final alcançado!")
    desenhar_estado(normalize_state(estado), titulo="Objetivo Final Alcançado!", descricao="Todos os robôs estão satisfeitos.")
else:
    print("\nSimulação encerrada sem alcançar o objetivo.")
