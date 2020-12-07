'''
1- Calcule a soma dos N primeiros números ímpares digitado pelo usuário. 
   O primeiro valor será atribuído a N, os demais serão somados, caso sejam ímpares.
        num1 = int(input('Digite um número ímpar: '))

        while num1 % 2 == 0 :
            num1 = int(input('Esse número não é ímpar, digite um número ímpar: '))

        count = int(input('Quantas somas serão feitas? '))

        while count > 0 :
            num2 = int(input('Digite um número ímpar: '))
            
            while num2 % 2 == 0 :
                num2 = int(input('Esse número não é ímpar, digite um número ímpar: '))
            
            count -= 1
            num1 += num2

        print('A soma total é:',num1)

2- Calcule o N-ésimo valor da sequência de Fibonacci.
        menor = 0
        maior = 1

        count = int(input('Escolha o termo desejado: '))
        countNum = count

        if(count <= 1):
            print('O',countNum,'º valor na sequéncia fibonnaci é:',menor)
        else:
            while(count > 2):
                fibbonacci = maior + menor
                menor = maior
                maior = fibbonacci
                count -= 1
            print('O',countNum,'º valor na sequéncia fibonnaci é:',maior)

3- Calcule o N-ésimo valor da sequência x ← 2N + 5.
        print('Quantos números você irá querer?')
        N = int(input('Forneça um valor para N: '))
        x = (2 ** N) + 5
        print(x)

4- Calcule o fatorial de N.
        fatorial = int(input('Digite um número positivo: '))
        num1 = fatorial

        while fatorial < 0:
            fatorial = int(input('Não foi digitado um número positivo, digite um número positivo: '))

        if fatorial == 0 or fatorial == 1:
            print(1)
        else:
            i = fatorial - 1

            while i > 1:
                fatorial = fatorial * i
                i -= 1
            
            print('O fatorial de',num1,'é:',fatorial)

    Outro método, utilizando o for
        N = int(input('Forneça o valor N: '))
        fatorial = 1
        N += 1
        for i in range (1,N):
            fatorial *= i
        print(fatorial)

    Outro método, utilizando o for invertido
        N = int(input('Forneça o valor N: '))
        fatorial = 1
        N += 1
        for i in range (N,1,-1):
            fatorial *= i
        print(fatorial)


5- Dado um valor inteiro, calcule o valor posterior e antecessor.
        num = int(input('Digite um número: '))
        print('O valor posterior de',num,'é:',num+1)
        print('O valor antecessor de',num,'é:',num-1)

6- Dado duas variáveis inteiras, troque os valores das variáveis utilizando apenas essas duas variáveis.
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha outro número: '))

        num1Before = num1
        num2Before = num2

        num2 = num1 - num2
        num1 -= num2
        num2 += num1

        print('Antes o primeiro número era:',num1Before,' Agora ele é:', num1)
        print('Antes o segundo número era:',num2Before,' Agora ele é:', num2)

7- Uma empresa vende os produtos mostrados na tabela abaixo. Os valores unitário, e atacados com desconto. 
   Faça um programa pra solicitar a lista de pedido de um cliente, e ao final mostre a lista com os valores da quantidade comprada
   e do valor a ser pago, seguindo a tabela e o total a ser pago. 
   Código      Item             Valor ( R$ )
                          Unitário      >100         >500
   001     Parafuso 1/8     0,10     0,08(cada)   0,06(cada)
   002     Porca 1/8        0.05     0,04(cada)   0,03(cada)
   003     Prego            0,10     0,09(cada)   0,08(cada)
        code = ''
        amount = ''
        codeList = []
        itemList = []
        itemQuantity = []
        total = 0

        while code != '001' or code != '002' or code != '003':
            code = input('Insira o código de um produto: ')
            if code != '001' and code != '002' and code != '003':
                code = "Finalizar"
                amount = "Não definido"
                break 

            amount = int(input('Insira a quantidade: '))
            while amount < 1:
                print('Quantidade inválida')
                amount = int(input('Insira uma quantidade válida: '))
            
            codeList.append(code)
            itemQuantity.append(amount)

        i = 0

        for n in codeList:
            if codeList[i] == '001':
                itemList.append('Parafuso 1/8')
                if itemQuantity[i] > 500:
                    total += itemQuantity[i] * 0.06
                elif itemQuantity[i] > 100:
                    total += itemQuantity[i] * 0.08
                else:
                    total += itemQuantity[i] * 0.1
            elif codeList[i] == '002':
                itemList.append('Porca 1/8')
                if itemQuantity[i] > 500:
                    total += itemQuantity[i] * 0.03
                elif itemQuantity[i] > 100:
                    total += itemQuantity[i] * 0.04
                else:
                    total += itemQuantity[i] * 0.05
            elif codeList[i] == '003':
                itemList.append('Prego') 
                if itemQuantity[i] > 500:
                    total += itemQuantity[i] * 0.08
                elif itemQuantity[i] > 100:
                    total += itemQuantity[i] * 0.09
                else:
                    total += itemQuantity[i] * 0.1
            else:
                input('Erro, código errado digitado, refaça a lista. Aperte Enter para continuar')
                exit()
            i += 1

        i = 0

        for n in itemList:
            print(n,':',itemQuantity[i])
            i+=1
        print (round(total,2))

8- Construa uma calculadora que execute as quatro operações básicas em sequência, e mostre o valor final quando for digitado a operação (=).
        num1 = int(input('Escolha o primeiro número: '))
        num2 = int(input('Escolha o segundo número: '))
        sign = input('Escolha o sinal que será usado: ')

        if sign == '+':
            print(num1,'+',num2,':',num1 + num2)
        elif sign == '-':
            print(num1,'-',num2,':',num1 - num2)
        elif sign == '*':
            print(num1,'*',num2,':',num1 * num2)
        elif sign == '/':
            print(num1,'/',num2,':',round(num1 / num2,2))
        else:
            print('Erro, sinal errado utilizado. Reinicie.')

9- Construa um programa que aceite uma sequência infinita de valores inteiros e mostre qual o maior valor digitado a cada entrada. 
    O programa termina quando o usuário digitar o valor 0 (zero).
        num1 = int(input('Escolha o primeiro número: '))
        num2 = int(input('Escolha o segundo número: '))

        while num1 != 0 and num2 != 0:
            if num1 > num2:
                print ('O número',num1,'é maior que o número',num2)
                num2 = int(input('Escolha novamente um número: '))
            else:
                print ('O número',num2,'é maior que o número',num1)
                num1 = int(input('Escolha novamente um número: '))
'''