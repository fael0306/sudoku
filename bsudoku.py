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

# Não precisa testar se a soma dá 45. Se todos os números estão entre 1 e 9 e não repetem na vertical, horizontal ou nos quadrados, está certo o jogo.
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

def testarepetidoslistadenove(lista):
    for k in range(8):
        for i in range(k+1,9):
            if lista[k]==lista[i]:
                return False
    return True

def testarepetidosq(jogo):
    lista1 = []
    lista2 = []
    lista3 = []
    soma = 0
    for i in range(3):
        for c in range(soma,soma+3):
            for k in range(3):
                lista1.append(sudoku1[c][k])
        if testarepetidoslistadenove(lista1)==False:
            return False
        soma = soma+3
    soma = 0
    for i in range(3,6):
        for c in range(soma,soma+3):
            for k in range(3,6):
                lista2.append(sudoku1[i][c])
        if testarepetidoslistadenove(lista2)==False:
            return False
        soma = soma+3
    soma = 0
    for i in range(6,9):
        for c in range(soma,soma+3):
            for k in range(6,9):
                lista3.append(sudoku1[i][c])
        if testarepetidoslistadenove(lista3)==False:
            return False
    return True

def testavitoria(jogo):
    if testarepetidosv and testarepetidosh and testarepetidosq:
        return True
    else:
        return False

def mostrajogo(jogo):
    a = ""
    for i in range(9):
        for k in list(jogo[i]):
            a = a+str(k)
        print(a)
        a=""
