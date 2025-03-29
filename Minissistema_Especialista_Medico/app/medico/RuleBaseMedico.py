from api.esBooleanRuleBase import BooleanRuleBase
from api.esRuleVariable import RuleVariable
from api.esCondition import Condition
from api.esRule import Rule
from api.esClause import Clause

class RuleBaseMedico:

    def __init__(self, nome, listaDeObjetivos):
        self.br = BooleanRuleBase(nome)
        self.lista_de_objetivos = listaDeObjetivos

    def get_goal_list(self):
        return self.lista_de_objetivos

    def create(self):
        temperatura = RuleVariable(self.br, "temperatura")
        temperatura.set_labels("36 42")
        temperatura.set_prompt_text("Qual é a temperatura do paciente? [36, 42]")

        espirro = RuleVariable(self.br, "espirro")
        espirro.set_labels("sim nao")
        espirro.set_prompt_text("O paciente está espirrando? [sim, nao]")

        nariz_entupido = RuleVariable(self.br, "narizEntupido")
        nariz_entupido.set_labels("sim nao")
        nariz_entupido.set_prompt_text("O paciente está com nariz entupido? [sim, nao]")

        tosse = RuleVariable(self.br, "tosse")
        tosse.set_labels("nao seca produtiva")
        tosse.set_prompt_text("O paciente está com tosse? [nao, seca, produtiva]")

        dificuldade_engolir = RuleVariable(self.br, "dificuldadeEngolir")
        dificuldade_engolir.set_labels("sim nao")
        dificuldade_engolir.set_prompt_text("O paciente está com dificuldade para engolir? [sim, nao]")

        dor_cabeca = RuleVariable(self.br, "dorCabeca")
        dor_cabeca.set_labels("sim nao")
        dor_cabeca.set_prompt_text("O paciente está sentindo dor de cabeça? [sim, nao]")

        dor_corpo = RuleVariable(self.br, "dorCorpo")
        dor_corpo.set_labels("sim nao")
        dor_corpo.set_prompt_text("O paciente está sentindo dor no corpo? [sim, nao]")

        dor_articulacao = RuleVariable(self.br, "dorArticulacao")
        dor_articulacao.set_labels("sim nao")
        dor_articulacao.set_prompt_text("O paciente está sentindo dor nas articulações? [sim, nao]")

        pressao_peito = RuleVariable(self.br, "pressaoPeito")
        pressao_peito.set_labels("sim nao")
        pressao_peito.set_prompt_text("O paciente está sentindo pressão no peito? [sim, nao]")

        dificuldade_respirar = RuleVariable(self.br, "dificuldadeRespirar")
        dificuldade_respirar.set_labels("sim nao")
        dificuldade_respirar.set_prompt_text("O paciente está sentindo dificuldade para respirar? [sim, nao]")

        perda_olfato = RuleVariable(self.br, "perdaOlfato")
        perda_olfato.set_labels("sim nao")
        perda_olfato.set_prompt_text("O paciente está com perda de olfato? [sim, nao]")

        perda_paladar = RuleVariable(self.br, "perdaPaladar")
        perda_paladar.set_labels("sim nao")
        perda_paladar.set_prompt_text("O paciente está com perda de paladar? [sim, nao]")

        manchas_vermelhas = RuleVariable(self.br, "manchasVermelhas")
        manchas_vermelhas.set_labels("sim nao")
        manchas_vermelhas.set_prompt_text("O paciente está com manchas vermelhas pelo corpo? [sim, nao]")

        dor_olhos = RuleVariable(self.br, "dorOlhos")
        dor_olhos.set_labels("sim nao")
        dor_olhos.set_prompt_text("O paciente está com dor nos olhos? [sim, nao]")

        febre = RuleVariable(self.br, "febre")
        febre.set_labels("sim nao")
        febre.set_prompt_text("O paciente está com febre (acima de 37ºC)? [sim, nao]")

        febre_alta = RuleVariable(self.br, "febreAlta")
        febre_alta.set_labels("sim nao")
        febre_alta.set_prompt_text("O paciente está com febre alta (acima de 38ºC)? [sim, nao]")

        coriza = RuleVariable(self.br, "coriza")
        coriza.set_labels("sim nao")
        coriza.set_prompt_text("O paciente está com coriza? [sim, nao]")

        catarro = RuleVariable(self.br, "catarro")
        catarro.set_labels("sim nao")
        catarro.set_prompt_text("O paciente está com catarro? [sim, nao]")

        dor_garganta = RuleVariable(self.br, "dorGarganta")
        dor_garganta.set_labels("sim nao")
        dor_garganta.set_prompt_text("O paciente está com dor de garganta? [sim, nao]")

        pressao_face = RuleVariable(self.br, "pressaoFace")
        pressao_face.set_labels("sim nao")
        pressao_face.set_prompt_text("O paciente está com pressão na face? [sim, nao]")

        doenca = RuleVariable(self.br, "doenca")
        doenca.set_labels("gripe sinusite covid19 dengue pneumonia indefinido")
        doenca.set_prompt_text("Qual é a doença? [gripe, sinusite, covid19, dengue, pneumonia, indefinido]")

        c_equals = Condition("=")
        c_less_than = Condition("<")
        c_more_than = Condition(">")
        c_less_or_equal_than = Condition("<=")
        c_more_or_equal_than = Condition(">=")

        
        bicicleta = Rule(self.br, "bicicleta", [
            Clause(tipo_de_veiculo, c_equals, "velocipede"),
            Clause(numero_de_rodas, c_equals, "2"),
            Clause(motor, c_equals, "nao")
        ], Clause(veiculo, c_equals, "bicicleta"))


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

