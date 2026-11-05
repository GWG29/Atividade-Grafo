import os
"""
Ana Julia - RA: 2037490
João Filipe - RA: 2089420
Guilherme - RA: 2029851 
Andreas - RA: 2086833
"""

def criar_grafo():
    """
    Retorna um novo grafo vazio.
    Passos:
    1. Criar um dicionário vazio: {}
    2. Retornar o dicionário (representa o grafo)
    """
    grafo = {}
    return grafo

grafo = criar_grafo()

def inserir_vertice(grafo, vertice):
    """
    Insere um vértice no grafo, sem arestas iniciais.
    Passos:
    1. Verificar se 'vertice' já é chave em grafo.
    2. Se não for, criar entrada grafo[vertice] = []
    3. Se já existir, não fazer nada (ou avisar)
    """
    if vertice in grafo:
        print("vertice já existe")
    else:
        grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Adiciona aresta entre origem e destino.
    Passos:
    1. Garantir que 'origem' e 'destino' existam no grafo (inserir se necessário).
    2. adicionar destino como vizinho de origem (append).
    3. Se for Nâo Direcionado, também:
         - adicionar origem como vizinho de destino
    """
    
    grafo.setdefault(origem, []).append(destino)
    grafo.setdefault(destino, [])

    if nao_direcionado:
        grafo[destino].append(origem)
    return grafo

def vizinhos(grafo, vertice):
    """
    Retorna a lista de vizinhos de 'vertice'.
    Passos:
    1. Se 'vertice' estiver em grafo, retornar grafo[vertice] (lista).
    2. Se não existir, retornar lista vazia ou sinalizar erro.
    """
    if vertice in grafo:
        return(grafo[vertice])
    else:
        print("lista vazia")

def listar_vizinhos(grafo, vertice):
    """
    Função semântica: imprimir/retornar os vizinhos de 'vertice'.
    Passos:
    1. Obter lista = vizinhos(grafo, vertice)
    2. Retornar/imprimir essa lista (ou informar que o vértice não existe)
    """
    listar = vizinhos(grafo, vertice)
    if vertice in grafo:
        print(vertice, " = ", grafo[vertice])
    else:
        print("Vértice não existe")

def exibir_grafo(grafo):
    """
    Exibe o grafo em forma legível (lista de adjacência).
    Passos:
    1. Para cada vertice em ordem
         - imprimir: vertic e -> vizinhos
    """
    for vertice in grafo:
        print(f"{vertice}: {grafo[vertice]}\n")
    print("\n")
    

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    Passos:
    1. Verificar se 'origem' existe; se não, terminar.
    2. Se destino estiver em grafo[origem], remover essa ocorrência.
    3. Se for não direcionado, também:
         - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
    """
    if origem not in grafo:
        pass
    elif destino in grafo[origem]:
        grafo[origem].remove(destino)
    elif nao_direcionado:
        if destino in grafo and origem in grafo[destino]:
            destino.remove(origem)
    


def remover_vertice(grafo, vertice, nao_direcionado=True):
    """
    Remove um vértice e todas as arestas que o tocam.
    Passos:
    1. Verificar se 'vertice' existe em grafo; se não, terminar.
    2. Para cada outro vertice no grafo:
         - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
    3. Remover o vertice do grafo
    4. Opcional: retornar confirmação/erro.
    """
    if vertice not in grafo:
        return False
    
    for d in grafo.values():
            if vertice in d:
                d.remove(vertice)

    del grafo[vertice]
    return True


def existe_aresta(grafo, origem, destino):
    """
    Verifica se existe aresta direta origem -> destino.
    Passos:
    1. Verificar se 'origem' é chave no grafo.
    2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
    """
    if destino in grafo[origem]:
        print("True")
        return True
    else:
        print("False")
        return False

def grau_vertices(grafo):
    """
    Calcula e retorna o grau (out, in, total) de cada vértice.
    Passos:
    1. Inicializar um dict de graus vazia
    2. Para cada vertice, colocar no dict uma estrutura com in, out e total zerado
    3. Para cada u em grafo:
         - out_degree[u] = tamanho de vizinhos
         - para cada v em grafo:
            - verificar se u está na lista de vizinho de v,
            - caso esteja, adicionar +1 para o grau de entrada de u
    4. Calcular o grau total somando entrada + saida
    5. Retornar uma estrutura contendo out,in,total por vértice (ex: dict de tuplas).
    """
    graus = {}
    for vertice in grafo:
        graus[vertice] =  {"out": 0, "in": 0, "total": 0}
    for grau in grafo:
        graus[grau]["out"] = len(grafo[grau])
        for v in grafo:
            if grau in grafo[v]:
                graus[grau]["in"] += 1
    for u in graus:
        graus[u]["total"] = graus[u]["in"] + graus[u]["out"]
    return {u: (g["out"], g["in"], g["total"]) for u, g in graus.items()}


