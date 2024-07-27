import time
import random
import numpy as np
import pandas as pd
from web3 import Web3

pd.set_option('display.max_colwidth', None)

def prize(UserWinner):
    for winner in UserWinner:
        print(f'{winner[0]}')
  #      while True:
   #         addressWinner = input(f"{winner[0]} de CPF: {winner[1]} informe o endereço da sua carteira do MetaMask  (exemplo de formato: 0xe34FC27644eaE4271435F66784F11Cf31e797E1a): ")
     #       try:
     #           address2 = Web3.to_checksum_address(addressWinner)
       #         break
       #     except ValueError:
       #         print("Informe a hex string da sua carteira (exemplo de formato: 0xe34FC27644eaE4271435F66784F11Cf31e797E1a): ")

       # w3 = Web3(Web3.HTTPProvider(''))

      #  from_account = ''
      #  private_key = ''

     #   address1 = Web3.to_checksum_address(from_account)
      #  nonce = w3.eth.get_transaction_count(address1)

       # tx = {
        #    'nonce': nonce,
         #   'to': address2,
          #  'value': w3.to_wei(0.000001, 'ether'),
           # 'gas': 21000,
            #'gasPrice': w3.to_wei(40, 'gwei')
        #}

        #signed_tx = w3.eth.account.sign_transaction(tx, private_key)
        #try:
         #   tx_Transaction = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
          #  print("\nPREMIACAO ENVIADA!!!!!\n")
        #except:
         #   print("\nInfelizmente o preco do eth esta muito caro para ficar fazendo tantas transações\n")
            

