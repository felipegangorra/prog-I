#Prog1 - UFCG - 20/dezembro/2021
#Aluno: Felipe da Silva Gangorra - 121111084    
#Calculando expressão matemática a,b,c e d.

#ENTRADA
a = int(input())
b = int(input())
c = int(input())
d = int(input())

#CÁLCULO
dc = int(str(d) + str(c))
ca = int(str(c) + str(a))
bb = int(str(b) + str(b))
aad = int(str(a) + str(a) + str(d))
resultado = dc - a - b - ca - d + bb + aad

#SAIDA
print(f'{resultado}')