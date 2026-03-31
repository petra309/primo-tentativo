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

#vedi se va bene con sotto cambia
'''
isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
'''
#punto 8 

#come specchiare

#print(lista_righe)
#lista_righe[01]


for indice in [2, 7, 12, 17]:
    lista_prima_riga = list(lista_righe[indice])
    print (lista_prima_riga)




