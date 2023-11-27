'''
Crie um programa que receba a idade de várias pessoas, calcule e apresenta a média da idade
das pessoas. A entrada de dados é encerrada quando for digitado o valor 0 para a idade
'''
# entrada de dados
idade = int(input('Informe uma idade (0 interrompe): '))
soma = 0
contador = 0

# processar
while(idade != 0):
    soma += idade
    contador += 1
    idade = int(input('Informe uma idade (0 interrompe): '))

# retornoo
print ('A média de idade, é: {}'.format(soma/contador))