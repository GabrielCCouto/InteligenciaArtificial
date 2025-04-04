# Gastroenterologista.py

class Gastroenterologista:
    """
    Especialista Gastroenterologista que utiliza as informações coletadas pela enfermeira para
    diagnosticar:
      - Refluxo gastroesofágico: associado a refluxo e enjoo.
      - Intoxicação alimentar: associado a dor abdominal e diarreia.
    O diagnóstico é calculado em porcentagem com base em pontuações definidas.
    """
    def __init__(self, enfermeira):
        self.enfermeira = enfermeira
        self.score_refluxo = 0
        self.score_intoxicacao = 0

        self.max_refluxo = 2
        self.max_intoxicacao = 2

    def analisar_triagem(self):
        print("\n--- Análise pelo Gastroenterologista ---")
        sintomas_refluxo = []
        sintomas_intoxicacao = []
        exame_recomendado = None

        # Processa os dados de "Mal Estar" para identificar refluxo e enjoo (Refluxo gastroesofágico)
        if "Mal Estar" in self.enfermeira.dados_sintomas:
            for mal in self.enfermeira.dados_sintomas["Mal Estar"]:
                if mal.refluxo:
                    self.score_refluxo += 1
                    sintomas_refluxo.append("refluxo")
                if mal.enjoo:
                    self.score_refluxo += 1
                    sintomas_refluxo.append("enjoo")
                # Processa também os dados para Intoxicação alimentar
                if mal.dor_abdominal:
                    self.score_intoxicacao += 1
                    sintomas_intoxicacao.append("dor abdominal")
                if mal.diarreia:
                    self.score_intoxicacao += 1
                    sintomas_intoxicacao.append("diarreia")

        # Calcula as porcentagens de chance para cada doença
        porcentagem_refluxo = (self.score_refluxo / self.max_refluxo) * 100 if self.max_refluxo else 0
        porcentagem_intoxicacao = (self.score_intoxicacao / self.max_intoxicacao) * 100 if self.max_intoxicacao else 0

        # Define o diagnóstico com base na pontuação
        if self.score_refluxo >= self.score_intoxicacao:
            diagnostico = f"Refluxo gastroesofágico ({porcentagem_refluxo:.1f}% de chance)"
        else:
            diagnostico = f"Intoxicação alimentar ({porcentagem_intoxicacao:.1f}% de chance)"

        # Monta a mensagem final
        sintomas_str_refluxo = ", ".join(set(sintomas_refluxo))
        sintomas_str_intoxicacao = ", ".join(set(sintomas_intoxicacao))
        print("\nDiagnóstico Gastrointestinal:")
        print(f"Refluxo gastroesofágico: {self.score_refluxo} pontos - {porcentagem_refluxo:.1f}% de chance ({sintomas_str_refluxo})")
        print(f"Intoxicação alimentar: {self.score_intoxicacao} pontos - {porcentagem_intoxicacao:.1f}% de chance ({sintomas_str_intoxicacao})")
        print(f"\nVerifiquei sua ficha e, de acordo com os sintomas, você provavelmente está com: {diagnostico}")

        # Exemplo: se o paciente apresentar refluxo intenso, o especialista pode solicitar exames específicos.
        if self.score_refluxo == self.max_refluxo:
            print("Como os sintomas de refluxo são intensos, vou solicitar exames complementares (ex.: endoscopia).")
