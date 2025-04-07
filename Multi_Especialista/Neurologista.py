import json
import os
import shutil

class Neurologista:
    """
    Especialista Neurologista utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Enxaqueca: associada à dor de cabeça e tontura.
      - Parkinson: associada a tremores e movimentos involuntários.
    Se a intensidade da dor de cabeça for entre 8 e 10, recomenda a realização de exames.
    """
    def __init__(self, nome_especialista="Neurologista"):
        self.nome = nome_especialista
        self.max_enxaqueca = 2
        self.max_parkinson = 2

    def diagnosticar(self, ficha):
        score_enxaqueca = 0
        score_parkinson = 0
        exame_recomendado = None
        sintomas = ficha.get("sintomas", {})

        # Verifica "Dor" para dor de cabeça
        if "Dor" in sintomas:
            for dor in sintomas["Dor"]:
                if dor.get("dor_na_cabeca", False):
                    score_enxaqueca += 1
                    if 8 <= dor.get("intensidade_dor_na_cabeca", 0) <= 10:
                        exame_recomendado = "tomografia ou encefalograma"
        # Verifica "Mal Estar" para sinais neurológicos
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

        diagnósticos = []
        if score_enxaqueca > 0:
            diagnósticos.append(f"Enxaqueca ({porcentagem_enxaqueca:.1f}% de chance)")
        if score_parkinson > 0:
            diagnósticos.append(f"Parkinson ({porcentagem_parkinson:.1f}% de chance)")
        if diagnósticos:
            diagnostico = ", ".join(diagnósticos)
        else:
            diagnostico = ""
        return diagnostico, exame_recomendado

    def processar_fichas(self):
        """
        Processa os pacientes da pasta 'QuadroDeFichas'. Se os pacientes apresentarem sinais
        compatíveis, atualiza a ficha com o diagnóstico e informações do atendimento, movendo-a para
        a pasta 'PacientesAtendidos'.
        """
        pasta_fichas = "QuadroDeFichas"
        pasta_atendidos = "PacientesAtendidos"
        if not os.path.exists(pasta_atendidos):
            os.makedirs(pasta_atendidos)

        for nome_arquivo in os.listdir(pasta_fichas):
            if nome_arquivo.endswith(".json"):
                caminho = os.path.join(pasta_fichas, nome_arquivo)
                with open(caminho, "r", encoding="utf-8") as f:
                    ficha = json.load(f)

                # Se o paciente já foi atendido por esse especialista, move o arquivo e continua
                if ficha.get("atendido_por") and self.nome in ficha["atendido_por"]:
                    shutil.move(caminho, os.path.join(pasta_atendidos, nome_arquivo))
                    continue

                diagnostico, exame_recomendado = self.diagnosticar(ficha)
                if diagnostico:  # Se houver algum diagnóstico
                    ficha["atendido_por"] = self.nome
                    ficha["diagnostico_neurologico"] = diagnostico
                    ficha["observacao"] = f"Paciente atendido por {self.nome}"
                    if exame_recomendado:
                        ficha["exame_recomendado_neurologico"] = exame_recomendado
                    novo_caminho = os.path.join(pasta_atendidos, nome_arquivo)
                    with open(novo_caminho, "w", encoding="utf-8") as f:
                        json.dump(ficha, f, indent=4, ensure_ascii=False)
                    os.remove(caminho)
                #     print(f"Paciente {ficha['nome']} atendido por {self.nome}.")
                # else:
                #     print(f"Paciente {ficha['nome']} não apresenta sinais suficientes para atendimento por {self.nome}.")

    def processar_fichas_atendidos(self):
        """
        Realiza a segunda verificação: lê cada ficha em 'PacientesAtendidos' e, se o
        paciente não tiver sido atendido por esse especialista, verifica se os sintomas
        indicam que ele deve ser atendido. Se sim, atualiza a ficha com o diagnóstico.
        """
        pasta_atendidos = "PacientesAtendidos"
        for nome_arquivo in os.listdir(pasta_atendidos):
            if nome_arquivo.endswith(".json"):
                caminho = os.path.join(pasta_atendidos, nome_arquivo)
                with open(caminho, "r", encoding="utf-8") as f:
                    ficha = json.load(f)
                # Verifica se o paciente já foi atendido por esse especialista
                atendidos = ficha.get("atendido_por", "")
                if self.nome in atendidos:
                    continue  # Já atendido, passa para o próximo

                diagnostico, exame_recomendado = self.diagnosticar(ficha)
                if diagnostico:
                    # Atualiza o campo "atendido_por": se já existir, adiciona; senão, cria
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
                #     print(f"(Segunda verificação) Paciente {ficha['nome']} atendido por {self.nome}.")
                # else:
                #     print(f"(Segunda verificação) Paciente {ficha['nome']} não necessita de atendimento por {self.nome}.")

    def finalizar_atendimento(self):
        """
        Move todos os arquivos da pasta 'PacientesAtendidos' para 'PacienteTeveAlta'.
        """
        origem = "PacientesAtendidos"
        destino = "PacienteTeveAlta"
        if not os.path.exists(destino):
            os.makedirs(destino)
        for nome_arquivo in os.listdir(origem):
            if nome_arquivo.endswith(".json"):
                shutil.move(os.path.join(origem, nome_arquivo), os.path.join(destino, nome_arquivo))
        # print("\nTodos os atendimentos foram finalizados e as fichas foram movidas para 'PacienteTeveAlta'.")

    def processar_todas_fichas(self):
        """
        Executa a segunda verificação dos pacientes e, em seguida, finaliza o atendimento,
        movendo os arquivos para 'PacienteTeveAlta'.
        """
        self.processar_fichas_atendidos()
        self.finalizar_atendimento()
