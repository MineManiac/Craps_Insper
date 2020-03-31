#O jogo consiste em apostar no resultado de um par de dados. 

#As apostas serão sempre de números inteiros positivos de fichas, e o jogador começa com uma quantidade de fichas definida por você.

#Rodadas sucessivas, o jogador decide apostar ou sair do jogo. Automaticamente sai se as fichas acabarem.

#1 Rodada pode ter duas fases, "Come out" e pode passar para a fase de "Point".

#Deixe sempre o jogador informado de que fase ele está. Mostre para o jogador as possibilidades de apostas e pergunte qual a opção e o valor que deseja apostar.
#Ele pode fazer apostas de mais de um tipo por vez

# O computador é quem realiza o lançamento de dois dados (6 lados) para o jogo.
import random


#Pass Line Bet - Na fase de 'Come Out', "if" a soma dos dados for 7 ou 11 o jogador ganha e as fichas apostadas sao dobradas.
#"if" a soma for 2, 3 ou 12 (Craps) o jogador perde a aposta.
#"if" a soma for 4, 5, 6, 8, 9 ou 10 o jogo muda para a fase de 'Point'.
#A aposta continua valendo, o valor tirado se torna o 'Point', para ganhar a soma do novo lancamento deve ser igual ao do point.
#"if" a soma dos dados der 7 o jogador perde tudo.
#"if" qualquer outro numero continua rodando o dado
fichas = 10
print("Você possui {0} fichas".format(fichas))
print("")
aposta = int(input("Qual é a sua aposta ? "))

k = True
while k:
    if aposta > 0 and aposta <= fichas:
    fichas = fichas - aposta
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
    elif soma == 2 or soma == 3 or soma == 12 :
        print("Você perdeu a aposta.")
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

                



else:
    print("A quantidade de aposta está incompatível com o número de fichas que você possui")
    print("Aposte novamente")





#Field - Pode ser feita em qualquer fase do jogo.
#"if" a soma dos dados derem 5, 6, 7 ou 8 o jogador perde tudo.
#"if" a soma der 3, 4, 9, 10 ou 11 ganha o mesmo que apostou mais o dobro.
#"if" a soma der 12 ganha o mesmo mais o triplo.



#Any Craps - Pode ser feita em qualquer fase do jogo.
#"if" soma dos dados der 2, 3 ou 12 o jogador ganha 7 vezes o que apostou.
#"if" qualquer outra soma, o jogador perde.


#Twelve - Pode ser feita em qualquer fase do jogo.
#"if" if soma dos dados derem 12, o jogador ganha 30 vezes o que apostou.
#"if" qualquer outra soma, o jogador perde