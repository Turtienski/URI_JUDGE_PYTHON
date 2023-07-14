def ler_expressoes(T):
    expressoes = []
    for i in range(T):
        entrada = input().replace("=", " ")
        numeros = entrada.split()
        numeros = [int(numero) for numero in numeros]
        expressoes.append(numeros)
    return expressoes

def respostas(T):
    jogadores = []
    for i in range(T):
        jogada = input().split()
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
        if sinal == "*":
            if expressao[0] * expressao[1] != expressao[2]:
                 perdedores.append(jogador)
        if sinal == "-":
            if expressao[0] - expressao[1] != expressao[2]:
                 perdedores.append(jogador)
        if sinal == "I":
            if (expressao[0] - expressao[1] == expressao[2] or 
               expressao[0] + expressao[1] == expressao[2] or
               expressao[0] * expressao[1] == expressao[2]):
                 perdedores.append(jogador)
    return perdedores

def main():
    while True:
        try:
            T = int(input())
            expressoes = ler_expressoes(T)
            jogadores = respostas(T)
            resultado = verifica_resposta(T, expressoes, jogadores)
            if len(resultado) == 0:
                print("You Shall All Pass!")
            elif len(resultado) == T:
                print("None Shall Pass!") 
            else:
                string_final = " ".join(sorted(resultado))
                print("{}".format(string_final))
        except EOFError:
            break
                    
if __name__ == "__main__":
    main()