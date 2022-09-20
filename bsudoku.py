def testadiferencah(jogo): # Não está comparando todos os elementos
    for k in range(0,3):
        for i in range(0,3):
            if jogo[k][i]==jogo[k-1][i-1]: # Isso está errado
                return False
    return True

    
def testahorizontal(jogo):
    soma = 0
    if(testadiferencah(jogo)):
        for k in range(0,3):
            for i in range(0,3):
                if jogo[k][i]!="_":
                    soma = soma+jogo[k][i]
    if soma==45:
        return True
    else:
        return False
                    
                
#def testafimvertical(jogo1,jogo2,jogo3):

#matriz = [[1,2,2],[4,5,6],[7,8,9]]
#resultado = testahorizontal(matriz)
