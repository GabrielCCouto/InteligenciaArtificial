import json
import os
import shutil

class Otorrinolaringologista:
    """
    Especialista Otorrinolaringologista utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Infecção no ouvido: associada à dor no ouvido e perda auditiva.
      - Faringite: associada à dor na garganta e dificuldade para engolir.
    O especialista avalia também a intensidade dos sintomas para recomendar exames,
    como audiometria ou tomografia (para dor no ouvido) e endoscopia (para dor na garganta).
    """
    def __init__(self, nome_especialista="Otorrinolaringologista"):
        self.nome = nome_especialista
        self.score_infeccao_ouvido = 0
        self.score_faringite = 0
        self.max_infeccao_ouvido = 2
        self.max_faringite = 2

    def diagnosticar(self, ficha):
        """
        Processa a ficha do paciente e retorna o diagnóstico (possivelmente combinando
        Infecção no ouvido e Faringite) e, se aplicável, a recomendação de exame.
        """
        self.score_infeccao_ouvido = 0
        self.score_faringite = 0
        exame_recomendado = None
        sintomas = ficha.get("sintomas", {})

        # Processa dados de "Dor" para Infecção no ouvido
        if "Dor" in sintomas:
            for dor in sintomas["Dor"]:
                if dor.get("dor_no_ouvido", False):
                    self.score_infeccao_ouvido += 1
                    if dor.get("perda_auditiva", False):
                        self.score_infeccao_ouvido += 1
                    if 8 <= dor.get("intensidade_dor_no_ouvido", 0) <= 10:
                        exame_recomendado = "Audiometria ou tomografia do ouvido"
                # Processa dados de "Dor" para Faringite
                if dor.get("dor_na_garganta", False):
                    self.score_faringite += 1
                    if dor.get("dificuldade_engolir", False):
                        self.score_faringite += 1
                    if 8 <= dor.get("intensidade_dor_na_garganta", 0) <= 10:
                        exame_recomendado = "endoscopia ou exame de imagem da garganta"

        porcentagem_ouvido = (self.score_infeccao_ouvido / self.max_infeccao_ouvido) * 100 if self.max_infeccao_ouvido else 0
        porcentagem_faringite = (self.score_faringite / self.max_faringite) * 100 if self.max_faringite else 0

        diagnósticos = []
        if self.score_infeccao_ouvido > 0:
            diagnósticos.append(f"Infecção no ouvido ({porcentagem_ouvido:.1f}% de chance)")
        if self.score_faringite > 0:
            diagnósticos.append(f"Faringite ({porcentagem_faringite:.1f}% de chance)")
        if diagnósticos:
            diagnostico = ", ".join(diagnósticos)
        else:
            diagnostico = "Sem diagnóstico otorrinolaringológico suficiente"

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
                if self.score_infeccao_ouvido > 0 or self.score_faringite > 0:
                    ficha["atendido_por"] = self.nome
                    ficha["diagnostico_otorrino"] = diagnostico
                    ficha["observacao"] = f"Paciente atendido por {self.nome}"
                    if exame_recomendado:
                        ficha["exame_recomendado_otorrino"] = exame_recomendado
                    novo_caminho = os.path.join(pasta_atendidos, nome_arquivo)
                    with open(novo_caminho, "w", encoding="utf-8") as f:
                        json.dump(ficha, f, indent=4, ensure_ascii=False)
                    os.remove(caminho)
                #     print(f"Paciente {ficha['nome']} atendido por {self.nome}.")
                # else:
                #     print(f"Paciente {ficha['nome']} não apresenta sinais suficientes para atendimento por {self.nome}.")

    def processar_fichas_atendidos(self):
        """
        Realiza a segunda verificação: lê cada ficha na pasta 'PacientesAtendidos' e, se o
        paciente ainda não tiver sido atendido por este especialista, processa a ficha.
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
                if self.score_infeccao_ouvido > 0 or self.score_faringite > 0:
                    if "atendido_por" in ficha and ficha["atendido_por"]:
                        ficha["atendido_por"] += f", {self.nome}"
                    else:
                        ficha["atendido_por"] = self.nome
                    ficha["diagnostico_otorrino"] = diagnostico
                    ficha["observacao"] = f"Paciente atendido por {self.nome}"
                    if exame_recomendado:
                        ficha["exame_recomendado_otorrino"] = exame_recomendado
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
