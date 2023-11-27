# Informa o valor
valor = int(input())
valor2 = valor
resultado = 1

# Calcular o fatorial desse valor
while(valor > 0):
    resultado = valor * resultado
    valor = valor - 1

# Imprimir o resultado
print(f"O fatorial de {valor2} = {resultado}")