from api.esMenu import APP
from app.veiculo.RuleBaseVehicle import RuleBaseVehicle

class Main:
    def __init__(self):
        self.app = APP("Rule Application")

    def main(self):
        try:
            # RuleBaseVehicle recebe dois parâmetros:
            # o primeiro é nome da base de regras e
            # o segundo é lista de várias presentes na base de regras.
            # Essas variáveis fazem parte dos possíveis objetivos
            br_vehicle = RuleBaseVehicle("Veiculos Rule Base", "[veiculo] :")
            self.app.add_rule_base(br_vehicle)
            self.app.menu()
        except Exception as e:
            print("Exception: RuleApp ", e.with_traceback())


if __name__ == '__main__':
    Main().main()
