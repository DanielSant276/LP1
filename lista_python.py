'''
1- Indique qual o resultado será obtido das seguintes expressões (lembre-se de usar “.” não “,” para casas decimais): 
    a. 44 + 1 
    b. 6 +20-23 
    c. 3,0 5,0 +1 
    d. 1/4+2 
    e. 29,0/7+4 
    f. 3/6,0-7 
    g. 2 / 2 
    h. 2 // 2 
    i. 4 % 2 
    j. ( 100 // 5 ) % 5

        a = 44 + 1 
        b = 6 + 20 -23 
        c = 3.0 + 5.0 +1 
        d = 1 / 4 + 2 
        e = 29.0 / 7 + 4 
        f = 3 / 6.0 - 7 
        g = 2 / 2 
        h = 2 // 2 
        i = 4 % 2 
        j = ( 100 // 5 ) % 5

        print(a,' ',b,' ',c,' ',d,' ',e,' ',f,' ',g,' ',h,' ',i,' ',j) #45   3   9.0   2.25   8.142857142857142   -6.5   1.0   1   0   0

2- Faça uma função python para multiplicar dois números.
        def multiply(a, b):
            return a * b

        print(multiply(4, 60)) #240

3- Faça uma função para calcular a raiz do número passado. 
    a. Raiz quadrada. 
    b. Raiz cúbica. 
    c.Passe também o expoente índice da raiz.

        def squareRoot(num1):
            return num1 ** (1/2)

        print(squareRoot(6)) #2.449489742783178

        def cubeRoot(num1):
            return num1 ** (1/3)

        print(cubeRoot(18)) #2.6207413942088964

        def root(num1, index):
            return num1 ** (1/index)

        print(root(36,4)) #2.449489742783178

4- Faça um função para calcular a área de: um quadrado, um triângulo, um retângulo. Para cada função, determine os parâmetros que precisam.
        def square(base):
            return base ** 2

        print(square(10)) #100

        def rectangle(base, height):
            return base * height

        print(rectangle(8, 12)) #96

        def triangle(base, height):
            return rectangle(base, height)/2

        print(triangle(30, 75)) #1125

5- Faça um função para receber 3 parâmetros com valores inteiros. Considere que os valores inteiros correspondem ao tamanho de três arestas. 
   Verifique se é possível formar um triângulo com essas arestas (nesse caso usaremos o 'if' para verificar condições).
        def triangleValidation(a, b, c):
            validation = ""

            if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
                validation = "É um triângulo"
            else:
                validation = "Não é um triângulo"
    
            return validation

        print(triangleValidation(10,2,7)) #Não é um triângulo
        print(triangleValidation(9,12,15)) #É um triângulo

6- Faça programas que: 
    a. Leia um número e imprima o seu quadrado.
    b. Leia dois números e imprima a divisão do primeiro pelo segundo.
    c. Leia um número e imprima o resto da divisão desse número por 2. 
    d. Leia dois número e imprima a média. 
    e. Calcule a área de uma circunferência considerando que o usuário informe o comprimento do raio. 
        Para essa questão, declare uma variável “pi” com valor de 3,14 e use como valor de π. Calcule também o comprimento e o diâmetro.

        def square(num1):
            return num1 ** 2

        print(square(13)) #169

        def division(num1, num2):
            return num1 / num2

        print(division(7,25)) #0.28

        def remainder(num1, num2):
            return num1 % num2

        print(remainder(21,6)) #3

        def mean(num1, num2):
            return (num1 + num2) / 2

        print(mean(16,29)) #22,5

        pi = 3.14
        radius = int(input("Defina o raio: ")) #5

        def circleArea():
            return pi * (radius ** 2)

        def circleLength():
            return 2 * pi * radius

        def diameter():
            return 2 * radius

        print(circleArea()) #78,5
        print(circleLength()) #31,4
        print(diameter()) # 10

7- Indique o resultado lógico das seguintes expressões (faça com o python): 
    a. 2 < 3 
    b. ( 6 < 3 ) OU ( 10 > 11 ) 
    c. ((( 6 // 3 ) % 2 ) > 5 ) E ( 2 < ( 3 % 2 ) ) 
    d. !( 2 < 3 )

        def questionA():
            return 2 < 3

        def questionB():
            return ( 6 < 3 ) or ( 10 < 11 )

        def questionC():
            return  ((( 6 // 3 ) % 2 ) > 5 ) and ( 2 < ( 3 % 2 )) 

        def questionD():
            return not(2 < 3)

        print(questionA(), ' ', questionB(), ' ', questionC(), ' ', questionD())
'''