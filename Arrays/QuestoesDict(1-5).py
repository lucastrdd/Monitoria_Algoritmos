'''
1. Crie um dicionário com as chaves sendo nomes de países e os valores sendo suas capitais.
2. Adicione um novo país ao dicionário.
3. Remova um país do dicionário.
4. Imprima todas as chaves do dicionário.
5. Verifique se um determinado país está presente no dicionário.
'''
# 1
paises = {"Brasil": "Brasilia", "Argentina": "Buenos Aires", "França": "Paris"}

for pais, capital in paises.items():
    print(f"A Capital do {pais} é {capital}")

print()

# 2
paises.update({"Espanha": "Madrid"})

for pais, capital in paises.items():
    print(f"A Capital do {pais} é {capital}")

print()

# 3
paises.pop("Argentina")
for pais, capital in paises.items():
    print(f"A Capital do {pais} é {capital}")


# 4
for pais in paises.keys():
    print(f"{pais}, ", end='')

print()

# 5
if "Argentina" in paises:
    print("Tem a argentina")
else:
    print("Não tem a argentina")
