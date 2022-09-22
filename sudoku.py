import bsudoku

jogo1 = [[0,0,0],[0,0,0],[0,0,0]]
jogo2 = [[0,0,0],[0,0,0],[0,0,0]]
jogo3 = [[0,0,0],[0,0,0],[0,0,0]]
jogo4 = [[0,0,0],[0,0,0],[0,0,0]]
jogo5 = [[0,0,0],[0,0,0],[0,0,0]]
jogo6 = [[0,0,0],[0,0,0],[0,0,0]]
jogo7 = [[0,0,0],[0,0,0],[0,0,0]]
jogo8 = [[0,0,0],[0,0,0],[0,0,0]]
jogo9 = [[0,0,0],[0,0,0],[0,0,0]]

bsudoku.mostrajogo(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6,jogo7,jogo8,jogo9)
while bsudoku.testavitoria(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6,jogo7,jogo8,jogo9)==False:
    n = int(input("Digite o número: "))
    while n<1 or n>9:
        n = int(input("Digite um número válido: "))
    p1 = int(input("Digite a linha: "))
    while p1<1 or p1>9:
        p1 = int(input("Digite uma linha válida: "))
    p2 = int(input("Digite a coluna: "))
    while p2<1 or p2>9:
        p2 = int(input("Digite uma coluna válida: "))
    # if's errados. Necessário rever como colocar na linha e coluna correta.
    if p1==1:
        jogo1[p1-1][p2-1] = n
    if p1==2:
        jogo2[p1-1][p2-1] = n
    if p1==3:
        jogo3[p1-1][p2-1] = n
    if p1==4:
        jogo4[p1-1][p2-1] = n
    if p1==5:
        jogo5[p1-1][p2-1] = n
    if p1==6:
        jogo6[p1-1][p2-1] = n
    if p1==7:
        jogo7[p1-1][p2-1] = n
    if p1==8:
        jogo8[p1-1][p2-1] = n
    if p1==9:
        jogo9[p1-1][p2-1] = n
    bsudoku.mostrajogo(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6,jogo7,jogo8,jogo9)
    
