# Laboratório de Grafos, BFS e DFS

Disciplina: Estrutura de Dados II — Ciência da Computação
Estudo de caso motivador: pane relacionada ao GPS no Aeroporto de Brasília (G1, 22 set. 2026).

> **Aviso:** simulação computacional didática. As conexões são fictícias e o programa não serve para orientar voos reais.

## Problema e objetivo

Uma indisponibilidade de recursos de navegação pode forçar replanejamento. Aqui, as conexões entre cidades são modeladas como um grafo para estudar conectividade e comparar BFS e DFS.

**Pergunta de pesquisa:** na rede fictícia, quantas conexões podem ser bloqueadas antes que Brasília deixe de alcançar Curitiba, e como BFS e DFS se comportam em cada cenário?

## Estrutura do grafo

Grafo não dirigido, 9 vértices e 15 arestas, em lista de adjacência (dicionário de listas), gerada a partir de uma lista de conexões para garantir simetria.

![Diagrama do grafo](https://graphonline.top/tmp/saved/SC/SCJljPqzviMsRRBs.svg)

| Aresta | Justificativa (fictícia) |
|---|---|
| Brasília–Goiânia, Brasília–Uberlândia, Brasília–Belo Horizonte | Brasília como hub com três saídas |
| Goiânia–Uberlândia | corredor Goiás–Triângulo Mineiro |
| Goiânia–São Paulo | ligação Centro-Oeste–Sudeste |
| Uberlândia–Belo Horizonte, Uberlândia–Campinas | ligações pelo Triângulo Mineiro |
| Belo Horizonte–Rio de Janeiro, Belo Horizonte–São Paulo, Rio de Janeiro–São Paulo | malha entre metrópoles do Sudeste |
| São Paulo–Campinas | ligação metropolitana |
| São Paulo–Curitiba, Rio de Janeiro–Curitiba | entradas do Sul via Sudeste |
| Campinas–Londrina, Londrina–Curitiba | rota alternativa pelo interior |

Curitiba tem grau 3 (São Paulo, Rio de Janeiro, Londrina), então são necessários 3 bloqueios para isolá-la.

## Resultados (Brasília → Curitiba)

| Cenário | BFS | DFS |
|---|---|---|
| A. Rede completa | Brasília → Goiânia → São Paulo → Curitiba (3 arestas) | Brasília → Goiânia → Uberlândia → Belo Horizonte → Rio de Janeiro → São Paulo → Campinas → Londrina → Curitiba (8 arestas) |
| B. Bloqueio São Paulo–Curitiba | Brasília → Belo Horizonte → Rio de Janeiro → Curitiba (3 arestas) | mesmo caminho de 8 arestas |
| C1. + bloqueio Rio de Janeiro–Curitiba | Brasília → Uberlândia → Campinas → Londrina → Curitiba (4 arestas) | mesmo caminho de 8 arestas |
| C2. + bloqueio Londrina–Curitiba | sem caminho | sem caminho |
| D. Vizinhos de Brasília invertidos | 3 arestas (outro caminho de mesmo tamanho) | 6 arestas (caminho diferente) |

**Interpretação:**
- **B:** o bloqueio não desconecta a rede; o BFS encontra outra rota com o mesmo número de arestas.
- **C2:** Curitiba fica isolada (grau 0), o grafo deixa de ser conexo e os dois algoritmos devolvem `None`. A resposta à pergunta de pesquisa é: **2 bloqueios ainda deixam caminho; o 3º, nas arestas de Curitiba, o elimina.**
- **D:** o grafo é o mesmo, mas a ordem dos vizinhos muda o caminho do DFS.

## Comparação BFS × DFS

| | BFS | DFS |
|---|---|---|
| Estrutura | fila (FIFO) | pilha (LIFO) |
| Caminho com menos arestas | sim, em grafo não ponderado | não garantido |
| Depende da ordem dos vizinhos | só para desempate | sim, muito |
| Encontra caminho se existir | sim | sim |

## Limitações

- "Menor caminho" do BFS significa **menos arestas**, não menor tempo, distância ou custo (o grafo não tem pesos).
- A rede é fictícia e simplificada; não há horários, capacidade, regras operacionais nem condições meteorológicas.
- Os bloqueios são hipóteses didáticas, não consequências comprovadas da pane noticiada.
- Para custo ou tempo seria preciso um grafo ponderado e algoritmos como Dijkstra.

## Questões para reflexão

1. **Grafo × árvore binária:** a árvore não tem ciclos nem múltiplos caminhos e cada nó tem um único pai; a rede de conexões tem ciclos e caminhos alternativos.
2. **Menor caminho no BFS:** em grafo não ponderado; "menor" é o número de arestas.
3. **DFS ≠ BFS:** o DFS aprofunda um ramo antes de testar os outros e segue a ordem dos vizinhos.
4. **Sem conjunto de visitados:** em grafos com ciclos a busca pode repetir vértices indefinidamente.
5. **Para tempo ou custo:** pesos nas arestas (duração, distância, tarifa), horários e restrições.
6. **Voo real:** o modelo é fictício e ignora segurança, regulação e dados operacionais.
