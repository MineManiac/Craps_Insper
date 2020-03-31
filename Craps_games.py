#O jogo consiste em apostar no resultado de um par de dados. 

#As apostas serão sempre de números inteiros positivos de fichas, e o jogador começa com uma quantidade de fichas definida por você.

#Rodadas sucessivas, o jogador decide apostar ou sair do jogo. Automaticamente sai se as fichas acabarem.

#1 Rodada pode ter duas fases, "Come out" e pode passar para a fase de "Point".

#Deixe sempre o jogador informado de que fase ele está. Mostre para o jogador as possibilidades de apostas e pergunte qual a opção e o valor que deseja apostar.
#Ele pode fazer apostas de mais de um tipo por vez

# O computador é quem realiza o lançamento de dois dados (6 lados) para o jogo.



#Pass Line Bet - Na fase de 'Come Out', "if" a soma dos dados for 7 ou 11 o jogador ganha e as fichas apostadas sao dobradas.
#"if" a soma for 2, 3 ou 12 (Craps) o jogador perde a aposta.
#"if" a soma for 4, 5, 6, 8, 9 ou 10 o jogo muda para a fase de 'Point'.
#A aposta continua valendo, o valor tirado se torna o 'Point', para ganhar a soma do novo lancamento deve ser igual ao do point.
#"if" a soma dos dados der 7 o jogador perde tudo.
#"if" qualquer outro numero continua rodando o dado



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