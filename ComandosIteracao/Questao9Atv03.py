'''
A prefeitura está coletando informações sobre o salário e o número de filhos dos habitantes. A
leitura de dados é realizada até que seja informado o valor -1 para o salário. Apresenta a média
de salário da população, a média de filhos e o maior salário.
'''
# entrada 
salario = float(input('Digite o valor do seu salário (-1 interrompe): '))
filhos = int(input('Quantos filhos você tem: '))
maior = 0
soma_sal = 0
soma_fil = 0
cont = 0

# processamento
while(salario != -1):
    if (salario > maior):
        maior = salario
    soma_sal += salario
    soma_fil += filhos
    cont += 1
    salario = float(input('Digite o valor do seu salário (-1 interrompe): '))
    if (salario != -1):
        filhos = int(input('Quantos filhos você tem: '))

# retorna
print('A média de salário da população é: {}'.format(soma_sal/cont))
print('A média de filhos da população é: {}'.format(soma_fil/cont))
print('O maior Salário é: {}'.format(maior))