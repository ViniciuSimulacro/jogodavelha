from time import sleep

a= [['-'],['-'],['-']]
b= [['-'],['-'],['-']]
c= [['-'],['-'],['-']]

while True:
    while True:
        print('Bem vindo ao Jogo da velha da empresa')
        sleep(0)
        print('-*' * 8)
        print('|Simulacro Inc.|')
        print('-*' * 8)
        sleep(0)
        print('')
        print('Caso o jogo empate digite o numero 4 no campo "linha" para recomeçar o jogo!')
        sleep(0)
        print('')
        print('Vamos começar?')
        sleep(0)
        print('-*'*13)
        while True:
            todos = (a,b,c)
            print('     A      B      C')
            cont = 1
            for i in todos:
                print(cont, i)
                cont += 1
            print('-*'*13)
            print('Jogador 1 - "X"')
            linha = int(input('Em qual linha vc quer jogar [1,2,3]: '))
            if linha == 4:
                break
            coluna = str(input('Em qual coluna vc quer jogar: [A,B,C]: '))
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

            # segundo jogador?
            todos = (a, b, c)
            print('     A      B      C')
            cont = 1
            for i in todos:
                print(cont, i)
                cont += 1
            print('-*' * 13)
            print('Jogador 2 - "0"')
            linha = int(input('Em qual linha vc quer jogar [1,2,3]: '))
            if linha == 4:
                break
            coluna = str(input('Em qual coluna vc quer jogar: [A,B,C]: '))
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
        print('')
        novo = str(input('Jogo empatado, querem jogar mais uma partida? [s/n]: '))
        if novo == 's':
            print('-*' * 13)
            sleep(2)
            break
        else:
            break
    if novo == 'n':
        break
if novo == 'n':
    print('')
    print('-*' * 20)
    sleep(1)
    print("|Obrigado por jogar com a Simulacro Inc|")
    sleep(1)
    print('-*' * 20)