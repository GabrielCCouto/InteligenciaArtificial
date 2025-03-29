# main.py
from enfermeira import Enfermeira
from medico import Medico

def main():
    enfermeira = Enfermeira()
    enfermeira.iniciar_triagem()
    if enfermeira.estado != "Bem" or (enfermeira.estado == "Bem" and enfermeira.consulta == "Retorno"):
        medico = Medico(enfermeira)
        medico.analisar_triagem()

if __name__ == "__main__":
    main()
