'''
Faça uma função recursiva que inverta todos os caracteres de uma string.
'''


def inverter_string(palavra):
    if (len(palavra) <= 1):
        return palavra
    else:
        return palavra[-1] + inverter_string(palavra[:-1])


nome = input("Digite uma palavra: ")
print(inverter_string(nome))
