produtos = []

while True:

    print("\n=== SISTEMA DE CADASTRO ===")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
        produtos.append(produto)# Adiciona o produto à lista de produtos
        
        print("Produto cadastrado com sucesso!")


    elif opcao == "2":
        print("Listando produtos")

    elif opcao == "3":
        print("Saindo do sistema")
        break

    else:
        print("Opção inválida")