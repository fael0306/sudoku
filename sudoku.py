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
# Descobrir onde está o erro: o número vai para a posição errada
    if p1==1:
        bsudoku.lugarcorreto(jogo1,p2,n)
    if p1==2:
        bsudoku.lugarcorreto(jogo2,p2,n)
    if p1==3:
        bsudoku.lugarcorreto(jogo3,p2,n)
    if p1==4:
        bsudoku.lugarcorreto(jogo4,p2,n)
    if p1==5:
        bsudoku.lugarcorreto(jogo5,p2,n)
    if p1==6:
        bsudoku.lugarcorreto(jogo6,p2,n)
    if p1==7:
        bsudoku.lugarcorreto(jogo7,p2,n)
    if p1==8:
        bsudoku.lugarcorreto(jogo8,p2,n)
    if p1==9:
        bsudoku.lugarcorreto(jogo9,p2,n)
        
    bsudoku.mostrajogo(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6,jogo7,jogo8,jogo9)
    
