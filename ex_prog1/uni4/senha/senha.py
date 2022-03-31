#Prog1 - UFCG - 22/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#convertendo senha com criptografia.

#ENTRADA
senha = str(input())

#CÁLCULO
cont = 0    #para ele não começa a mudar a partir da primeira letra
cod = ''

for s in senha:             #ele percorre o if até o else, onde add 1 para entrar no if.
    if cont > 0:
        if s == 'a' or s == 'A':
            s = '4'
            cont += 1

        elif s == 'e' or s == 'E':
            s = '3'
            cont += 1

        elif s == 'i' or s == 'I':
            s = '1'
            cont += 1
        
        elif s == 'o' or s == 'O':
            s = '0'
            cont += 1
    else:
        cont += 1       #ele mesmo e soma mais 1

    cod += s            #ele transcreve com as alterações, se não tiver, retorna o valor original

#SAIDA
print(f'{cod} ({cont -1} troca(s))')

    