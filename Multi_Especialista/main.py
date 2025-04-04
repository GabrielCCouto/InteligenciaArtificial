# main.py
from Enfermeira import Enfermeira
from Neurologista import Neurologista
from Pneumologista import Pneumologista
from Gastroenterologista import Gastroenterologista
from Otorrinolaringologista import Otorrinolaringologista

def main():
    enfermeira = Enfermeira()
    enfermeira.iniciar_triagem()

    # Encaminhamento automático definido na enfermeira
    if "Neurologista" in enfermeira.encaminhar_especialista:
        neurologista = Neurologista(enfermeira)
        neurologista.analisar_triagem()
    if "Pneumologista" in enfermeira.encaminhar_especialista:
        pneumologista = Pneumologista(enfermeira)
        pneumologista.analisar_triagem()
    if "Gastroenterologista" in enfermeira.encaminhar_especialista:
        gastro = Gastroenterologista(enfermeira)
        gastro.analisar_triagem()
    if "Otorrinolaringologista" in enfermeira.encaminhar_especialista:
        otorrino = Otorrinolaringologista(enfermeira)
        otorrino.analisar_triagem()

if __name__ == "__main__":
    main()
