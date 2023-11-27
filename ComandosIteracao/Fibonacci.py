#Passos
# input pra saber até onde é:
num = int(input("Digite até qual termo deseja ir: "))
ultimo = 1
penultimo = 1

# Realizas as somas até chegar no input:
if num == 1:
    print(1)
    # o primeiro elemento da sequência é sempre 1
elif num == 2:
    print("1, 1")
    # o primeiro e o segundo elemento da sequência são sempre 1
else:
    #caso num seja maior  ou igual a 3, podemos então trabalhar os resultados:
    print(ultimo,", ",penultimo, end="")
    while(num > 2): #por a impressão já conter 2 valores, enquanto num for menor que 2, realizamos o laço
        impressao = ultimo + penultimo
        #o valor a ser impresso vai ser sempre o ultimo mais o penultimo
        penultimo = ultimo
        #a partir daí quem era ultimo vira penultimo
        ultimo = impressao
        #e o ultimo agora é quem vai ser impresso
        print (", ",impressao,end="")
        #imprimimos então antes de atualizar, o valor a ser impresso (lin 18)
        num -= 1
        # e diminuimos o contador.