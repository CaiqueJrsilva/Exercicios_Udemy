# Inicializa o dicionário de produtos
produtos = {}
codigo_produto = 1  # Inicializa o contador de códigos de produtos

def gerar_codigo_produto():
    global codigo_produto
    codigo = codigo_produto
    codigo_produto += 1
    return codigo

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    codigo = gerar_codigo_produto()
    produtos[codigo] = {'nome': nome, 'preco': preco, 'estoque': estoque}
    print(f"Produto {nome} cadastrado com sucesso! Código do Produto: {codigo}")

def editar_produto():
    codigo = int(input("Digite o código do produto que deseja editar: "))
    if codigo in produtos:
        novo_nome = input("Digite o novo nome: ")
        novo_preco = float(input("Digite o novo preço: "))
        novo_estoque = int(input("Digite a nova quantidade em estoque: "))
        produtos[codigo]['nome'] = novo_nome
        produtos[codigo]['preco'] = novo_preco
        produtos[codigo]['estoque'] = novo_estoque
        print(f"Produto {novo_nome} editado com sucesso!")
    else:
        print(f"Código do produto {codigo} não encontrado.")

def excluir_produto():
    codigo = int(input("Digite o código do produto que deseja excluir: "))
    if codigo in produtos:
        del produtos[codigo]
        print(f"Produto com código {codigo} excluído com sucesso!")
    else:
        print(f"Código do produto {codigo} não encontrado.")

def vender_produto():
    codigo = int(input("Digite o código do produto que deseja vender: "))
    if codigo in produtos:
        quantidade = int(input(f"Digite a quantidade de {produtos[codigo]['nome']} a ser vendida: "))
        if quantidade <= produtos[codigo]['estoque']:
            total = quantidade * produtos[codigo]['preco']
            print(f"Total a pagar: R$ {total:.2f}")
            pagamento = float(input("Digite o valor pago pelo cliente: "))
            troco = pagamento - total
            if troco >= 0:
                produtos[codigo]['estoque'] -= quantidade
                print(f"Venda realizada com sucesso! Troco: R$ {troco:.2f}")
            else:
                print("Valor insuficiente.")
        else:
            print("Estoque insuficiente.")
    else:
        print(f"Código do produto {codigo} não encontrado.")

def consultar_produto():
    codigo = int(input("Digite o código do produto que deseja consultar: "))
    if codigo in produtos:
        print(f"Código: {codigo}")
        print(f"Nome: {produtos[codigo]['nome']}")
        print(f"Preço: R$ {produtos[codigo]['preco']:.2f}")
        print(f"Estoque: {produtos[codigo]['estoque']} unidades")
    else:
        print(f"Código do produto {codigo} não encontrado.")

while True:
    print("\nMenu:")
    print("1 - Cadastrar Produto")
    print("2 - Editar Produto")
    print("3 - Excluir Produto")
    print("4 - Vender Produto")
    print("5 - Consultar Produto")
    print("6 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        editar_produto()
    elif opcao == '3':
        excluir_produto()
    elif opcao == '4':
        vender_produto()
    elif opcao == '5':
        consultar_produto()
    elif opcao == '6':
        break
    else:
        print("Opção inválida. Tente novamente.")
