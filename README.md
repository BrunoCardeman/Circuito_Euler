# Projeto de Estruturas Discretas: Circuitos de Euler e Redes de Inspeção

Repositório dedicado ao trabalho de implementação da disciplina de **Estruturas Discretas (INF1631)**. O projeto modela um problema de inspeção urbana utilizando a Teoria dos Grafos.

## Sobre o Problema
O objetivo é simular um robô autônomo que precisa inspecionar todas as ruas de uma cidade (arestas) exatamente uma vez, passando por todos os cruzamentos (vértices) e retornando ao ponto de partida. Isso corresponde à existência e à construção de um **Circuito de Euler** em um grafo não direcionado.

O programa gera redes aleatoriamente e utiliza critérios matemáticos formais para verificar a viabilidade da rota antes de construir o percurso do robô de forma automatizada.

---

## Funcionalidades e Funções Obrigatórias

O código está estruturado modularmente contemplando as seguintes funções:
* `gerar_grafo(n, p)`: Gera um grafo simples não direcionado com $N$ vértices e probabilidade $p$ de inclusão de arestas.
* `graus(conexao)`: Calcula o grau de incidência de cada vértice da rede.
* `conexo(vertices, conexao)`: Verifica se todos os vértices de grau não nulo pertencem à mesma componente conexa.
* `euleriano(vertices, conexao)`: Determina se o grafo é euleriano (conexo + todos os graus pares).
* `circuito_euler(conexao)`: Constrói o circuito de Euler utilizando uma abordagem baseada no algoritmo de Hierholzer.
* `valida_circuito(conexao, caminho)`: Realiza a validação automática do circuito gerado.

---

## Parâmetros do Experimento
* **Número de Vértices (N):** 10
* **Probabilidade (p):** 0.30
* **Semente (Seed):** 728

---

## Como Executar o Projeto

Certifique-se de ter o **Python 3** instalado em sua máquina.

1. Clone o repositório ou baixe os arquivos para a sua pasta local:
   ```bash
   git clone https://github.com/BrunoCardeman/Circuito_Euler.git
   cd Circuito_Euler
   python3 main.py
   
2. Se preferir em vez do python3 main.py. Pode-se executar pelo botao de run do ambiente.  
