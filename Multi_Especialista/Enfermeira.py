import json
import os
from Sintomas import Dor, Tosse, MalEstar

class Enfermeira:
    def __init__(self):
        self.nome = None              # Nome do paciente
        self.estado = None            # "Bem", "Razoável", "Mal"
        self.consulta = None          # "Primeira consulta" ou "Retorno"
        self.exame = None             # "Sim" ou "Não" (apenas para retorno)
        self.medico_atendente = None  # Médico que atendeu, para pacientes de retorno
        self.opcoes_sintomas = ["Dor", "Tosse", "Mal Estar"]
        self.dados_sintomas = {"Dor": [], "Tosse": [], "Mal Estar": []}

    def perguntar_com_opcoes(self, pergunta, opcoes):
        print(pergunta)
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")
        while True:
            escolha = input(f"Escolha a opção (1-{len(opcoes)}): ").strip()
            if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
                return int(escolha)
            else:
                print("Opção inválida. Tente novamente.")

    def iniciar_triagem(self):
        print("\n=== Início da Triagem ===")
        self.nome = input("Qual o seu nome? ").strip()

        consulta_opcoes = ["Primeira consulta", "Retorno"]
        escolha = self.perguntar_com_opcoes("É sua primeira consulta ou é retorno?", consulta_opcoes)
        self.consulta = consulta_opcoes[escolha - 1]

        if self.consulta == "Retorno":
            medico_opcoes = ["Pneumologista", "Neurologista", "Gastroenterologista", "Otorrinolaringologista"]
            escolha_medico = self.perguntar_com_opcoes("Qual foi o médico que atendeu da última vez?", medico_opcoes)
            self.medico_atendente = medico_opcoes[escolha_medico - 1]

            opcoes_sim_nao = ["Sim", "Não"]
            resposta = self.perguntar_com_opcoes("Você trouxe o exame solicitado?", opcoes_sim_nao)
            self.exame = opcoes_sim_nao[resposta - 1]

            if self.exame == "Não":
                print("\nVocê precisa trazer o exame solicitado para dar continuidade no atendimento.")
                self.salvar_ficha()
                return
            else:
                self.nome_exame = input("Digite o nome do arquivo do exame (ex: exame_001.jpg): ").strip()

            print(f"\nExame recebido. Encaminhando ficha para o médico {self.medico_atendente}.")
            self.salvar_ficha()
            return

        estado_opcoes = ["Bem", "Razoável", "Mal"]
        escolha = self.perguntar_com_opcoes("Como você está se sentindo hoje?", estado_opcoes)
        self.estado = estado_opcoes[escolha - 1]

        if self.estado == "Bem":
            print("\nO paciente está bem e, por ser a primeira consulta, não há o que investigar.")
            self.salvar_ficha()
            return

        continuar = True
        while continuar:
            escolha_sintoma = self.perguntar_com_opcoes("\nQual seu sintoma?", self.opcoes_sintomas)
            sintoma_selecionado = self.opcoes_sintomas[escolha_sintoma - 1]
            if sintoma_selecionado == "Dor":
                nova_dor = Dor()
                nova_dor.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Dor"].append(nova_dor)
            elif sintoma_selecionado == "Tosse":
                nova_tosse = Tosse()
                nova_tosse.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Tosse"].append(nova_tosse)
            elif sintoma_selecionado == "Mal Estar":
                novo_malestar = MalEstar()
                novo_malestar.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Mal Estar"].append(novo_malestar)

            opcoes_sim_nao = ["Sim", "Não"]
            resposta = self.perguntar_com_opcoes("\nVocê tem mais algum sintoma?", opcoes_sim_nao)
            if opcoes_sim_nao[resposta - 1] == "Não":
                continuar = False

        self.salvar_ficha()


    def exibir_resumo(self):
        print("\n--- Resumo da Triagem ---")
        print(f"Nome do paciente: {self.nome}")
        print(f"Tipo de consulta: {self.consulta}")
        if self.consulta == "Retorno":
            print(f"Médico atendente anterior: {self.medico_atendente}")
        print(f"Estado geral do paciente: {self.estado}")
        if self.consulta == "Retorno" and self.estado == "Bem":
            print(f"Exame realizado: {self.exame}")
        for sintoma, lista in self.dados_sintomas.items():
            print(f"\nSintoma: {sintoma}")
            for idx, dados in enumerate(lista, start=1):
                print(f"  Entrada {idx}:")
                if sintoma == "Dor":
                    if dados.dor_no_peito:
                        print(f"    Dor no peito: Intensidade {dados.intensidade_dor_no_peito}")
                    if dados.dor_na_cabeca:
                        print(f"    Dor na cabeça: Intensidade {dados.intensidade_dor_na_cabeca}")
                        if dados.dor_subita or dados.dor_gradual:
                            inicio = "Subita" if dados.dor_subita else "Gradual"
                            print(f"      Início: {inicio}")
                    if dados.dor_no_ouvido:
                        print(f"    Dor no ouvido: Intensidade {dados.intensidade_dor_no_ouvido}")
                        if dados.perda_auditiva or dados.ouvido_escorrendo:
                            print(f"      Perda auditiva: {dados.perda_auditiva}, Ouvido escorrendo: {dados.ouvido_escorrendo}")
                    if dados.dor_na_garganta:
                        print(f"    Dor na garganta: Intensidade {dados.intensidade_dor_na_garganta}")
                        if dados.dificuldade_engolir:
                            print(f"      Dificuldade para engolir: {dados.dificuldade_engolir}")
                elif sintoma == "Tosse":
                    if dados.tosse_seca:
                        print("    Tosse seca")
                    if dados.tosse_com_muco:
                        print("    Tosse com muco")
                    if dados.dificuldade_respiratoria:
                        print("    Dificuldade respiratória")
                    if dados.gripe_resfriado:
                        print("    Teve gripe ou resfriado recentemente")
                elif sintoma == "Mal Estar":
                    if dados.enjoo:
                        print("    Enjoo")
                    if dados.refluxo:
                        print("    Refluxo")
                    if dados.dor_abdominal:
                        print("    Dor abdominal")
                    if dados.diarreia:
                        print("    Diarreia")
                    if dados.tontura:
                        print("    Tontura")
                    if dados.tremores:
                        print("    Tremores")
                    if dados.movimento_involuntario:
                        print("    Movimentos involuntários")

    def salvar_ficha(self):
        ficha = {
            "nome": self.nome,
            "consulta": self.consulta,
            "medico_atendente": self.medico_atendente if self.consulta == "Retorno" else None,
            "estado": self.estado,
            "exame": self.exame,
            "sintomas": {}
        }

        if hasattr(self, "nome_exame"):
            ficha["nome_exame"] = self.nome_exame

        for sintoma, lista in self.dados_sintomas.items():
            sintomas_agrupados = {}

            for dados in lista:
                if sintoma == "Dor":
                    if dados.dor_no_peito:
                        sintomas_agrupados["dor_no_peito"] = True
                        sintomas_agrupados["intensidade_dor_no_peito"] = max(
                            sintomas_agrupados.get("intensidade_dor_no_peito", 0),
                            dados.intensidade_dor_no_peito
                        )
                    if dados.dor_na_cabeca:
                        sintomas_agrupados["dor_na_cabeca"] = True
                        sintomas_agrupados["intensidade_dor_na_cabeca"] = max(
                            sintomas_agrupados.get("intensidade_dor_na_cabeca", 0),
                            dados.intensidade_dor_na_cabeca
                        )
                        if dados.dor_subita:
                            sintomas_agrupados["dor_subita"] = True
                        if dados.dor_gradual:
                            sintomas_agrupados["dor_gradual"] = True
                    if dados.dor_no_ouvido:
                        sintomas_agrupados["dor_no_ouvido"] = True
                        sintomas_agrupados["intensidade_dor_no_ouvido"] = max(
                            sintomas_agrupados.get("intensidade_dor_no_ouvido", 0),
                            dados.intensidade_dor_no_ouvido
                        )
                        if dados.perda_auditiva:
                            sintomas_agrupados["perda_auditiva"] = True
                        if dados.ouvido_escorrendo:
                            sintomas_agrupados["ouvido_escorrendo"] = True
                    if dados.dor_na_garganta:
                        sintomas_agrupados["dor_na_garganta"] = True
                        sintomas_agrupados["intensidade_dor_na_garganta"] = max(
                            sintomas_agrupados.get("intensidade_dor_na_garganta", 0),
                            dados.intensidade_dor_na_garganta
                        )
                        if dados.dificuldade_engolir:
                            sintomas_agrupados["dificuldade_engolir"] = True

                elif sintoma == "Tosse":
                    if dados.tosse_seca:
                        sintomas_agrupados["tosse_seca"] = True
                    if dados.tosse_com_muco:
                        sintomas_agrupados["tosse_com_muco"] = True
                    if dados.dificuldade_respiratoria:
                        sintomas_agrupados["dificuldade_respiratoria"] = True
                    if dados.gripe_resfriado:
                        sintomas_agrupados["gripe_resfriado"] = True

                elif sintoma == "Mal Estar":
                    if dados.enjoo:
                        sintomas_agrupados["enjoo"] = True
                    if dados.refluxo:
                        sintomas_agrupados["refluxo"] = True
                    if dados.dor_abdominal:
                        sintomas_agrupados["dor_abdominal"] = True
                    if dados.diarreia:
                        sintomas_agrupados["diarreia"] = True
                    if dados.tontura:
                        sintomas_agrupados["tontura"] = True
                    if dados.tremores:
                        sintomas_agrupados["tremores"] = True
                    if dados.movimento_involuntario:
                        sintomas_agrupados["movimento_involuntario"] = True

            if sintomas_agrupados:
                ficha["sintomas"][sintoma] = [sintomas_agrupados]

        pasta = "QuadroDeFichas"
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        if self.consulta == "Retorno" and self.medico_atendente:
            base_filename = f"Retorno_{self.medico_atendente}_{self.nome}.json"
        else:
            base_filename = f"{self.estado}_{self.nome}.json"

        arquivo = os.path.join(pasta, base_filename)
        name_without_ext, ext = os.path.splitext(base_filename)
        counter = 1
        while os.path.exists(arquivo):
            arquivo = os.path.join(pasta, f"{name_without_ext}_{counter}{ext}")
            counter += 1

        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(ficha, f, indent=4, ensure_ascii=False)

        print(f"\nFicha do paciente salva no arquivo '{arquivo}'.")
