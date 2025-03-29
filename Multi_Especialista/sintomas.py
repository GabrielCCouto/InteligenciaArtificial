# sintomas.py

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
        self.febre = None      # "Sim" ou "Não"
        self.calafrios = None  # "Sim" ou "Não"
        self.contato = None    # "Sim" ou "Não"

    def coletar_dados(self, perguntar_com_opcoes):
        self.febre = "Sim"
        
        opcoes_sim_nao = ["Sim", "Não"]
        escolha = perguntar_com_opcoes("\nHouve calafrios ou suores intensos?", opcoes_sim_nao)
        self.calafrios = opcoes_sim_nao[escolha - 1]

        escolha = perguntar_com_opcoes("Você teve contato com alguém doente recentemente?", opcoes_sim_nao)
        self.contato = opcoes_sim_nao[escolha - 1]


class Tosse:
    def __init__(self):
        self.presenca = None   # "Sim" ou "Não"
        self.tipo = None       # "Seca" ou "Com produção de muco"
        self.falta_ar = None   # "Sim" ou "Não"

    def coletar_dados(self, perguntar_com_opcoes):
        self.presenca = "Sim"
        
        tosse_opcoes = ["Seca", "Com produção de muco"]
        escolha = perguntar_com_opcoes("\nQual o tipo de tosse?", tosse_opcoes)
        self.tipo = tosse_opcoes[escolha - 1]

        opcoes_sim_nao = ["Sim", "Não"]
        escolha = perguntar_com_opcoes("Tem sentido falta de ar, mesmo em repouso ou durante atividades?", opcoes_sim_nao)
        self.falta_ar = opcoes_sim_nao[escolha - 1]
