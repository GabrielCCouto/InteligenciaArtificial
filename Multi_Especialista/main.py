import os
import shutil
import threading
import time
from Enfermeira import Enfermeira
from Neurologista import Neurologista
from Pneumologista import Pneumologista
from Gastroenterologista import Gastroenterologista
from Otorrinolaringologista import Otorrinolaringologista

stop_event = threading.Event()

pasta_fichas = "QuadroDeFichas"
pasta_precisa = "PrecisaInvestigar"

def mover_fichas_nao_atendidas():
    try:
        if not os.path.exists(pasta_precisa):
            os.makedirs(pasta_precisa)
        for nome_arquivo in os.listdir(pasta_fichas):
            if nome_arquivo.endswith(".json"):
                try:
                    shutil.move(os.path.join(pasta_fichas, nome_arquivo),
                                os.path.join(pasta_precisa, nome_arquivo))
                except Exception as e:
                    print(f"Erro ao mover o arquivo {nome_arquivo}: {e}")
                    continue
        print("Fichas não atendidas foram movidas para 'PrecisaInvestigar'.")
    except Exception as e:
        print(f"Erro na função mover_fichas_nao_atendidas: {e}")

def especialista_runner(especialista):
    while not stop_event.is_set():
        try:
            if hasattr(especialista, "processar_fichas"):
                try:
                    especialista.processar_fichas()
                except Exception as e:
                    print(f"Erro em processar_fichas de {especialista.nome}: {e}")
            if hasattr(especialista, "processar_fichas_atendidos"):
                try:
                    especialista.processar_fichas_atendidos()
                except Exception as e:
                    print(f"Erro em processar_fichas_atendidos de {especialista.nome}: {e}")
        except Exception as ex:
            print(f"Erro no especialista {especialista.nome}: {ex}")
        time.sleep(2)

def main():
    if not os.path.exists(pasta_fichas):
            os.makedirs(pasta_fichas)

    if not os.path.exists(pasta_precisa):
            os.makedirs(pasta_precisa)

    # Inicia as threads dos especialistas
    especialistas = [
        Neurologista(),
        Pneumologista(),
        Gastroenterologista(),
        Otorrinolaringologista()
    ]
    threads = []
    for esp in especialistas:
        t = threading.Thread(target=especialista_runner, args=(esp,))
        t.daemon = True
        t.start()
        threads.append(t)

    # Cadastro dos pacientes pela enfermeira
    while True:
        try:
            enfermeira = Enfermeira()
            enfermeira.iniciar_triagem()
        except Exception as e:
            print(f"Erro no cadastro do paciente: {e}")
        continuar = input("\nDeseja registrar outro paciente? (s/n): ").strip().lower()
        if continuar not in ["s", "sim"]:
            break

    print("\nRegistro finalizado.")
    stop_event.set()
    time.sleep(2)

    # Finalização: cada especialista finaliza o atendimento (movendo as fichas para 'PacienteTeveAlta')
    for esp in especialistas:
        if hasattr(esp, "finalizar_atendimento"):
            try:
                esp.finalizar_atendimento()
            except Exception as e:
                print(f"Erro ao finalizar atendimento de {esp.nome}: {e}")
            break

    mover_fichas_nao_atendidas()

    print("\nAtendimento concluído. Verifique as pastas 'PacienteTeveAlta' e 'PrecisaInvestigar' para as fichas dos pacientes.")

if __name__ == "__main__":
    main()
