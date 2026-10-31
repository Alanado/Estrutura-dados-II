from collections import deque

CONEXOES = [
    ("Brasília", "Goiânia"),
    ("Brasília", "Uberlândia"),
    ("Brasília", "Belo Horizonte"),
    ("Goiânia", "Uberlândia"),
    ("Goiânia", "São Paulo"),
    ("Uberlândia", "Belo Horizonte"),
    ("Uberlândia", "Campinas"),
    ("Belo Horizonte", "Rio de Janeiro"),
    ("Belo Horizonte", "São Paulo"),
    ("Rio de Janeiro", "São Paulo"),
    ("Rio de Janeiro", "Curitiba"),
    ("São Paulo", "Campinas"),
    ("São Paulo", "Curitiba"),
    ("Campinas", "Londrina"),
    ("Londrina", "Curitiba"),
]


def construir_grafo(conexoes):
    grafo = {}
    for a, b in conexoes:
        grafo.setdefault(a, []).append(b)
        grafo.setdefault(b, []).append(a)
    return grafo


def bloquear(grafo, bloqueios):
    copia = {cidade: list(vizinhos) for cidade, vizinhos in grafo.items()}
    for a, b in bloqueios:
        copia[a].remove(b)
        copia[b].remove(a)
    return copia


def bfs(grafo, origem, destino):
    fila = deque([[origem]])
    visitados = {origem}
    while fila:
        caminho = fila.popleft()
        atual = caminho[-1]
        if atual == destino:
            return caminho
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])
    return None


def dfs(grafo, origem, destino):
    pilha = [[origem]]
    visitados = set()
    while pilha:
        caminho = pilha.pop()
        atual = caminho[-1]
        if atual in visitados:
            continue
        visitados.add(atual)
        if atual == destino:
            return caminho
        for vizinho in reversed(grafo[atual]):
            if vizinho not in visitados:
                pilha.append(caminho + [vizinho])
    return None


def mostrar(titulo, grafo, origem, destino):
    print(f"\n{titulo}")
    for nome, busca in (("BFS", bfs), ("DFS", dfs)):
        caminho = busca(grafo, origem, destino)
        if caminho:
            print(f"  {nome}: {' -> '.join(caminho)} ({len(caminho) - 1} arestas)")
        else:
            print(f"  {nome}: nenhum caminho encontrado")


def main():
    grafo = construir_grafo(CONEXOES)
    origem, destino = "Brasília", "Curitiba"
    print(f"Rede: {len(grafo)} vértices, {len(CONEXOES)} arestas")

    mostrar("A. Rede completa", grafo, origem, destino)

    b1 = ("São Paulo", "Curitiba")
    b2 = ("Rio de Janeiro", "Curitiba")
    b3 = ("Londrina", "Curitiba")

    mostrar("B. Bloqueio São Paulo-Curitiba",
            bloquear(grafo, [b1]), origem, destino)
    mostrar("C1. + bloqueio Rio de Janeiro-Curitiba",
            bloquear(grafo, [b1, b2]), origem, destino)
    mostrar("C2. + bloqueio Londrina-Curitiba",
            bloquear(grafo, [b1, b2, b3]), origem, destino)

    invertido = bloquear(grafo, [])
    invertido[origem].reverse()
    mostrar("D. Vizinhos de Brasília invertidos", invertido, origem, destino)


if __name__ == "__main__":
    main()
