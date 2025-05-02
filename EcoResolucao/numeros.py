import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

# --- CONFIGURAÇÃO DO PROBLEMA ---

# Estado inicial (primeira imagem)
# [9, 7, 1]
# [7, 2, 8]
# [3, 5, 4]
# (se houver duplicatas, ajuste ao seu caso real)
inicial = [
    [9, 7, 1],
    [7, 2, 8],
    [3, 5, 4],
]

# Estado desejado (segunda imagem)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
meta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

N = 3            # dimensão da grade
PASSOS_MAX = 50  # limite de iterações

# --- DEFINIÇÃO DE AMBIENTE E AGENTES ---

class Ambiente:
    def __init__(self):
        self.ocupado = {}  # (x,y) -> agente.numero

    def esta_livre(self, pos):
        return pos not in self.ocupado

    def atualizar(self, agente, nova_pos):
        # limpa posição antiga
        self.ocupado = {p: n for p, n in self.ocupado.items() if n != agente.numero}
        # marca nova
        self.ocupado[nova_pos] = agente.numero

class Agente:
    def __init__(self, numero, pos_inicial, pos_meta, cor):
        self.numero    = numero
        self.posicao   = pos_inicial
        self.meta      = pos_meta
        self.cor       = cor
        self.log       = []

    def decidir(self):
        x, y    = self.posicao
        gx, gy  = self.meta
        dx = 1 if gx > x else -1 if gx < x else 0
        dy = 1 if gy > y else -1 if gy < y else 0
        return (x+dx, y+dy)

    def alternativas(self):
        x, y = self.posicao
        viz = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        return [(i,j) for (i,j) in viz if 0<=i<N and 0<=j<N]

    def mover(self, nova, amb):
        self.log.append(f"{self.numero}: {self.posicao} → {nova}")
        self.posicao = nova
        amb.atualizar(self, nova)

    def chegou(self):
        return self.posicao == self.meta

# --- MONTAGEM DOS AGENTES ---

# cores para distinguir (pode repetir se quiser)
paleta = ["C0","C1","C2","C3","C4","C5","C6","C7","C8"]

amb = Ambiente()
agentes = {}

# cria agentes lendo o grid inicial e meta
for i in range(N):
    for j in range(N):
        num_ini = inicial[j][i]
        # busca onde esse número aparece na meta
        for jm in range(N):
            for im in range(N):
                if meta[jm][im] == num_ini:
                    pos_m = (im, jm)
        ag = Agente(num_ini, (i,j), pos_m, paleta[num_ini%9])
        agentes[num_ini] = ag
        amb.atualizar(ag, (i,j))

# --- FUNÇÃO DE DESENHO PASSO A PASSO ---

def desenhar(passo, conflitos):
    fig, ax = plt.subplots(figsize=(4,4))
    ax.set_xlim(-0.5, N-0.5); ax.set_ylim(-0.5, N-0.5)
    ax.set_xticks(range(N)); ax.set_yticks(range(N))
    ax.grid(True)
    ax.set_title(f"Passo {passo}")

    # desenha alvo
    for ag in agentes.values():
        gx, gy = ag.meta
        circ = patches.Circle((gx,gy), 0.25, edgecolor=ag.cor, facecolor='none', linestyle='--')
        ax.add_patch(circ)
        ax.text(gx,gy+0.3, f"{ag.numero}", color=ag.cor, ha='center')

    # desenha agentes
    for ag in agentes.values():
        x,y = ag.posicao
        sq = patches.Rectangle((x-0.4,y-0.4), 0.8,0.8, color=ag.cor)
        ax.add_patch(sq)
        ax.text(x,y, f"{ag.numero}", color='white', ha='center', va='center')

    # marca conflitos
    for pos in conflitos:
        cx, cy = pos
        ax.add_patch(patches.Circle((cx,cy), 0.15, color='red'))

    plt.gca().invert_yaxis()
    plt.show()

# --- LOOP PRINCIPAL ECO‐RESOLUÇÃO ---

for passo in range(PASSOS_MAX):
    print(f"\n=== PASSO {passo} ===")

    # verifica se todos chegaram
    if all(ag.chegou() for ag in agentes.values()):
        print("Todos os agentes chegaram às suas metas!")
        break

    desejos = {}
    for ag in agentes.values():
        if not ag.chegou():
            desejos[ag.numero] = ag.decidir()

    posicoes = list(desejos.values())
    conflitos = [p for p in posicoes if posicoes.count(p) > 1]

    # executa movimentos
    for ag in agentes.values():
        if ag.chegou():
            ag.log.append(f"{ag.numero}: já em {ag.posicao}")
            continue

        alvo = desejos[ag.numero]
        if (alvo in conflitos) or (not amb.esta_livre(alvo)):
            # resolve conflito local
            for alt in random.sample(ag.alternativas(), k=len(ag.alternativas())):
                if amb.esta_livre(alt):
                    ag.mover(alt, amb)
                    break
            else:
                ag.log.append(f"{ag.numero}: sem movimento possível")
        else:
            ag.mover(alvo, amb)

    desenhar(passo, conflitos)

# --- LOG FINAL ---

print("\n=== LOGS FINAIS ===")
for ag in sorted(agentes.values(), key=lambda a: a.numero):
    print(f"\nAgente {ag.numero}:")
    for l in ag.log:
        print("   ", l)
