#Prog1 - 09/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#PRIMEIRO MENOR QUE 100: modificando código/arquiterura 

import sys
import os

filename = "dados.dat"
if not os.path.exists(filename):
    print("O arquivo de dados (dados.dat) não existe")
    print("Execute: python3 gendata.py pra gerar o arquivo")
    sys.exit(1)


arq = open(filename)

x = 1
linha = 0
while True:
    linha = int(arq.readline())
    if linha < 100: break
    x += 1

print(f"{linha}, na posição {x}")