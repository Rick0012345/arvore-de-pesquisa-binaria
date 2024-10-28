import matplotlib.pyplot as plt
import json

# Função para desenhar a linha (vértice) entre dois nós
def desenhar_aresta(ax, pos1, pos2):
    linha_x = [pos1[0], pos2[0]]
    linha_y = [pos1[1], pos2[1]]
    ax.plot(linha_x, linha_y, 'k-')  # Desenha a linha em preto

# Função para plotar a árvore completa com vértices usando o elemento central como raiz
def plotar_arvore_completa(vetor, ax, posicoes, inicio, fim, depth=0, pos_x=0):
    if inicio <= fim:
        # Encontrar o índice do elemento central
        posicao = (inicio + fim) // 2
        posicoes[posicao] = (pos_x, -depth)  # Define a posição do nó atual

        # Desenha o nó atual
        ax.text(pos_x, -depth, f'{vetor[posicao]}', ha='center', va='center', 
                bbox=dict(facecolor='white', edgecolor='black'))

        # Desenha o vértice com o nó filho esquerdo, se existir
        if inicio <= posicao - 1:
            filho_esquerdo_pos = (pos_x - 2**(-(depth + 1)), -(depth + 1))
            desenhar_aresta(ax, (pos_x, -depth), filho_esquerdo_pos)
            plotar_arvore_completa(vetor, ax, posicoes, inicio, posicao - 1, depth + 1, pos_x - 2**(-(depth + 1)))

        # Desenha o vértice com o nó filho direito, se existir
        if posicao + 1 <= fim:
            filho_direito_pos = (pos_x + 2**(-(depth + 1)), -(depth + 1))
            desenhar_aresta(ax, (pos_x, -depth), filho_direito_pos)
            plotar_arvore_completa(vetor, ax, posicoes, posicao + 1, fim, depth + 1, pos_x + 2**(-(depth + 1)))

# Função para atualizar o nó atual (destacar)
def atualizar_no(ax, pos_x, pos_y, valor, cor):
    ax.text(pos_x, pos_y, f'{valor}', ha='center', va='center', bbox=dict(facecolor=cor, edgecolor='black'))
    plt.pause(0.5)  # Pausa para visualizar a atualização

# Função de busca binária recursiva com visualização e vértices
def busca_binaria_visualizada(vetor, item, inicio, fim, ax, posicoes):
    if inicio <= fim:
        posicao = (inicio + fim) // 2

        # Destacar o item atual sendo analisado
        pos_x, pos_y = posicoes[posicao]
        atualizar_no(ax, pos_x, pos_y, vetor[posicao], 'yellow')

        # Verificar se o item é o do meio
        if vetor[posicao] == item:
            atualizar_no(ax, pos_x, pos_y, vetor[posicao], 'green')  # Destacar o item encontrado em verde
            return posicao

        # Se o item for maior que o do meio, busca na metade direita
        elif vetor[posicao] < item:
            atualizar_no(ax, pos_x, pos_y, vetor[posicao], 'white')  # Voltar à cor original (branco)
            return busca_binaria_visualizada(vetor, item, posicao + 1, fim, ax, posicoes)

        # Se o item for menor, busca na metade esquerda
        else:
            atualizar_no(ax, pos_x, pos_y, vetor[posicao], 'white')  # Voltar à cor original (branco)
            return busca_binaria_visualizada(vetor, item, inicio, posicao - 1, ax, posicoes)

    else:
        # Exibir mensagem de "não encontrado" no centro
        ax.text(0, -len(vetor)//2 - 1, "Item não encontrado", ha='center', va='center', color='red')
        plt.pause(1)
        return -1

# Função principal para iniciar a busca binária visualizada
# Função principal para iniciar a busca binária visualizada
def realizar_busca_visualizada(dicionario):
    vetor = dicionario["Vetor"]
    item = dicionario["Item"]
    # Ordenar o vetor antes da busca binária
    vetor.sort()
    # Adiciona um print para visualizar o vetor ordenado
    print("Vetor ordenado:", vetor)

    # Criar a figura e os eixos
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-len(vetor)//2 - 1, 1)
    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title(f'Busca Binária Visualizada para o item {item}')

    # Inicializar as posições dos nós
    posicoes = [None] * len(vetor)

    # Plotar a árvore completa com vértices
    plotar_arvore_completa(vetor, ax, posicoes, 0, len(vetor) - 1)

    # Realizar a busca binária com visualização
    resultado = busca_binaria_visualizada(vetor, item, 0, len(vetor) - 1, ax, posicoes)

    plt.show()

    # Exibir o resultado final
    if resultado != -1:
        print(f"Item {item} encontrado na posição {resultado}.")
    else:
        print(f"Item {item} não encontrado.")


arquivo = "vetor.txt"

def ler_dicionario(arquivo):
    with open(arquivo, 'r') as arq:
        dic = json.load(arq)
    return dic

# Armazena o resultado da função
resultado = ler_dicionario(arquivo)

# Realiza a busca binária visualizada
realizar_busca_visualizada(resultado)
