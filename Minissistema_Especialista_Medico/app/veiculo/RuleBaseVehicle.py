from api.esBooleanRuleBase import BooleanRuleBase
from api.esRuleVariable import RuleVariable
from api.esCondition import Condition
from api.esRule import Rule
from api.esClause import Clause

class RuleBaseVehicle:

    def __init__(self, nome, listaDeObjetivos):
        self.br = BooleanRuleBase(nome)
        self.lista_de_objetivos = listaDeObjetivos

    def get_goal_list(self):
        return self.lista_de_objetivos

    def create(self):
        veiculo = RuleVariable(self.br, "veiculo")
        veiculo.set_labels("bicicleta triciclo motocicleta carroEsporte sedan minivan")
        veiculo.set_prompt_text("Que tipo de veículo é esse {bicicleta triciclo motocicleta carroEsporte sedan minivan} ?")

        tipo_de_veiculo = RuleVariable(self.br, "tipoDeVeiculo")
        tipo_de_veiculo.set_labels("velocipede automotivo")
        tipo_de_veiculo.set_prompt_text("Que tipo de veículo é esse {velocipede  automotivo} ?")

        tamanho = RuleVariable(self.br, "tamanho")
        tamanho.set_labels("pequeno medio grande")
        tamanho.set_prompt_text("Qual o tamanho do veículo {pequeno medio grande} ?")

        motor = RuleVariable(self.br, "motor")
        motor.set_labels("sim nao")
        motor.set_prompt_text("O veículo tem um motor {sim nao} ?")

        numero_de_rodas = RuleVariable(self.br, "numeroDeRodas")
        numero_de_rodas.set_labels("2 3 4")
        numero_de_rodas.set_prompt_text("Quantas rodas o veículo possui {2 3 4} ?")

        numeroDePortas = RuleVariable(self.br, "numeroDePortas")
        numeroDePortas.set_labels("2 3 4")
        numeroDePortas.set_prompt_text("Quantas portas o veículo tem {2 3 4} ?")

        c_equals = Condition("=")
        c_not_equals = Condition("!=")
        c_less_than = Condition("<")

        bicicleta = Rule(self.br, "bicicleta", [
            Clause(tipo_de_veiculo, c_equals, "velocipede"),
            Clause(numero_de_rodas, c_equals, "2"),
            Clause(motor, c_equals, "nao")
        ], Clause(veiculo, c_equals, "bicicleta"))

        triciclo = Rule(self.br, "triciclo", [
            Clause(tipo_de_veiculo, c_equals, "velocipede"),
            Clause(numero_de_rodas, c_equals, "3"),
            Clause(motor, c_equals, "nao")
        ], Clause(veiculo, c_equals, "triciclo"))

        motocicleta = Rule(self.br, "motocicleta", [
            Clause(tipo_de_veiculo, c_equals, "velocipede"),
            Clause(numero_de_rodas, c_equals, "2"),
            Clause(motor, c_equals, "sim")
       ], Clause(veiculo, c_equals, "motocicleta"))

        carroEsporte = Rule(self.br, "sportsCar", [
            Clause(tipo_de_veiculo, c_equals, "automotivo"),
            Clause(tamanho, c_equals, "medio"),
            Clause(numeroDePortas, c_equals, "2")
        ], Clause(veiculo, c_equals, "carroEsporte"))

        sedan = Rule(self.br, "sedan",
                     [Clause(tipo_de_veiculo, c_equals, "automotivo"),
                      Clause(tamanho, c_equals, "medio"),
                      Clause(numeroDePortas, c_equals, "4")],
                     Clause(veiculo, c_equals, "sedan"))

        minivan = Rule(self.br, "minivan",
                       [Clause(tipo_de_veiculo, c_equals, "automotivo"),
                        Clause(tamanho, c_equals, "medio"),
                        Clause(numeroDePortas, c_equals, "3")],
                       Clause(veiculo, c_equals, "minivan"))

        suv = Rule(self.br, "SUV",
                   [Clause(tipo_de_veiculo, c_equals, "automotivo"),
                    Clause(tamanho, c_equals, "grande"),
                    Clause(numeroDePortas, c_equals, "4")],
                   Clause(veiculo, c_equals, "veiculoEsporteUtilitario"))

        velocipede = Rule(self.br, "velocipede ",
                          [Clause(numero_de_rodas, c_less_than, "4")],
                          Clause(tipo_de_veiculo, c_equals, "velocipede "))

        automotivo = Rule(self.br, "automotivo",
                          [Clause(numero_de_rodas, c_equals, "4"),
                           Clause(motor, c_equals, "sim")],
                          Clause(tipo_de_veiculo, c_equals, "automotivo"))

        return self.br

    def demo_fc(self, LOG):
        LOG.append("\n --- Ajustando valores para Tipo de Veículo para demo ForwardChain --- ")
        self.br.set_variable_value("veiculo", None)
        self.br.set_variable_value("tipoDeVeiculo", None)
        self.br.set_variable_value("tamanho", "grande")
        self.br.set_variable_value("numeroDeRodas", "4")
        self.br.set_variable_value("numeroDePortas", "4")
        self.br.set_variable_value("motor", "sim")
        self.br.display_variables(LOG)

    def demo_bc(self, LOG):
        LOG.append("\n --- Ajustando valores para Tipo de Veículo para demo BackwardChain ---")
        self.br.set_variable_value("veiculo", None)
        self.br.set_variable_value("tipoDeVeiculo", None)
        self.br.set_variable_value("tamanho", None)
        self.br.set_variable_value("numeroDeRodas", "4")
        self.br.set_variable_value("numeroDePortas", None)
        self.br.set_variable_value("motor", "sim")
        self.br.display_variables(LOG)

