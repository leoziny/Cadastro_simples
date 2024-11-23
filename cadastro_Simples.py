import time

# Lista global para armazenar os usuários
usuarios = []


def verificarListaVazia():
    """
    Verifica se a lista de usuários está vazia.

    Retorna:
        - True: se a lista estiver vazia.
        - False: se houver pelo menos um usuário cadastrado.
    """
    return len(usuarios) == 0


def mostrarUsuarios():
    """
    Exibe a lista de usuários cadastrados, incluindo nome, idade e gênero.
    Se não houver usuários cadastrados, informa que a lista está vazia.
    """
    if verificarListaVazia():
        print("\nAinda não foi cadastrado nenhum usuário!")
        return

    print("\nLista de usuários cadastrados:")
    for usuario in usuarios:
        print("-" * 40)
        print(f"Nome: {usuario['Nome']}\nIdade: {usuario['Idade']}\nGênero: {usuario['Gênero']}")
        print("-" * 40)
    input("Aperte Enter para voltar ao menu principal...")


def cadastrarUsuario():
    """
    Permite cadastrar novos usuários, solicitando nome, idade e sexo.
    O usuário é armazenado como um dicionário na lista global `usuarios`.
    Oferece a opção de continuar cadastrando ou finalizar.
    """
    while True:
        try:
            print("\n--- Cadastro de Usuário ---")
            nome = str(input("Digite o nome do usuário: ")).strip()
            idade = int(input("Digite a idade do usuário: "))

            # Validação do sexo
            while True:
                sexo = str(input("Digite o sexo (M ou F): ")).strip().lower()
                if sexo in ["m", "f"]:
                    sexo = "Masculino" if sexo == "m" else "Feminino"
                    break
                else:
                    print("Por favor, digite 'M' para masculino ou 'F' para feminino.")

            # Adiciona o usuário à lista
            cliente = {"Nome": nome, "Idade": idade, "Gênero": sexo}
            usuarios.append(cliente)
            print(f"\nUsuário cadastrado com sucesso: {cliente}")

            # Perguntar se deseja continuar
            while True:
                try:
                    escolha = int(input("\nDigite [1] para cadastrar outro ou [2] para finalizar: "))
                    if escolha in [1, 2]:
                        break
                    else:
                        print("Escolha um número válido (1 ou 2).")
                except ValueError:
                    print("Por favor, insira apenas números (1 ou 2).")

            if escolha == 2:
                break

        except ValueError:
            print("Por favor, insira um valor válido para a idade.")


def editarCliente():
    """
    Permite editar as informações de um cliente existente (nome ou idade).
    O usuário seleciona o cliente pela posição na lista e escolhe o que deseja alterar.
    """
    if verificarListaVazia():
        print("Ainda não foi cadastrado nenhum usuário!")
        return

    mostrarUsuarios()

    print("Qual desses você deseja editar?")
    while True:
        try:
            escolha = int(input("Digite o número do cliente (começando em 1): ")) - 1
            if escolha < 0 or escolha >= len(usuarios):
                print("Digite um número válido!")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")

    while True:
        print("\nO que deseja editar?")
        print("[1] Nome")
        print("[2] Idade")
        print("[3] Sair da edição")
        try:
            oqueEditar = int(input("Digite sua escolha: "))
            if oqueEditar == 1:
                novo_nome = str(input("Digite o novo nome: ")).strip()
                print(f"Nome alterado de {usuarios[escolha]['Nome']} para {novo_nome}")
                usuarios[escolha]["Nome"] = novo_nome
            elif oqueEditar == 2:
                nova_idade = int(input("Digite a nova idade: "))
                print(f"Idade alterada de {usuarios[escolha]['Idade']} para {nova_idade}")
                usuarios[escolha]["Idade"] = nova_idade
            elif oqueEditar == 3:
                print("Saindo da edição", end="")
                for _ in range(3):
                    print(".", end="")
                    time.sleep(0.4)
                print()
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")


def main():
    """
    Função principal que exibe o menu interativo e gerencia as operações.
    """
    while True:
        print("\n" + "-" * 40)
        print("Sistema de Gerenciamento de Clientes")
        print("[1] Cadastrar Cliente")
        print("[2] Listar Clientes")
        print("[3] Sair do Programa")
        print("[4] Editar Cliente")
        print("-" * 40)

        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha == 1:
                cadastrarUsuario()
            elif escolha == 2:
                mostrarUsuarios()
            elif escolha == 3:
                print("Saindo", end="")
                for _ in range(3):
                    print(".", end="")
                    time.sleep(0.4)
                print("\nAté mais!")
                break
            elif escolha == 4:
                editarCliente()
            else:
                print("Escolha inválida! Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")


# Inicia o programa
main()
