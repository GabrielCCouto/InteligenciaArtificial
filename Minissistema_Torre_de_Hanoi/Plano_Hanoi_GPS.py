from gps import gps
from itertools import product
import pyvis
from pyvis.network import Network

def gerar_problema_hanoi(N):
    hastes = ["A", "B", "C"]
    estado_inicial = [f"config:{'A'*N}"]
    estado_meta    = [f"config:{'C'*N}"]
    operadores = []

    # Gera todos os estados possíveis e todos os movimentos legais
    for cfg in [''.join(p) for p in product(hastes, repeat=N)]:
        for origem in hastes:
            discos_na_origem = [i for i, peg in enumerate(cfg) if peg == origem]
            if not discos_na_origem:
                continue
            topo = max(discos_na_origem)

            for destino in hastes:
                if destino == origem:
                    continue
                discos_no_dest = [i for i, peg in enumerate(cfg) if peg == destino]
                # só move se destino vazio ou topo do destino for maior
                if discos_no_dest and max(discos_no_dest) >= topo:
                    continue

                novo_cfg = list(cfg)
                novo_cfg[topo] = destino
                novo_cfg = ''.join(novo_cfg)

                operadores.append({
                    "action": f"mover disco {N-topo} de {origem} para {destino}",
                    "preconds": [f"config:{cfg}"],
                    "add":      [f"config:{novo_cfg}"],
                    "delete":   [f"config:{cfg}"]
                })

    return {"init": estado_inicial, "finish": estado_meta, "ops": operadores}


def main():
    N = 3  # ← basta mudar este valor para 1, 2, 3, 4, 5…
    problema = gerar_problema_hanoi(N)
    plano = gps(problema["init"], problema["finish"], problema["ops"], msg="Você deve: ")

    if plano:
        for i, passo in enumerate(plano, start=1):
            print(f"{i} - {passo}")
    elif problema["init"] == problema["finish"]:
        print("Problema resolvido!")
    else:
        print("Nenhum plano encontrado")

    # Create a new network object
    network = Network(height='900px', width='100%', directed=True)

    #network.add_node(0, label=problema["init"][0])

    finite_states = list(enumerate(set(map(lambda x: x["preconds"][0], problema["ops"]))))

    solution_path = []
    previous = problema["init"][0]
    for i in map(lambda a: a[11:], plano):
        step = list(filter(lambda a: a["preconds"][0] == previous and a["action"] == i, problema["ops"]))[0]
        solution_path.append(step)
        previous = step["add"][0]

    solution_states = problema["init"] + list(map(lambda a: a["add"][0], solution_path))


    for i, state in finite_states:
        if state in solution_states:
            network.add_node(i, label=f"{i} - {state}", shape='box', color='red')
        else:
            network.add_node(i, label=f"{i} - {state}", shape='box', color='gray')

    for state in problema["ops"]:
        precond = state["preconds"][0]
        add = state["add"][0]
        source = list(filter(lambda a: a[1] == precond , finite_states))[0]
        destination = list(filter(lambda a: a[1] == add , finite_states))[0]

        if state in solution_path:
            network.add_edge(source[0], destination[0], color='red')  # , label=f"{state["action"]}")
        else:
            network.add_edge(source[0], destination[0], color='gray')#, label=f"{state["action"]}")

    network.show('Graph.html', notebook=False)

if __name__ == "__main__":
    main()
