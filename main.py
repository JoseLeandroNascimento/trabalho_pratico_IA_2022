# Esse algoritmo gera todos estados apartir das acões e do nó pai
from audioop import reverse


def lista_nos_filhos(no_pai):

    # A lista de nó visitados é fornecido com o objetivo de impedir que o algoritmo gere um nó já visitado

    # Lista das ações possíveis
    lista_acoes_possiveis = [

        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)

    ]

    # Controla a quantidade missionarios do lado de origem da margem do rio
    num_mis_lado_origem = no_pai[0]

    # Controla o número de missionarios do lado de destino da margem do rio
    num_mis_lado_destino = abs(no_pai[0]-3)

    # Controla o número de canibais do lado de origem da margem do rio
    num_can_lado_origem = no_pai[1]

    # Controla o número de canibais do lado de destino da margem do rio
    num_can_lado_destino = abs(no_pai[1]-3)

    # Informa em que lado do rio o barco está
    lado_embarcao = no_pai[2]

    lista_nos_filhos = []

    # Tenta Aplicar todas as ações
    for acao in lista_acoes_possiveis:

        # Caso o barco esteja do lado de inicio do rio
        if(lado_embarcao == 1):

            # Nós codigo a baixo é calculado o número de missionarios e canibais de ambos os lados do rio
            operacao1 = num_mis_lado_origem - acao[0]
            operacao2 = num_can_lado_origem - acao[1]
            operacao3 = num_mis_lado_destino + acao[0]
            operacao4 = num_can_lado_destino + acao[1]

            # Nesse trecho é validado se o número de membros obdece o limites
            valida1 = operacao1 >= 0 and operacao1 <= 3
            valida2 = operacao2 >= 0 and operacao2 <= 3
            valida3 = operacao3 >= 0 and operacao3 <= 3
            valida4 = operacao4 >= 0 and operacao4 <= 3

            # Verifica se o número de missionarios em ambos os lados da margem é maior ou igual do que a canibais com essa ação
            # caso a ação leve ao número de missionarios a ser zero a operação será valida
            if(((operacao1 >= operacao2 or operacao1 == 0) and (operacao3 >= operacao4 or operacao3 == 0))):

                if(valida1 and valida2 and valida3 and valida4):

                    # gera o nó filho
                    no_filho = (operacao1, operacao2, 0)

                    # Verifica se o nó filho gerado já não foi gerado anteriormente

                    lista_nos_filhos.append(no_filho)

        else:

            operacao1 = num_mis_lado_origem + acao[0]
            operacao2 = num_can_lado_origem + acao[1]
            operacao3 = num_mis_lado_destino - acao[0]
            operacao4 = num_can_lado_destino - acao[1]

            valida1 = operacao1 >= 0 and operacao1 <= 3
            valida2 = operacao2 >= 0 and operacao2 <= 3
            valida3 = operacao3 >= 0 and operacao3 <= 3
            valida4 = operacao4 >= 0 and operacao4 <= 3

            # Verifica se o número de missionarios em ambos os lados da margem é maior ou igual do que a canibais com essa ação
            # caso a ação leve ao número de missionarios a ser zero a operação será valida
            if(((operacao1 >= operacao2 or operacao1 == 0) and (operacao3 >= operacao4 or operacao3 == 0))):

                if(valida1 and valida2 and valida3 and valida4):

                    no_filho = (operacao1, operacao2, 1)

                    lista_nos_filhos.append(no_filho)

    return lista_nos_filhos


##############################################################################################

# Essa função é responsável por criar o grafo
def gerarGrafo():

    no_raiz = (3, 3, 1)

    grafo = []

    nos_a_visitar = []
    nos_a_visitar.append(no_raiz)
    nos_explorados = []

    while(len(nos_a_visitar) > 0):

        no_pai = nos_a_visitar.pop()

        if(no_pai in nos_explorados):

            continue

        nos_explorados.append(no_pai)

        lista_de_filhos = lista_nos_filhos(no_pai)

        # print(nos_a_visitar)
        # print(lista_de_filhos)

        grafo.append([no_pai, lista_de_filhos])

        for no in lista_de_filhos:

            if(no not in nos_explorados):

                nos_a_visitar.append(no)

    return grafo

