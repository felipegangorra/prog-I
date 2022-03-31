#Prog1 - 16/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#INVERTER TRIPLAS: trocando ordem dos elementos de 3 em 3

def inverte3a3(s):
    resultado = ""
    for i in range(len(s)-1,0,-3):
        resultado += f"{s[i-2]}{s[i-1]}{s[i]}"
    
    return resultado