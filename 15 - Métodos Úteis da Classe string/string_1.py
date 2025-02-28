nome = "CaMilLy"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá, Mundo!  "
print(texto.strip() +".")
print(texto.lstrip() +". Essa ")
print(texto.rstrip() +".")

menu = "Pyhton"

print(menu.center(14, "-"))
print("-".join(menu))
for letra in menu:
    print(letra, end="-")

