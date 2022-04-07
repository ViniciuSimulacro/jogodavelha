from time import sleep
from random import randint

linha = ''
coluna = ''
cont = 1
novo = ''


def entrada():
    print('Bem vindo ao Jogo da velha da empresa')
    sleep(0)
    print('')
    print('-*' * 8)
    print('|Simulacro Inc.|')
    print('-*' * 8)
    sleep(0)
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
            if a[coluna] == ['-']:
                a[coluna] = ['X']
                break
            elif a[coluna] == ['0'] or ['X']:
                print('Espaço ocupado, tente outra jogada!')
                print('-*' * 13)
        if linha == 2:
            if b[coluna] == ['-']:
                b[coluna] = ['X']
                break
            elif b[coluna] == ['0'] or ['X']:
                print('Espaço ocupado, tente outra jogada!')
                print('-*' * 13)
        if linha == 3:
            if c[coluna] == ['-']:
                c[coluna] = ['X']
                break
            elif c[coluna] == ['0'] or ['X']:
                print('Espaço ocupado, tente outra jogada!')
                print('-*' * 13)


def jogador2():
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
            if a[coluna] == ['-']:
                a[coluna] = ['0']
                break
            elif a[coluna] == ['X'] or ['0']:
                print('Espaço ocupado, tente outra jogada!')
                print('-*' * 13)
        if linha == 2:
            if b[coluna] == ['-']:
                b[coluna] = ['0']
                break
            elif b[coluna] == ['X'] or ['0']:
                print('Espaço ocupado, tente outra jogada!')
                print('-*' * 13)
        if linha == 3:
            if c[coluna] == ['-']:
                c[coluna] = ['0']
                break
            elif c[coluna] == ['X'] or ['0']:
                print('Espaço ocupado, tente outra jogada!')
                print('-*' * 13)


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


