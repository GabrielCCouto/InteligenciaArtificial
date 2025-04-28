import json
import os
import shutil

class Gastroenterologista:
    """
    Especialista Gastroenterologista utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Refluxo gastroesofágico: associado a refluxo e enjoo.
      - Intoxicação alimentar: associado a dor abdominal e diarreia.
    O diagnóstico é calculado em porcentagem com base em pontuações definidas.
    Se os sintomas forem intensos (pontuação máxima atingida), recomenda exames complementares.
    """
    def __init__(self, nome_especialista="Gastroenterologista"):
        self.nome = nome_especialista
        self.score_refluxo = 0
        self.score_intoxicacao = 0
        self.max_refluxo = 2
        self.max_intoxicacao = 2

    def diagnosticar(self, ficha):
        """
        Processa os dados da ficha (dicionário) e retorna o diagnóstico e, se aplicável,
        a recomendação de exame.
        """
        self.score_refluxo = 0
        self.score_intoxicacao = 0
        exame_recomendado = None
        sintomas = ficha.get("sintomas", {})

        # Processa os dados de "Mal Estar" para identificar sintomas
        for mal in sintomas.get("Mal Estar", []):
            if mal.get("refluxo", False):
                self.score_refluxo += 1
            if mal.get("enjoo", False):
                self.score_refluxo += 1
            if mal.get("dor_abdominal", False):
                self.score_intoxicacao += 1
            if mal.get("diarreia", False):
                self.score_intoxicacao += 1

        porcentagem_refluxo = (self.score_refluxo / self.max_refluxo) * 100 if self.max_refluxo else 0
        porcentagem_intoxicacao = (self.score_intoxicacao / self.max_intoxicacao) * 100 if self.max_intoxicacao else 0

        diagnósticos = []
        if self.score_refluxo > 0:
            diagnósticos.append(f"Refluxo gastroesofágico ({porcentagem_refluxo:.1f}% de chance)")
            if self.score_refluxo == self.max_refluxo:
                exame_recomendado = "endoscopia"
        if self.score_intoxicacao > 0:
            diagnósticos.append(f"Intoxicação alimentar ({porcentagem_intoxicacao:.1f}% de chance)")
            if self.score_intoxicacao == self.max_intoxicacao:
                exame_recomendado = "exame de fezes"

        if diagnósticos:
            diagnostico = ", ".join(diagnósticos)
        else:
            diagnostico = "Sem diagnóstico gastrointestinal suficiente"

        return diagnostico, exame_recomendado

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
                # Se o paciente já foi atendido por este especialista, pula para o próximo
                if ficha.get("atendido_por") and self.nome in ficha["atendido_por"]:
                    continue
                diagnostico, exame_recomendado = self.diagnosticar(ficha)
                if self.score_refluxo > 0 or self.score_intoxicacao > 0:
                    # Atualiza o campo "atendido_por": adiciona o nome do especialista
                    if "atendido_por" in ficha and ficha["atendido_por"]:
                        ficha["atendido_por"] += f", {self.nome}"
                    else:
                        ficha["atendido_por"] = self.nome
                    ficha["diagnostico_gastro"] = diagnostico
                    ficha["observacao"] = f"Paciente atendido por {self.nome}"
                    if exame_recomendado:
                        ficha["exame_recomendado_gastro"] = exame_recomendado
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
        print("\nTodos os atendimentos foram finalizados e as fichas foram movidas para 'PacienteTeveAlta'.")

    def processar_todas_fichas(self):
        """
        Executa a segunda verificação dos pacientes e, em seguida, finaliza o atendimento,
        movendo os arquivos para 'PacienteTeveAlta'.
        """
        self.processar_fichas_atendidos()
        self.finalizar_atendimento()
