# sintomas.py

class Dor:
    def __init__(self):
        # Peito
        self.dor_no_peito = False
        self.intensidade_dor_no_peito = 0

        # Cabeça
        self.dor_na_cabeca = False
        self.dor_subita = False
        self.dor_gradual = False
        self.intensidade_dor_na_cabeca = 0

        # Ouvido
        self.dor_no_ouvido = False
        self.perda_auditiva = False
        self.ouvido_escorrendo = False
        self.intensidade_dor_no_ouvido = 0

        # Garganta
        self.dor_na_garganta = False
        self.dificuldade_engolir = False
        self.intensidade_dor_na_garganta = 0

    def coletar_dados(self, perguntar_com_opcoes):
        locais = ["Peito", "Cabeça", "Ouvido", "Garganta"]
        escolha = perguntar_com_opcoes("Onde você está sentindo dor?", locais)
        local_selecionado = locais[escolha - 1]

        if local_selecionado == "Peito":
            self.dor_no_peito = True
            while True:
                intensidade = input("Qual a intensidade da dor no peito (1 a 10)? ").strip()
                if intensidade.isdigit() and 1 <= int(intensidade) <= 10:
                    self.intensidade_dor_no_peito = int(intensidade)
                    break
                else:
                    print("Entrada inválida. Digite um número entre 1 e 10.")
        elif local_selecionado == "Cabeça":
            self.dor_na_cabeca = True
            while True:
                intensidade = input("Qual a intensidade da dor na cabeça (1 a 10)? ").strip()
                if intensidade.isdigit() and 1 <= int(intensidade) <= 10:
                    self.intensidade_dor_na_cabeca = int(intensidade)
                    break
                else:
                    print("Entrada inválida. Digite um número entre 1 e 10.")
            inicio_opcoes = ["Subita", "Gradual"]
            escolha_inicio = perguntar_com_opcoes("Como foi o início da dor na cabeça?", inicio_opcoes)
            if inicio_opcoes[escolha_inicio - 1] == "Subita":
                self.dor_subita = True
            else:
                self.dor_gradual = True
        elif local_selecionado == "Ouvido":
            self.dor_no_ouvido = True
            while True:
                intensidade = input("Qual a intensidade da dor no ouvido (1 a 10)? ").strip()
                if intensidade.isdigit() and 1 <= int(intensidade) <= 10:
                    self.intensidade_dor_no_ouvido = int(intensidade)
                    break
                else:
                    print("Entrada inválida. Digite um número entre 1 e 10.")
            opcoes_sim_nao = ["Sim", "Não"]
            escolha_perda = perguntar_com_opcoes("Você sentiu perda auditiva?", opcoes_sim_nao)
            self.perda_auditiva = (opcoes_sim_nao[escolha_perda - 1] == "Sim")
            escolha_escorrendo = perguntar_com_opcoes("Seu ouvido está escorrendo?", opcoes_sim_nao)
            self.ouvido_escorrendo = (opcoes_sim_nao[escolha_escorrendo - 1] == "Sim")
        elif local_selecionado == "Garganta":
            self.dor_na_garganta = True
            while True:
                intensidade = input("Qual a intensidade da dor na garganta (1 a 10)? ").strip()
                if intensidade.isdigit() and 1 <= int(intensidade) <= 10:
                    self.intensidade_dor_na_garganta = int(intensidade)
                    break
                else:
                    print("Entrada inválida. Digite um número entre 1 e 10.")
            opcoes_sim_nao = ["Sim", "Não"]
            escolha_engolir = perguntar_com_opcoes("Você está com dificuldade para engolir?", opcoes_sim_nao)
            self.dificuldade_engolir = (opcoes_sim_nao[escolha_engolir - 1] == "Sim")
        print(f"\nDados de dor coletados para {local_selecionado}.")


class Tosse:
    def __init__(self):
        self.tosse_com_muco = False
        self.tosse_seca = False
        self.dificuldade_respiratoria = False
        self.gripe_resfriado = False

    def coletar_dados(self, perguntar_com_opcoes):
        opcoes_tosse = ["Tosse seca", "Tosse com muco"]
        escolha = perguntar_com_opcoes("Você está com tosse seca ou com muco?", opcoes_tosse)
        if opcoes_tosse[escolha - 1] == "Tosse seca":
            self.tosse_seca = True
        else:
            self.tosse_com_muco = True
        opcoes_sim_nao = ["Sim", "Não"]
        escolha = perguntar_com_opcoes("Você tem dificuldade respiratória?", opcoes_sim_nao)
        if opcoes_sim_nao[escolha - 1] == "Sim":
            self.dificuldade_respiratoria = True
        escolha = perguntar_com_opcoes("Teve gripe ou resfriado recentemente?", opcoes_sim_nao)
        if opcoes_sim_nao[escolha - 1] == "Sim":
            self.gripe_resfriado = True
        print("\nDados de tosse coletados.")


class MalEstar:
    def __init__(self):
        self.enjoo = False
        self.refluxo = False
        self.dor_abdominal = False
        self.diarreia = False
        self.tontura = False
        self.movimento_involuntario = False

    def coletar_dados(self, perguntar_com_opcoes):
        opcoes_sim_nao = ["Sim", "Não"]
        escolha = perguntar_com_opcoes("Você está com enjoo?", opcoes_sim_nao)
        self.enjoo = (opcoes_sim_nao[escolha - 1] == "Sim")
        escolha = perguntar_com_opcoes("Você está com refluxo?", opcoes_sim_nao)
        self.refluxo = (opcoes_sim_nao[escolha - 1] == "Sim")
        escolha = perguntar_com_opcoes("Você sente dor abdominal?", opcoes_sim_nao)
        self.dor_abdominal = (opcoes_sim_nao[escolha - 1] == "Sim")
        escolha = perguntar_com_opcoes("Teve diarreia?", opcoes_sim_nao)
        self.diarreia = (opcoes_sim_nao[escolha - 1] == "Sim")
        escolha = perguntar_com_opcoes("Sentiu tontura?", opcoes_sim_nao)
        self.tontura = (opcoes_sim_nao[escolha - 1] == "Sim")
        escolha = perguntar_com_opcoes("Está sentindo tremores ou movimentos involuntários?", opcoes_sim_nao)
        self.movimento_involuntario = (opcoes_sim_nao[escolha - 1] == "Sim")
        print("\nDados de mal estar coletados.")
