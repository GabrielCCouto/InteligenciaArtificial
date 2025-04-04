# Neurologista.py

class Neurologista:
    """
    Especialista Neurologista utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Enxaqueca: associada à dor de cabeça e tontura.
      - Parkinson: associada a tremores e movimentos involuntários.
    Se a intensidade da dor de cabeça for entre 8 e 10, recomenda a realização de exames.
    """
    def __init__(self, enfermeira):
        self.enfermeira = enfermeira
        self.score_enxaqueca = 0
        self.score_parkinson = 0

        self.max_enxaqueca = 2
        self.max_parkinson = 2

    def analisar_triagem(self):
        print("\n--- Análise pelo Neurologista ---")
        sintomas_relacionados = []
        exame_recomendado = None

        if "Dor" in self.enfermeira.dados_sintomas:
            for dor in self.enfermeira.dados_sintomas["Dor"]:
                if dor.dor_na_cabeca:
                    self.score_enxaqueca += 1
                    sintomas_relacionados.append("dor de cabeça")
                    if 8 <= dor.intensidade_dor_na_cabeca <= 10:
                        exame_recomendado = "tomografia ou encefalograma"

        if "Mal Estar" in self.enfermeira.dados_sintomas:
            for mal in self.enfermeira.dados_sintomas["Mal Estar"]:
                if getattr(mal, "tontura", False):
                    self.score_enxaqueca += 1
                    sintomas_relacionados.append("tontura")
                if getattr(mal, "tremores", False):
                    self.score_parkinson += 1
                    sintomas_relacionados.append("tremores")
                if getattr(mal, "movimento_involuntario", False):
                    self.score_parkinson += 1
                    sintomas_relacionados.append("movimentos involuntários")

        porcentagem_enxaqueca = (self.score_enxaqueca / self.max_enxaqueca) * 100 if self.max_enxaqueca else 0
        porcentagem_parkinson = (self.score_parkinson / self.max_parkinson) * 100 if self.max_parkinson else 0

        if self.score_enxaqueca >= self.score_parkinson:
            diagnostico = f"Enxaqueca ({porcentagem_enxaqueca:.1f}% de chance)"
        else:
            diagnostico = f"Parkinson ({porcentagem_parkinson:.1f}% de chance)"

        sintomas_str = ", ".join(set(sintomas_relacionados))
        print(f"\nVerifiquei a sua ficha que a enfermeira me passou e, de acordo com os sintomas: {sintomas_str},")
        print(f"você provavelmente está com: {diagnostico}")

        if exame_recomendado:
            print(f"E como você está sentindo uma dor muito intensa, vou solicitar um exame: {exame_recomendado}")
