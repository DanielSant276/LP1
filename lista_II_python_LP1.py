'''
1. Já feita na lista I

2. Já feita na lista I

3. Já feita na lista I

4. Já feita na lista I

5. Já feita na lista I

6. Já feita na lista I

7. Já feita na lista I

8. Já feita na lista I

9. Já feita na lista I

10. Já feita na lista I

11.Crie um programa para ler uma string fornecida pelo usuário. Informe se essa string forma um palíndromo.
R=
string = input('Insira uma palavra: ')

def palindrome(string):
    if string == string[::-1]:
        return 'É um palíndromo'
    return 'Não é um palíndromo'

print(palindrome(string))

12.Crie um programa para ler duas strings fornecidas pelo usuário. Verifique se elas foram um anagrama.
R=
string1 = input('Escolha a primeira palavra: ')
string2 = input('Escolha a segunda palavra do mesmo tamanho qua a anterior: ')
total = 0

def anagram(string1, string2, total):
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                total += 1
                break
            
    if total == len(string1):
        return 'É anagrama'
    else:
        return 'Não é anagrama'

print(anagram(string1, string2, total))

13.Faça um programa para multiplicar matrizes 3x3.
R=
m1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
m2 = [[9, 10, 11], [12, 13, 14], [15, 16, 17]]

def arrayMultiply(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        mMultiply = [['','',''],['','',''],['','','']]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                aux = 0
                for k in range(len(m1[0])):
                    aux += m1[i][k] 0 m2[k][j]
                mMultiply[i][j] = aux 
    return mMultiply

print(arrayMultiply(m1, m2))

14.Faça um programa para calcular a soma, a subtração e a multiplicação de matrizes. 
   Você pode fornecer a matriz no código, em vez de ler o que o usuário digitar, mas suas funções 
   que fazem os cálculos devem ser úteis para qualquer tamanho de matriz desde que as propriedades matemáticas sejam respeitadas.
R=
m1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
m2 = [[9, 10, 11], [12, 13, 14], [15, 16, 17]]
option = input('Escolha entre soma, multiplicação e subtração: ')

def mult(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        mMultiply = [['','',''],['','',''],['','','']]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                aux = 0
                for k in range(len(m1[0])):
                    aux += m1[i][k] * m2[k][j]
                mMultiply[i][j] = aux 
    return mMultiply

def plus(m1, m2):
    if len(m1) == len(m2):
        mSum = []
        for i in range(len(m1)):
            mSum.append([])
            for j in range(len(m2[0])):
                multiply = m1[i][j] + m2[i][j]
                mSum[i].append(multiply)
    return mSum

def min(m1, m2):
    if len(m1) == len(m2):
        mMin = []
        for i in range(len(m1)):
            mMin.append([])
            for j in range(len(m2[0])):
                multiply = m1[i][j] - m2[i][j]
                mMin[i].append(multiply)
    return mMin

def choose(m1, m2, option):
    if option == 'soma':
        print(plus(m1, m2))
    elif option == 'multiplicação':
        print(mult(m1, m2))
    else:
        print(min(m1, m2))

choose(m1, m2, option)

15.Crie um programa que verifica todos os números perfeitos em um intervalo fornecido pelo usuário. 
   Ou seja, o usuário fornece dois valores (inicial e final) e o programa verifica se existe e quais são os números perfeitos nesse intervalo. 
   Para saber o que são números perfeitos, busque na wikipedia.
R=
num1 = int(input('Escolha um número inicial: '))
num2 = int(input('Escolha um número final: '))
perfectNumberList = []

def perfectNumber(number1, number2):
    for i in range(number1, number2):
        total = []
        for j in range(2, i + 1):
            if i == 1:
                pass
            elif  (i / j).is_integer():
                total.append(int(i / j))
        if i == sum(total):
            perfectNumberList.append(i)

perfectNumber(num1, num2)

print(perfectNumberList)

16.Faça um programa para o jogo da velha. Considere dois jogadores que se alternam nas jogadas. O primeiro é o “x” e o segundo o “o”. 
   -A cada jogada você deve atualizar a visualização do jogo da velha e verificar se o jogo chegou ao fim. 
   As opções de finalização são: empate ou vencedor. 
   No caso de ter um vencedor, indique qual jogador venceu. 
   -A cada jogada permita que o jogador indique em qual linha x coluna deseja jogar. 
   -Não permita que o jogador insira uma jogada em um local que já recebeu uma marcação. 
   -Não permita que um jogador jogue duas vezes seguidas tomando a vez do adversário.
   Qualquer jogador pode desistir do jogo inserindo algum valor específico para isso. 
   Ele também pode encerrar o programa com uma entrada específica. 
   No caso em que ele desiste do jogo, o adversário deve ser considerado vencedor e o jogo deve poder ser reiniciado. 
   No caso de saída do programa, ele deve parar a execução com uma mensagem de “tchau, até logo!”.
R=
from os import system 

ticTacToe = [['-','-','-'],['-','-','-'],['-','-','-']]
finish = False
draw = False

def clear(): 
    _ = system('cls')

def ticTacToeFormation():
        print(ticTacToe[0][0], ticTacToe[0][1], ticTacToe[0][2])
        print(ticTacToe[1][0], ticTacToe[1][1], ticTacToe[1][2])
        print(ticTacToe[2][0], ticTacToe[2][1], ticTacToe[2][2])

def question():
    global finish
    quest = input('desistir? ')
    if quest == 's' or quest == 'sim':
        finish = True

def play():
    global finish, draw

    xTurn = True
    oTurn = False

    while not finish:
        while xTurn:
            question()
            if finish:
                winner = 'o'
                print('O jogador x desistiu.', end=' ')
                break
            
            valid = False
            while not valid:
                player1Row = int(input('Jogador 1, escolhar uma linha: ')) - 1
                player1Col = int(input('Jogador 1, escolha uma coluna: ')) - 1
                if  0 <= player1Row < 3 and 0 <= player1Col < 3:   
                    if ticTacToe[player1Row][player1Col] == '-':
                        valid = True
                    else:
                        print('Espaço ocupado por uma jogada, escolha outro espaço')
                else:
                    print('Espaço inválido')
            ticTacToe[player1Row][player1Col] = 'x'

            clear()
            ticTacToeFormation()
            
            if (ticTacToe[0][0] == 'x' and ticTacToe[0][1] == 'x' and ticTacToe[0][2] == 'x') or (ticTacToe[1][0] == 'x' and ticTacToe[1][1] == 'x' and ticTacToe[1][2] == 'x') or (ticTacToe[2][0] == 'x' and ticTacToe[2][1] == 'x' and ticTacToe[2][2] == 'x') or (ticTacToe[0][0] == 'x' and ticTacToe[1][0] == 'x' and ticTacToe[2][0] == 'x') or (ticTacToe[0][1] == 'x' and ticTacToe[1][1] == 'x' and ticTacToe[2][1] == 'x') or (ticTacToe[0][2] == 'x' and ticTacToe[1][2] == 'x' and ticTacToe[2][2] == 'x') or (ticTacToe[0][0] == 'x' and ticTacToe[1][1] == 'x' and ticTacToe[2][2] == 'x') or (ticTacToe[0][2] == 'x' and ticTacToe[1][1] == 'x' and ticTacToe[2][0] == 'x'):
                winner = 'x'
                finish = True
                break

            xTurn = False
            oTurn = True

        if not finish:
            while oTurn:
                question()
                if finish:
                    winner = 'x'
                    print('O jogador o desistiu.', end=' ')
                    break

                valid = False
                while not valid:
                    player2Row = int(input('Jogador 2, escolhar uma linha: ')) - 1
                    player2Col = int(input('Jogador 2, escolha uma coluna: ')) - 1
                    if  0 <= player2Row < 3 and 0 <= player2Col < 3:   
                        if ticTacToe[player2Row][player2Col] == '-':
                            valid = True
                        else:
                            print('Espaço ocupado por uma jogada, escolha outro espaço')
                    else:
                        print('Espaço inválido')
                ticTacToe[player2Row][player2Col] = 'o'

                clear()
                ticTacToeFormation()
                
                if (ticTacToe[0][0] == 'o' and ticTacToe[0][1] == 'o' and ticTacToe[0][2] == 'o') or (ticTacToe[1][0] == 'o' and ticTacToe[1][1] == 'o' and ticTacToe[1][2] == 'o') or (ticTacToe[2][0] == 'o' and ticTacToe[2][1] == 'o' and ticTacToe[2][2] == 'o') or (ticTacToe[0][0] == 'o' and ticTacToe[1][0] == 'o' and ticTacToe[2][0] == 'o') or (ticTacToe[0][1] == 'o' and ticTacToe[1][1] == 'o' and ticTacToe[2][1] == 'o') or (ticTacToe[0][2] == 'o' and ticTacToe[1][2] == 'o' and ticTacToe[2][2] == 'o') or (ticTacToe[0][0] == 'o' and ticTacToe[1][1] == 'o' and ticTacToe[2][2] == 'o') or (ticTacToe[0][2] == 'o' and ticTacToe[1][1] == 'o' and ticTacToe[2][0] == 'o'):
                    winner = 'o'
                    finish = True
                    break

                xTurn = True
                oTurn = False
        
        total = 0
        for i in range(len(ticTacToe)):
            for j in range(len(ticTacToe[0])):
                if ticTacToe[i][j] != '-':
                    total += 1
        if total == 9:
            finish = True
            draw = True

        
    if finish:
        if draw:
            print('O jogo empatou, não houve vencedores')
        else:
            print('O vencedor foi o jogador', winner)

play()
print('tchau, até logo!')
'''
m1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
m2 = [[9, 10, 11], [12, 13, 14], [15, 16, 17]]
option = input('Escolha entre soma, multiplicação e subtração: ')

def mult(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        mMultiply = [['','',''],['','',''],['','','']]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                aux = 0
                for k in range(len(m1[0])):
                    aux += m1[i][k] * m2[k][j]
                mMultiply[i][j] = aux 
    return mMultiply

def plus(m1, m2):
    if len(m1) == len(m2):
        mSum = []
        for i in range(len(m1)):
            mSum.append([])
            for j in range(len(m2[0])):
                multiply = m1[i][j] + m2[i][j]
                mSum[i].append(multiply)
    return mSum

def min(m1, m2):
    if len(m1) == len(m2):
        mMin = []
        for i in range(len(m1)):
            mMin.append([])
            for j in range(len(m2[0])):
                multiply = m1[i][j] - m2[i][j]
                mMin[i].append(multiply)
    return mMin

def choose(m1, m2, option):
    if option == 'soma':
        print(plus(m1, m2))
    elif option == 'multiplicação':
        print(mult(m1, m2))
    else:
        print(min(m1, m2))

choose(m1, m2, option)

total = 0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j] != '-':
                total += 1
    if total == 9:
        empate = True
        break