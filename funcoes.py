def realizar_login():

    cor_vermelha = '\033[91m'
    cor_amarela = '\033[93m'
    cor_ciano = '\033[96m'
    cor_verde = '\033[92m'
    cor_reset = '\033[0m'

    print(cor_ciano + "==================== Área de Login ====================\n\n" + cor_reset)
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    try:
        
        with open('usuarios.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

            
            for linha in linhas:
                usuario_arquivo, senha_arquivo = linha.strip().split(',')
                if usuario == usuario_arquivo and senha == senha_arquivo:
                    print(cor_verde + "\nLogin bem-sucedido!" + cor_reset)
                    return True
                
        print(cor_vermelha + "\nUsuário ou senha incorretos." + cor_reset)
        return False
        

    except FileNotFoundError:
        
        with open('usuarios.txt', 'w') as arquivo:
            pass  

        cadastrar_usuario_senha()  
        return True
    
def cadastrar_usuario_senha():
    cor_amarela = '\033[93m'
    cor_ciano = '\033[96m'
    cor_verde = '\033[92m'
    cor_reset = '\033[0m'

    print(cor_ciano + "==================== Área de cadastro ====================\n\n" + cor_reset)
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    try:
        with open('usuarios.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                usuario_arquivo, _ = linha.strip().split(',')
                if usuario == usuario_arquivo:
                    print(cor_amarela + "\nUsuário já cadastrado!" + cor_reset)
                    menu_principal()
                    return

        # Se o usuário não estiver cadastrado, adiciona ao arquivo
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f"{usuario},{senha}\n")

        print(cor_verde + "\nUsuário cadastrado com sucesso!" + cor_reset)
        print("Agora realize o Login!\n")

    except FileNotFoundError:
        # Se o arquivo não existir, cria um novo
        with open('usuarios.txt', 'w') as arquivo:
            arquivo.write(f"{usuario},{senha}\n")

        print(cor_verde + "\nUsuário cadastrado com sucesso!" + cor_reset)
        print("Agora realize o Login!\n")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

            

def pre_consulta():
    
    cor_verde = '\033[92m'
    cor_reset = '\033[0m'

    while True:
        nome = input("Digite o seu nome: ")
        idade = input("Digite a sua idade: ")
        tipo_s = input("Digite o seu tipo sanguineo: ")
        alergia = input("Você possui algum tipo de alergia? Se sim qual? ")
        medicacao = input("Você toma algum tipo de remedio? Se sim qual? ")
        motivo = input("Qual o motivo da consulta?")

        with open('consultas.txt', 'a') as arquivo:
            arquivo.write(f"{nome},{idade},{tipo_s},{alergia},{medicacao},{motivo}\n")

        print(cor_verde + "\nConsulta agendada com sucesso!" + cor_reset) 

        op_preconsulta()
       


def op_preconsulta():
    cor_vermelha = '\033[91m'
    cor_reset = '\033[0m' 

    while True:
        try:
            op = int(input("Digite [1] para realizar outra pré consulta ou [2] para sair.\n"))

            if op == 2:
                menu_principal()
                break
            elif op == 1:
                pre_consulta()
            else:
                print("\033[91m\nOperação inválida. Escolha uma opção válida!\033[0m")
        except ValueError:
            print("\033[91m\nEntrada inválida. Por favor, digite um número!\033[0m")



def menu_principal():
    cor_vermelha = '\033[91m'
    cor_ciano = '\033[96m'
    cor_reset = '\033[0m'

    print(cor_ciano + "\n\n==================== Bem vindo! ====================" + cor_reset + "\nPara acessar a pré-consulta faça login ou cadastre-se.")
    cor_vermelha = "\033[91m"
    cor_reset = "\033[0m"

    while True:
        try:
            op = int(input("\n\nEscolha uma das opções abaixo e digite o número correspondente: \n[1] para login \n[2] para se cadastrar \n[3] para sair\n"))
            
            if op == 1:
                logado = realizar_login() 
                if logado:
                    print(cor_ciano + "==================== Bem-vindo à Pré-consulta! ====================" + cor_reset + "\nPreencha as perguntas seguintes para agilizar a sua consulta e ter um atendimento mais eficaz.\n\n")
                    pre_consulta()
            elif op == 2:
                cadastrar_usuario_senha()
            elif op == 3:
                break
            else:
                print(cor_vermelha + "\nOperação inválida. Escolha uma opção válida!" + cor_reset)
        except ValueError:
            print(cor_vermelha + "\nErro: Por favor, digite apenas números para escolher uma opção!" + cor_reset)
            
            
    