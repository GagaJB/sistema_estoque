# Sistema de Estoque e Vendas

Sistema de linha de comando para controle de produtos e gestão de estoque, desenvolvido em Python. O projeto aplica conceitos de estruturas de dados e análise de complexidade de algoritmos.

## Funcionalidades
* Cadastro, edição e remoção de produtos.
* Busca O(log n) por código e busca O(n) por nome.
* Registro de vendas com validação de estoque.
* Relatórios de produtos por categoria e de estoque baixo.
* Persistência de dados automática em arquivo JSON.

## Como Executar

Certifique-se de ter o Python 3 instalado na sua máquina.

1. Clone este repositório:
```bash
git clone https://github.com/GagaJB/sistema_estoque.git
```

2. Acesse a pasta do projeto:
```bash
cd sistema_estoque
```

3. Execute o arquivo principal:
```bash
python main.py
```

## Exemplo de Uso
Ao iniciar o sistema, um menu interativo será exibido. Você pode começar digitando 1 para cadastrar o primeiro produto (ex: Código: 101, Nome: Teclado Mecânico, Categoria: Periféricos, Preço: 250.00, Quantidade: 15). Os dados serão salvos automaticamente no arquivo `estoque.json`.

---
**Autores:** Gabriel de Jesus, Arthur Augusto, Isaque Rocha, Kaio Vinicyus, Nicolas Pereira
````https://github.com/GagaJB/sistema_estoque