# enfermeira.py
from sintomas import Dor, Febre, Tosse

class Enfermeira:
    def __init__(self):
        self.estado = None            # "Bem", "Razoável", "Mal"
        self.consulta = None          # "Primeira consulta" ou "Retorno"
        self.exame = None             # "Sim" ou "Não" (apenas para retorno)
        self.opcoes_sintomas = ["Dor", "Febre", "Tosse"]
        self.dados_sintomas = {}
        self.dor = Dor()
        self.febre = Febre()
        self.tosse = Tosse()

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

        # Se o paciente estiver bem:
        if self.estado == "Bem":
            if self.consulta == "Primeira consulta":
                print("\nO paciente está bem e, por ser a primeira consulta, não há o que investigar.")
                return
            else:
                # Se for retorno, pergunta se já realizou algum exame.
                opcoes_sim_nao = ["Sim", "Não"]
                resposta = self.perguntar_com_opcoes("Você fez algum exame?", opcoes_sim_nao)
                self.exame = opcoes_sim_nao[resposta - 1]
                print(f"\nO paciente está bem. Encaminhando para o médico (Exame realizado: {self.exame}).")
                return

        # Se o paciente não está bem, coleta os sintomas
        while self.opcoes_sintomas:
            escolha = self.perguntar_com_opcoes(
                "\nQual é o principal sintoma que o trouxe aqui?",
                self.opcoes_sintomas
            )
            sintoma = self.opcoes_sintomas[escolha - 1]
            if sintoma == "Dor":
                self.dor.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Dor"] = self.dor
            elif sintoma == "Febre":
                self.febre.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Febre"] = self.febre
            elif sintoma == "Tosse":
                self.tosse.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Tosse"] = self.tosse

            # Remove o sintoma já coletado para evitar repetições
            self.opcoes_sintomas.remove(sintoma)
            if self.opcoes_sintomas:
                opcoes_sim_nao = ["Sim", "Não"]
                resposta = self.perguntar_com_opcoes("\nVocê sente mais algum sintoma?", opcoes_sim_nao)
                if opcoes_sim_nao[resposta - 1] == "Não":
                    break
            else:
                break

        self.exibir_resumo()

    def exibir_resumo(self):
        print("\n--- Resumo da Triagem ---")
        print(f"Tipo de consulta: {self.consulta}")
        print(f"Estado geral do paciente: {self.estado}")
        if self.consulta == "Retorno" and self.estado == "Bem":
            print(f"Exame realizado: {self.exame}")
        for sintoma, dados in self.dados_sintomas.items():
            print(f"\nSintoma: {sintoma}")
            if sintoma == "Dor":
                print(f"  Região: {dados.regiao}")
                print(f"  Intensidade: {dados.intensidade}")
                print(f"  Início: {dados.inicio}")
                print(f"  Irradiação: {dados.irradia}")
                print(f"  Dor facial: {dados.facial}")
                print(f"  Dores musculares: {dados.musculares}")
            elif sintoma == "Febre":
                print(f"  Febre/Aumento da temperatura: {dados.febre}")
                print(f"  Calafrios/Suores intensos: {dados.calafrios}")
                print(f"  Contato com doente: {dados.contato}")
            elif sintoma == "Tosse":
                print(f"  Tosse: {dados.presenca}")
                print(f"  Tipo de tosse: {dados.tipo}")
                print(f"  Falta de ar: {dados.falta_ar}")
