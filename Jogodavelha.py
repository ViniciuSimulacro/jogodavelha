from time import sleep

linha = 0
coluna = 0
cont = 0
novo = ''


def entrada():
    print('Bem vindo ao Jogo da velha da empresa')
    sleep(0)
    print('')
    print('-*' * 8)
    print('|Simulacro Inc.|')
    print('-*' * 8)
    sleep(0)
    '''print('')
    print('Caso o jogo empate digite o numero 4 no campo "linha" para recomeçar o jogo!')
    sleep(0)'''
    print('')
    print('Vamos começar?')
    sleep(0)
    print('-*'*13)

def jogador1():
    x = [1, 2, 3]
    while True:
        while True:
            try:
                linha = int(input('Em qual linha vc quer jogar [1,2,3]: '))
                if linha not in x:
                    print('Erro! Digite um numero de 1 a 3!')
                if linha in x:
                    break
            except ValueError:
                print('Erro! Digite um numero de 1 a 3!')


        while True:
            y = ['a','b','c']
            try:
                coluna = str(input('Em qual coluna vc quer jogar: [A,B,C]: '))
                if coluna not in y:
                    print('Erro! Digite uma letra entre A, B ou C')
                if coluna in y:
                    break
            except ValueError:
                print('Erro! Digite uma letra entre A, B ou C')


        print('-*' * 13)
        if coluna == 'a':
            coluna = 0
        if coluna == 'b':
            coluna = 1
        if coluna == 'c':
            coluna = 2

        if linha == 1:
            a[coluna] = ['X']
        if linha == 2:
            b[coluna] = ['X']
        if linha == 3:
            c[coluna] = ['X']

def jogador2():
    x = [1, 2, 3]
    while True:
        try:
            linha = int(input('Em qual linha vc quer jogar [1,2,3]: '))
            if linha not in x:
                print('Erro! Digite um numero de 1 a 3!')
            if linha in x:
                break
        except ValueError:
            print('Erro! Digite um numero de 1 a 3!')

    while True:
        y = ['a', 'b', 'c']
        try:
            coluna = str(input('Em qual coluna vc quer jogar: [A,B,C]: '))
            if coluna not in y:
                print('Erro! Digite uma letra entre A, B ou C')
            if coluna in y:
                break
        except ValueError:
            print('Erro! Digite uma letra entre A, B ou C')


    print('-*' * 13)

    if coluna == 'a':
        coluna = 0
    if coluna == 'b':
        coluna = 1
    if coluna == 'c':
        coluna = 2

    if linha == 1:
        a[coluna] = ['0']
    if linha == 2:
        b[coluna] = ['0']
    if linha == 3:
        c[coluna] = ['0']

def quadro():
    todos = (a, b, c)
    print('     A      B      C')
    cont = 1
    for i in todos:
        print(cont, i)
        cont += 1
    print('-*' * 13)

def vitoria():
   if a[0] == ['X'] and a[1] == ['X'] and a[2] == ['X']\
           or b[0] == ['X'] and b[1] == ['X'] and b[2] == ['X']\
           or c[0] == ['X'] and c[1] == ['X'] and c[2] == ['X']\
           or a[0] == ['X'] and b[0] == ['X'] and c[0] == ['X']\
           or a[1] == ['X'] and b[1] == ['X'] and c[1] == ['X']\
           or a[2] == ['X'] and b[2] == ['X'] and c[2] == ['X']\
           or c[0] == ['X'] and b[1] == ['X'] and a[2] == ['X']\
           or c[2] == ['X'] and b[1] == ['X'] and a[0] == ['X']:
        print('O jogador "X" ganhou')
        print('')
        quadro()
        global cont
        cont = 10
   if a[0] == ['0'] and a[1] == ['0'] and a[2] == ['0'] \
           or b[0] == ['0'] and b[1] == ['0'] and b[2] == ['0'] \
           or c[0] == ['0'] and c[1] == ['0'] and c[2] == ['0'] \
           or a[0] == ['0'] and b[0] == ['0'] and c[0] == ['0'] \
           or a[1] == ['0'] and b[1] == ['0'] and c[1] == ['0'] \
           or a[2] == ['0'] and b[2] == ['0'] and c[2] == ['0'] \
           or c[0] == ['0'] and b[1] == ['0'] and a[2] == ['0'] \
           or c[2] == ['0'] and b[1] == ['0'] and a[0] == ['0']:
       print('O jogador "0" ganhou')
       print('')
       quadro()

       cont = 10

def empate():
    print('')
    print('-*' * 8)
    print('| Jogo Empatado |')
    print('-*' * 8)
    print('')

while True:
    while True:
        novo = ''
        entrada()
        cont = 0
        a = [['-'], ['-'], ['-']]
        b = [['-'], ['-'], ['-']]
        c = [['-'], ['-'], ['-']]
        while cont <= 9:
            quadro()
            print('Jogador 1 - "X"')
            jogador1()
            cont += 1
            vitoria()
            if cont == 9:
                empate()
                break
            # segundo jogador?
            quadro()
            print('Jogador 2 - "0"')
            jogador2()
            cont += 1
            vitoria()
        print(''
              '')
        sleep(2)

        while novo not in ['s', 'n']:
            opcao = ('s','n')
            try:
                novo = str(input('Você gostaria de jogar mais uma vez [s/n]: '))
                if novo not in opcao:
                    print('Erro! Digite [s] ou [n], POR FAVOR!')
                if novo in opcao:
                    break
            except ValueError:
                print('Erro! Digite [s] ou [n], POR FAVOR!')
        print(''
              '')
        sleep(2)
        print('-*' * 13)
        if novo == 's' or 'n':
            break

    if novo == 'n':
        break

print('')
print('-*' * 20)
sleep(1)
print("|Obrigado por jogar com a Simulacro Inc|")
sleep(1)
print('-*' * 20)