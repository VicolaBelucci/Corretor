import nltk
nltk.download('punkt')

with open("C:\\Users\\User\\Desktop\\Projetos - Pycharm\\ComecandoPython\\Python - Alura\\Corretor ortográfico - aplicando tecnicas de NLP\\Dados do corretor\\artigos.txt", "r", encoding='utf-8') as f:
    artigos = f.read()
def separa_palavra(lista_tokens):
    lista_palavras = []
    for t in lista_tokens:
        if t.isalpha():
            lista_palavras.append(t)
    return lista_palavras
def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada
def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras
def deleta_letras(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras
def troca_letras(fatias):
    palavras_novas = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            palavras_novas.append(E + letra + D[1:])
    return palavras_novas
def inverte_letras(fatias):
    novas_palavras = []
    for E, D in fatias:
        if len(D) > 1:
            novas_palavras.append(E + D[1] + D[0] + D[2:])
    return novas_palavras
def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deleta_letras(fatias)
    palavras_geradas += troca_letras(fatias)
    palavras_geradas += inverte_letras(fatias)
    return palavras_geradas
def gerador_aumentado(palavras_geradas):

    novas_palavras = []
    for palavra in palavras_geradas:
        novas_palavras += gerador_palavras(palavra)
    return novas_palavras
def corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key = probabilidade)
    return palavra_correta
def novo_corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavras_geradas_turbinadas = gerador_aumentado(palavras_geradas)
    todas_palavras = set(palavras_geradas + palavras_geradas_turbinadas)
    candidatos = [palavra]
    for palavra in todas_palavras:
        if (palavra in palavras_unicas):
            candidatos.append(palavra)
    palavra_correta = max(candidatos, key=probabilidade)
    return palavra_correta
def probabilidade(palavra_gerada):
    return frequencia[palavra_gerada]/total_palavras
def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f = open(nome_arquivo, 'r', encoding='utf-8')
    for linha in f:
        correta = linha.split()[0]
        errada = linha.split()[1]
        lista_palavras_teste.append((correta, errada))
    f.close()
    return lista_palavras_teste
def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    print("O numero de palavras na base de testes é: {}".format(numero_palavras))
    acertou_1 = 0
    acertou_2 = 0
    desconhecida = 0
    for item in testes:
        correta = item[0]
        errada = item[1]
        corretor_1 = corretor(errada)
        corretor_2 = novo_corretor(errada)
        desconhecida += (correta not in vocabulario)
        if (corretor_1 == correta):
            acertou_1 += 1
        if (corretor_2 == correta):
            acertou_2 += 1

    print("Taxa de acerto do primeiro corretor: {}%".format(round(acertou_1 * 100 / numero_palavras, 2)))
    print("Taxa de acerto do segundo corretor: {}%".format(round(acertou_2 * 100 / numero_palavras, 2)))
    print("Taxa de palavras desconhecidas: {}%".format(round(desconhecida * 100 / numero_palavras, 2)))

palavras_separadas = nltk.tokenize.word_tokenize(artigos)
tokens_corretos = separa_palavra(palavras_separadas)

lista_normalizada = normalizacao(tokens_corretos)
total_palavras = len(lista_normalizada)

palavras_unicas = set(lista_normalizada)

frequencia = nltk.FreqDist(lista_normalizada)

lista_teste = cria_dados_teste("C:\\Users\\User\\Desktop\\Projetos - Pycharm\\ComecandoPython\\Python - Alura\\Corretor ortográfico - aplicando tecnicas de NLP\\Dados do corretor\\palavras.txt")
avaliador(lista_teste, palavras_unicas)




