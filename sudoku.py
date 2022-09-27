import bsudoku

jogo = bsudoku.sorteiasudoku()

bsudoku.mostrajogo(jogo)
print("")
imutaveis = bsudoku.verificapreenchidos(jogo)

while bsudoku.testavitoria(jogo)==False:
    n = int(input("Digite o número: "))
    while n<1 or n>9:
        n = int(input("Digite um número válido: "))
    p1 = int(input("Digite a linha: "))
    while p1<1 or p1>9:
        p1 = int(input("Digite uma linha válida: "))
    p2 = int(input("Digite a coluna: "))
    while p2<1 or p2>9:
        p2 = int(input("Digite uma coluna válida: "))
    if jogo[p1-1][p2-1]==0:
        jogo[p1-1][p2-1]=n
    else:
        for k in (0,len(imutaveis)-1):
            for i in range(0,len(imutaveis[k])-1):
                if imutaveis[k,i]==jogo[p1-1][p2-1]:
                    print("Essa posição está automaticamente preenchida. Escolha outra.")
                    bsudoku.mostrajogo(jogo)
        jogo[p1-1][p2-1]=n
    bsudoku.mostrajogo(jogo)
    print("")
