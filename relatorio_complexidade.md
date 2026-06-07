# Relatório de Complexidade e Estruturas de Dados

Para atender aos requisitos de eficiência e aplicar os conceitos da disciplina, a arquitetura do sistema utiliza dois vetores espelhados para armazenar os produtos, cada um otimizado para um tipo de operação.

## 1. Busca Linear e Vetor Não Ordenado
Para operações de filtragem, como **Busca por Nome**, **Listagem por Categoria** e **Relatório de Estoque Baixo**, utilizamos o vetor não ordenado associado a uma busca linear clássica. 

* **Justificativa:** Como a busca por nome permite resultados parciais (ex: digitar "teclado" e retornar diferentes modelos) e nomes não são chaves únicas e sequenciais como os códigos numéricos, a ordenação alfabética constante seria custosa na inserção sem ganho significativo. A busca linear varre o vetor em tempo proporcional ao número de elementos, possuindo complexidade de tempo de $O(n)$.

## 2. Busca Binária e Vetor Ordenado
Para operações críticas envolvendo a identificação exata do produto (como **Busca por Código**, **Edição**, **Remoção** e **Registro de Venda**), o sistema mantém um vetor estritamente ordenado pelo campo numérico `codigo`.

* **Justificativa:** A busca binária corta o espaço de busca pela metade a cada iteração, resultando em uma complexidade assintótica extremamente eficiente de $O(\log n)$. Isso garante que, mesmo com um estoque com milhares de itens, as vendas e atualizações sejam processadas quase instantaneamente. 

## 3. Manutenção da Ordenação
Ao inserir um novo produto, o sistema utiliza busca binária para verificar a duplicidade em $O(\log n)$. Em seguida, ele localiza a posição correta e faz a inserção mantendo a ordenação. O deslocamento dos itens na lista durante a inserção gera um custo de $O(n)$, o que é um compromisso aceitável, visto que as operações de leitura e busca (vendas e consultas) tendem a ser muito mais frequentes do que o cadastro de novos itens.

