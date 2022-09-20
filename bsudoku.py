def testahorizontal(jogo):
    soma = 0
    for k in range(0,3):
        for i in range(0,3):
            if jogo[k][i]!="_":
                soma = soma+jogo[k][i]
                if jogo[k][i]==jogo[k-1][i-1]:
                    return False
                elif soma==45:
                    return True
    return False
                
#def testafimvertical(jogo1,jogo2,jogo3):
    
