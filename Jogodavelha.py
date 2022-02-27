a= [['-'],['-'],['-']]
b= [['-'],['-'],['-']]
c= [['-'],['-'],['-']]
while True:
    todos = (a,b,c)
    print('     A      B      C')
    cont = 1
    for i in todos:
        print(cont, i)
        cont += 1
    linha = int(input('Em qual linha vc quer jogar [1,2,3]: '))
    coluna = str(input('Em qual coluna vc quer jogar: [A,B,C]: '))
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
