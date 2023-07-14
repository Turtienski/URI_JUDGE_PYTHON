# Jogo do Operador

Por João Marcos Salvanini Bellini de Moraes, IFSULDEMINAS ![BR](https://resources.beecrowd.com.br/gallery/images/flags/br.gif) Brazil

**Timelimit: 1**

Samu Elmito adora criar jogos peculiares para desafiar seus amigos. Desta vez, ele inventou um jogo chamado "Jogo do Operador", em que ele cria expressões básicas e cada jogador deve escolher uma expressão e preencher a lacuna com o operador correto para validá-la. Os jogadores poderão escolher operadores de somente três tipos: adição, subtração e multiplicação. Porém, se o jogador achar que não há operador entre os três tipos que valide a expressão, poderá responder Impossível.

Sua tarefa é simples: dadas as expressões e as respostas dos jogadores, determinar os jogadores que não passarão para a outra fase do jogo.

## Entrada

A entrada é composta por um inteiro **T** (2 ≤ **T** ≤ 50) que indica a quantidade de expressões e de jogadores. Cada caso de teste é composto por **T** expressões na forma "X Y=Z", indicando que **X** operador **Y** (0 ≤ **X**, **Y** ≤ 10^3) é igual a **Z** (-10^3 ≤ **Z** ≤ 10^6), seguido de **T** jogadores e suas respectivas respostas na forma "N E R", sendo **N** o nome do jogador (até 50 caracteres e sem espaços), **E** o índice da expressão escolhida (1 ≤ **E** ≤ **T**) e **R** a resposta (+, -, * ou I, indicando Impossível). A entrada termina com EOF (fim de arquivo).

## Saída

Para cada caso de teste, se todos os jogadores passarem, imprima "You Shall All Pass!"; se nenhum jogador passar, imprima "None Shall Pass!"; caso contrário, imprima, em ordem lexicográfica e entre espaços, o nome dos jogadores que erraram a resposta e, desta forma, não passarão para a próxima fase do jogo.

**Exemplo de Entrada**

3

8 4=5

2 5=5

1 3=4

Samuel 2 +

Abner 3 +

Aline 1 *

2

1 2=-1

0 7=7

Luiz 2 -

Absolut 1 +


**Exemplo de Saída**

Aline Samuel
None Shall Pass!
