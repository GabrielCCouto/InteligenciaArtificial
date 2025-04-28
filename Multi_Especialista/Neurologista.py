import json
import os
import shutil
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class Neurologista:
    def __init__(self, nome_especialista="Neurologista"):
        self.nome = nome_especialista
        self.max_enxaqueca = 2
        self.max_parkinson = 2
        self.modelo_tumor = load_model("modelo_tumor_cerebral.h5")

    def diagnosticar_exame_imagem(self, nome_arquivo):
        caminho_imagem = os.path.join("Exames", nome_arquivo)
        if not os.path.exists(caminho_imagem):
            return "Exame não encontrado"

        try:
            img = image.load_img(caminho_imagem, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            resultado = self.modelo_tumor.predict(img_array)[0][0]
            if resultado > 0.5:
                return "Tumor cerebral detectado"
            else:
                return "Sem sinais de tumor cerebral"
        except Exception as e:
            return f"Erro ao processar o exame: {str(e)}"

    def diagnosticar(self, ficha):
        score_enxaqueca = 0
        score_parkinson = 0
        exame_recomendado = None
        sintomas = ficha.get("sintomas", {})

        if "Dor" in sintomas:
            for dor in sintomas["Dor"]:
                if dor.get("dor_na_cabeca", False):
                    score_enxaqueca += 1
                    if 8 <= dor.get("intensidade_dor_na_cabeca", 0) <= 10:
                        exame_recomendado = "tomografia ou encefalograma"

        if "Mal Estar" in sintomas:
            for mal in sintomas["Mal Estar"]:
                if mal.get("tontura", False):
                    score_enxaqueca += 1
                if mal.get("tremores", False):
                    score_parkinson += 1
                if mal.get("movimento_involuntario", False):
                    score_parkinson += 1

        porcentagem_enxaqueca = (score_enxaqueca / self.max_enxaqueca) * 100 if self.max_enxaqueca else 0
        porcentagem_parkinson = (score_parkinson / self.max_parkinson) * 100 if self.max_parkinson else 0

        diagnosticos = []
        if score_enxaqueca > 0:
            diagnosticos.append(f"Enxaqueca ({porcentagem_enxaqueca:.1f}% de chance)")
        if score_parkinson > 0:
            diagnosticos.append(f"Parkinson ({porcentagem_parkinson:.1f}% de chance)")

        return ", ".join(diagnosticos) if diagnosticos else "", exame_recomendado

    def processar_fichas(self):
        pasta_fichas = "QuadroDeFichas"
        pasta_atendidos = "PacientesAtendidos"
        os.makedirs(pasta_atendidos, exist_ok=True)

        for nome_arquivo in os.listdir(pasta_fichas):
            if nome_arquivo.endswith(".json"):
                caminho = os.path.join(pasta_fichas, nome_arquivo)
                with open(caminho, "r", encoding="utf-8") as f:
                    ficha = json.load(f)

                if ficha.get("atendido_por") and self.nome in ficha["atendido_por"]:
                    shutil.move(caminho, os.path.join(pasta_atendidos, nome_arquivo))
                    continue

                # Diagnóstico baseado nos sintomas
                diagnostico, exame_recomendado = self.diagnosticar(ficha)

                # Diagnóstico baseado em exame, se houver
                if ficha.get("medico_atendente") == "Neurologista" and ficha.get("exame") == "Sim" and ficha.get("nome_exame"):
                    resultado_exame = self.diagnosticar_exame_imagem(ficha["nome_exame"])
                    ficha["diagnostico_exame_neurologico"] = resultado_exame

                if diagnostico or ficha.get("diagnostico_exame_neurologico"):
                    ficha["atendido_por"] = self.nome
                    ficha["diagnostico_neurologico"] = diagnostico
                    ficha["observacao"] = f"Paciente atendido por {self.nome}"
                    if exame_recomendado:
                        ficha["exame_recomendado_neurologico"] = exame_recomendado

                    novo_caminho = os.path.join(pasta_atendidos, nome_arquivo)
                    with open(novo_caminho, "w", encoding="utf-8") as f:
                        json.dump(ficha, f, indent=4, ensure_ascii=False)
                    os.remove(caminho)

    def processar_fichas_atendidos(self):
        pasta_atendidos = "PacientesAtendidos"
        for nome_arquivo in os.listdir(pasta_atendidos):
            if nome_arquivo.endswith(".json"):
                caminho = os.path.join(pasta_atendidos, nome_arquivo)
                with open(caminho, "r", encoding="utf-8") as f:
                    ficha = json.load(f)

                atendidos = ficha.get("atendido_por", "")
                if self.nome in atendidos:
                    continue

                diagnostico, exame_recomendado = self.diagnosticar(ficha)

                if ficha.get("medico_atendente") == "Neurologista" and ficha.get("exame") == "Sim" and ficha.get("nome_exame"):
                    resultado_exame = self.diagnosticar_exame_imagem(ficha["nome_exame"])
                    ficha["diagnostico_exame_neurologico"] = resultado_exame

                if diagnostico or ficha.get("diagnostico_exame_neurologico"):
                    if "atendido_por" in ficha and ficha["atendido_por"]:
                        ficha["atendido_por"] += f", {self.nome}"
                    else:
                        ficha["atendido_por"] = self.nome
                    ficha["diagnostico_neurologico"] = diagnostico
                    ficha["observacao"] = f"Paciente atendido por {self.nome}"
                    if exame_recomendado:
                        ficha["exame_recomendado_neurologico"] = exame_recomendado
                    with open(caminho, "w", encoding="utf-8") as f:
                        json.dump(ficha, f, indent=4, ensure_ascii=False)

    def finalizar_atendimento(self):
        origem = "PacientesAtendidos"
        destino = "PacienteTeveAlta"
        os.makedirs(destino, exist_ok=True)
        for nome_arquivo in os.listdir(origem):
            if nome_arquivo.endswith(".json"):
                shutil.move(os.path.join(origem, nome_arquivo), os.path.join(destino, nome_arquivo))

    def processar_todas_fichas(self):
        self.processar_fichas_atendidos()
        self.finalizar_atendimento()
