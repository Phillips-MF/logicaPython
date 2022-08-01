#PRIMEIRA PARTE:
    #O usuário é "bem vindo!", depois escolhe qual modalidade de jogo
    #Se escolher partida joga uma partida contra o computador
    #Se escolher campeonato joga 3 partidas contra o computador
def jogo():
    print("Bem vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    res = int(input("2 - para jogar um campeonato"))
    if res == 1:
        print("Você escolheu partida isolada")
        partida()
    elif res == 2:
        print("Você escolheu campeonato!")
        campeonato()
    else:
        while res!= 1 or res != 2:
            print("1 - para jogar uma partida isolada" )
            res = int(input("2 - para jogar um campeonato" ))
    
    
    
#SEGUNDA PARTE(preparo da partida):
    #O usuário define qual o número de peças(n) na mesa e qual o número máximo
    # de peças que podem ser retiradas(m)(função partida())
    #Caso n seja múltiplo de (m +1 ) o jogador começa
    #Caso contrário o computador começa.
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("Você começa!")
        while n > 0:
            numeroDePeçasRemovidas = usuario_escolhe_jogada(n, m)
            n -= numeroDePeçasRemovidas
            print("O jogador tirou", numeroDePeçasRemovidas, " peças")
            print("Agora restam", n, " peças no tabuleiro")
            if n == 0:
                    fraseVencedora = "O jogador venceu!"
                    print(fraseVencedora)
                    return fraseVencedora
            else:
                numeroDePeçasRemovidas = computador_escolhe_jogada(n, m)
                n -= numeroDePeçasRemovidas
                print("O comptuador tirou", numeroDePeçasRemovidas, " peças")
                print("Agora restam", n, " peças no tabuleiro")
                if n == 0:
                     fraseVencedora = "O computador venceu!"
                     print(fraseVencedora)
                     return fraseVencedora
                    
            
    else:
        print("Computador começa")
        while n > 0:
            numeroDePeçasRemovidas = computador_escolhe_jogada(n, m)
            n -= numeroDePeçasRemovidas
            print("O computador tirou", numeroDePeçasRemovidas, "peças")
            print("Agora restam", n, " peças no tabuleiro")
            if n == 0:
                 fraseVencedora = "O computador venceu!"
                 print(fraseVencedora)
                 return fraseVencedora
            else:
                numeroDePeçasRemovidas = usuario_escolhe_jogada(n, m)
                n -= numeroDePeçasRemovidas
                print("O jogador tirou", numeroDePeçasRemovidas," peças")
                print("Agora restam,", n, " peças no tabuleiro")
                if n == 0:
                    fraseVencedora = "O jogador venceu!"
                    print(fraseVencedora)
                    return fraseVencedora


def campeonato():
    vencedor1 = partida()
    if vencedor1 == "O jogador venceu!":
        pontoParaJogador1 = 1
        pontoParaComputador1 = 0
    else:
        pontoParaJogador1 = 0
        pontoParaComputador1 = 1
     
    vencedor2 = partida()
    if vencedor2 == "O jogador venceu!":
        pontoParaJogador2 = 1
        pontoParaComputador2 = 0 
    else:
        pontoParaJogador2 = 0
        pontoParaComputador2 = 1
    
    vencedor3 = partida()
    if vencedor3 == "O jogador venceu!":
        pontoParaJogador3 = 1
        pontoParaComputador3 = 0 
    else:
        pontoParaJogador3 = 0
        pontoParaComputador3 = 1
    

    pontoFinalJogador = pontoParaJogador1 + pontoParaJogador2 + pontoParaJogador3
    pontoFinalComputador = pontoParaComputador1 + pontoParaComputador2 + pontoParaComputador3
    print("Placar: Você ", pontoFinalJogador," X ",pontoFinalComputador, " Computador")

#TERCEIRA PARTE(o jogo)
    #A função computador_escolhe_jogada(n, m). Baseado no número de peças e no
    #número de peças que podem ser retiradas, o computador deve sempre deixar na
    #mesa uma quantidade de peças iguais aos múltiplos de (m + 1)
def computador_escolhe_jogada(n, m):
    jogada = 1
    multiplo = m + 1
    while jogada <= m:
        if (n - jogada) % multiplo == 0:
            return jogada
        else:
            jogada += 1
    return m 
        
    #A função jogador_escolhe_jogada(n, m). Irá verificar se o jogador informou
    #um número válido de peças para serem retiradas, caso não, deve solicitar
    #novamente um novo valor.
def usuario_escolhe_jogada(n, m):
    peçasRetiradas = int(input("Quantas peças você vai retirar? "))
    while peçasRetiradas > n or peçasRetiradas > m or peçasRetiradas < 1:
        print("Ops! Jogada inválida, tente de novo.")
        peçasRetiradas = int(input("Quantas peças você vai retirar? "))
        
    return peçasRetiradas

    #O programa deve sempre se lembrar qual o número de peças atualmente no tabu
    #leiro e qual o máximo de peças pode ser retirado.

jogo()
