testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''
# Risolvendo parte 1 esercizio 2

#divido il testo in base al carattere \n
lista_righe = testo.split('\n')

contatore = 0
for riga in lista_righe:
    if len(riga) > 0:
        contatore = contatore + 1

print(contatore)


#parte 2 
lista_parole = testo.split() 
# testo.split('\n') DEVO AGGIUNGERE


#72 + 15 = 88

#print (lista_parole)

contatore_parole = 0
for parola in lista_parole:
    if len(parola) > 0:
        contatore_parole = contatore_parole + 1

print(contatore_parole)


#PUNTO 3

#testo_lista = list(testo)
#testo_lista

#print(testo_lista)
lista_lettere = list(testo)

alfanumerici = 'abcdefghijklmnopqrstuvwxyzèéàòùABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


#carattere in alfanumerici
#risponde true false

contatore_lettere = 0
for lettera in lista_lettere:
    if lettera in alfanumerici:
        contatore_lettere = contatore_lettere + 1

print(contatore_lettere)

#351 devono essere alfanumerici, 87  parole

contatore_lettere = 0
for lettera in lista_lettere:
    if lettera.isalnum():
        contatore_lettere = contatore_lettere + 1

print(contatore_lettere)







#vedi se va bene con sotto cambia
'''
isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
'''

#PUNTO 4

contatore_variabile = 0
for variabile in lista_lettere:
    if lettera == variabile:
        contatore_variabile = contatore_variabile + 1

print(contatore_variabile)

#c'è qualcosa che non va pk non so come far chiedere la variabile


#PUNTO 5

 #Sostituite tutte le parole day, water e about con la parola PYTHON in tutti i versi



cambio = {
    "day": "PYTHON",
    "water": "PYTHON",
    "about": "PYTHON",
    "Day": "PYTHON",
    "Water": "PYTHON",
    "About": "PYTHON"
}

# help upper lower


for vecchio, nuovo in cambio.items() :
    testo = testo.replace(vecchio, nuovo)

print(testo)
'''
nuovo_testo = testo.replace("day", "PYTHON")
testo.replace("water", "PYTHON")
testo.replace("water", "PYTHON")


print(nuovo_testo)
#str.replace(vecchia, nuova): S
'''
'''
python
testo = "Il gatto mangia la mela sul tavolo."
cambiamenti = {
    "gatto": "cane",
    "mela": "pera",
    "tavolo": "divano"
}

for vecchia, nuova in cambiamenti.items():
    testo = testo.replace(vecchia, nuova)

'''



#punto 8 

#come specchiare

#print(lista_righe)
#lista_righe[01]


for indice in [2, 7, 12, 17]:
    lista_prima_riga = list(lista_righe[indice])
    print (lista_prima_riga)