def computador_jogando():
    print('Computador jogando!')
    print('-*' * 13)
    while True:
        sleep(1)
        global cont, linha, coluna

        # vitória do computador
        if a[0] == ['0'] and a[1] == ['0']:
            if a[2] == ['-']:
                a[2] = ['0']
                break
        if a[0] == ['0'] and b[0] == ['0']:
            if c[0] == ['-']:
                c[0] = ['0']
                break
        if a[1] == ['0'] and b[1] == ['0']:
            if c[1] == ['-']:
                c[1] = ['0']
                break
        if a[2] == ['0'] and b[2] == ['0']:
            if c[2] == ['-']:
                c[2] = ['0']
                break
        if a[1] == ['0'] and c[1] == ['0']:
            if b[1] == ['-']:
                b[1] = ['0']
                break
        if a[2] == ['0'] and c[0] == ['0']:
            if b[1] == ['-']:
                b[1] = ['0']
                break
        if a[2] == ['0'] and c[2] == ['0']:
            if b[2] == ['-']:
                b[2] = ['0']
                break
        if a[0] == ['0'] and a[2] == ['0']:
            if a[1] == ['-']:
                a[1] = ['0']
                break

        if b[0] == ['0'] and b[1] == ['0']:
            if b[2] == ['-']:
                b[2] = ['0']
                break
        if b[0] == ['0'] and b[2] == ['0']:
            if b[1] == ['-']:
                b[1] = ['0']
                break
        if b[1] == ['0'] and b[2] == ['0']:
            if b[0] == ['-']:
                b[0] = ['0']
                break
        if b[2] == ['0'] and c[2] == ['0']:
            if a[2] == ['-']:
                a[2] = ['0']
                break

        if c[0] == ['0'] and c[1] == ['0']:
            if c[2] == ['-']:
                c[2] = ['0']
                break
        if c[0] == ['0'] and b[1] == ['0']:
            if a[2] == ['-']:
                a[2] = ['0']
                break
        if c[2] == ['0'] and b[1] == ['0']:
            if a[0] == ['-']:
                a[0] = ['0']
                break
        if c[0] == ['0'] and c[2] == ['0']:
            if c[1] == ['-']:
                c[1] = ['0']
                break
        if c[1] == ['0'] and c[2] == ['0']:
            if c[0] == ['-']:
                c[0] = ['0']
                break

        #defesa do computador
        if a[0] == ['X'] and a[1] == ['X']:
            if a[2] == ['-']:
                a[2] = ['0']
                break
        if a[0] == ['X'] and b[0] == ['X']:
            if c[0] == ['-']:
                c[0] = ['0']
                break
        if a[0] == ['X'] and a[2] == ['X']:
            if a[1] == ['-']:
                a[1] = ['0']
                break
        if a[1] == ['X'] and a[2] == ['X']:
            if a[0] == ['-']:
                a[0] = ['0']
                break
        if a[0] == ['X'] and b[1] == ['X']:
            if c[2] == ['-']:
                c[2] = ['0']
                break
        if a[0] == ['X'] and c[0] == ['X']:
            if b[0] == ['-']:
                b[0] = ['0']
                break
        if a[1] == ['X'] and b[1] == ['X']:
            if c[1] == ['-']:
                c[1] = ['0']
                break
        if a[1] == ['X'] and c[1] == ['X']:
            if b[1] == ['-']:
                b[1] = ['0']
                break
        if a[2] == ['X'] and b[2] == ['X']:
            if c[2] == ['-']:
                c[2] = ['0']
                break
        if a[1] == ['X'] and b[2] == ['X']:
            if c[0] == ['-']:
                c[0] = ['0']
                break
        if a[2] == ['X'] and c[2] == ['X']:
            if b[2] == ['-']:
                b[2] = ['0']
                break

        if b[0] == ['X'] and b[1] == ['X']:
            if b[2] == ['-']:
                b[2] = ['0']
                break
        if b[0] == ['X'] and b[2] == ['X']:
            if b[1] == ['-']:
                b[1] = ['0']
                break
        if b[1] == ['X'] and c[1] == ['X']:
            if a[1] == ['-']:
                a[1] = ['0']
                break

        if c[0] == ['X'] and c[1] == ['X']:
            if c[2] == ['-']:
                c[2] = ['0']
                break
        if c[0] == ['X'] and b[1] == ['X']:
            if a[2] == ['-']:
                a[2] = ['0']
                break
        if c[2] == ['X'] and b[1] == ['X']:
            if a[0] == ['-']:
                a[0] = ['0']
                break
        if c[0] == ['X'] and c[2] == ['X']:
            if c[1] == ['-']:
                c[1] = ['0']
                break

        #jogada randomica do computador
        while True:
            x = randint(1, 3)
            y = randint(0, 2)

            linha = x
            coluna = y


            if a[coluna] == ['X'] or ['0'] \
                or b[coluna] == ['X'] or ['0'] \
                or c[coluna] == ['X'] or ['0']:

                if linha == 1:
                    if a[coluna] == ['-']:
                        a[coluna] = ['0']
                        break

                if linha == 2:
                    if b[coluna] == ['-']:
                        b[coluna] = ['0']
                        break

                if linha == 3:
                    if c[coluna] == ['-']:
                        c[coluna] = ['0']
                        break
        break



while True:
    while True:

        novo = ''
        entrada()
        cont = 0
        a = [['-'], ['-'], ['-']]
        b = [['-'], ['-'], ['-']]
        c = [['-'], ['-'], ['-']]
        resposta = (1,2)
        jogadores = ''
        while jogadores not in resposta:
            try:
                jogadores = int(input('\nDigite 1 para jogar com o computador \nou digite 2 para jogar com um amigo: '))
                if jogadores not in resposta:
                    print('Erro! Escolha 1 ou 2 jogadores! ')
                if jogadores in resposta:
                    break
            except ValueError:
                print('Erro! Digite [1] para jogar com PC ou [2] para jogar com amigo, POR FAVOR!')
        print('')
        print('-*' * 13)
        while True:
            while cont <= 9:
                if jogadores == 1 or 2:
                    quadro()
                    print('Jogador 1 - "X"')
                    jogador1()
                    cont += 1
                    vitoria()
                    if cont == 9:
                        empate()
                        quadro()
                        break
                    if cont == 10:
                        break
                    quadro()
                if jogadores == 1:
                    computador_jogando()
                    cont +=1
                    vitoria()
                    if cont == 9:
                        empate()
                        break
                    if cont == 10:
                        break
                if jogadores == 2:
                    print('Jogador 2 - "0"')
                    jogador2()
                    cont += 1
                    vitoria()
                    if cont == 9:
                        empate()
                        break
                    if cont == 10:
                        break
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
    if novo == 'n':
        break

print('')
print('-*' * 20)
sleep(1)
print("|Obrigado por jogar com a Simulacro Inc|")
sleep(1)
print('-*' * 20)