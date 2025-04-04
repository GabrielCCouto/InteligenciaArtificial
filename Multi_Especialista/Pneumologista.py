# Pneumologista.py

class Pneumologista:
    """
    Especialista Pneumologista utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Influenza: associada à presença de tosse e histórico de gripe/resfriado.
      - Asma: associada à dificuldade respiratória e dor no peito.
    Se a intensidade da dor no peito for entre 8 e 10, recomenda a realização de um exame (Raio-X do tórax).
    """
    def __init__(self, enfermeira):
        self.enfermeira = enfermeira
        self.score_influenza = 0
        self.score_asma = 0

        self.max_influenza = 2
        self.max_asma = 2

    def analisar_triagem(self):
        print("\n--- Análise pelo Pneumologista ---")
        sintomas_influenza = []
        sintomas_asma = []
        exame_recomendado = None

        if "Tosse" in self.enfermeira.dados_sintomas:
            for tosse in self.enfermeira.dados_sintomas["Tosse"]:
                if tosse.gripe_resfriado:
                    self.score_influenza += 1
                    sintomas_influenza.append("histórico de gripe/resfriado")
                self.score_influenza += 1
                sintomas_influenza.append("tosse")
                if tosse.dificuldade_respiratoria:
                    self.score_asma += 1
                    sintomas_asma.append("dificuldade respiratória")

        if "Dor" in self.enfermeira.dados_sintomas:
            for dor in self.enfermeira.dados_sintomas["Dor"]:
                if dor.dor_no_peito:
                    self.score_asma += 1
                    sintomas_asma.append("dor no peito")
                    if 8 <= dor.intensidade_dor_no_peito <= 10:
                        exame_recomendado = "Raio-X do tórax"

        porcentagem_influenza = (self.score_influenza / self.max_influenza) * 100 if self.max_influenza else 0
        porcentagem_asma = (self.score_asma / self.max_asma) * 100 if self.max_asma else 0

        if self.score_influenza >= self.score_asma:
            diagnostico = f"Influenza ({porcentagem_influenza:.1f}% de chance)"
        else:
            diagnostico = f"Asma ({porcentagem_asma:.1f}% de chance)"

        sintomas_str_influenza = ", ".join(set(sintomas_influenza))
        sintomas_str_asma = ", ".join(set(sintomas_asma))

        print("\nDiagnóstico Pneumológico:")
        print(f"Influenza: {self.score_influenza} pontos - {porcentagem_influenza:.1f}% de chance ({sintomas_str_influenza})")
        print(f"Asma: {self.score_asma} pontos - {porcentagem_asma:.1f}% de chance ({sintomas_str_asma})")
        print(f"\nVerifiquei sua ficha e, de acordo com os sintomas, você provavelmente está com: {diagnostico}")
        if exame_recomendado:
            print(f"E como a dor no peito é intensa, vou solicitar o exame: {exame_recomendado}")
