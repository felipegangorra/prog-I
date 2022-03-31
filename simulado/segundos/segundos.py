#Prog1 - 03 - fevereiro - 2022 
#Aluno: Felipe da Silva Gangorra - 121111084
#Programa que encontra o segundo menor e o segundo maior de 4 números int.

#ENTRADA
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(f'Considerando os números {a}, {b}, {c} e {d}')

#CÁLCULO
#maior valor
if b >= a and b >=c and b>= d:
    maior = a
    a = b
    b = maior
elif c >= a and c >= b and c >= d:
    maior = a
    a = c
    c = maior
elif d >= a and d >= b and d >= c:
    maior = a
    a = d
    d = maior

#segundo maior
if c >= d and c >= b:
    maior = b
    b = c
    c = maior
elif d >= c and d >= b:
    maior = b
    b = d
    d = maior
    
#terceiro maior
if d >= c:
    maior = c
    c = d
    d = maior

print(f'O segundo menor número é {c}')
print(f'O segundo maior número é {b}')
