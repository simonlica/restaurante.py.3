import os

restaurantes = [
    {'nome': 'Lilica na cozinha ', 'categoria': 'prato-feito', 'ativo': True},
    {'nome': 'Simons', 'categoria': 'pizzaria', 'ativo': False},
    {'nome': 'Lanche ou Net', 'categoria': 'lanchonete', 'ativo': True}
]

def finalizar_app():
    os.system("clear")
    os.system("cls")
    print("Finalizando o app\n")

def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")

def mostrar_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()

def escolher_opcoes():
    mostrar_subtitulo("Programa Expresso\n")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def opcao_invalida():
    mostrar_subtitulo("Opção inválida\n")
    voltar_menu_principal()

def chamar_nome_do_app():
     print ('''ℜ𝔈𝔰𝔱𝔞𝔲𝔯𝔞𝔫𝔱𝔢 𝔢𝔵𝔭𝔯𝔢𝔰𝔰𝔬''') 

def listarRestaurantes():
    mostrar_subtitulo('Listando os Restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'-{nome_restaurante}--{categoria}--{ativo}')

def cadastrar_novo_restaurante():
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"Você cadastrou o restaurante: {nome_do_restaurante}")

def main():
    while True:
        try:
            escolher_opcoes()
            opcaodigitada = int(input("Digite a opção desejada: "))
            if opcaodigitada == 1:
                print("Você escolheu cadastrar restaurante\n")
                cadastrar_novo_restaurante()
                main()
            elif opcaodigitada == 2:
                listarRestaurantes()
                voltar_menu_principal()
                main()
            elif opcaodigitada == 3:
                print("Você escolheu ativar restaurante\n")
                main()
            elif opcaodigitada == 4:
                print("Você escolheu sair do aplicativo\n")
                finalizar_app()
                break
            else:
                opcao_invalida()
                main()
        except ValueError:
            print("Por favor, digite um número.")
            main()

if __name__ == "__main__":
    chamar_nome_do_app()
    main()