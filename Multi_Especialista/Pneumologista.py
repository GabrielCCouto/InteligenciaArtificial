import json
import os
import shutil

class Pneumologista:
    """
    Especialista Pneumologista utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Influenza: associada à presença de tosse e histórico de gripe/resfriado.
      - Asma: associada à dificuldade respiratória e dor no peito.
    Se a intensidade da dor no peito for entre 8 e 10, recomenda a realização de um exame (Raio-X do tórax).
    """
    def __init__(self, nome_especialista="Pneumologista"):
        self.nome = nome_especialista
        self.score_influenza = 0
        self.score_asma = 0
        self.max_influenza = 2
        self.max_asma = 2

    def diagnosticar(self, ficha):
        """
        Processa os dados da ficha do paciente e retorna o diagnóstico (possivelmente
        combinando Influenza e Asma) e, se aplicável, a recomendação de exame.
        """
        self.score_influenza = 0
        self.score_asma = 0
        exame_recomendado = None
        sintomas = ficha.get("sintomas", {})

        # Processa dados de "Tosse" para Influenza
        if "Tosse" in sintomas:
            for tosse in sintomas["Tosse"]:
                if tosse.get("gripe_resfriado", False):
                    self.score_influenza += 1
                self.score_influenza += 1  # Soma ponto pela presença de tosse
                if tosse.get("dificuldade_respiratoria", False):
                    self.score_asma += 1

        # Processa dados de "Dor" para dor no peito (Asma)
        if "Dor" in sintomas:
            for dor in sintomas["Dor"]:
                if dor.get("dor_no_peito", False):
                    self.score_asma += 1
                    if 8 <= dor.get("intensidade_dor_no_peito", 0) <= 10:
                        exame_recomendado = "Raio-X do tórax"

        porcentagem_influenza = (self.score_influenza / self.max_influenza) * 100 if self.max_influenza else 0
        porcentagem_asma = (self.score_asma / self.max_asma) * 100 if self.max_asma else 0

        diagnósticos = []
        if self.score_influenza > 0:
            diagnósticos.append(f"Influenza ({porcentagem_influenza:.1f}% de chance)")
        if self.score_asma > 0:
            diagnósticos.append(f"Asma ({porcentagem_asma:.1f}% de chance)")

        if diagnósticos:
            diagnostico = ", ".join(diagnósticos)
        else:
            diagnostico = "Sem diagnóstico pneumológico suficiente"

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

                # Se o paciente já foi atendido por este especialista, move o arquivo e continua
                if ficha.get("atendido_por") and self.nome in ficha["atendido_por"]:
                    shutil.move(caminho, os.path.join(pasta_atendidos, nome_arquivo))
                    continue

                diagnostico, exame_recomendado = self.diagnosticar(ficha)
                if self.score_influenza > 0 or self.score_asma > 0:
                    ficha["atendido_por"] = self.nome
                    ficha["diagnostico_pneumo"] = diagnostico
                    ficha["observacao"] = f"Paciente atendido por {self.nome}"
                    if exame_recomendado:
                        ficha["exame_recomendado_pneumo"] = exame_recomendado
                    novo_caminho = os.path.join(pasta_atendidos, nome_arquivo)
                    with open(novo_caminho, "w", encoding="utf-8") as f:
                        json.dump(ficha, f, indent=4, ensure_ascii=False)
                    os.remove(caminho)
                #     print(f"Paciente {ficha['nome']} atendido por {self.nome}.")
                # else:
                #     print(f"Paciente {ficha['nome']} não apresenta sinais suficientes para atendimento por {self.nome}.")

    def processar_fichas_atendidos(self):
        """
        Realiza a segunda verificação: lê cada ficha na pasta 'PacientesAtendidos'
        e, se o paciente ainda não tiver sido atendido por este especialista, processa a ficha.
        """
        pasta_atendidos = "PacientesAtendidos"
        for nome_arquivo in os.listdir(pasta_atendidos):
            if nome_arquivo.endswith(".json"):
                caminho = os.path.join(pasta_atendidos, nome_arquivo)
                with open(caminho, "r", encoding="utf-8") as f:
                    ficha = json.load(f)
                if ficha.get("atendido_por") and self.nome in ficha["atendido_por"]:
                    continue
                diagnostico, exame_recomendado = self.diagnosticar(ficha)
                if self.score_influenza > 0 or self.score_asma > 0:
                    if "atendido_por" in ficha and ficha["atendido_por"]:
                        ficha["atendido_por"] += f", {self.nome}"
                    else:
                        ficha["atendido_por"] = self.nome
                    ficha["diagnostico_pneumo"] = diagnostico
                    ficha["observacao"] = f"Paciente atendido por {self.nome}"
                    if exame_recomendado:
                        ficha["exame_recomendado_pneumo"] = exame_recomendado
                    with open(caminho, "w", encoding="utf-8") as f:
                        json.dump(ficha, f, indent=4, ensure_ascii=False)
                #     print(f"(Segunda verificação) Paciente {ficha['nome']} atendido por {self.nome}.")
                # else:
                #     print(f"(Segunda verificação) Paciente {ficha['nome']} não apresenta sinais para atendimento por {self.nome}.")

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
