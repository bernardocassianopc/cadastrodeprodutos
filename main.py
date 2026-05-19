from funcoes import *
from database import conexao

#Menu principal do sistema

while True:

    print("\n=== SISTEMA DE CADASTRO ===")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Excluir produto")
    print("5 - Editar produto")
    print("6 - Sair do sistema")

    opcao = input("Escolha uma opção: ")


#CADASTRAR PRODUTO

    if opcao == "1":
        cadastrar_produtos()

#LISTAR PRODUTOS

    elif opcao == "2":
        listar_produtos()

#BUSCAR PRODUTO

    elif opcao == "3":
        buscar_produto()  

#EXCLUIR PRODUTO

    elif opcao == "4":
        excluir_produto()

 #EDITAR PRODUTO
    elif opcao == "5":

        editar_produto()

#SAIR DO SISTEMA

    elif opcao == "6":

        print("Saindo do sistema")
        break
        
    else:

        print("Opção inválida")

conexao.close()