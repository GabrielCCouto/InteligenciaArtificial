# Neurologista.py

class Neurologista:
    """
    Especialista Neurologista que utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Enxaqueca: associada à dor de cabeça e tontura.
      - Parkinson: associada a tremores e movimentos involuntários.
    Se a intensidade da dor de cabeça for entre 8 e 10, recomenda a realização de exames.
    """
    def __init__(self, enfermeira):
        self.enfermeira = enfermeira
        self.score_enxaqueca = 0
        self.score_parkinson = 0
        # Definindo os máximos de pontos
        self.max_enxaqueca = 5
        self.max_parkinson = 4

    def analisar_triagem(self):
        print("\n--- Análise pelo Neurologista ---")

        if "Dor" in self.enfermeira.dados_sintomas:
            for dor in self.enfermeira.dados_sintomas["Dor"]:
                if dor.dor_na_cabeca:
                    self.score_enxaqueca += 1
                    if 8 <= dor.intensidade_dor_na_cabeca <= 10:
                        print("Observação: Dor de cabeça intensa. Recomenda-se realizar exames (tomografia ou encefalograma).")

        if "Mal Estar" in self.enfermeira.dados_sintomas:
            for mal in self.enfermeira.dados_sintomas["Mal Estar"]:
                if getattr(mal, "tontura", False):
                    self.score_enxaqueca += 1
                if getattr(mal, "tremores", False):
                    self.score_parkinson += 1
                if getattr(mal, "movimento_involuntario", False):
                    self.score_parkinson += 1

        porcentagem_enxaqueca = (self.score_enxaqueca / self.max_enxaqueca) * 100 if self.max_enxaqueca else 0
        porcentagem_parkinson = (self.score_parkinson / self.max_parkinson) * 100 if self.max_parkinson else 0

        print(f"\nDiagnóstico Neurológico:")
        print(f"Enxaqueca: {self.score_enxaqueca} pontos - {porcentagem_enxaqueca:.1f}% de chance")
        print(f"Parkinson: {self.score_parkinson} pontos - {porcentagem_parkinson:.1f}% de chance")
