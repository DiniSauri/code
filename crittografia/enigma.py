alfabeto = "abcdefghijklmnopqrstuvwxyz"
def cesarecifra(lettera,chiave):
    indice = alfabeto.index(lettera)
    indice = (indice + chiave) % len(alfabeto)
    return alfabeto[indice]
def scambiatore(lettera):
    indice = alfabeto.index(lettera)
    indice = len(alfabeto) - indice % len(alfabeto)
    return alfabeto[indice]

#chiavi
print("inserisci le chiavi dei tre rotori")
chiave1 = int(input());
chiave2 = int(input());
chiave3 = int(input());

#stecker
quadro = list("abcdefghijklmnopqrstuvwxyz")
print("inserisci 6 coppie di lettere")
for i in range(0,6):
    coppia = input()
    lettera1 = coppia[0]
    lettera2 = coppia[1]
    indice1 = quadro.index(lettera1)
    indice2 = quadro.index(lettera2)
    tmp = quadro[indice1] 
    quadro[indice1] = quadro[indice2]
    quadro[indice2] = tmp

#cifra la parola
print("inserisci la frase")
frase = input()
cifrata = ""
for i in range(0,len(frase)):
    #stecker
    indice = alfabeto.index(frase[i])
    uscita = quadro[indice]

    #rotori
    uscita_r1 = cesarecifra(uscita,chiave1)
    uscita_r2 = cesarecifra(uscita_r1,chiave2)
    uscita_r3 = cesarecifra(uscita_r2,chiave3)

    #riflettore
    uscita_rif = scambiatore(uscita_r3)

    #rotori (indietro)
    uscita_r4 = cesarecifra(uscita_rif,-chiave1)
    uscita_r5 = cesarecifra(uscita_r4,-chiave2)
    uscita_r6 = cesarecifra(uscita_r5,-chiave3)

    #stecker (indietro)
    indice = alfabeto.index(uscita_r6)
    uscita = quadro[indice]

    cifrata = cifrata + uscita
    
    #movimento rotori dopo ogni lettera
    chaive1 = chiave1 +1
    if chiave1 > len(alfabeto):
        chiave1 = 0
        chiave2 = chiave2 + 1
        if chiave2 > len(alfabeto):
            chiave2 = 0
            chiave3 = chiave3 + 1
            if chiave3 > len(alfabeto):
                chiave3 = 0
print(cifrata)
