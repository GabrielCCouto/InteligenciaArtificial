# sintomas.py

class Dor:
    def __init__(self):
        self.dor_no_peito = False
        self.intensidade_dor_no_peito = 0

        self.dor_na_cabeca = False
        self.dor_subita = False
        self.dor_gradual = False
        self.intensidade_dor_na_cabeca = 0

        self.dor_no_ouvido = False
        self.perda_auditiva = False
        self.ouvido_escorrendo = False
        self.intensidade_dor_no_ouvido = 0

        self.dor_na_garganta = False
        self.intensidade_dor_na_garganta = 0

        '''
            Perguntas que a Enfermeira deve fazer sobre Dor

            1 - Onde você está sentindo dor?
                Opções:
                    Se Peito
                        Então
                            dor_no_peito = True
                            Qual a intensidade da dor?
                                intensidade_dor_no_peito = intensidade dado pelo paciente
                            Você tem mais algum sintoma?
                                se sim Então fazer a pergunta inicial Qual seu sintoma? e começar tudo novamente
                                se não Finalizar
                    Se Cabeça
                        Então
                            dor_na_cabeca = True
                            Qual a intensidade da dor?
                                intensidade_dor_na_cabeca = intensidade dado pelo paciente
                            Como foi o inicio da dor?
                                Se Subita
                                    Então
                                        dor_subita = True
                                Se Gradual
                                    então
                                        dor_gradual = True
                            Você tem mais algum sintoma?
                                se sim Então fazer a pergunta inicial Qual seu sintoma? e começar tudo novamente
                                se não Finalizar


                    Se Ouvido
                        Então
                            dor_no_ouvido = True
                            Qual a intensidade da dor?
                                intensidade_dor_na_cabeca = intensidade dado pelo paciente
                            Sentiu perda auditiva?
                                se sim perda_auditiva = true
                            Seu ouvido está escorrendo?
                                se sim ouvido_escorrendo = True
                            Você tem mais algum sintoma?
                                se sim Então fazer a pergunta inicial Qual seu sintoma? e começar tudo novamente
                                se não Finalizar

                    Se Garganta

        '''

class Tosse:
    def __init__(self):
        self.tosse_com_muco = False
        self.tosse_seca = False
        self.dificuldade_respiratoria = False
        self.gripe_resfriado = False

class MalEstar:
    def __init__(self):
        self.enjoo = False
        self.refluxo = False
        self.dor_abdominal = False
        self.diarreia = False
        self.tontura = False
        self.movimento_involuntario = False
        self.movimento_involuntario = False
