import sqlite3
import random
import time
import pandas as pd
from database import connect_db, get_cursor

def fin(cursos, db, DrawDone):
            cpfDuplicate = 0  # Variável para saber se o CPF é duplicado
            
            if DrawDone:  # Se o sorteio já foi realizado, mostra uma mensagem e volta para o menu inicial
                print('''Sorteio ja realizado, nao aceitando novas apostas
                Para conferir a apuracao selecione a opcao 4
                Para realizar um novo sorteio selecione a opcao 1''')
            else:
                nameUser = input("Informe o nome do usuario: ")  # Salva o nome do usuário
                nameUser = "'"+nameUser+"'"  # Deixa o nome em formato para ser salvo no banco de dados
                print(nameUser)
                while True:  # Laço de repetição até um CPF válido
                    # VARIÁVEIS CÁLCULO CPF
                    j = 10
                    k = 11
                    sumJ = 0
                    sumK = 0
                    accept = 0
                    try:
                        if cpfDuplicate == 2:  # Se o CPF foi duplicado e deseja usar ele para outra aposta, sai do laço de repetição
                            break
                        cpf = input("Informa o CPF (somente o numero): ")  # Salva o CPF
                        if cpf.isdigit() and len(cpf) == 11:  # Confere se o CPF é composto só por números e tem 11 de tamanho
                            for i in range(9):  # Verifica o primeiro número verificador
                                sumJ += int(cpf[i]) * j  # Soma os 9 primeiros números do CPF * a variável j
                                j -= 1
                            for i in range(10):  # Verifica o segundo número verificador
                                sumK += int(cpf[i]) * k  # Soma os 10 primeiros números do CPF * a variável k
                                k -= 1

                            remainderJ = sumJ % 11  # Resto da soma dos números dividido por 11
                            remainderK = sumK % 11  # Resto da soma dos números dividido por 11

                            if remainderJ == 0 or remainderJ == 1:  # Se o resto for 1 ou 0
                                if int(cpf[9]) == 0:  # O 10º número tem que ser 0
                                    accept += 1  # Variável para saber se o número verificador está certo
                            elif int(cpf[9]) == 11 - remainderJ:  # Se o resto não for 1 ou 0, o número verificador tem que ser 11 - o resto
                                accept += 1  # Variável para saber se o número verificador está certo
                            if remainderK == 0 or remainderK == 1:  # Se o resto for 1 ou 0
                                if int(cpf[10]) == 0:  # O 11º número tem que ser 0
                                    accept += 1  # Variável para saber se o número verificador está certo
                            elif int(cpf[10]) == 11 - remainderK:  # Se o resto não for 1 ou 0, o número verificador tem que ser 11 - o resto
                                accept += 1  # Variável para saber se o número verificador está certo
                            
                            if accept == 2:  # Se a variável for 2 então o CPF é válido
                                print("CPF VALIDO")

                                cursor = get_cursor(db)
                                comandUser = f'INSERT INTO USERDATA(nameUser, cpf, winner) VALUES({nameUser}, {cpf}, 0)'  # Salva o CPF e o nome no banco de dados
                                cursor.execute(comandUser)
                                break
                            else:
                                print("CPF INVALIDO")
                        else:
                            print("CPF INVALIDO")
                    except:  # Se o CPF já está no banco de dados
                        while True:
                            try:
                                # Pergunta se quer usar um novo CPF ou usar o mesmo CPF para outra aposta
                                cpfDuplicate = int(input('''CPF ja cadastrado
                                [1] Cadastrar novo cpf
                                [2] Usar o mesmo cadastro para outra aposta
                                ''')) 
                                if cpfDuplicate == 2:  # Usar o mesmo CPF
                                    break
                                if cpfDuplicate == 1:  # Cadastrar um novo CPF
                                    break
                                if cpfDuplicate > 2 or cpfDuplicate < 1:
                                    print("Informe 1 ou 2")
                            except:
                                print("Valor numerico nao informado")
                
                numsBet = [-1, -2, -3, -4, -5]  # Array onde serão salvos os números apostados
                
                for i in range(5):  # For que percorre os 5 números
                    while True:  # While para garantir que nenhum número foi informado de forma errada
                        try:
                            numsBet[i] = int(input(f"Informe o {i+1}° numero da aposta (1 a 50) \nDigite 0 para escolher um numero surpresinha(aleatorio): "))
                            if numsBet[i] == 0:  # Se for 0, um número aleatório é sorteado
                                while True:
                                    numsBet[i] = random.randrange(1, 51)  # Sorteia um número aleatório
                                    if len(numsBet) != len(set(numsBet)):  # Se o número sorteado já foi escolhido, outro número é sorteado
                                        numsBet[i] = random.randint(1, 50)
                                    else:
                                        break
                            if numsBet[i] < 0 or numsBet[i] > 50:  # Se o número escolhido pelo usuário for maior que 0 ou menor, a função repete
                                print("Numero invalido, informe um numero entre 1 e 50")
                            elif len(numsBet) != len(set(numsBet)):  # Se um número repetido foi escolhido, a função repete
                                print("Informe um numero diferentes dos escolhidos anteriormente")
                            else:
                                print(f"O {i+1}° Numero apostado foi: {numsBet[i]}\n")  # Mostra o número escolhido
                                break
                        except:
                            print("Opção escolhida em formato nao numerico")  # Garante que foi salvo em int
                
                comandBet = f'INSERT INTO BET(cpf, n1, n2, n3, n4, n5) VALUES({cpf},{numsBet[0]},{numsBet[1]}, {numsBet[2]}, {numsBet[3]}, {numsBet[4]})'  # Salva os números no banco de dados, usando o CPF para saber de quem foi a aposta
                
                cursor = get_cursor(db)
                cursor.execute(comandBet)
                db.commit()
                time.sleep(1.5)
                print('''
                Aposta realizada com sucesso!
                Boa Sorte!
                ''')
        