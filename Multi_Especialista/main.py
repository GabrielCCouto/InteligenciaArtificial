class Dor:
    def __init__(self):
        self.regiao = None         # Ex: "Cabeça", "Tórax", "Membros"
        self.intensidade = None    # Valor numérico de 1 a 10
        self.inicio = None         # "Súbita" ou "Gradual"
        self.irradia = None        # "Sim" ou "Não"
        self.facial = None         # "Sim" ou "Não"
        self.musculares = None     # "Sim" ou "Não"

    def coletar_dados(self, perguntar_com_opcoes):
        regioes = ["Cabeça", "Tórax", "Membros", "Outra"]
        escolha = perguntar_com_opcoes("\nEm qual região do corpo você sente a dor?", regioes)
        self.regiao = regioes[escolha - 1]
        
        while True:
            intensidade = input("\nQual a intensidade da dor em uma escala de 1 a 10? ").strip()
            if intensidade.isdigit() and 1 <= int(intensidade) <= 10:
                self.intensidade = int(intensidade)
                break
            else:
                print("Entrada inválida. Digite um número entre 1 e 10.")

        inicio_opcoes = ["Súbita", "Gradual"]
        escolha = perguntar_com_opcoes("\nComo a dor começou?", inicio_opcoes)
        self.inicio = inicio_opcoes[escolha - 1]

        irradiacao_opcoes = ["Sim", "Não"]
        escolha = perguntar_com_opcoes("\nA dor se irradia para outras partes do corpo?", irradiacao_opcoes)
        self.irradia = irradiacao_opcoes[escolha - 1]

        escolha = perguntar_com_opcoes("\nVocê sente dor facial?", irradiacao_opcoes)
        self.facial = irradiacao_opcoes[escolha - 1]

        escolha = perguntar_com_opcoes("\nVocê sente dores musculares?", irradiacao_opcoes)
        self.musculares = irradiacao_opcoes[escolha - 1]


class Febre:
    def __init__(self):
        self.febre = None      # "Sim" ou "Não" (definido automaticamente)
        self.calafrios = None  # "Sim" ou "Não"
        self.contato = None    # "Sim" ou "Não"

    def coletar_dados(self, perguntar_com_opcoes):
        # Como o paciente já selecionou "Febre", definimos automaticamente que ele notou febre.
        self.febre = "Sim"
        
        opcoes_sim_nao = ["Sim", "Não"]
        escolha = perguntar_com_opcoes("\nHouve calafrios ou suores intensos?", opcoes_sim_nao)
        self.calafrios = opcoes_sim_nao[escolha - 1]

        escolha = perguntar_com_opcoes("Você teve contato com alguém doente recentemente?", opcoes_sim_nao)
        self.contato = opcoes_sim_nao[escolha - 1]


class Tosse:
    def __init__(self):
        self.presenca = None   # "Sim" ou "Não" (definido automaticamente)
        self.tipo = None       # "Seca" ou "Com produção de muco"
        self.falta_ar = None   # "Sim" ou "Não"

    def coletar_dados(self, perguntar_com_opcoes):
        # Como o paciente já selecionou "Tosse", definimos automaticamente a presença como "Sim"
        self.presenca = "Sim"
        
        tosse_opcoes = ["Seca", "Com produção de muco"]
        escolha = perguntar_com_opcoes("\nQual o tipo de tosse?", tosse_opcoes)
        self.tipo = tosse_opcoes[escolha - 1]

        opcoes_sim_nao = ["Sim", "Não"]
        escolha = perguntar_com_opcoes("Tem sentido falta de ar, mesmo em repouso ou durante atividades?", opcoes_sim_nao)
        self.falta_ar = opcoes_sim_nao[escolha - 1]


class Enfermeira:
    def __init__(self):
        self.estado = None  # "Bem", "Razoável", "Mal"
        # Lista de sintomas disponíveis para a triagem
        self.opcoes_sintomas = ["Dor", "Febre", "Tosse"]
        # Dicionário para armazenar os dados coletados para cada sintoma
        self.dados_sintomas = {}
        # Instâncias de cada sintoma
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
        print("Olá, sou a enfermeira. Vamos iniciar a sua triagem!\n")
        # Estado geral
        estado_opcoes = ["Bem", "Razoável", "Mal"]
        escolha = self.perguntar_com_opcoes("Como você está se sentindo hoje?", estado_opcoes)
        self.estado = estado_opcoes[escolha - 1]
        if self.estado == "Bem":
            print("\nO paciente está bem e não tem o que investigar.")
            return

        # Loop para coletar todos os sintomas desejados
        while self.opcoes_sintomas:
            escolha = self.perguntar_com_opcoes(
                "\nQual é o principal sintoma que o trouxe aqui?",
                self.opcoes_sintomas
            )
            sintoma = self.opcoes_sintomas[escolha - 1]

            # Coleta dos dados do sintoma escolhido
            if sintoma == "Dor":
                self.dor.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Dor"] = self.dor
            elif sintoma == "Febre":
                self.febre.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Febre"] = self.febre
            elif sintoma == "Tosse":
                self.tosse.coletar_dados(self.perguntar_com_opcoes)
                self.dados_sintomas["Tosse"] = self.tosse

            # Remove o sintoma já coletado para não ser perguntado novamente
            self.opcoes_sintomas.remove(sintoma)

            # Se ainda houver opções, perguntar se sente mais alguma coisa
            if self.opcoes_sintomas:
                opcoes_sim_nao = ["Sim", "Não"]
                resposta = self.perguntar_com_opcoes(
                    "\nVocê sente mais algum sintoma?",
                    opcoes_sim_nao
                )
                if opcoes_sim_nao[resposta - 1] == "Não":
                    break
            else:
                break

        # Exibir resumo final
        self.exibir_resumo()

    def exibir_resumo(self):
        print("\n--- Resumo da Triagem ---")
        print(f"Estado geral do paciente: {self.estado}")
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


class Medico:
    def __init__(self, enfermeira):
        # O médico recebe o objeto enfermeira com os dados da triagem
        self.enfermeira = enfermeira

    def analisar_triagem(self):
        print("\n--- Análise da Triagem pelo Médico ---")
        if self.enfermeira.estado == "Bem":
            print("O paciente está bem, sem sintomas a relatar.")
            return

        # O médico informa os sintomas coletados
        for sintoma, dados in self.enfermeira.dados_sintomas.items():
            if sintoma == "Dor":
                print("O paciente apresenta dor.")
            elif sintoma == "Febre":
                print("O paciente apresenta febre.")
            elif sintoma == "Tosse":
                print("O paciente apresenta tosse.")


# Exemplo de uso:
if __name__ == "__main__":
    enfermeira = Enfermeira()
    enfermeira.iniciar_triagem()

    # Se a triagem foi realizada (ou seja, o paciente não estava "Bem")
    if enfermeira.estado != "Bem":
        medico = Medico(enfermeira)
        medico.analisar_triagem()
