import bsudoku

def main():
    jogo = bsudoku.sorteiasudoku()

    bsudoku.mostrajogo(jogo)
    print("")
    imutaveis = bsudoku.verificapreenchidos(jogo)

    while bsudoku.testavitoria(jogo)==False:
        try:
            n = int(input("Digite o número: "))
            while n<1 or n>9:
                n = int(input("Digite um número válido: "))
            p1 = int(input("Digite a linha: "))
            while p1<1 or p1>9:
                p1 = int(input("Digite uma linha válida: "))
            p2 = int(input("Digite a coluna: "))
            print("")
            while p2<1 or p2>9:
                p2 = int(input("Digite uma coluna válida: "))
        except ValueError:
            print("Você digitou algo que não é um número inteiro. O jogo será resetado.")
            main()
        if jogo[p1-1][p2-1]==0:
            jogo[p1-1][p2-1]=n
            bsudoku.mostrajogo(jogo)
        else:
            v = 0
            for k in range(0,len(imutaveis)-1):
                if imutaveis[k]==[p1-1, p2-1]:
                    v = 1
            if v==1:
                print("Essa posição está automaticamente preenchida. Escolha outra.")
            else:
                jogo[p1-1][p2-1]=n
            v = 0
            bsudoku.mostrajogo(jogo)
        print("")
    print("Parabéns, você venceu")
main()