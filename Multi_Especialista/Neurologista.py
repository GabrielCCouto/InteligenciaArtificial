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

        self.max_enxaqueca = 2
        self.max_parkinson = 2

    def analisar_triagem(self):
        print("\n--- Análise pelo Neurologista ---")
        sintomas_relacionados = []
        exame_recomendado = None

        # Processa os dados de "Dor" para identificar dor de cabeça
        if "Dor" in self.enfermeira.dados_sintomas:
            for dor in self.enfermeira.dados_sintomas["Dor"]:
                if dor.dor_na_cabeca:
                    self.score_enxaqueca += 1
                    sintomas_relacionados.append("dor de cabeça")
                    # Se a intensidade for alta, marca para exame
                    if 8 <= dor.intensidade_dor_na_cabeca <= 10:
                        exame_recomendado = "tomografia ou encefalograma"
                # Outras ocorrências de dor podem ser adicionadas se desejado

        # Processa os dados de "Mal Estar" para identificar sintomas neurológicos
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

        # Calcula as porcentagens de chance para cada doença
        porcentagem_enxaqueca = (self.score_enxaqueca / self.max_enxaqueca) * 100 if self.max_enxaqueca else 0
        porcentagem_parkinson = (self.score_parkinson / self.max_parkinson) * 100 if self.max_parkinson else 0

        # Decide qual diagnóstico tem maior pontuação (pode-se aprimorar a lógica)
        if self.score_enxaqueca >= self.score_parkinson:
            diagnostico = f"Enxaqueca ({porcentagem_enxaqueca:.1f}% de chance)"
        else:
            diagnostico = f"Parkinson ({porcentagem_parkinson:.1f}% de chance)"

        # Monta a mensagem final
        sintomas_str = ", ".join(set(sintomas_relacionados))  # remove duplicatas
        print(f"\nVerifiquei a sua ficha que a enfermeira me passou e, de acordo com os sintomas: {sintomas_str},")
        print(f"você provavelmente está com: {diagnostico}")

        # Se houver indicação de dor de cabeça intensa, solicita exame
        if exame_recomendado:
            print(f"E como você está sentindo uma dor muito intensa, vou solicitar um exame: {exame_recomendado}")
