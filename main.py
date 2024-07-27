import sqlite3
import random
import time
import pandas as pd
from utils import prize
from draw import drawMake
from counting import countingMake
from func2 import fin
from fun4 import f4

from database import connect_db, get_cursor
import numpy as np
def main():
    db = connect_db()
    cursor = get_cursor(db)
    
    DrawDone = False  # Variável para saber se o sorteio já foi realizado
    
    while True:
        print("=================== SISTEMA DE CONTROLE DE APOSTAS DE ETHEREUM  ===================")
        if DrawDone:
            print("Status Sorteio: Realizado")  # Mostra o status do sorteio
        else:
            print("Status Sorteio: Em andamento")
        time.sleep(1.0)
        
        # Menu inicial de funcionalidades
        print('''
        Bem vindo!

        Escolha umas das opcoes abaixo:
        [1] Novas edicao do sorteio
        [2] Realizar nova aposta
        [3] Exibir a lista de aposta
        [4] Finalizar apostas e executar o sorteio
        ''')
        
        try:
            func = int(input("Opcao Escolhida: "))  # Seleciona a funcionalidade
        except:
            print("Valor nao numerico informado")  # Verifica se está em formato numérico
            func = -1
        
        print('\n=====================================================================================\n')
        
        if func == 1:  # Funcionalidade 1
            while True:
                try:
                    # Pergunta se quer reiniciar todos os dados e começar o sorteio
                    confirm = int(input('''Tem certeza que desejas apagar todos os dados do sorteio e comecar uma novo?
                    [1]Nao
                    [2]Sim
                    '''))
                    if confirm == 1:  # Se não, volta para o menu inicial
                        break
                    if confirm == 2:  # Se sim
                        DrawDone = False  # Define a variável como False, para um novo sorteio
                        cursor.execute("TRUNCATE TABLE bet;")  # Apaga todos os valores da tabela bet
                        cursor.execute("TRUNCATE TABLE userdata;")  # Apaga todos os valores da tabela userdata
                        cursor.execute("ALTER TABLE BET AUTO_INCREMENT = 1000;")  # Reinicia a contagem do ID
                        db.commit()
                        break
                    if confirm > 2 or confirm < 1:
                        print("Informe ou a opcao 1 ou a opcao 2")
                except:
                    print("Valor numerico nao informado")
        
        elif func == 2:  # Funcionalidade 2
            f2 = fin(cursor, db, DrawDone)
        elif func == 3:  # Funcionalidade 3
            time.sleep(1.0)
            db = connect_db()
            cursor = get_cursor(db)
            cursor.execute("SELECT B.id, A.nameUser, A.cpf, B.n1, B.N2, B.N3, B.N4, B.N5 FROM BET B INNER JOIN USERDATA A ON B.cpf = A.cpf")  # Busca o id, nome, cpf e os números apostados, usando o inner join para juntar pelo CPF as tabelas
            result = cursor.fetchall()
            
            if len(result) != 0:  # Se tiver alguma aposta realizada
                dfResult = pd.DataFrame(result, columns=['ID', 'Name', 'CPF', 'N1', 'N2', 'N3', 'N4', 'N5'])  # Cria um DataFrame com os dados
                print(dfResult)  # Exibe o DataFrame
                time.sleep(1.5)
                time.sleep(1.5)
            else:
                print("Nenhuma aposta registrada")  # Se nenhuma aposta foi realizada exibe a mensagem
                time.sleep(1.5)
        
        elif func == 4:  # Funcionalidade 4
            cursor = db.cursor()
            DrawDone = f4(db, cursor, DrawDone)
        
        if func > 4 or func < 1:  # Garante que o número informado é menor que 4 e maior que 1
            print("Por favor, insira um numero de 1 a 4\n")
            time.sleep(2)

if __name__ == "__main__":
    main()
