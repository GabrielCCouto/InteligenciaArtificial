class APP:
    def __init__(self, app):
        try:
            self.br = None
            self.ref_BR = None
            self.LOG = []
            self.LOG.append(app)
        except Exception as e:
            print("Exception lançada")
            print(e)

    def add_rule_base(self, ref_br):
        self.ref_BR = ref_br

    def show_log(self):
        for x in self.LOG:
            print(x, end=' ')

    def show_log_new_line(self):
        for x in self.LOG:
            print(x, end='\n')

    def clear_text(self):
        self.LOG.clear()
        self.LOG.append("")
        self.br.reset()

    def menu(self):
        naoCarregada = False
        while True:
            print('\n              : [0] sair', end='\n')
            print('        REGRAS: [1] carregar, [2] mostrar', end='\n')
            print(' FORWARD-CHAIN: [3] carregar variaveis, [4] executar, [7] reset', end='\n')
            print('BACKWARD-CHAIN: [5] carregar variaveis, [6] executar, [7] reset', end='\n')
            print('Digite sua opcao: ')
            option = int(input())

            if option == 0:
                return
            elif option == 1:
                if not naoCarregada:
                    self.br = self.ref_BR.create()
                    naoCarregada = True
                else:
                    print("Base de regas já foi carregada!!")
            elif option == 2:
                self.br.display_rules(self.LOG)
                self.show_log()
                self.LOG = []
            elif option == 3:
                self.ref_BR.demo_fc(self.LOG)
                self.show_log_new_line()
                self.LOG = []
            elif option == 4:
                self.LOG.append(" --- Starting Inferencing Cycle --- ")
                self.br.forward_chain()
                self.br.display_variables(self.LOG)
                self.show_log_new_line()
                self.LOG = []
            elif option == 5:
                self.ref_BR.demo_bc(self.LOG)
                self.show_log_new_line()
                self.LOG = []
            elif option == 6:
                goal_list = self.ref_BR.get_goal_list()
                print("Informe a variavel objetivo ", goal_list)
                goal = input()
                goal_var = self.br.get_variable(goal)
                if goal_var is not None:
                    self.br.backward_chain(goal)
                else:
                    self.LOG.append("goalVar.__name__: NAO ENCONTEADA")
                self.LOG.append(" --- Ending Inferencing Cycle --- ")
                if goal_var is not None:
                    result = goal_var.get_value()
                else:
                    result = "DESCONHECIDO"
                self.LOG.append("RESULTADO: " + str(result))
                self.br.display_variables(self.LOG)
                self.show_log_new_line()
                self.LOG = []
            elif option == 7:
                self.clear_text()
