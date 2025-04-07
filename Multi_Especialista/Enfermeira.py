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
        # Armazena múltiplas ocorrências para cada sintoma
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
        # Pergunta: Nome do paciente
        self.nome = input("Qual o seu nome? ").strip()

        # Pergunta se é primeira consulta ou retorno
        consulta_opcoes = ["Primeira consulta", "Retorno"]
        escolha = self.perguntar_com_opcoes("É sua primeira consulta ou é retorno?", consulta_opcoes)
        self.consulta = consulta_opcoes[escolha - 1]

        # Para pacientes de retorno, pergunta qual foi o médico que atendeu da última vez (opções)
        if self.consulta == "Retorno":
            medico_opcoes = ["Pneumologista", "Neurologista", "Gastroenterologista", "Otorrinolaringologista"]
            escolha_medico = self.perguntar_com_opcoes("Qual foi o médico que atendeu da última vez?", medico_opcoes)
            self.medico_atendente = medico_opcoes[escolha_medico - 1]

        # Pergunta sobre o estado geral do paciente
        estado_opcoes = ["Bem", "Razoável", "Mal"]
        escolha = self.perguntar_com_opcoes("Como você está se sentindo hoje?", estado_opcoes)
        self.estado = estado_opcoes[escolha - 1]

        if self.estado == "Bem":
            if self.consulta == "Primeira consulta":
                print("\nO paciente está bem e, por ser a primeira consulta, não há o que investigar.")
                self.salvar_ficha()
                return
            else:
                opcoes_sim_nao = ["Sim", "Não"]
                resposta = self.perguntar_com_opcoes("Você fez algum exame?", opcoes_sim_nao)
                self.exame = opcoes_sim_nao[resposta - 1]
                print(f"\nO paciente está bem. Encaminhando para o médico (Exame realizado: {self.exame}).")
                self.salvar_ficha()
                return

        # Se o paciente não está bem, coleta os sintomas
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

        # self.exibir_resumo()
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
        # Monta o dicionário com os dados do paciente
        ficha = {
            "nome": self.nome,
            "consulta": self.consulta,
            "medico_atendente": self.medico_atendente if self.consulta == "Retorno" else None,
            "estado": self.estado,
            "exame": self.exame,
            "sintomas": {}
        }

        for sintoma, lista in self.dados_sintomas.items():
            ficha["sintomas"][sintoma] = []
            for dados in lista:
                registro = {}

                if sintoma == "Dor":
                    if dados.dor_no_peito:
                        registro["dor_no_peito"] = True
                        if dados.intensidade_dor_no_peito > 0:
                            registro["intensidade_dor_no_peito"] = dados.intensidade_dor_no_peito
                    if dados.dor_na_cabeca:
                        registro["dor_na_cabeca"] = True
                        if dados.intensidade_dor_na_cabeca > 0:
                            registro["intensidade_dor_na_cabeca"] = dados.intensidade_dor_na_cabeca
                        if dados.dor_subita:
                            registro["dor_subita"] = True
                        if dados.dor_gradual:
                            registro["dor_gradual"] = True
                    if dados.dor_no_ouvido:
                        registro["dor_no_ouvido"] = True
                        if dados.intensidade_dor_no_ouvido > 0:
                            registro["intensidade_dor_no_ouvido"] = dados.intensidade_dor_no_ouvido
                        if dados.perda_auditiva:
                            registro["perda_auditiva"] = True
                        if dados.ouvido_escorrendo:
                            registro["ouvido_escorrendo"] = True
                    if dados.dor_na_garganta:
                        registro["dor_na_garganta"] = True
                        if dados.intensidade_dor_na_garganta > 0:
                            registro["intensidade_dor_na_garganta"] = dados.intensidade_dor_na_garganta
                        if dados.dificuldade_engolir:
                            registro["dificuldade_engolir"] = True

                elif sintoma == "Tosse":
                    if dados.tosse_seca:
                        registro["tosse_seca"] = True
                    if dados.tosse_com_muco:
                        registro["tosse_com_muco"] = True
                    if dados.dificuldade_respiratoria:
                        registro["dificuldade_respiratoria"] = True
                    if dados.gripe_resfriado:
                        registro["gripe_resfriado"] = True

                elif sintoma == "Mal Estar":
                    if dados.enjoo:
                        registro["enjoo"] = True
                    if dados.refluxo:
                        registro["refluxo"] = True
                    if dados.dor_abdominal:
                        registro["dor_abdominal"] = True
                    if dados.diarreia:
                        registro["diarreia"] = True
                    if dados.tontura:
                        registro["tontura"] = True
                    if dados.tremores:
                        registro["tremores"] = True
                    if dados.movimento_involuntario:
                        registro["movimento_involuntario"] = True

                # Adiciona ao json apenas se houver algo preenchido
                if registro:
                    ficha["sintomas"][sintoma].append(registro)

        # Define a pasta de destino
        pasta = "QuadroDeFichas"
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        # Gera o nome base do arquivo conforme a consulta e estado
        if self.consulta == "Retorno" and self.medico_atendente:
            base_filename = f"Retorno_{self.medico_atendente}_{self.nome}.json"
        else:
            base_filename = f"{self.estado}_{self.nome}.json"

        # Garante que o arquivo não seja sobrescrito: se já existir, adiciona um sufixo numérico.
        arquivo = os.path.join(pasta, base_filename)
        name_without_ext, ext = os.path.splitext(base_filename)
        counter = 1
        while os.path.exists(arquivo):
            arquivo = os.path.join(pasta, f"{name_without_ext}_{counter}{ext}")
            counter += 1

        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(ficha, f, indent=4, ensure_ascii=False)

        print(f"\nFicha do paciente salva no arquivo '{arquivo}'.")
