import sys

def ler_expressoes(lines, start, T):
    expressoes = []
    for i in range(start, start + T):
        entrada = lines[i].replace("=", " ")
        numeros = entrada.split()
        numeros = [int(numero) for numero in numeros]
        expressoes.append(numeros)
    return expressoes

def respostas(lines, start, T):
    jogadores = []
    for i in range(start, start + T):
        jogada = lines[i].split()
        jogadores.append(jogada)
    return jogadores

def verifica_resposta(T, expressoes, jogadores):
    perdedores = []
    for i in range(T):
        jogador = jogadores[i][0]
        sinal = jogadores[i][2]
        indice = int(jogadores[i][1]) - 1
        expressao = expressoes[indice]
        if sinal == "+":
            if expressao[0] + expressao[1] != expressao[2]:
                 perdedores.append(jogador)
        elif sinal == "*":
            if expressao[0] * expressao[1] != expressao[2]:
                 perdedores.append(jogador)
        elif sinal == "-":
            if expressao[0] - expressao[1] != expressao[2]:
                 perdedores.append(jogador)
        elif sinal == "I":
            if (expressao[0] + expressao[1] == expressao[2] or
                expressao[0] * expressao[1] == expressao[2] or
                expressao[0] - expressao[1] == expressao[2]):
                 perdedores.append(jogador)
    return perdedores

def main():
    lines = sys.stdin.readlines()
    start = 0
    while start < len(lines):
        T = int(lines[start])
        start += 1
        expressoes = ler_expressoes(lines, start, T)
        start += T
        jogadores = respostas(lines, start, T)
        start += T
        resultado = verifica_resposta(T, expressoes, jogadores)
        if len(resultado) == 0:
            print("You Shall All Pass!")
        elif len(resultado) == T:
            print("None Shall Pass!")
        else:
            string_final = " ".join(sorted(resultado))
            print("{}".format(string_final))
                    
if __name__ == '__main__':
    main()