def percurso_valido(grafo, caminho):
    """
    Verifica se uma sequência específica de vértices (caminho) é válida:
    i.e., se existem arestas consecutivas entre os nós do caminho.
    Passos:
    1. Se caminho tiver tamanho < 2, retornar True (trivial).
    2. Para i de 0 até len(caminho)-2:
         - origem = caminho[i], destino = caminho[i+1]
         - se não existe_aresta(grafo, origem, destino): retornar False
    3. Se todas as arestas existirem, retornar True.
    """
    if len(caminho) < 2:
        return True
    for i in range (len(caminho - 1)):
        origem = caminho [i]
        destino = caminho[i + 1]

        if not existe_aresta(grafo, origem, destino):
            return False
    return True

def converte_grafo(x, y):
    global grafo
    grafo = [[0 for i in range(x)] for j in range(y)]

def matriz_grafo(grafo):
    converte_grafo(len(grafo), len(grafo))
    j = 0
    dict_temp = {}
    for i in grafo:
        dict_temp[i] = j
        j += 1
    for i in grafo:
        for k in grafo[i]:
            inserir_aresta(dict_temp[i], dict_temp[k])

def lista_aresta(grafo):
    lista_adjacentes = []
    for vertice in grafo:
        for aresta in grafo[vertice]:
            sub_lista = []
            sub_lista.append(vertice)
            sub_lista.append(aresta)
            lista_adjacentes.append(sub_lista)

    return lista_adjacentes


def main():
    """
    Crie um menu onde seja possível escolher qual ação deseja realizar
    ex:
        1 - Mostrar o Grafo
        2 - inserir vertice
        3 - inserir aresta
        4 - remover vértice.
        ....
    """

    global grafo
    os.system("cls")
    print("------------------------------\n" \
          "1 -> Mostrar o Grafo\n" \
          "2 -> Inserir vertice\n" \
          "3 -> Inserir aresta\n"  \
          "4 -> Remover vertice\n" \
          "5 -> Mostrar grau do vertice\n" \
          "6 -> Mostrar vizinhos\n"\
          "7 -> Mostrar percurso\n" \
          "8 -> Mostrar Matriz de adjacencia\n" \
          "9 -> Listar arestas\n" \
          "0 -> Sair"
          "------------------------------\n   ")
    opt = int(input("-> "))
    

    match opt:
        case 1:
            exibir_grafo(grafo)
            os.system("pause")
            main()
        case 2:
            v = input("Insira a Vertice: ").upper()
            inserir_vertice(grafo, v)
            os.system("pause")
            main()
        case 3:
            v1 = input("Vertice origem: ").upper()
            v2 = input("Vertice destino: ").upper()
            d = input("Grafo direcionado? [s/n]").upper()
            if d == "S":
                d = True
            else:
                d = False
            inserir_aresta(grafo, v1, v2, nao_direcionado=d)
            os.system("pause")
            main()
        case 4:
            v = input("Vertice a ser removida: ").upper()
            d = input("Grafo direcionado? [s/n]").upper()
            if d == "S":
                d = True
            else:
                d = False
            remover_vertice(grafo, v, nao_direcionado=d)
            os.system("pause")
            main()
        case 5:
            grau_vertices(grafo)
            os.system("pause")
            main()
        case 6:
            v = input("Insira a Vertice: ")
            listar_vizinhos(grafo, v)
            os.system("pause")
            main()
        case 7:
            v = 10000000000000000000000
            lista_v = []
            print("Digite 0 para parar de inserir vertices\n")
            while v != 0:
                v = lista_v.append(input("Insira a vertice: ").upper())
            percurso_valido(grafo, lista_v)
        case 8:
            matriz_grafo(grafo)
            os.system("pause")
            main()
        case 9:
            print("lista de arestas:", lista_aresta(grafo))
            os.system("pause")
            main()
        case 0:
            print("Até mais!!!\n")
        case _:
            print("Comando não reconhecido...\n")
            os.system("pause")
            main()

            
    print(grafo)
    inserir_aresta (grafo, "A", "B")
    inserir_aresta (grafo, "A", "C", nao_direcionado=True)
    exibir_grafo(grafo)
    vizinhos(grafo, "B")
    print(grau_vertices(grafo))
    """
    remover_aresta(grafo, "C", "A")
    exibir_grafo(grafo)
    remover_vertice(grafo,"C")
    exibir_grafo(grafo)
    """
    existe_aresta(grafo, "B","C")

if __name__ == "__main__":
    main()
