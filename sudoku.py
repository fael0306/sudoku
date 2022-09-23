import bsudoku

jogo = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

bsudoku.mostrajogo(jogo)
#while bsudoku.testavitoria(jogo)==False:
#    n = int(input("Digite o número: "))
#    while n<1 or n>9:
#        n = int(input("Digite um número válido: "))
#    p1 = int(input("Digite a linha: "))
#    while p1<1 or p1>9:
#        p1 = int(input("Digite uma linha válida: "))
#    p2 = int(input("Digite a coluna: "))
#    while p2<1 or p2>9:
#        p2 = int(input("Digite uma coluna válida: "))
#    jogo[p1-1][p2-1]=n   
#    bsudoku.mostrajogo(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6,jogo7,jogo8,jogo9)
#    print("")
