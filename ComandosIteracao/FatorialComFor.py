# Passos:
# Ler um número
num = int(input('Digite um número inteiro: '))
prod = 1

# Calcular o fatorial
for i in range(num,0,-1):
    prod *= i

# retornar o valor
print(f'o fatorial {num} é: {prod}')