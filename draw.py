import time
import random
import numpy as np
import pandas as pd

def drawMake(cursor, db, numsDraw):
    numWin = 0
    cont = 0

    cursor.execute("SELECT B.id, A.nameUser, A.cpf, B.n1,B.N2, B.N3, B.N4, B.N5 FROM BET B INNER JOIN USERDATA A  ON B.cpf = A.cpf")
    resultBet = cursor.fetchall()
    while True:
        if cont < 25:
            for row in resultBet:
                arrayBet = [row[3], row[4], row[5], row[6], row[7]]
                if set(arrayBet).issubset(set(numsDraw)):
                    numWin += 1
                    print("TEMOS UM GANHADOR!!!!!!!!!!!!!!!!!!!!!!\n")
                    time.sleep(1.5)
                    print(f"Se apresente {row[1]} que tem o cpf {row[2]} para receber seu premio!!!!\n")
                    print("--------------------\n")
                    cursor.execute(f'UPDATE userdata SET winner = 1 WHERE cpf = {row[2]} ;')
                    time.sleep(1.5)
                    db.commit()

            if numWin == 0:
                print('''AH NAO!
Parece que nao temos nenhum ganhador ainda
Vamos sortear mais um numero!\n''')
                time.sleep(1.5)
                while True:
                    numsDraw[5 + cont] = str(random.randrange(1, 51))
                    if len(numsDraw) == len(set(numsDraw)):
                        print(f"O novo numero sortado e...\n {numsDraw[5 + cont]}!!!")
                        time.sleep(2.0)
                        print("Vamos ver se temos um ganhador\n")
                        print("--------------------\n")
                        time.sleep(1.5)
                        break
            else:
                return numsDraw
        else:
            time.sleep(1.0)
            print('''NUMERO MAXIMO DE NUMEROS SORTEADOS
INFELIZMENTE NAO TEMOS NENHUM VENCEDOR DESSE SORTEIO
BOA SORTE NA PROXIMA\n''')
            print("--------------------\n")
            time.sleep(1.0)
            return numsDraw
        cont += 1
