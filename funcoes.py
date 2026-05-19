from database import cursor, conexao
# Sistema de cadastro de produtos

def cadastrar_produtos():

    nome = input("Digite o nome do produto: ")
    try:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
    except ValueError:
        print("Valor inválido. Certifique-se de digitar um número para preço e quantidade")
        return


    cursor.execute("""
    INSERT INTO produtos (nome, preco, quantidade)
    VALUES (?, ?, ?)
    """, (nome, preco, quantidade))

    conexao.commit()

    print("Produto cadastrado com sucesso!")

#Sistema de Listar produtos
def listar_produtos():

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    if len(produtos) == 0:

        print("Nenhum produto cadastrado")

    else:

        for produto in produtos:

            print("\nProduto:")
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Preço: R${produto[2]}")
            print(f"Quantidade: {produto[3]}")


#Sistema de Buscar produtos
       
def buscar_produto():

    busca = input("Digite o nome do produto: ")

    cursor.execute(
        "SELECT * FROM produtos WHERE nome = ?",
        (busca,)
    )

    produto = cursor.fetchone()

    if produto:

        print("\nProduto encontrado:")
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Preço: R${produto[2]}")
        print(f"Quantidade: {produto[3]}")

    else:

        print("Produto não encontrado")

#Sistema de Excluir produtos

def excluir_produto():

    nome_excluir = input("Digite o nome do produto que deseja excluir: ")

    cursor.execute(
        "SELECT * FROM produtos WHERE nome = ?",
        (nome_excluir,)
    )

    produto = cursor.fetchone()

    if produto:

        cursor.execute(
            "DELETE FROM produtos WHERE nome = ?",
            (nome_excluir,)
        )

        conexao.commit()

        print("Produto excluído com sucesso!")

    else:

        print("Produto não encontrado")

#Sistema de Editar produtos

def editar_produto():

    nome_busca = input("Digite o nome do produto que deseja editar: ")

    cursor.execute(
        "SELECT * FROM produtos WHERE nome = ?",
        (nome_busca,)
    )

    produto = cursor.fetchone()

    if produto:

        novo_nome = input("Novo nome: ")
        novo_preco = float(input("Novo preço: "))
        nova_quantidade = int(input("Nova quantidade: "))

        cursor.execute("""
        UPDATE produtos
        SET nome = ?, preco = ?, quantidade = ?
        WHERE nome = ?
        """, (novo_nome, novo_preco, nova_quantidade, nome_busca))

        conexao.commit()

        print("Produto atualizado com sucesso!")

    else:

        print("Produto não encontrado")