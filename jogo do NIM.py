
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:""\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha()

def escolha():
    
    x = int(input())
    if x != 1 and x != 2:
        print("O número",x,"é inválido""\n")        
        main()
    else:
        if x == 1:
            print ("Você escolheu uma partida isolada!""\n")            
            print("**** Rodada 1 ****")            
            partida()            
        else:
            print ("Você escolheu um campeonato!""\n")
            campeonato()

def partida():
    
    print()
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    pcJoga = True

    # o usuário começa a jogada, caso o número de peças seja múltiplo de m + 1
    if n % (m + 1) == 0:
        pcJoga = False

    if pcJoga:
        print("\n""Computador começa!""\n")
    else:
        print("\n""Você começa!""\n") 
    
    # enquanto houver peças no jogo, informar quantas peças foram removidas
    while n > 0:
        if pcJoga:            
            resultado = computador_escolhe_jogada(n,m)
            pcJoga = False
            if resultado > 1:
                print("O computador tirou",resultado,"peças.")
            else:
                print("O computador tirou uma peça.")                
        else:            
            resultado = usuario_escolhe_jogada(n,m)
            pcJoga = True
            if resultado > 1:
                print("\n""Você tirou",resultado,"peças.")
            else:
                print("\n""Você tirou uma peça.")                

        n = n - resultado
        if n > 1:
            print("Agora restam",n,"peças no tabuleiro.""\n")
        if n == 1 and n != 0:
            print("Agora resta apenas uma peça no tabuleiro.""\n")           

    # analisa quem é o próximo a jogar depois que as peças acabaram, pra definir o vencedor
    if pcJoga:
        print("Fim do jogo! Você ganhou!""\n")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!""\n")
        return 0

def usuario_escolhe_jogada(n,m):
    
    n = 0
    erro = True

    while erro:
        n = int(input("Quantas peças você vai tirar? "))
        if n < 1 or n > m or n > n:
            print("\n""Oops! Jogada inválida! Tente de novo.""\n")
            erro = True
        else:
            erro = False
    return n

# a estratégia do computador é deixar o número de peças múltiplo de m + 1, quando possível
def computador_escolhe_jogada(n,m):

    if n <= m:
        return n
    else:
        multiplo = n % (m + 1)
        if multiplo > 0:
            return multiplo
        else:
            return m

def campeonato():

    usuario = 0
    computador = 0
    i = 1

    for _ in range(3):
        print("**** Rodada",i,"****")
        i = i + 1
        vence = partida()

        if vence == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1

            
    print("**** Final do campeonato! ****""\n")    
    print("Placar: Você",usuario,"X",computador,"Computador")

main()

        
    

    
    

    



   
       
