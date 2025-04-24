import json
import os
import shutil
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class Pneumologista:
    def __init__(self, nome_especialista="Pneumologista"):
        self.nome = nome_especialista
        self.score_influenza = 0
        self.score_asma = 0
        self.max_influenza = 2
        self.max_asma = 2
        self.modelo_pneumonia = load_model("modelo_pneumonia_torax.h5")

    def diagnosticar_exame_imagem(self, nome_arquivo):
        caminho_imagem = os.path.join("Exames", nome_arquivo)
        if not os.path.exists(caminho_imagem):
            return "Exame não encontrado"

        try:
            img = image.load_img(caminho_imagem, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            resultado = self.modelo_pneumonia.predict(img_array)[0][0]
            if resultado > 0.5:
                return "Pneumonia detectada"
            else:
                return "Sem sinais de pneumonia"
        except Exception as e:
            return f"Erro ao processar o exame: {str(e)}"

    def diagnosticar(self, ficha):
        self.score_influenza = 0
        self.score_asma = 0
        exame_recomendado = None
        sintomas = ficha.get("sintomas", {})

        if "Tosse" in sintomas:
            for tosse in sintomas["Tosse"]:
                if tosse.get("gripe_resfriado", False):
                    self.score_influenza += 1
                self.score_influenza += 1
                if tosse.get("dificuldade_respiratoria", False):
                    self.score_asma += 1

        if "Dor" in sintomas:
            for dor in sintomas["Dor"]:
                if dor.get("dor_no_peito", False):
                    self.score_asma += 1
                    if 8 <= dor.get("intensidade_dor_no_peito", 0) <= 10:
                        exame_recomendado = "Raio-X do tórax"

        porcentagem_influenza = (self.score_influenza / self.max_influenza) * 100 if self.max_influenza else 0
        porcentagem_asma = (self.score_asma / self.max_asma) * 100 if self.max_asma else 0

        diagnosticos = []
        if self.score_influenza > 0:
            diagnosticos.append(f"Influenza ({porcentagem_influenza:.1f}% de chance)")
        if self.score_asma > 0:
            diagnosticos.append(f"Asma ({porcentagem_asma:.1f}% de chance)")

        diagnostico = ", ".join(diagnosticos) if diagnosticos else ""
        return diagnostico, exame_recomendado

    def adicionar_observacao_pneumonia(self, ficha):
        observacao_pneumonia = (
            "Pneumonia detectada: iniciar tratamento com antibióticos de amplo espectro "
            "(ex: amoxicilina), repouso, hidratação e monitoramento. Avaliação médica em 48h recomendada."
        )
        if "observacao" in ficha and ficha["observacao"]:
            ficha["observacao"] += f" | {observacao_pneumonia}"
        else:
            ficha["observacao"] = observacao_pneumonia

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

                diagnostico, exame_recomendado = self.diagnosticar(ficha)

                resultado_exame = None
                if ficha.get("medico_atendente") == "Pneumologista" and ficha.get("exame") == "Sim" and ficha.get("nome_exame"):
                    resultado_exame = self.diagnosticar_exame_imagem(ficha["nome_exame"])
                    ficha["diagnostico_exame_pneumo"] = resultado_exame

                if diagnostico or resultado_exame:
                    ficha["atendido_por"] = self.nome
                    ficha["diagnostico_pneumo"] = diagnostico
                    if exame_recomendado:
                        ficha["exame_recomendado_pneumo"] = exame_recomendado

                    if resultado_exame == "Pneumonia detectada":
                        self.adicionar_observacao_pneumonia(ficha)
                    else:
                        ficha["observacao"] = f"Paciente atendido por {self.nome}"

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

                if ficha.get("atendido_por") and self.nome in ficha["atendido_por"]:
                    continue

                diagnostico, exame_recomendado = self.diagnosticar(ficha)

                resultado_exame = None
                if ficha.get("medico_atendente") == "Pneumologista" and ficha.get("exame") == "Sim" and ficha.get("nome_exame"):
                    resultado_exame = self.diagnosticar_exame_imagem(ficha["nome_exame"])
                    ficha["diagnostico_exame_pneumo"] = resultado_exame

                if diagnostico or resultado_exame:
                    if "atendido_por" in ficha and ficha["atendido_por"]:
                        ficha["atendido_por"] += f", {self.nome}"
                    else:
                        ficha["atendido_por"] = self.nome

                    ficha["diagnostico_pneumo"] = diagnostico
                    if exame_recomendado:
                        ficha["exame_recomendado_pneumo"] = exame_recomendado

                    if resultado_exame == "Pneumonia detectada":
                        self.adicionar_observacao_pneumonia(ficha)
                    else:
                        ficha["observacao"] = f"Paciente atendido por {self.nome}"

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