# Esse algoritmo realiza a busca do caminho através da lista de nós visitados
def caminho(lista, g):

    indice = len(lista)-1 
    lista_aux = [] # lista que será retornada com a ordem correta

    lista_aux.append(lista[len(lista)-1]) #Coloca o elemento do final da lista na lista aux

    # Prox_no é o nó que se deve procurar o pai
    prox_no = lista[len(lista)-1]

    indice_aux = indice

    # laço para percorrer a lista de visitados
    while indice > 0:

        indice_g = 0
        # Laço para percorer o grafo
        while indice_g < len(g):

            # Verifica se o nó do garfo é igual ao nó anterior ao nó prox_no e se prox_no está na sua lista de nós filhos
            if(g[indice_g][0] == lista[indice-1] and prox_no in g[indice_g][1] and lista[indice-1][2] != prox_no[2]):

                prox_no = lista[indice-1]
                lista_aux.append(lista[indice-1])
                indice_aux -= 1
                break

            indice_g += 1

        indice -= 1

    lista_aux.reverse()

    return lista_aux


def busca_profundidade(g):

    pilha = []
    visitados = []

    no_pai = g[0][0]

    pilha.append(no_pai)
    # Quantidade nos gerados começa me pois o no raiz já foi gerado antes
    cont_nos_gerados = 1

    profundidade_max = 1

    while(len(pilha) > 0):

        no_atual = pilha.pop()

        visitados.append(no_atual)

        if(no_atual == (0, 0, 0)):

            profundidade_max += 1
            print("Caminho: ")
            print(caminho(visitados, g))
            print("Quantidade nós gerados: "+str(cont_nos_gerados))
            print("Quantidade nó visitados: "+str(len(visitados)))
            # Como cada nó está em um nivel pra baixo então o tamanho do caminho fornece o nivel da solução, no caso o nivel começa em 1
            print("Profundidade da solução: "+str(len(caminho(visitados, g))))
            print("Profundidade máxima: "+str(profundidade_max))

        else:

            # Retorna todos os filhos de um nó
            filhos = lista_nos_filhos(no_atual)

            filhos.reverse()

            cont_filhos_validos = 0

            for filho in filhos:

                if filho not in visitados and filho not in pilha:

                    pilha.append(filho)
                    cont_nos_gerados += 1
                    cont_filhos_validos += 1

            if(cont_filhos_validos > 0):

                profundidade_max += 1

            else:

                profundidade_max -= 1


def busca_largura(g):

    fila = []
    visitados = []
    no_pai = g[0][0]

    fila.append(no_pai)
    cont_nos_gerados = 1
    profundidade_max = 1
    while(len(fila) > 0):

        no_atual = fila.pop(0)

        visitados.append(no_atual)

        if(no_atual == (0, 0, 0)):

            print("Caminho: ")
            print(caminho(visitados, g))
            print("Quantidade nós gerados: "+str(cont_nos_gerados))
            print("Quantidade nó visitados: "+str(len(visitados)))
            # Como cada nó está em um nivel pra baixo então o tamanho do caminho fornece o nivel da solução, no caso o nivel começa em 1
            print("Profundidade da solução: " +str(len(caminho(visitados, g))))
            

        else:

            filhos = lista_nos_filhos(no_atual)

            filhos.reverse()

            for filho in filhos:

                if filho not in visitados and filho not in fila:

                    fila.append(filho)
                    cont_nos_gerados+=1


g = gerarGrafo()


print("#Usando algoritmo de busca em profundidade")

busca_profundidade(g)

print(end="\n\n")
print("#Usando algoritmo de busca em largura")
busca_largura(g)
