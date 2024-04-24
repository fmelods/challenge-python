# Este código Python é um sistema de login e menu de funcionalidades do Site MechAI.

import os

# Tela de Login
def main_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("|  Menu  |")
    print("=" * 50)
    print("1. Usuário Logar")
    print("2. Mecânico Logar")
    print("3. Fechar")
    print("=" * 50)

    option = input("Selecione uma opção: ")

    if option == "1":
        user_login_screen()
    elif option == "2":
        mechanic_login_screen()
    elif option == "3":
        print("Fechando...")
    else:
        print("Opção inválida. Tente novamente.")
        main_screen()

def user_login_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tela de Login do Usuário")
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username in ["marcos", "leo", "melo"] and password == "123":
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta. Tente novamente.")
        user_login_screen()

main_screen()

print ()

# Menu Principal com 3 Funcionalidades e Saída
def menu_principal():
    print("Bem-vindo ao MechAI - Assistente de Diagnóstico e Reparo Automotivo")
    print("1 - Diagnóstico do Veículo")
    print("2 - Encontrar Mecânicos Próximos")
    print("3 - Confirmar Serviço")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

print()

# Funcionalidade 1
def diagnosticar_veiculo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nIniciando o Diagnóstico do Veículo...")
    input("Descreva o problema do seu veículo: ")
    # Simulação de diagnóstico
    problemas_identificados = ['falha no motor', 'problema nos freios', 'vazamento de óleo']
    print(f"Diagnóstico sugerido: {problemas_identificados[0]} - baseado na sua descrição.")
    return problemas_identificados[0]

print()

# Funcionalidade 2
def encontrar_mecanicos(problema):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nEncontrando mecânicos próximos que podem resolver: ", problema)
    # Simulação de opções de mecânicos
    mecanicos = [('Alberto - Auto Fix', '14:00 PM - 22 de abril'), ('Ricardo - FindRepair', '11:30 AM - 23 de abril')]
    for i, mecanico in enumerate(mecanicos):
        print(f"{i+1} - {mecanico[0]}, horários disponíveis: {mecanico[1]}")
    
    try:
        escolha = int(input("Escolha um mecânico: "))
        if escolha < 1 or escolha > len(mecanicos):
            print("Opção inválida. Escolha um número dentro das opções disponíveis.")
            return encontrar_mecanicos(problema)  # Recursivamente chama a função novamente
        return mecanicos[escolha-1]
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return encontrar_mecanicos(problema)

print()

# Funcionalidade 3
def confirmar_servico(mecanico):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nConfirmação de Serviço")
    print(f"Você escolheu {mecanico[0]} para o horário {mecanico[1]}.")
    while True:
        confirmar = input("Digite 'sim' para confirmar ou 'não' para cancelar: ")
        if confirmar.lower() == 'sim':
            print("Serviço confirmado, será gerado uma fatura. Por favor, após o pagamento, dirija-se ao endereço do mecânico escolhido.")
            break
        elif confirmar.lower() == 'não':
            print("Serviço não confirmado.")
            break
        else:
            print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

print()

# Implementação do menu
def main():
    while True:
        escolha = menu_principal()
        if escolha == '1':
            problema = diagnosticar_veiculo()
        elif escolha == '2':
            if 'problema' in locals():
                mecanico = encontrar_mecanicos(problema)
            else:
                print("Por favor, realize o diagnóstico do veículo primeiro.")
        elif escolha == '3':
            if 'mecanico' in locals():
                confirmar_servico(mecanico)
            else:
                print("Por favor, escolha um mecânico primeiro.")
        # Saída
        elif escolha == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Obrigado por usar o MechAI. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()