import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:""\n")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():    
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []    
    texto = input("\n""Digite o texto " + str(i) +" (aperte enter para sair):")    
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\n""Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    # compara a assinatura fornecida com a assinatura do texto
    diferenca = [(a - b) for a,b in zip(as_a,as_b)]
    dif = [abs(n) for n in diferenca]
    sab = (sum(dif)) / 6

    # sab é uma lista com a diferença numérica das assinaturas comparadas    
    return sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''    

    lista_frases = []
    lista_palavras = []

    lista_sentencas = separa_sentencas(texto)
    for sentenca in lista_sentencas:
        lista_frases.extend(separa_frases(sentenca))
    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))

    total_sentencas = len(lista_sentencas)
    tam_sentenca = 0
    for i in range(total_sentencas):
        tam_sentenca = tam_sentenca + len(lista_sentencas[i])     

    total_frases = len(lista_frases)
    tam_frase = 0
    for i in range(total_frases):
        tam_frase = tam_frase + len(lista_frases[i])    
                          
    total_palavras = len(lista_palavras)   
    tam_palavras = 0    
    for i in range(total_palavras):
        tam_palavras = tam_palavras + len(lista_palavras[i])        

    # define os valores da assinatura de cada texto
    tamanho_m_palavra = tam_palavras / total_palavras
    type_token = n_palavras_diferentes(lista_palavras) / total_palavras
    hapax_legomana = n_palavras_unicas(lista_palavras) / total_palavras
    tamanho_m_sentenca = tam_sentenca / total_sentencas
    complexidade_m_sentenca = total_frases / total_sentencas 
    tamanho_m_frase = tam_frase / total_frases

    assinatura = [tamanho_m_palavra, type_token, hapax_legomana, tamanho_m_sentenca, complexidade_m_sentenca, tamanho_m_frase]
    
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    lista_assinaturas = []
    lista_sab = []
    i = 1
        
    for texto in textos:        
        lista_assinaturas.append(calcula_assinatura(texto))
        i = i + 1

    for assinatura in lista_assinaturas:        
        lista_sab.append(compara_assinatura(assinatura, ass_cp))
        i = i + 1

    # encontra o texto com a maior probabilidade de plágio, o menor sab
    sab = lista_sab.index(min(lista_sab)) + 1
    
    print("\n""O autor do texto",sab,"está infectado com COH-PIAH")
    return sab
    
def main():
    assinatura_copiah = le_assinatura()
    textos = le_textos()
    avalia_textos(textos, assinatura_copiah)

main()


