from produto import criar_produto

def busca_binaria_por_codigo(vetor_ordenado, codigo):
    inicio = 0
    fim = len(vetor_ordenado) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        codigo_meio = vetor_ordenado[meio]["codigo"]
        
        if codigo_meio == codigo:
            return meio
        elif codigo_meio < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return -1 # Não encontrado

def busca_linear_por_nome(vetor_nao_ordenado, nome):
    resultados = []
    nome_lower = nome.lower()
    
    for i in range(len(vetor_nao_ordenado)):
        if nome_lower in vetor_nao_ordenado[i]["nome"].lower():
            resultados.append(vetor_nao_ordenado[i])
            
    return resultados

def adicionar_produto(dados, codigo, nome, categoria, preco, quantidade):
    indice_existente = busca_binaria_por_codigo(dados["ordenado"], codigo)
    if indice_existente != -1:
        raise ValueError("Já existe um produto cadastrado com este código.")
        
    novo_produto = criar_produto(codigo, nome, categoria, preco, quantidade)
    
    dados["nao_ordenado"].append(novo_produto)
    
    vetor_ord = dados["ordenado"]
    posicao = 0
    while posicao < len(vetor_ord) and vetor_ord[posicao]["codigo"] < codigo:
        posicao += 1
        
    vetor_ord.insert(posicao, novo_produto)
    return dados

def remover_produto(dados, codigo):
    indice_ord = busca_binaria_por_codigo(dados["ordenado"], codigo)
    if indice_ord == -1:
        raise ValueError("Produto não encontrado para remoção.")
        
    dados["ordenado"].pop(indice_ord)
    
    for i in range(len(dados["nao_ordenado"])):
        if dados["nao_ordenado"][i]["codigo"] == codigo:
            dados["nao_ordenado"].pop(i)
            break
            
    return dados