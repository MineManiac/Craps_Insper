#O jogo consiste em apostar no resultado de um par de dados. 

#As apostas serão sempre de números inteiros positivos de fichas, e o jogador começa com uma quantidade de fichas definida por você.

#Rodadas sucessivas, o jogador decide apostar ou sair do jogo. Automaticamente sai se as fichas acabarem.

#1 Rodada pode ter duas fases, "Come out" e pode passar para a fase de "Point".

#Deixe sempre o jogador informado de que fase ele está. Mostre para o jogador as possibilidades de apostas e pergunte qual a opção e o valor que deseja apostar.
#Ele pode fazer apostas de mais de um tipo por vez

# O computador é quem realiza o lançamento de dois dados (6 lados) para o jogo.
import random
fichas = 100
print("Você possui {0} fichas".format(fichas))
while fichas != 0:
    print("")
    tipo_de_aposta= int(input("Qual o tipo de aposta que vc quer fazer? Digite 1 para Pass Line, Digite 2 para Field, Digite 3 para Any Craps, Digite 4 para Twelve: "))
    if tipo_de_aposta < 1 or tipo_de_aposta > 5:
        print("Você deve escolher entre os números de 1 a 5")
        print("")
    if tipo_de_aposta == 5:
            print("Você saiu com {0}".format(fichas))
            fichas = 0
    else:
        aposta = int(input("Qual é a sua aposta ? "))
        if aposta > 0 and aposta <= fichas:
            fichas = fichas - aposta   
    #Pass Line Bet - Na fase de 'Come Out', "if" a soma dos dados for 7 ou 11 o jogador ganha e as fichas apostadas sao dobradas.
    #"if" a soma for 2, 3 ou 12 (Craps) o jogador perde a aposta.
    #"if" a soma for 4, 5, 6, 8, 9 ou 10 o jogo muda para a fase de 'Point'.
    #A aposta continua valendo, o valor tirado se torna o 'Point', para ganhar a soma do novo lancamento deve ser igual ao do point.
    #"if" a soma dos dados der 7 o jogador perde tudo.
    #"if" qualquer outro numero continua rodando o dado

            if tipo_de_aposta == 1:
                Pass_Line= 0
                while Pass_Line == 0:
                    dado1 = random.randint(1,6)
                    dado2 = random.randint(1,6)
                    soma = dado1 + dado2
                    print("o valor do primeiro dado foi {0}".format(dado1))
                    print("")
                    print("o valor do segundo dado foi {0}".format(dado2))
                    print("")
                    print("A soma dos dados foi {0}".format(soma))
                    print("")
                    if soma == 7 or soma == 11:
                        aposta = aposta*2
                        fichas = fichas + aposta
                        print("Você ganhou!")
                        print("")
                        print("Você agora possui {0}.".format(fichas))
                        print("")
                        Pass_Line+=1
                    elif soma == 2 or soma == 3 or soma == 12 :
                        print("Você perdeu a aposta.")
                        Pass_Line+=1
                    elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
                        print("Você passou de fase!!")
                        print("")
                        print("Agora você está na fase de Point.")
                        print("")
                        point = soma
                        i = True
                        t = True
                        while i:
                            while t :
                                ok = input("Digite ok para continuar: ")
                                print("")
                                if ok == "ok":
                                    t = False
                                else:
                                    print("")
                                    print("Você precisa digitar ok!")
                                    print("")
                            t = True
                            dado1 = random.randint(1,6)
                            dado2 = random.randint(1,6)
                            soma = dado1 + dado2
                            print("o valor do primeiro dado foi {0}".format(dado1))
                            print("")
                            print("o valor do segundo dado foi {0}".format(dado2))
                            print("")
                            print("A soma dos dados foi {0}".format(soma))
                            print("")
                            
                            if soma == point :
                                aposta = aposta*2
                                fichas = fichas + aposta
                                print("Você ganhou!")
                                print("")
                                print("Você agora possui {0}.".format(fichas))
                                print("")
                                i = False
                            elif soma == 7:
                                print("Você perdeu.")
                                print("")
                                print("Você agora possui {0}.".format(fichas))
                                print("")
                                i = False
                        if i == False:
                            Pass_Line+=1
        
    #Field - Pode ser feita em qualquer fase do jogo.
    #"if" a soma dos dados derem 5, 6, 7 ou 8 o jogador perde tudo.
    #"if" a soma der 3, 4, 9, 10 ou 11 ganha o mesmo que apostou mais o dobro.
    #"if" a soma der 12 ganha o mesmo mais o triplo.
            if tipo_de_aposta == 2:
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                soma = dado1+dado2
                print("o valor do primeiro dado foi {0}".format(dado1))
                print("")
                print("o valor do segundo dado foi {0}".format(dado2))
                print("")
                print("A soma dos dados foi {0}".format(soma))
                print("")
                if soma == 12 :
                    aposta = aposta + 3*aposta
                    fichas = fichas + aposta
                    print("")
                    print("Você ganhou {0} fichas".format(aposta))
                elif soma == 5 or soma == 6 or soma == 7 or soma == 8:
                    aposta = 0
                    print("")
                    print("Você perdeu!")
                    print("")
                elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                    aposta = aposta + 2*aposta
                    fichas = fichas + aposta
                    print("Você ganhou {0} fichas".format(aposta))
                print("Agora você possui {0}".format(fichas))
        

    #Any Craps - Pode ser feita em qualquer fase do jogo.
    #"if" soma dos dados der 2, 3 ou 12 o jogador ganha 7 vezes o que apostou.
    #"if" qualquer outra soma, o jogador perde.
            if tipo_de_aposta == 3:
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                soma = dado1+dado2
                print("o valor do primeiro dado foi {0}".format(dado1))
                print("")
                print("o valor do segundo dado foi {0}".format(dado2))
                print("")
                print("A soma dos dados foi {0}".format(soma))
                print("")
                if soma == 2 or soma == 3 or soma == 12 :
                    aposta = aposta + 7*aposta
                    fichas = fichas + aposta
                    print("Você ganhou {0} fichas".format(aposta))
                else:
                    aposta = 0
                    print("Você perdeu!")
            print("")
            print("Agora você possui {0}.".format(fichas))


    #Twelve - Pode ser feita em qualquer fase do jogo.
    #"if" if soma dos dados derem 12, o jogador ganha 30 vezes o que apostou.
    #"if" qualquer outra soma, o jogador perde

            if tipo_de_aposta == 4:
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                soma = dado1+dado2
                print("o valor do primeiro dado foi {0}".format(dado1))
                print("")
                print("o valor do segundo dado foi {0}".format(dado2))
                print("")
                print("A soma dos dados foi {0}".format(soma))
                print("")
                if soma == 12:
                    aposta = aposta + 30*aposta
                    fichas = fichas + aposta
                    print("Você ganhou {0} fichas".format(aposta))
                else:
                    aposta = 0
                    print("Você perdeu!")
                print("")
                print("Agora você possui {0}.".format(fichas))


        else:
            print("A quantidade de aposta está incompatível com o número de fichas que você possui")
            print("Aposte novamente")
print("O jogo terminou!")