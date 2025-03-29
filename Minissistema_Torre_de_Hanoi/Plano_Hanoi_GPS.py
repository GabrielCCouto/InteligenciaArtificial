from gps import gps
from itertools import product

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
                    "action": f"mover disco {N-topo} \tde {origem} para {destino}",
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

if __name__ == "__main__":
    main()
