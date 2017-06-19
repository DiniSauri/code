frase = input()
chiave = int(input())

alfabeto = "abcdefghijklmnopqrstuvwxyz"
cifrata = ""

for i in range(0,len(frase)):
    indice = alfabeto.index(frase[i])
    indice = (indice + chiave) % len(alfabeto)
    cifrata = cifrata + alfabeto[indice]

print(cifrata)
frase = ""
for i in range(0,len(cifrata)):
    indice = alfabeto.index(cifrata[i])
    indice = (indice - chiave) % len(alfabeto)
    frase = frase + alfabeto[indice]

print(frase)
