import random
import time

random.seed(728)
SEED = 728
P = 0.3
N = 10

def gerar_grafo(p):
    l = [1,2,3,4,5,6,7,8,9,10]
    conexao = []
    for index , i in enumerate(l):

        for j in l[index+1:]:
            if random.uniform(0,1)<=p and j !=i:
                conexao.append([i,j])


    return conexao

def graus(conexao):
    vertices = [0,0,0,0,0,0,0,0,0,0]

    for i in conexao:
        vertices[i[0]-1] = vertices[i[0]-1] + 1
        vertices[i[1]-1] =   vertices[i[1]-1] + 1
    return vertices

def conexo(vertices, conexao):
    partida = 0
    exploracao = []
    for i, grau in enumerate(vertices):
        if grau >0:
            partida= i+1
            break

    exploracao.append(partida)

    for atual in exploracao:
        for ruas in conexao:
            if ruas[0] == atual:
                if ruas[1] not in exploracao:
                    exploracao.append(ruas[1])
            elif ruas[1] == atual:
                if ruas[0] not in exploracao:
                    exploracao.append(ruas[0])

    for index, vertice in enumerate(vertices):
        if vertice > 0 and (index+1) not in exploracao:
            return False
    return True

def euleriano(vertices, conexao):
    if conexo(vertices, conexao) == True:
        for vertice in vertices:
            if vertice % 2 !=0:
                return False
        return True
    return False

def circuito_euler(conexao):
    arestas_disponiveis = list(conexao)
    caminho = []
    vertice_atual = conexao[0][0]

    while arestas_disponiveis != []:
        retirou = False
        for aresta in arestas_disponiveis:
            if aresta[0] == vertice_atual:
                caminho.append(aresta)
                vertice_atual = aresta[1]
                arestas_disponiveis.remove(aresta)
                retirou = True
                break
            elif aresta[1] == vertice_atual:
                caminho.append(aresta)
                vertice_atual = aresta[0]
                arestas_disponiveis.remove(aresta)
                retirou = True
                break

        if retirou == False:
            encontrou_novo_ponto = False
            for passo in caminho:
                for v in passo:
                    for a in arestas_disponiveis:
                        if a[0] == v or a[1] == v:
                            vertice_atual = v
                            encontrou_novo_ponto = True
                            break
                    if encontrou_novo_ponto:
                        break
                if encontrou_novo_ponto:
                    break   
            if not encontrou_novo_ponto:
                break 
    return caminho

def valida_circuito(conexao, caminho):
   
    if len(caminho) != len(conexao):
        return False

    arestas_originais = []
    for a in conexao:
        ordenada = sorted(a)
        arestas_originais.append((ordenada[0], ordenada[1]))
    arestas_originais.sort()

    arestas_caminho = []
    for a in caminho:
        ordenada = sorted(a)
        arestas_caminho.append((ordenada[0], ordenada[1]))
    arestas_caminho.sort()

    if arestas_originais != arestas_caminho:
        return False

    for i in range(len(caminho) - 1):
        atual = caminho[i]
        proxima = caminho[i+1]
        if not (atual[0] in proxima or atual[1] in proxima):
            return False

    ultima = caminho[-1]
    primeira = caminho[0]
    if not (ultima[0] in primeira or ultima[1] in primeira):
        return False

    return True

#TESTE

print(f"Numero de vertices: {N}")
print(f"Probabilidade p: {P:.2f}")
print(f"Seed: {SEED}")

contador_gerados = 0
grafo_encontrado = None
vertices_encontrados = None

while True:
    contador_gerados += 1
    g = gerar_grafo(P)
    v = graus(g)
    if euleriano(v, g):
        grafo_encontrado = g
        vertices_encontrados = v
        print("Grafo Euleriano encontrado!")
        print(f"Numero de grafos gerados: {contador_gerados}")
        break

print("Arestas:")
for a in grafo_encontrado:
    print(f"({a[0]},{a[1]})", end=" ")
print() 

print("Graus:")
for idx, g_val in enumerate(vertices_encontrados):
        print(f"v{idx+1}: {g_val}")

print("Conexo: sim")
print("Todos os graus sao pares: sim")
print("Euleriano: sim")


circuito = circuito_euler(grafo_encontrado)
caminho_formatado = [str(circuito[0][0]), str(circuito[0][1])]
atual = circuito[0][1]
for aresta in circuito[1:]:
    if aresta[0] == atual:
        atual = aresta[1]
    else:
        atual = aresta[0]
    caminho_formatado.append(str(atual))

print("Circuito de Euler:")

vertices_circuito = [circuito[0][0]]
atual = circuito[0][1]
vertices_circuito.append(atual)

for aresta in circuito[1:]:
    if aresta[0] == atual:
        atual = aresta[1]
    else:
        atual = aresta[0]
    vertices_circuito.append(atual)

# Imprime os vértices conectados por setas sem usar join
for i, v in enumerate(vertices_circuito):
    if i == 0:
        print(v, end="")
    else:
        print(f" -> {v}", end="")
print()

valido = valida_circuito(grafo_encontrado, circuito)
if valido :
    print("Validacao do circuito: OK")
else:
    print("Validacao do circuito: FALHA")

print("--------------------------------")


print("Experimento com 1000 grafos:")
inicio_tempo = time.time()

grafos_eulerianos_1000 = 0
for _ in range(1000):
    g_temp = gerar_grafo(P)
    v_temp = graus(g_temp)
    if euleriano(v_temp, g_temp):
        grafos_eulerianos_1000 += 1

fim_tempo = time.time()
tempo_total = fim_tempo - inicio_tempo

print(f"Grafos Eulerianos: {grafos_eulerianos_1000}")
print(f"Proporcao: {grafos_eulerianos_1000 / 1000:.3f}")
print(f"Tempo total gasto: {tempo_total:.4f} segundos")