import time
import random
import numpy as np
import pandas as pd
def countingMake(cursor, db, numsDraw):
    time.sleep(1.0)
    print('''Sorteio ja realizado
Vamos para a apuracao das apostas
Espere um pouquinho enquando realizamos os calculos''')
    time.sleep(2.0)
    print("Os numeros sorteados foram: ")
    dfDraw = pd.DataFrame(numsDraw, columns=['Numeros sorteados'])
    print(dfDraw)
    time.sleep(2.0)
    print(f"A quantidade de sorteios extras realizados: {len(numsDraw) - 5}\n")
    time.sleep(2.0)
    cursor.execute("SELECT  nameUser, cpf FROM userdata WHERE winner = 1 ORDER BY nameUser")
    UserWinner = cursor.fetchall()
    time.sleep(2.0)
    print(f"Quantidade de apostas vencedoras: {len(UserWinner)}")
    time.sleep(2.0)

    print("\nOs vencedores sao: ")
    dfWinner = pd.DataFrame(UserWinner, columns=['Vencerdores', 'CPF'])
    if len(UserWinner) == 0:
        print("Nao ouve vencedores\n")
    else:
        print(dfWinner)

    cursor.execute("SELECT  n1, n2, n3, n4, n5 FROM bet")
    allNum = cursor.fetchall()
    time.sleep(2.0)

    list1 = []
    save = []
    for num in allNum:
        list1 += list(num)
    list1 = [eval(m) for m in list1]

    for l in range(51):
        times = list1.count(l + 1)
        if times > 0:
            save.append([(times, l + 1)])
    time.sleep(2.0)
    print("Nro apostados \t Qtd de apostas")
    for i in sorted(save, reverse=True):
        print(f"{i[0][1]} \t\t {i[0][0]}")
    time.sleep(2.0)
