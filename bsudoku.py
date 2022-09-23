import random

#def sorteiasudoku(jogo):
#    sudoku1 = 
#        [[4,0,9,8,0,2,1,7,0],
#        [0,0,1,0,4,0,3,0,9],
#        [0,3,5,0,0,6,0,0,0],
#        [0,0,0,0,0,3,0,9,0],
#        [6,9,0,0,5,7,0,0,3],
#        [0,0,0,0,0,4,6,2,7],
#        [9,2,6,0,0,8,4,5,1],
#        [1,5,0,0,2,0,0,3,0],
#        [0,0,0,0,0,1,9,0,2]]
#    sudoku2 = 
# Incluir 10 possibilidades de Sudoku nível fácil retirados do site https://sudoku.com/pt/facil/
# lista = [sudoku1,sudoku2,sudoku3,sudoku4,sudoku5,sudoku6,sudoku7,sudoku8,sudoku9,sudoku10]
# return random.choice(lista)

def testarepetidosh(jogo):
    for i in range(0,9):
        for j in range(0,8):
            for n in range(j+1,9):
                if (jogo[i][j] == jogo[i][n]):
                    return False
    return True
    
def testahorizontal(jogo):
    soma = 0
    if(testarepetidosh(jogo)):
        for k in range(0,9):
            for i in range(0,9):
                soma = soma+jogo[k][i]
            if soma!=45:
                return False
            soma = 0
    else:
        return False
    return True

def testarepetidosv(matriz):
    for k in range(0,9):
        for i in range(0,8):
            for j in range(i+1,9):
                if (jogo[j][k]==jogo[i][k]):
                    return False
    return True
#def testavertical(jogo) - Verifica se a soma dá 45 em todas as verticais. Chama a função para testar repetidos antes, caso haja repetidos, nem roda a soma.
#                          Vertical: repete a coluna e varia cada linha, depois varia a coluna e repete a linha... 
#def testarepetidosq(jogo) - Verifica se cada elemento de cada quadrado 3x3 da matriz possui números diferentes
#def testaquadrados(jogo) - Verifica se 00 01 02 10 11 12 20 21 22 são diferentes e somam 45
#                                       03 04 05 13 14 15 23 24 25 são diferentes e somam 45
#                                       06 07 08 16 17 18 26 27 28 são diferentes e somam 45
#                                       30 31 32 40 41 42 50 51 52 são diferentes e somam 45
#                                       33 34 35 43 44 52 53 54 55 são diferentes e somam 45
#                                       36 37 38 46 47 48 56 57 58 são diferentes e somam 45
#                                       60 61 62 70 71 72 80 81 82 são diferentes e somam 45
#                                       63 64 65 73 74 75 83 84 85 são diferentes e somam 45
#                                       66 67 68 76 77 78 86 87 88 são diferentes e somam 45
#                                       NECESSÁRIO ACHAR O PADRÃO DE REPETIÇÃO PARA TESTAR

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
