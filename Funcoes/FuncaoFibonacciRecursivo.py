'''
Crie uma função de fibonacci recursiva, que exiba toda a sequência até o número informado.
'''
def fibonacci(numero, ultimo = 1, penultimo = 0, impressao = 1):
    aux = ultimo
    if (numero > 0):
        if impressao < numero:
            print(ultimo, end=', ')
            ultimo += penultimo
            penultimo = aux
            return fibonacci(numero,ultimo,penultimo,impressao + 1)
        elif impressao == numero:
            print (ultimo)
    else:
        print("Número Inválido! Digite um número maior que 0")


num = int(input("Digite até qual termo deseja ir: "))
fibonacci(num)