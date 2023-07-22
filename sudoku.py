import bsudoku

def main():
    jogo = bsudoku.sorteiasudoku()
    bsudoku.mostrajogo(jogo)
    print("")

    imutaveis = bsudoku.verificapreenchidos(jogo)

    while not bsudoku.testavitoria(jogo):
        try:
            n = int(input("Digite o número: "))
            while n < 1 or n > 9:
                n = int(input("Digite um número válido: "))

            p1 = int(input("Digite a linha: "))
            while p1 < 1 or p1 > 9:
                p1 = int(input("Digite uma linha válida: "))

            p2 = int(input("Digite a coluna: "))
            while p2 < 1 or p2 > 9:
                p2 = int(input("Digite uma coluna válida: "))
        except ValueError:
            print("Você digitou algo que não é um número inteiro. O jogo será resetado.")
            main()

        if jogo[p1 - 1][p2 - 1] == 0:
            jogo[p1 - 1][p2 - 1] = n
        else:
            if [p1 - 1, p2 - 1] in imutaveis:
                print("Essa posição está automaticamente preenchida. Escolha outra.")
            else:
                jogo[p1 - 1][p2 - 1] = n

        bsudoku.mostrajogo(jogo)
        print("")

    print("Parabéns, você venceu!")

if __name__ == "__main__":
    main()
