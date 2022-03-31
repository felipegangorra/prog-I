#Prog1 - UFCG - 18/dezembro/2021
#Auno: Felipe Gangorra - 12111184
#Formatando cpf`s com hífen antes dos dois útlimos digitos.

cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

#Primeiro CPF
cpf01 = cpf1 // 100
digito1 = cpf1 % 100

#Segundo CPF
cpf02 = cpf2 // 100
digito2 = cpf2 % 100

#Terceiro CPF
cpf03 = cpf3 // 100
digito3 = cpf3 % 100

print(f'{cpf01}-{digito1}\n{digito1 // 10 + digito1 % 10}')
print(f'{cpf02}-{digito2}\n{digito2 // 10 + digito2 % 10}')
print(f'{cpf03}-{digito3}\n{digito3 // 10 + digito3 % 10}')