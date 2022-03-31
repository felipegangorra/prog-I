#Programação 1 - UFCG - 09/dezembro/2021
#Aluno: Felipe da Silva Gangorra
#Atividade Fli Flai

#ENUNCIADO: 3 números, se forem divididos por 10, imprimir "tumba"
#se for dividido por 2, imprimir fli, por 3 flai e por 5 flu.

#my code

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if (num1 % 2) == 0:
    print("Fli")
elif (num2 % 3) == 0:
    print("Flai")
elif (num3 % 5) == 0:
    print("Flu")
elif (num4 % 10) == 0:
    print("Tumba")

# right code

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 % 10 == 0 or num2 % 10 == 0 or num3 % 10 == 0:
    print("Tumba")

else:
    if num1 % 2 == 0:
        print("Fli")
    
    if num2 % 3 == 0:
        print("Flai")
    
    if num3 % 5 == 0:
        print("Flu")