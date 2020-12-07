'''
1. Faça programas que:
    a. Leia um número e imprima o seu quadrado.
    b. Leia dois números e imprima a divisão do primeiro pelo segundo.
    c. Leia um número e imprima o resto da divisão desse número por 2.
    d. Leia dois número e imprima a média.
    e. Calcule a área de uma circunferência considerando que o usuário informe o comprimento do raio. 
    Para essa questão, declare uma variável “pi” com valor de 3,14 e use como valor de π. Calcule também o comprimento e o diâmetro.
R=
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
pi = 3.14

def square (number):
    return number ** 2

def division (number1, number2):
    return number1 / number2

def remainder (number):
    return number % 2

def average (number1, number2):
    return (number1 + number2) / 2

def circleDiameter (ray):
    return ray * 2

def circleLength (ray):
    return pi * circleDiameter (num1)

def circleArea (ray):
    return pi * (ray ** 2)


print(num1,'  ', num2)
print(square(num1))
print(division(num1,num2))
print(remainder(num1))
print(average(num1,num2))
print(circleDiameter(num1))
print(circleLength(num1))
print(circleArea(num1))

2. Indique qual o resultado será obtido das seguintes expressões (lembre-se de usar “.” não “,” para casas decimais):
    a. 4*4 + 1
    b. 6 +20-23
    c. 3,0* 5,0 +1
    d. 1/4+2
    e. 29,0/7+4
    f. 3/6,0-7
    g. 2 / 2
    h. 2 // 2
    i. 4 % 2
    j. ( 100 // 5 ) % 5

R=
print(4 * 4 + 1)
print(6 + 20 - 23)
print(3.0 * 5.0 + 1)
print(1 / 4 + 2)
print(29.0 / 7 + 4)
print(3 / 6.0 - 7)
print(2 / 2)
print(2 // 2)
print(4 % 2)
print((100 // 5) % 5)

3. Indique o resultado lógico das seguintes expressões:
    a. 2 < 3
    b. ( 6 < 3 ) OU ( 10 > 11 )
    c. ((( 6 // 3 ) % 2 ) > 5 ) E ( 2 < ( 3 % 2 ) )
    d. !( 2 < 3 )

R=
print(2 < 3)
print(( 6 < 3 ) or ( 10 > 11 ))
print(((( 6 // 3 ) % 2 ) > 5 ) and ( 2 < ( 3 % 2 ) ))
print(not( 2 < 3 ))

4. Escreva o comando de atribuição e resolva a expressão das seguintes fórmulas matemáticas.
    a) ver no pdf
    b) ver no pdf
R=
a)
a = 10
b = 3
c = b
d = 4
e = d
f = 2
x = ((a - ((b / c) * 2)) / (d + (e / f))) * 2
print(x)

b)
z = 4
y = ((((2 + z - (2 * (((z) ** 2) ** (z + 2)))) / 2) - (((z + 1) ** (1 / 2)) / z)) / (3 ** z))
print(y)

5. Faça um programa para ler o nome do usuário e escrever na tela “Olá [nome informando]”. 
Por exemplo, considere que eu use seu programa, vou escrever meu nome e o programa deve imprimir “Olá Tiago”.
R=
name = input('Digite seu nome: ')

print('Olá',name)

6. Escreva um programa para ler 3 valores inteiros diferentes e escrevê-los em ordem crescente.
R=
numbers = [7, 3, 9]

def ordering(numberList):
    for i in range (len(numberList)):
        for j in range (len(numberList)):
            if numberList[i] < numberList[j]:
                tmp = numberList[j]
                numberList[j] = numberList[i]
                numberList[i] = tmp
    
    return numberList

print(ordering(numbers))

7. Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.
R=
num1 = int(input('Digite um número: '))

def evenOrOdd(number):
    if (number % 2 == 0):
        return print('Esse número é positivo')
    return print('Esse número é falso')

evenOrOdd(num1)

8. Escreva um programa para ler uma temperatura em graus Celsius, calcular e escrever o valor correspondente em graus Fahrenheit e Kelvin.
R=
import math

celsiusTemperature = int(input('Digite uma temperatura em Celsius: '))

def conversion(celsius):
    fahrenheit = math.ceil((5/9)*(celsius-32))
    kelvin = celsius + 273

    return print('A temperatura em fahrenheit é: ', fahrenheit, '   A temperatura em kelvin é: ', kelvin)

conversion(celsiusTemperature)

9. Faça um programa que leia duas entradas de tipos numéricos. Verifique qual o maior dos dois ou se eles são iguais. 
   Imprima uma mensagem informando.
R=
num1 = int(input('Primeiro número: ')) 
num2 = int(input('Segundo número: '))

def compare (number1, number2):
    if number1 == number2:
        print('Os dois número são iguais')
    elif number1 > number2:
        print('O primeiro número é maior que o segundo, ou seja,', number1, '>', number2)
    else:
        print('O primeiro número é menor que o segundo, ou seja,', number1, '<', number2)

compare(num1, num2)

10. Escreva um programa que leia um número menor igual a 10 e informe se esse número é primo.
R=
num = int(input('Insira um número menor que 10: '))

def isPrime(number):
    if number == 7 or number == 5 or number == 3 or number == 2:
        print('O número',number, 'é primo')
    else:
        print('O número',number, 'não é primo')

isPrime(num)

11. Faça um programa que leia três entradas de inteiros. Considere que cada entrada corresponde ao comprimento de uma aresta de um triângulo. 
    Verifique se os valores passados permitem que seja formado um triângulo considerando que elas devem se tocar nas extremidades.
R=
num1 = int(input('Insira um valor para a primeira aresta: '))
num2 = int(input('Insira um valor para a segunda aresta: '))
num3 = int(input('Insira um valor para a terceira aresta: '))

def triangleValidation(a, b, c):
    validation = ""

    if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
        print("É um triângulo")
    else:
        print("Não é um triângulo")

triangleValidation(num1,num2,num3)

12. Faça um programa para calcular a área de um triângulo. O usuário deve fornecer os valores da base e da altura.
R=
num1 = int(input('Insira um valor para a base: '))
num2 = int(input('Insira um valor para a altura: '))

def triangleArea(base, height):
    return (base * height) / 2

print(triangleArea(num1,num2))

13. Escreva um programa que leia três entradas numéricas correspondentes às arestas de um triângulos. 
    Caso os valores permitam que seja formado um triângulo, informe qual tipo de triângulo (equilátero, isósceles ou escaleno).
R=
num1 = int(input('Insira um valor para a primeira aresta: '))
num2 = int(input('Insira um valor para a segunda aresta: '))
num3 = int(input('Insira um valor para a terceira aresta: '))

def triangleType(a, b, c):
    if a == b and a == c and b == c:
        print('Esse triângulo é equilátero')
    elif a != b and a != c and b != c:
        print('Esse triângulo é escaleno')
    else:
        print('Esse triângulo é isósceles')
    
triangleType(num1,num2,num3)

14. Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
    - Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
    - Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
    - Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)
R=
num1 = int(input('Insira um valor para o primeiro ângulo: '))
num2 = int(input('Insira um valor para o segundo ângulo: '))
num3 = int(input('Insira um valor para o terceiro ângulo: '))

def triangleType(a, b, c):
    if a + b + c == 180:
        if a == 90 or b == 90 or c == 90:
            print('Esse triângulo é retângulo')
        elif a > 90 or b > 90 or c > 90:
            print('Esse triângulo é obtusângulo')
        else:
            print('Esse triângulo é Acutângulo')
    elif a + b + c < 180:
        print('Soma dos ângulos internos é menor que 180º')
    else:
        print('Soma dos ângulos internos é maior que 180º')
    
triangleType(num1,num2,num3)

15. Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
    Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. 
    Considere que a potência necessária é de 18 watts por metro quadrado.
R=
import math

lampPot = int(input('Insira a potência da lâmpada: '))
roomWidth = int(input('Insira a largura da sala: '))
roomLength = int(input('Insira o comprimento da sala: '))

def howManyLampsINeed(lampPot, roomWidth, roomLength):
    return 'Eu preciso de ' + str(math.ceil(roomWidth * roomLength * 18 / lampPot)) + ' lâmpadas de ' + str(lampPot) + ' watts de potência.' 
    
print(howManyLampsINeed(lampPot, roomWidth, roomLength))

16. Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), 
    calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes 
    (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de azulejos possui 1,5 m2.1 
R=
import math

floorLength = int(input('Insira a largura da cozinha: '))
floorWidth = int(input('Insira o comprimento da cozinha: '))
height = int(input('Insira a altura da cozinha: '))

def necessaryTiles(floorLength, floorWidth, height):
    return 'Serão necessárias ' + str(math.ceil(((2 * floorLength  * height) + (2 * floorWidth * height)) / 1.5)) + ' caixas de azulejos.'

print(necessaryTiles(floorLength, floorWidth, height))

17. Um motorista de táxi deseja calcular o rendimento de seu carro na praça. 
    Sabendo-se que o preço do combustível é de R$ 1,90, escreva um programa para ler: 
    - a marcação do odômetro (Km) no início do dia
    - a marcação (Km) no final do dia, o número de litros de combustível gasto
    - o valor total (R$) recebido dos passageiros. 
    Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.
R=
odometer = int(input('Insira o valor marcado no odômetro no início do dia: '))
odometerFinal = int(input('Insira o valor marcado no odômetro no final do dia: '))
fuelUsed = int(input('Insira a quantidade de combustível utilizado: '))
moneyReceived = int(input('Insira a quantidade de dinheiro ganho com as viagens: '))
fuelPrice = 1.9

media = (odometerFinal - odometer) / fuelUsed
profit = moneyReceived - (fuelUsed * fuelPrice)

print('A media do consumo em Km/L é: ', media)
print('O lucro do dia foi de: ', profit)

18. Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa. 
    Caso o aluno não tenha feito a optativa deve ser fornecido o valor –1. 
    Calcular a média do semestre considerando que a nota mais baixa será excluída do calculo. 
    Escrever a média e mensagens que indiquem se o aluno foi aprovado, reprovado ou está em exame, de acordo com as informações abaixo¹:
        Aprovado : media >= 6.0
        Reprovado: media < 3.0
        Exame : media >= 3.0 e < 6.0
R=
av1 = int(input('Digite a nota recebida na primeira avaliação: '))
av2 = int(input('Digite a nota recebida na segunda avaliação: '))
av3 = int(input('Digite a nota da avaliação optativa (se não fizer a optativa, colocar -1): '))

avList = [av1, av2, av3]
avList.sort()

def media(avGrade):
    media = (avGrade[1] + avGrade[2]) / 2
    if media >= 6:
        return 'Aprovado'
    elif media < 3:
        return 'Reprovado'
    else:
        return 'Exame'

print(media(avList))

19. Escreva um programa que leia a idade de 2 homens e 2 mulheres. 
    Considere que a idade dos homens será sempre diferente, assim como as idades das mulheres. 
    Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, 
    e o produto das idades do homem mais novo com a mulher mais velha.
R=
man1Age = int(input('Insira a idade do primeiro homem: '))
man2Age = int(input('Insira a idade do segundo homem: '))
wom1Age = int(input('Insira a idade da primeira mulher: '))
wom2Age = int(input('Insira a idade da segunda mulher: '))

manAgeList = [man1Age, man2Age]
womAgeList = [wom1Age, wom2Age]

manAgeList.sort()
womAgeList.sort()

ageSum = man2Age + wom1Age
ageProduct = man1Age * wom2Age

print(ageSum)
print(ageProduct)

20. Crie um programa para ler duas entradas de Strings fornecidas pelo usuário. 
    Verifique se as Strings são iguais ou diferentes. 
    Imprima uma mensagem na saída padrão indicando o resultado da verificação.
R=
string1 = input('Insira a primeira string: ')
string2 = input('Insira a segunda string: ')

def equal(string1, string2):
    if string1 == string2:
        print('As strings são iguais')
    else:
        print('As strings são diferente')

equal(string1, string2)
'''