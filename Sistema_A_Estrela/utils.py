import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_choice(options, prompt):
    while True:
        print(prompt)
        sorted_options = sorted(options.items())  # Ordena pelo número da opção
        for key, value in sorted_options:
            print(f"{key} - {value}")
        try:
            choice = int(input("\nEscolha uma opção: "))
            if choice in options:
                return options[choice]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
