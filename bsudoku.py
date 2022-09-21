def testarepetidosh(jogo):
    for i in range(0,3):
        for j in range(0,3):
            comp = jogo[i][j]
            for k in range(0,3):
                for n in range(0,3):
                    if (comp == jogo[k][n] and (k!=i or n!=j)):
                        return False
    return True
    
def testahorizontal(jogo):
    soma = 0
    if(testarepetidosh(jogo)):
        for k in range(0,3):
            for i in range(0,3):
                if jogo[k][i]!="_":
                    soma = soma+jogo[k][i]
    if soma==45:
        return True
    else:
        return False

def testacompletahorizontal(matriz,matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8):
    total = 0
    if testahorizontal(matriz):
        total = total+1
    if testahorizontal(matriz1):
        total = total+1
    if testahorizontal(matriz2):
        total = total+1
    if testahorizontal(matriz3):
        total = total+1
    if testahorizontal(matriz4):
        total = total+1
    if testahorizontal(matriz5):
        total = total+1
    if testahorizontal(matriz6):
        total = total+1
    if testahorizontal(matriz7):
        total = total+1
    if testahorizontal(matriz8):
        total = total+1
    if total==9:
        return True
    return False

# Jogo ganho para testes
matriz1 = [[5,3,4],[6,7,8],[9,1,2]]
matriz2 = [[6,7,2],[1,9,5],[3,4,8]]
matriz3 = [[1,9,8],[3,4,2],[5,6,7]]
matriz4 = [[8,5,9],[7,6,1],[4,2,3]]
matriz5 = [[4,2,6],[8,5,3],[7,9,1]]
matriz6 = [[7,1,3],[9,2,4],[8,5,6]]
matriz7 = [[9,6,1],[5,3,7],[2,8,4]]
matriz8 = [[2,8,7],[4,1,9],[6,3,5]]
matriz9 = [[3,4,5],[2,8,6],[1,7,9]]

# Testa se o jogo horizontal está completo
if testacompletahorizontal(matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8,matriz9): #and testacompletavertical():
    print("Jogo vencido")
