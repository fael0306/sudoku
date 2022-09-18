def testafimhorizontal(jogo):
    soma = 0
    for k in range(1,3):
        for i in range(1,3):
            soma = soma+jogo[k][i]
            if jogo[k][i]==jogo[k-1][i-1]:
                continue
            elif soma==45:
                return True
                
def testafimvertical(jogo1,jogo2,jogo3):
    
