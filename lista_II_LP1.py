'''
1) Faça uma função para contar a quantidade de caracteres existem em uma cadeia de caracteres.
   Sabendo que o caractere que termina a cadeia é representado como sendo ‘\0’.
        phrase = input('Digite alguma coisa para saber quantos caracteres tem: ')
        def length(word):
            return len(word)
        print(length(phrase))

2) Faça uma função para saber se uma data cadeia de caracteres está vazia ou não. 
   Ela deve retornar Verdadeiro se estiver vazia ou falso se contiver algo.
        cell = ''
        def validation (var):
            if var == '':
                return True
            else:
                return False

        print(validation(cell))

3) Faça uma função para saber se uma cadeia de caracteres (s1), contendo 1 ou mais caracteres, 
   está contida em uma outra cadeia de caracteres (s2). 
   Deve retornar o valor -1 caso a cadeia s1 não for encontrada em s2 ou retornar aposição inicial de s1 em s2.
        str1 = 'ani'
        str2 = 'daniel'

        def find(word1, word2):
            return word2.find(word1)

        print(find(str1, str2))

4) Faça uma função que inverta a cadeia de caracteres, ou seja, mostre a cadeia de caracteres de tras para frente. 
   Exemplo: “faça a sua jogada.” → “adagoj aus aaçaf.”.
        str1 = input('Coloque sua palavra ou frase: ')

        def inverter(string):
            return string[::-1]

        print(inverter(str1))

5) Faça uma função para verificar se uma palavra é palíndromo ou não. 
   Essa função vai retornar Verdadeiro se a palavra for palíndromo ou falso se não for.
        str1 = input('Coloque sua palavra ou frase: ')

        def inverter(string):
            return string[::-1]

        def palindrome(string, inverter):
            if string == inverter:
                return True
            else:
                return False

        print(palindrome(str1,inverter(str1)))

6) Sabendo-se que o computador conta os segundos passados deste o dia 1 janeiro de 1970 e que 1972 foi um ano bissexto, 
   faça uma função que retorne a data no formato, dia/mês/ano. O dia e mês com 2 dígitos e o ano com 4. 
   Lembrando que o ano bissexto acontece de 4 em 4 anos, com o mês de fevereiro tendo 29 dias.

7) Faça uma função que leia uma temperatura em graus Farenheit e a imprima em graus Centígrados. 
   A conversão de graus Farenheit para Centígrados é obtida por C=(5/9)(F-32).
        farenheitTemp = int(input('Escolha a temperatura em Farenheit: '))

        def celsiusConversor(temperature):
            return round((5/9)*(temperature-32),1)

        print(celsiusConversor(farenheitTemp))

8) Faça uma função para contar dinheiro. Os valores correspondentes aos valores de nota e moeda corrente, 
   deverão ser passadas em dois vetores: um vetor de moedas e um vetor de notas, cada posição do vetor deverá 
   conter a quantidade de cada valor. Cada posição corresponderá aos seguintes valores:
   Vetor moeda[6] →{1, 5, 10, 25, 50, 1}
   Vetor notas[7] → {2, 5, 10, 20, 50, 100, 200}
        coinsValue = [1, 5, 10, 25, 50, 100]
        ballotValue = [2, 5, 10, 20, 50, 100, 200]
        total = 0

        for n in coinsValue:
            value = int(input('Escolha uma quatidade para a moeda de '+ str(n) +' centavos: '))
            total += value * (n/100)

        for n in ballotValue:
            value = int(input('Escolha uma quatidade para a nota de '+ str(n) +' reais: '))
            total += value * n

        print(round(total, 2))

9) Faça uma função que seja informado o tempo em segundos e a função retorna o tempo em X anos, Y meses, Z dias e W minutos.
        secs = int(input('Insira uma quatidade de segundos: '))
        mins = secs / 60
        hours = mins / 60
        days = hours / 24
        weeks = days / 30
        years = weeks / 12

        def time(mins, days, weeks, years):
            while mins >= 60:
                mins -= 60
            while days > 30:
                days -= 30
            while weeks > 12:
                weeks -= 12
            return (str(round(mins)) + ' minutos ' + str(round(days)) + ' dias ' + str(round(weeks)) + ' meses ' + str(round(years)) + ' anos' )

        print(secs,'segundos são:',time(mins,days,weeks,years))

10) Faça uma função que receba duas coordenadas (x,y) e calcule a distância entre elas. Sabendo-se que a distância é calculada da seguinte forma:
d=√(x2−x1)² + ( y2−y1)²
        dot1 = []
        dot2 = []

        dot1.append(int(input('Escolha o valor de x do ponto 1: ')))
        dot1.append(int(input('Escolha o valor de y do ponto 1: ')))
        dot2.append(int(input('Escolha o valor de x do ponto 2: ')))
        dot2.append(int(input('Escolha o valor de y do ponto 2: ')))

        def twoPointsDistance(dot1, dot2):
            return round((((dot2[0]-dot1[0])**2 + (dot2[1]-dot1[1])**2)**(1/2)),2)

        print('A distância entre os dois pontos é:',twoPointsDistance(dot1, dot2))
'''
N = int(input('insira um número'))
def fatorial(x):
    if x < 1:
        return 1
    return fatorial(x-1)

print(fatorial(N))