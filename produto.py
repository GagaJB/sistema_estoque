def criar_produto(codigo, nome, categoria, preco, quantidade):
    if preco <= 0:
        raise ValueError("Preço deve ser maior que zero.")
    if quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa.")
    
    return {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

def atualizar_dados_produto(produto, nome=None, categoria=None, preco=None, quantidade=None):
    if preco is not None and preco <= 0:
        raise ValueError("Preço deve ser maior que zero.")
    if quantidade is not None and quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa.")
    
    if nome is not None:
        produto["nome"] = nome
    if categoria is not None:
        produto["categoria"] = categoria
    if preco is not None:
        produto["preco"] = preco
    if quantidade is not None:
        produto["quantidade"] = quantidade
        
    return produto