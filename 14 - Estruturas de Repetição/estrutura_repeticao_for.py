texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()


for numero in range(0, 51, 5):
    print(numero, end=" ")