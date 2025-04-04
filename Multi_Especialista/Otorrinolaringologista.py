# Otorrinolaringologista.py

class Otorrinolaringologista:
    """
    Especialista Otorrinolaringologista que utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Infecção no ouvido: associada à dor no ouvido e perda auditiva.
      - Faringite: associada à dor na garganta e dificuldade para engolir.
    O especialista avalia também a intensidade dos sintomas para recomendar exames,
    como audiometria ou tomografia (para dor no ouvido) e endoscopia (para dor na garganta).
    """
    def __init__(self, enfermeira):
        self.enfermeira = enfermeira
        self.score_infeccao_ouvido = 0
        self.score_faringite = 0
        self.max_infeccao_ouvido = 2
        self.max_faringite = 2

    def analisar_triagem(self):
        print("\n--- Análise pelo Otorrinolaringologista ---")
        sintomas_ouvido = []
        sintomas_faringite = []
        exame_ouvido = None
        exame_faringite = None

        # Processa os dados de "Dor" para identificar sintomas específicos
        if "Dor" in self.enfermeira.dados_sintomas:
            for dor in self.enfermeira.dados_sintomas["Dor"]:
                # Infecção no ouvido: dor no ouvido e perda auditiva
                if dor.dor_no_ouvido:
                    self.score_infeccao_ouvido += 1
                    sintomas_ouvido.append("dor no ouvido")
                    if dor.perda_auditiva:
                        self.score_infeccao_ouvido += 1
                        sintomas_ouvido.append("perda auditiva")
                    # Se a intensidade for alta, recomenda exame
                    if 8 <= dor.intensidade_dor_no_ouvido <= 10:
                        exame_ouvido = "Audiometria ou tomografia do ouvido"
                # Faringite: dor na garganta e dificuldade para engolir
                if dor.dor_na_garganta:
                    self.score_faringite += 1
                    sintomas_faringite.append("dor na garganta")
                    if dor.dificuldade_engolir:
                        self.score_faringite += 1
                        sintomas_faringite.append("dificuldade para engolir")
                    if 8 <= dor.intensidade_dor_na_garganta <= 10:
                        exame_faringite = "endoscopia ou exame de imagem da garganta"

        porcentagem_ouvido = (self.score_infeccao_ouvido / self.max_infeccao_ouvido) * 100 if self.max_infeccao_ouvido else 0
        porcentagem_faringite = (self.score_faringite / self.max_faringite) * 100 if self.max_faringite else 0

        # Decide o diagnóstico (exibindo ambos os resultados)
        print("\nDiagnóstico Otorrinolaringológico:")
        print(f"Infecção no ouvido: {self.score_infeccao_ouvido} pontos - {porcentagem_ouvido:.1f}% de chance ({', '.join(set(sintomas_ouvido))})")
        print(f"Faringite: {self.score_faringite} pontos - {porcentagem_faringite:.1f}% de chance ({', '.join(set(sintomas_faringite))})")

        # Mensagens adicionais para exames, se aplicável
        if exame_ouvido:
            print(f"\nComo a intensidade da dor no ouvido é alta, recomendo realizar o exame: {exame_ouvido}.")
        if exame_faringite:
            print(f"\nComo a intensidade da dor na garganta é alta, recomendo realizar o exame: {exame_faringite}.")
