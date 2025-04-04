# enfermeira.py
from Sintomas import Dor, Tosse, MalEstar

class Enfermeira:
    def __init__(self):
        self.estado = None            # "Bem", "Razoável", "Mal"
        self.consulta = None          # "Primeira consulta" ou "Retorno"
        self.exame = None             # "Sim" ou "Não" (apenas para retorno)
        # Trabalhamos com os sintomas: Dor, Tosse e Mal Estar
        self.opcoes_sintomas = ["Dor", "Tosse", "Mal Estar"]
        # Armazena múltiplas ocorrências para cada sintoma
        self.dados_sintomas = {"Dor": [], "Tosse": [], "Mal Estar": []}
        # Lista para armazenar os especialistas para os quais encaminhar
        self.encaminhar_especialista = []

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
        print("Olá, sou a enfermeira. Vamos iniciar sua triagem!\n")
        # Pergunta se é primeira consulta ou retorno
        consulta_opcoes = ["Primeira consulta", "Retorno"]
        escolha = self.perguntar_com_opcoes("É sua primeira consulta ou é retorno?", consulta_opcoes)
        self.consulta = consulta_opcoes[escolha - 1]

        # Pergunta sobre o estado geral do paciente
        estado_opcoes = ["Bem", "Razoável", "Mal"]
        escolha = self.perguntar_com_opcoes("Como você está se sentindo hoje?", estado_opcoes)
        self.estado = estado_opcoes[escolha - 1]

        if self.estado == "Bem":
            if self.consulta == "Primeira consulta":
                print("\nO paciente está bem e, por ser a primeira consulta, não há o que investigar.")
                return
            else:
                opcoes_sim_nao = ["Sim", "Não"]
                resposta = self.perguntar_com_opcoes("Você fez algum exame?", opcoes_sim_nao)
                self.exame = opcoes_sim_nao[resposta - 1]
                print(f"\nO paciente está bem. Encaminhando para o médico (Exame realizado: {self.exame}).")
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

        self.exibir_resumo()
        self.encaminhar_especialistas()

    def encaminhar_especialistas(self):
        # Encaminhamento para Neurologista:
        count_neuro = 0
        if "Dor" in self.dados_sintomas:
            for dor in self.dados_sintomas["Dor"]:
                if dor.dor_na_cabeca:
                    count_neuro += 1
        if "Mal Estar" in self.dados_sintomas:
            for mal in self.dados_sintomas["Mal Estar"]:
                if mal.tontura:
                    count_neuro += 1
                if mal.tremores:
                    count_neuro += 1
                if mal.movimento_involuntario:
                    count_neuro += 1
        if count_neuro >= 3:
            print("\nEncaminhamento automático: O paciente será encaminhado para o Neurologista.")
            self.encaminhar_especialista.append("Neurologista")
        else:
            print("\nEncaminhamento automático: O paciente não necessita de encaminhamento para o Neurologista.")

        # Encaminhamento para Pneumologista:
        count_pneumo = 0
        if "Tosse" in self.dados_sintomas:
            for tosse in self.dados_sintomas["Tosse"]:
                if tosse.gripe_resfriado:
                    count_pneumo += 1
                count_pneumo += 1  # presença de tosse
                if tosse.dificuldade_respiratoria:
                    count_pneumo += 1
        if "Dor" in self.dados_sintomas:
            for dor in self.dados_sintomas["Dor"]:
                if dor.dor_no_peito:
                    count_pneumo += 1
        if count_pneumo >= 2:
            print("\nEncaminhamento automático: O paciente será encaminhado para o Pneumologista.")
            self.encaminhar_especialista.append("Pneumologista")
        else:
            print("\nEncaminhamento automático: O paciente não necessita de encaminhamento para o Pneumologista.")

        # Encaminhamento para Gastroenterologista:
        count_gastro = 0
        if "Mal Estar" in self.dados_sintomas:
            for mal in self.dados_sintomas["Mal Estar"]:
                if mal.refluxo:
                    count_gastro += 1
                if mal.enjoo:
                    count_gastro += 1
                if mal.dor_abdominal:
                    count_gastro += 1
                if mal.diarreia:
                    count_gastro += 1
        if count_gastro >= 2:
            print("\nEncaminhamento automático: O paciente será encaminhado para o Gastroenterologista.")
            self.encaminhar_especialista.append("Gastroenterologista")
        else:
            print("\nEncaminhamento automático: O paciente não necessita de encaminhamento para o Gastroenterologista.")

        # Encaminhamento para Otorrinolaringologista:
        count_otorrino = 0
        if "Dor" in self.dados_sintomas:
            for dor in self.dados_sintomas["Dor"]:
                # Se houver dor no ouvido e perda auditiva, soma pontos
                if dor.dor_no_ouvido and dor.perda_auditiva:
                    count_otorrino += 1
                # Se houver dor na garganta e dificuldade para engolir, soma pontos
                if dor.dor_na_garganta and dor.dificuldade_engolir:
                    count_otorrino += 1
        if count_otorrino >= 1:
            print("\nEncaminhamento automático: O paciente será encaminhado para o Otorrinolaringologista.")
            self.encaminhar_especialista.append("Otorrinolaringologista")
        else:
            print("\nEncaminhamento automático: O paciente não necessita de encaminhamento para o Otorrinolaringologista.")

        if not self.encaminhar_especialista:
            print("\nEncaminhamento automático: Não há necessidade de encaminhamento para nenhum especialista.")

    def exibir_resumo(self):
        print("\n--- Resumo da Triagem ---")
        print(f"Tipo de consulta: {self.consulta}")
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
        if self.encaminhar_especialista:
            print("\nEncaminhamento para especialistas:")
            for esp in self.encaminhar_especialista:
                print(f" - {esp}")
