import random

def sorteiasudoku():
    sudoku1 = [[4,0,9,8,0,2,1,7,0],
     [0,0,1,0,4,0,3,0,9],
     [0,3,5,0,0,6,0,0,0],
     [0,0,0,0,0,3,0,9,0],
     [6,9,0,0,5,7,0,0,3],
     [0,0,0,0,0,4,6,2,7],
     [9,2,6,0,0,8,4,5,1],
     [1,5,0,0,2,0,0,3,0],
     [0,0,0,0,0,1,9,0,2]]
    sudoku2 = [[0,0,6,0,0,8,0,0,0],
     [0,0,0,5,0,0,0,6,2],
     [2,9,0,0,0,0,5,7,0],
     [0,0,0,8,4,0,9,0,0],
     [0,2,5,1,6,0,8,3,7],
     [8,1,9,3,5,0,0,2,4],
     [0,4,2,9,0,3,0,0,0],
     [0,0,0,2,0,0,7,0,0],
     [6,8,0,0,0,5,0,0,3]]
    # Incluir 10 possibilidades de Sudoku nível fácil retirados do site https://sudoku.com/pt/facil/
    lista = [sudoku1,sudoku2]#,sudoku3,sudoku4,sudoku5,sudoku6,sudoku7,sudoku8,sudoku9,sudoku10]
    return mostrajogo(random.choice(lista))

# Não precisa testar se a soma dá 45. Se todos os números estão entre 1 e 9 e não repetem na vertical e horizontal, está certo o jogo.
def testarepetidosh(jogo):
    for i in range(0,9):
        for j in range(0,8):
            for n in range(j+1,9):
                if (jogo[i][j] == jogo[i][n]):
                    return False
    return True
    
def testarepetidosv(jogo):
    for k in range(0,9):
        for i in range(0,8):
            for j in range(i+1,9):
                if (jogo[j][k]==jogo[i][k]):
                    return False
    return True


#def testarepetidosq(jogo) - Verifica se cada elemento de cada quadrado 3x3 da matriz possui números diferentes
#def testaquadrados(jogo) - Verifica se 00 01 02 10 11 12 20 21 22 são diferentes
#                                       03 04 05 13 14 15 23 24 25 são diferentes
#                                       06 07 08 16 17 18 26 27 28 são diferentes
#                                       30 31 32 40 41 42 50 51 52 são diferentes
#                                       33 34 35 43 44 52 53 54 55 são diferentes
#                                       36 37 38 46 47 48 56 57 58 são diferentes
#                                       60 61 62 70 71 72 80 81 82 são diferentes
#                                       63 64 65 73 74 75 83 84 85 são diferentes
#                                       66 67 68 76 77 78 86 87 88 são diferentes
#                                       NECESSÁRIO ACHAR O PADRÃO DE REPETIÇÃO PARA TESTAR
# O def de testar quadrado gira em torno de algo parecido com as repetições abaixo
#soma = 0
#for i in range(3):
#    for c in range(soma,soma+3):
#        for k in range(3):
#            print(sudoku1[k][c])
#    soma = soma+3
#soma = 0
#for i in range(3):
#    for c in range(soma,soma+3):
#        for k in range(3,6):
#            print(sudoku1[k][c])
#    soma = soma+3
#for i in range(3):
#    for c in range(soma,soma+3):
#        for k in range(6,9):
#            print(sudoku1[k][c])
#    soma = soma+3

#def testavitoria(matriz):
#    if testahorizontal(matriz) and testavertical(matriz) and testaquadrados(matriz):
#        return True
#    return False

def mostrajogo(jogo):
    a = ""
    for i in range(9):
        for k in list(jogo[i]):
            a = a+str(k)
        print(a)
        a=""
