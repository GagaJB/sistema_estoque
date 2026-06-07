import arquivos
import estoque

# --- Funções Auxiliares de Entrada ---
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número inteiro numérico válido.")

def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido.")

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Erro: O campo não pode ficar vazio.")

# --- Menu Principal ---
def exibir_menu():
    print("\n" + "="*45)
    print("      SISTEMA DE ESTOQUE E VENDAS - UNASP      ")
    print("="*45)
    print("1. Cadastrar Produto")
    print("2. Editar Produto")
    print("3. Remover Produto")
    print("4. Buscar Produto por Código (Busca Binária)")
    print("5. Buscar Produto por Nome (Busca Linear)")
    print("6. Registrar Venda")
    print("7. Listar Todos os Produtos (Ordenados)")
    print("8. Listar Produtos por Categoria")
    print("9. Relatório de Estoque Baixo")
    print("0. Sair")
    print("="*45)

def main():
    dados = arquivos.carregar_dados()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                print("\n-- Cadastro de Produto --")
                codigo = ler_inteiro("Código: ")
                nome = ler_texto("Nome: ")
                categoria = ler_texto("Categoria: ")
                preco = ler_float("Preço: ")
                quantidade = ler_inteiro("Quantidade: ")
                
                dados = estoque.adicionar_produto(dados, codigo, nome, categoria, preco, quantidade)
                arquivos.salvar_dados(dados)
                print("Produto cadastrado com sucesso!")

            elif opcao == '2':
                print("\n-- Editar Produto --")
                codigo = ler_inteiro("Código do produto a editar: ")
                print("Deixe em branco se não quiser alterar o campo.")
                
                nome = input("Novo Nome: ").strip() or None
                categoria = input("Nova Categoria: ").strip() or None
                
                preco_str = input("Novo Preço: ").strip()
                preco = float(preco_str.replace(',', '.')) if preco_str else None
                
                qtd_str = input("Nova Quantidade: ").strip()
                quantidade = int(qtd_str) if qtd_str else None
                
                dados = estoque.editar_produto(dados, codigo, nome, categoria, preco, quantidade)
                arquivos.salvar_dados(dados)
                print("Produto editado com sucesso!")

            elif opcao == '3':
                print("\n-- Remover Produto --")
                codigo = ler_inteiro("Código do produto a remover: ")
                dados = estoque.remover_produto(dados, codigo)
                arquivos.salvar_dados(dados)
                print("Produto removido com sucesso!")

            elif opcao == '4':
                print("\n-- Busca por Código --")
                codigo = ler_inteiro("Código: ")
                indice = estoque.busca_binaria_por_codigo(dados["ordenado"], codigo)
                if indice != -1:
                    print("\nProduto encontrado:", dados["ordenado"][indice])
                else:
                    print("Produto não encontrado.")

            elif opcao == '5':
                print("\n-- Busca por Nome --")
                nome = ler_texto("Nome: ")
                resultados = estoque.busca_linear_por_nome(dados["nao_ordenado"], nome)
                if resultados:
                    for p in resultados:
                        print(p)
                else:
                    print("Nenhum produto encontrado com esse nome.")

            elif opcao == '6':
                print("\n-- Registrar Venda --")
                codigo = ler_inteiro("Código do produto: ")
                qtd = ler_inteiro("Quantidade vendida: ")
                dados = estoque.registrar_venda(dados, codigo, qtd)
                arquivos.salvar_dados(dados)
                print("Venda registrada e estoque atualizado com sucesso!")

            elif opcao == '7':
                print("\n-- Lista de Produtos (Ordenados por Código) --")
                if not dados["ordenado"]:
                    print("Nenhum produto cadastrado.")
                for p in dados["ordenado"]:
                    print(p)

            elif opcao == '8':
                print("\n-- Lista por Categoria --")
                categoria = ler_texto("Categoria: ")
                resultados = estoque.listar_por_categoria(dados, categoria)
                if resultados:
                    for p in resultados:
                        print(p)
                else:
                    print("Nenhum produto encontrado nesta categoria.")

            elif opcao == '9':
                print("\n-- Relatório de Estoque Baixo --")
                limite = ler_inteiro("Defina o limite de quantidade: ")
                resultados = estoque.relatorio_estoque_baixo(dados, limite)
                if resultados:
                    for p in resultados:
                        print(p)
                else:
                    print("Nenhum produto está abaixo do limite.")

            elif opcao == '0':
                print("Saindo do sistema... Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as e:
            print(f"Erro de Validação: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()