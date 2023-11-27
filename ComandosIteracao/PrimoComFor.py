'''
Crie um programa que receba um número inteiro maior que 1 e verifique se ele é primo.
'''
# entrada de dados
num = int(input('Digite um número inteiro (diferente de 1): '))
primo = True

# processamento
for i in range(2,num):
    if (num % i == 0):
        primo = False

# retorno
if (primo == False):
    print ('Não é Primo!')
else:
    print ('É Primo')