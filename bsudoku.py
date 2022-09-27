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
    sudoku3 = [[0,0,1,9,8,4,7,6,0],
     [6,0,0,0,5,7,0,0,0],
     [8,0,7,0,1,0,0,0,0],
     [9,6,0,3,0,8,1,0,5],
     [1,8,5,0,2,0,0,7,3],
     [3,0,0,0,0,0,2,0,8],
     [2,1,0,0,0,0,0,3,6],
     [0,0,0,1,0,0,0,0,4],
     [0,9,6,0,0,2,5,1,0]]
    sudoku4 = [[0,0,6,0,0,0,7,5,1],
     [2,0,0,7,0,0,0,9,0],
     [0,5,0,0,0,6,4,8,0],
     [9,0,2,0,7,0,0,0,4],
     [3,7,4,0,0,0,8,0,0],
     [1,8,5,4,2,9,0,0,7],
     [0,0,1,9,0,0,0,7,0],
     [0,0,9,0,5,0,1,0,0],
     [0,2,7,6,0,3,0,4,5]]
    sudoku5 = [[0,7,9,0,4,0,5,0,0],
     [1,8,0,3,5,0,0,0,0],
     [0,0,0,1,0,0,0,6,0],
     [4,1,0,2,0,9,6,7,5],
     [0,0,0,7,0,8,0,3,0],
     [3,2,7,5,0,4,8,0,1],
     [0,3,1,0,0,0,0,4,6],
     [9,0,0,0,7,0,0,0,0],
     [0,0,0,4,0,0,1,0,9]]
    sudoku6 = [[0,0,0,6,9,0,4,0,0],
     [0,2,9,0,0,5,0,0,3],
     [0,0,1,0,3,4,0,0,8],
     [9,8,0,0,0,1,0,7,0],
     [2,0,7,0,6,9,0,3,1],
     [0,0,3,2,0,7,5,4,0],
     [8,3,0,9,0,0,0,0,7],
     [0,0,5,0,2,0,0,0,0],
     [1,0,6,5,7,3,0,0,4]]
    sudoku7 = [[3,4,0,0,2,6,0,8,0],
     [0,0,1,0,7,0,0,0,0],
     [7,2,0,8,0,0,4,3,9],
     [4,0,9,6,0,0,3,0,2],
     [0,0,0,0,1,9,0,7,0],
     [1,0,0,0,0,4,9,0,0],
     [0,0,0,5,6,8,0,0,7],
     [0,0,0,0,0,2,0,0,5],
     [2,5,4,0,9,7,8,6,3]]
    sudoku8 = [[4,0,0,0,0,1,0,0,0],
     [0,5,8,0,0,0,6,0,3],
     [0,0,0,0,6,0,0,8,4],
     [0,0,0,9,1,0,5,0,0],
     [6,8,0,4,7,0,1,3,2],
     [5,7,1,6,2,0,0,9,8],
     [8,9,0,0,5,2,0,0,0],
     [0,0,0,0,8,0,3,0,0],
     [0,1,4,0,0,6,0,2,0]]
    sudoku9 = [[0,0,6,8,5,1,0,0,0],
     [3,4,0,9,0,6,8,0,0],
     [0,0,0,4,7,3,2,5,6],
     [4,0,9,6,0,0,0,3,0],
     [0,0,0,0,0,0,5,9,8],
     [0,0,8,2,1,0,0,6,0],
     [0,1,0,5,6,8,4,0,0],
     [0,0,0,3,4,0,0,0,0],
     [0,0,0,1,9,7,6,0,3]]
    sudoku10 = [[0,1,0,7,0,0,9,3,0],
     [6,9,0,0,0,2,0,1,7],
     [0,0,0,0,0,6,8,2,4],
     [2,6,0,0,7,8,0,4,0],
     [5,8,1,4,0,9,0,7,0],
     [0,7,0,5,6,1,0,0,8],
     [0,3,5,0,0,0,7,0,2],
     [7,0,0,6,1,0,0,0,9],
     [0,0,0,0,0,7,0,0,0]]
    lista = [sudoku1,sudoku2,sudoku3,sudoku4,sudoku5,sudoku6,sudoku7,sudoku8,sudoku9,sudoku10]
    return random.choice(lista)

def verificapreenchidos(jogo):
    try:
        imutaveis = []
        for l in range(9):
            for c in range(9):
                if jogo[l][c]!=0:
                    imutaveis.append([l,c])
        return imutaveis
    except:
        return imutaveis

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
    return(testarepetidosv==False and testarepetidosh==False and testarepetidosq==False)

def mostrajogo(jogo):
    a = ""
    for i in range(9):
        for k in list(jogo[i]):
            a = a+str(k)
        print(a)
        a=""
    
