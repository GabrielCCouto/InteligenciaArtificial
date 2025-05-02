# drawing.py

import matplotlib.pyplot as plt

# Função para desenhar o estado atual do ambiente
def desenhar_estado(estado_normalizado, titulo="Estado", descricao=""):
    n_cols = len(estado_normalizado[0])
    n_rows = len(estado_normalizado)

    fig, ax = plt.subplots(figsize=(n_cols * 4, 4))
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.axis('off')

    cores = {
        1: 'lightskyblue',
        2: 'lightgreen',
        3: 'salmon',
        4: 'khaki',
        5: 'gold'
    }

    # Desenha os robôs no gráfico
    for r_idx, row in enumerate(estado_normalizado):
        for c_idx, robo in enumerate(row):
            if robo != 0:
                ax.add_patch(plt.Rectangle((c_idx, n_rows - 1 - r_idx), 1, 0.8, edgecolor='black', facecolor=cores.get(robo, 'lightgray')))
                ax.text(c_idx + 0.5, n_rows - 0.6 - r_idx, f"Robô {robo}", ha='center', va='center', fontsize=14, weight='bold')

    plt.title(f"{titulo}\n{descricao}", fontsize=14)
    plt.tight_layout()
    plt.show()
