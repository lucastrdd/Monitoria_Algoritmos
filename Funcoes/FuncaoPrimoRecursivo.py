'''
Crie uma função que cheque se um número é primo, de forma recursiva.
'''
def primo (num,cont = 2):
    if (num % cont != 0):
        return primo (num,cont+1)
    elif(cont == num):
        return True
    else:
        return False


a = int(input("Informe um número inteiro: "))
while (a != 0):
    if(primo(a)):
        print(f"{a} é primo")
    else:
        print(f"{a} não é primo")
    a = int(input("Informe um número inteiro: "))