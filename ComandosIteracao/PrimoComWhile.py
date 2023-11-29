'''
Crie um programa que receba um número inteiro maior que 1 e verifique se ele é primo.
'''
# entrada de dados
num = int(input('Digite um número inteiro (diferente de 1): '))
contador = 2
primo = True

# processamento
while (contador < num):
    if (num % contador == 0):
        primo = False
    contador += 1

# retorno
if (primo == False):
    print('Não é Primo!')
else:
    print('É Primo')
