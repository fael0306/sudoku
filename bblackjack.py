import random as rd

cartas = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
    }

naipes = ["Espadas", "Copas", "Ouros", "Paus"]

cartasmao = []
naipesmao = []
pontuacaodacarta = []

cartaspc = []
naipespc = []
pontuacaopc =[]

def inicializamao():
    for _ in range(2):
        carta, ponto = rd.choice(list(cartas.items()))
        naipe = rd.choice(naipes)
        cartasmao.append(carta)
        naipesmao.append(naipe)
        pontuacaodacarta.append(ponto)

def inicializamaopc():
    for _ in range(2):
        carta, ponto = rd.choice(list(cartas.items()))
        naipe = rd.choice(naipes)
        cartaspc.append(carta)
        naipespc.append(naipe)
        pontuacaopc.append(ponto)
    
def mostramao():
    for k in range(3):
        print(cartasmao[k],"de",naipesmao[k])
    pontuacao = sum(pontuacaodacarta)
    print("Pontuação da mão:",pontuacao)

def puxacarta():
    carta, ponto = rd.choice(list(cartas.items()))
    naipe = rd.choice(naipes)
    cartasmao.append(carta)
    naipesmao.append(naipe)
    pontuacaodacarta.append(ponto)
    testavitoriabj()

def pcjoga():
    for _ in range(2):
        carta, ponto = rd.choice(list(cartas.items()))
        naipe = rd.choice(naipes)
        cartaspc.append(carta)
        naipespc.append(naipe)
        pontuacaopc.append(ponto)
    pontuacaototalpc = sum(pontuacaopc)
    while pontuacaototalpc<17 and len(cartaspc)<5:
        carta, ponto = rd.choice(list(cartas.items()))
        naipe = rd.choice(naipes)
        cartaspc.append(carta)
        naipespc.append(naipe)
        pontuacaopc.append(ponto)
    pontuacaototalpc = sum(pontuacaopc)
    testavitoriapc()

def jogar():
    try:
        pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória"))
        while pergunta==1:
            puxacarta()
            mostramao()
            pergunta = int(input("\n1 - Puxar mais uma carta\n2 - Encerrar rodada\n3 - Verificar vitória"))
        if pergunta==2:
            pcjoga()
        if pergunta==3:
            testavitoriapontos()
    except ValueError:
        print("O valor digitado é inválido")

def testavitoriabj():
    pontuacao = sum(pontuacaodacarta)
    if pontuacao==21:
        return True
    elif pontuacao>21:
        while "A" in cartasmao and pontuacao>21:
            i = cartasmao.index("A")
            pontuacaodacarta[i]=1
            pontuacao=sum(pontuacaodacarta)
        if pontuacao>21:
            return False
    return True

def testavitoriapc():
    pontuacaototalpc = sum(pontuacaopc)
    if pontuacaototalpc==21:
        return True
    elif pontuacaototalpc>21:
        return False
    else:
        jogar()

def testavitoriapontos():
    pontuacao = sum(pontuacaodacarta)
    if pontuacao>pontuacaopc:
        return True
    else:
        return False