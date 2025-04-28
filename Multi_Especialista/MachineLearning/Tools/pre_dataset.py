import os
import shutil
import pandas as pd

def preparar_dataset(csv_path, imagens_dir, destino_dir, extensao=".jpg"):
    df = pd.read_csv(csv_path)

    tumor_dir = os.path.join(destino_dir, "tumor")
    non_tumor_dir = os.path.join(destino_dir, "non_tumor")
    os.makedirs(tumor_dir, exist_ok=True)
    os.makedirs(non_tumor_dir, exist_ok=True)

    count_tumor = 0
    count_nontumor = 0

    for _, row in df.iterrows():
        nome_base = str(row['Image']).strip()
        classe = row['Class']

        nome_imagem = nome_base if nome_base.lower().endswith(extensao) else f"{nome_base}{extensao}"
        caminho_origem = os.path.join(imagens_dir, nome_imagem)

        if not os.path.exists(caminho_origem):
            print(f"[AVISO] Imagem não encontrada: {caminho_origem}")
            continue

        if classe == 1:
            destino = os.path.join(tumor_dir, nome_imagem)
            count_tumor += 1
        else:
            destino = os.path.join(non_tumor_dir, nome_imagem)
            count_nontumor += 1

        shutil.copy2(caminho_origem, destino)

    print(f"\n✅ Preparação concluída:")
    print(f"  -> Tumor: {count_tumor} imagens")
    print(f"  -> Não Tumor: {count_nontumor} imagens")
    print(f"\nImagens organizadas em: {destino_dir}")

preparar_dataset("./Brain Tumor.csv", "./Brain_Tumor", "Brain_Tumor_Organizado")
