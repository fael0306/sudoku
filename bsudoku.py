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

def testavitoria(matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8,matriz9):
    if testacompletahorizontal(matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8,matriz9) and testarepetidosvertical(matriz1,matriz2,matriz3,matriz4,matriz5,matriz6,matriz7,matriz8,matriz9):
        return True
    return False

def mostrajogo(jogo1,jogo2,jogo3,jogo4,jogo5,jogo6,jogo7,jogo8,jogo9):
    for k in range(3):
        print(" ".join(str(jogo1[k]))," ".join(str(jogo2[k]))," ".join(str(jogo3[k])))
        print(" ".join(str(jogo4[k]))," ".join(str(jogo5[k]))," ".join(str(jogo6[k])))
        print(" ".join(str(jogo7[k]))," ".join(str(jogo8[k]))," ".join(str(jogo9[k])))

def lugarcorreto(jogo,p2,n):
    if p2<=3:
        if p2==1:
            jogo[0][0]=n
        elif p2==2:
            jogo[0][1]=n
        elif p2==3:
            jogo[0][2]=n
    elif p2<=6:
        if p2==4:
            jogo[1][0]=n
        elif p2==5:
            jogo[1][1]=n
        elif p2==6:
            jogo[1][2]=n
    elif p2<=9:
        if p2==7:
            jogo[2][0]=n
        elif p2==8:
            jogo[2][1]=n
        elif p2==9:
            jogo[2][2]=n
