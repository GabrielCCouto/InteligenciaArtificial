# medico.py
class Medico:
    def __init__(self, enfermeira):
        self.enfermeira = enfermeira
        self.scores = {
            "Gripe (Influenza)": 0,
            "Sinusite": 0,
            "Resfriado Comum": 0,
            "Bronquite Aguda": 0,
            "Faringite": 0
        }
        self.scores_details = {doenca: [] for doenca in self.scores}
        self.max_scores = {
            "Gripe (Influenza)": 8,
            "Sinusite": 6,
            "Resfriado Comum": 7,
            "Bronquite Aguda": 3,
            "Faringite": 4
        }
        self.additional_questions = [
            ("O paciente apresenta fadiga intensa?", ["Gripe (Influenza)"]),
            ("O paciente apresenta dor de garganta?", ["Gripe (Influenza)", "Faringite"]),
            ("O paciente apresenta congestão nasal?", ["Gripe (Influenza)"]),
            ("O paciente apresenta congestão nasal persistente?", ["Sinusite"]),
            ("O paciente apresenta secreção nasal espessa e amarelada ou esverdeada?", ["Sinusite"]),
            ("O paciente apresenta redução ou perda do olfato?", ["Sinusite"]),
            ("O paciente apresenta nariz escorrendo ou entupido?", ["Resfriado Comum"]),
            ("O paciente apresenta espirros?", ["Resfriado Comum"]),
            ("O paciente apresenta dor de garganta leve?", ["Resfriado Comum"]),
            ("O paciente apresenta tosse moderada?", ["Resfriado Comum"]),
            ("O paciente apresenta dor de cabeça leve?", ["Resfriado Comum"]),
            ("O paciente apresenta fadiga leve?", ["Resfriado Comum"]),
            ("O paciente sente aperto no peito?", ["Bronquite Aguda"]),
            ("O paciente apresenta desconforto ao respirar profundamente?", ["Bronquite Aguda"]),
            ("O paciente apresenta dificuldade para engolir?", ["Faringite"]),
            ("O paciente apresenta vermelhidão na garganta?", ["Faringite"]),
            ("O paciente apresenta inchaço dos linfonodos no pescoço?", ["Faringite"])
        ]

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

    def obter_resposta_adicional(self, pergunta):
        opcoes = ["Sim", "Não"]
        print(pergunta)
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")
        while True:
            resposta = input("Escolha a opção (1-2): ").strip()
            if resposta.isdigit() and int(resposta) in [1, 2]:
                return opcoes[int(resposta) - 1]
            else:
                print("Opção inválida. Tente novamente.")

    def calcular_scores_iniciais(self):
        # Gripe (Influenza)
        if "Febre" in self.enfermeira.dados_sintomas:
            if self.enfermeira.febre.febre == "Sim":
                self.scores["Gripe (Influenza)"] += 1
                self.scores_details["Gripe (Influenza)"].append("febre")
            if self.enfermeira.febre.calafrios == "Sim":
                self.scores["Gripe (Influenza)"] += 1
                self.scores_details["Gripe (Influenza)"].append("calafrios")
        if "Dor" in self.enfermeira.dados_sintomas:
            dor = self.enfermeira.dados_sintomas["Dor"]
            if dor.musculares == "Sim":
                self.scores["Gripe (Influenza)"] += 1
                self.scores_details["Gripe (Influenza)"].append("dores musculares")
            if dor.regiao == "Cabeça":
                self.scores["Gripe (Influenza)"] += 1
                self.scores_details["Gripe (Influenza)"].append("dor de cabeça")
        if "Tosse" in self.enfermeira.dados_sintomas and self.enfermeira.tosse.presenca == "Sim":
            self.scores["Gripe (Influenza)"] += 1
            self.scores_details["Gripe (Influenza)"].append("tosse")

        # Sinusite
        if "Dor" in self.enfermeira.dados_sintomas:
            dor = self.enfermeira.dados_sintomas["Dor"]
            if dor.facial == "Sim":
                self.scores["Sinusite"] += 1
                self.scores_details["Sinusite"].append("dor facial")
            if dor.regiao == "Cabeça":
                self.scores["Sinusite"] += 1
                self.scores_details["Sinusite"].append("dor de cabeça")
        if "Febre" in self.enfermeira.dados_sintomas:
            if self.enfermeira.febre.febre == "Sim":
                self.scores["Sinusite"] += 1
                self.scores_details["Sinusite"].append("febre")

        # Resfriado Comum
        if "Tosse" in self.enfermeira.dados_sintomas and self.enfermeira.tosse.presenca == "Sim":
            self.scores["Resfriado Comum"] += 1
            self.scores_details["Resfriado Comum"].append("tosse")

        # Bronquite Aguda
        if "Tosse" in self.enfermeira.dados_sintomas and self.enfermeira.tosse.tipo == "Com produção de muco":
            self.scores["Bronquite Aguda"] += 1
            self.scores_details["Bronquite Aguda"].append("tosse com produção de muco")

        # Faringite
        # Nenhuma informação prévia específica foi coletada na triagem da enfermeira para Faringite.

    def diagnosticar_porcentagens(self):
        porcentagens = {}
        for doenca in self.scores:
            porcentagens[doenca] = (self.scores[doenca] / self.max_scores[doenca]) * 100
        return porcentagens

    def analisar_triagem(self):
        print("\n--- Análise da Triagem pelo Médico ---")
        if self.enfermeira.estado == "Bem":
            print("O paciente está bem, sem sintomas a relatar.")
            return

        print("O paciente apresenta os seguintes sintomas coletados pela enfermeira:")
        for sintoma in self.enfermeira.dados_sintomas.keys():
            print(f"- {sintoma}")

        self.calcular_scores_iniciais()
        print("\nSintomas identificados e contribuições iniciais:")
        for doenca, score in self.scores.items():
            detalhes = ", ".join(self.scores_details[doenca])
            print(f"{doenca}: {score} - {detalhes}")

        idx = 0
        while idx < len(self.additional_questions):
            pergunta, doencas_relacionadas = self.additional_questions[idx]
            resposta = self.obter_resposta_adicional(pergunta)
            if resposta == "Sim":
                for doenca in doencas_relacionadas:
                    self.scores[doenca] += 1
                    self.scores_details[doenca].append(pergunta)
            print("\nAtualização dos sintomas:")
            for doenca, score in self.scores.items():
                detalhes = ", ".join(self.scores_details[doenca])
                print(f"{doenca}: {score} - {detalhes}")
            idx += 1

        porcentagens = self.diagnosticar_porcentagens()
        print("\nCerteza do Diagnóstico:")
        for doenca, perc in porcentagens.items():
            detalhes = ", ".join(self.scores_details[doenca])
            print(f"- {doenca}: {perc:.1f}% ({detalhes})")

        if "Dor" in self.enfermeira.dados_sintomas:
            dor = self.enfermeira.dados_sintomas["Dor"]
            if dor.regiao == "Cabeça" and dor.inicio == "Súbita" and 8 <= dor.intensidade <= 10:
                print("\nObservação adicional: A dor de cabeça é intensa e de início súbito. Recomenda-se realizar exames como encefalograma ou tomografia.")
