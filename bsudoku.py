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

def testarepetidosvertical(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6,jogo7,jogo8,jogo9):
    for k in range(0,9):
        if (jogo1[k][k]==jogo2[k][k] 
        or jogo1[k][k]==jogo3[k][k] 
        or jogo1[k][k]==jogo4[k][k] 
        or jogo1[k][k]==jogo5[k][k] 
        or jogo1[k][k]==jogo6[k][k] 
        or jogo1[k][k]==jogo7[k][k] 
        or jogo1[k][k]==jogo8[k][k] 
        or jogo1[k][k]==jogo9[k][k]
        or jogo2[k][k]==jogo3[k][k]
        or jogo2[k][k]==jogo4[k][k]
        or jogo2[k][k]==jogo5[k][k]
        or jogo2[k][k]==jogo6[k][k]
        or jogo2[k][k]==jogo7[k][k]
        or jogo2[k][k]==jogo8[k][k]
        or jogo2[k][k]==jogo9[k][k]
        or jogo3[k][k]==jogo4[k][k]
        or jogo3[k][k]==jogo5[k][k]
        or jogo3[k][k]==jogo6[k][k]
        or jogo3[k][k]==jogo7[k][k]
        or jogo3[k][k]==jogo8[k][k]
        or jogo3[k][k]==jogo9[k][k]
        or jogo4[k][k]==jogo5[k][k]
        or jogo4[k][k]==jogo6[k][k]
        or jogo4[k][k]==jogo7[k][k]
        or jogo4[k][k]==jogo8[k][k]
        or jogo4[k][k]==jogo9[k][k]
        or jogo5[k][k]==jogo6[k][k]
        or jogo5[k][k]==jogo7[k][k]
        or jogo5[k][k]==jogo8[k][k]
        or jogo5[k][k]==jogo9[k][k]
        or jogo6[k][k]==jogo7[k][k]
        or jogo6[k][k]==jogo8[k][k]
        or jogo6[k][k]==jogo9[k][k]
        or jogo7[k][k]==jogo8[k][k]
        or jogo7[k][k]==jogo9[k][k]
        or jogo8[k][k]==jogo9[k][k]):
            return False
        else:
            return True


#def testaquadrado(matriz1,matriz2,matriz3):
    # Comparações:
    # 00: 01 02 dele próprio
    # 00: 00 01 02 das outras 2 matrizes
    # 10: 11 12 dele próprio
    # 10: 10 11 12 das outras 2 matrizes
    # 20: 21 22 dele próprio
    # 20: 20 21 22 das outras 2 matrizes
    # Além disso, a soma dos elementos comparados precisa dar 45

# Necessário uma função que testa se o quadrado jogo1[n], jogo2[n] e jogo3[n] soma 45 e estão com números diferentes, pois não pode repetir nos quadrados e precisa ter todos os números também
def testavitoria(matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8,matriz9):
    if testacompletahorizontal(matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8,matriz9) and testarepetidosvertical(matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8,matriz9) and :
        return True
    return False

# Refazer essa função. Está printando errado.
def mostrajogo(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6,jogo7,jogo8,jogo9):
    #print(" ".join(str(jogo1[0])))
    #print(" ".join(str(jogo1[1])))
    #print(" ".join(str(jogo2[k])))
    #print(" ".join(str(jogo3[k])))
    #print(" ".join(str(jogo4[k])))
    #print(" ".join(str(jogo5[k])))
    #print(" ".join(str(jogo6[k])))
    #print(" ".join(str(jogo7[k])))
    #print(" ".join(str(jogo8[k])))
    #print(" ".join(str(jogo9[k])))
