import sqlite3
import random
import time
import pandas as pd
from database import connect_db, get_cursor
from draw import drawMake
from counting import countingMake
from utils import prize
import numpy as np
def f4 (db, cursor, DrawDone):
            cursor.execute("SELECT * FROM bet")  # Seleciona as apostas
            betIsempty = cursor.fetchall()
            if DrawDone:  # Se o sorteio já foi realizado, só mostra a apuração
                countingMake(cursor, db, numsDraw)  # Chama a função de apuração
            elif len(betIsempty) != 0:
                if len(betIsempty) == 0:  # Confere se existe alguma aposta realizada
                    print("Nenhuma aposta realizada")
                    return False
                # Array de valores negativos onde serão salvos os números sorteados
                numsDraw = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30]
                while True:  # While para ter uma entrada de dados válida
                    try:
                        confirm = int(input('''
                        Desejas nao fazer mais nenhuma aposta e realizar o sorteio?
                        [1] NAO
                        [2] SIM
                        '''))  # Confirma que nenhuma aposta mais será realizada e começa o sorteio

                        if confirm == 2:  # Se confirm é igual a 2 começa a ser sorteado
                            break
                        if confirm == 1:
                            break
                        if confirm > 2 or confirm < 1:
                            print("Informe 1 ou 2")
                    except:
                        print("Valor numerico não informado")
                
                if confirm == 2:  # Se confirm é igual a 2 começa a ser sorteado
                    print('''
                    APOSTAS ENCERRADAS
                    VAMOS PARA O SORTEIO
                    ''')
                    time.sleep(1.0)

                    for i in range(5):  # Percorre os 5 primeiros espaços do array
                        print(f'''
                        O {i+1}° NUMERO SORTEADO É...
                        ''')
                        time.sleep(1.0)

                        while True:
                            numsDraw[i] = str(random.randrange(1, 51))  # Gera um número aleatório
                            if len(numsDraw) != len(set(numsDraw)):  # Verifica se o número aleatório não é repetido
                                numsDraw[i] = str(random.randint(1, 51))  # Gera um novo número aleatório se for repetido
                            else:
                                break
                        print(f"{numsDraw[i]}!!!!!!!!!!!!!")
                        time.sleep(2.0)

                    print("Agora vamos ver se temos um ganhador!\n")
                    time.sleep(1.0)
                    
                    numsDraw = drawMake(cursor, db, numsDraw)  # Chama a função draw() para ver se tem o vencedor e se precisar realizar novas rodadas do sorteio
                    
                    DrawDone = True  # Define sorteio como realizado
                    
                    numsDraw = np.array([int(x) for x in numsDraw])  # Deixa os números como int
                    numsDraw = numsDraw[numsDraw > 0]  # Deixa somente os números positivos no array
                    
                    countingMake(cursor, db, numsDraw )  # Chama a função para realizar a apuração
                    
                    cursor.execute("SELECT nameUser, cpf FROM userdata WHERE winner = 1 ORDER BY nameUser")  # Seleciona os nomes e CPF dos ganhadores
                    UserWinner = cursor.fetchall()
                    print("Agora vamos para a distribuição do premio: ")
                    
                    return DrawDone
                    if len(UserWinner) != 0:
                        prize(UserWinner)  # Função para distribuir prêmio
                    else:
                        print("Infelizmente nao tivemos vencedores")
            else:
                print("Nenhuma Aposta registrada")
                return DrawDone