'''
#
# File: esercizio2.py
#
# Author: Petra Zurini
#
# Date: 20/07/2026
#
# Version: 1.0
#
# Description: Programma risolutivo dell'esercizio 2, lezione 4
#
'''

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


#RISOLUZIONE PUNTO 1
"""
Contate le righe non vuote che compongono l’estratto
"""

#divido il testo in base al carattere \n
lista_righe = testo.split('\n')

#conto le righe non vuote
contatore = 0
for riga in lista_righe:
    if len(riga) > 0:
        contatore = contatore + 1

print(contatore)


#RISOLUZIONE PUNTO 2
"""
Contate le parole che compongono l’estratto
"""

#divido il testo per ogni parola
lista_parole = testo.split() 

#conto le parole
contatore_parole = 0
for parola in lista_parole:
    if len(parola) > 0:
        contatore_parole = contatore_parole + 1

print(contatore_parole)


#RISOLUZIONE PUNTO 3
"""
Contate i caratteri alfanumerici che compongono l’estratto
"""

#trasformo testo in una lista
lista_lettere = list(testo)

#conto gli alfanumerici in testo
contatore_lettere = 0
for lettera in lista_lettere:
    if lettera.isalnum():
        contatore_lettere = contatore_lettere + 1

print(contatore_lettere)

"""
#posso anche farlo alternativamente così

alfanumerici = 'abcdefghijklmnopqrstuvwxyzèéàòùABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

contatore_lettere = 0
for lettera in lista_lettere:
    if lettera in alfanumerici:
        contatore_lettere = contatore_lettere + 1

print(contatore_lettere)
"""


#RISOLUZIONE PUNTO 4
"""
Chiedere all’utente una lettera e contate quante volte compare nel testo
"""

#chiedo la lettera da contare
lettera = input("Inserisci una lettera da cercare nel testo: ")

#controllo che sia una lettera
if len(lettera) == 1 and lettera.isalpha():
    #convertmo tutto in minuscolo
    conteggio = testo.lower().count(lettera.lower())
    
    print(f"La lettera '{lettera}' compare {conteggio} volte nel testo.")
else:
    print("Errore: devi inserire un singolo carattere alfabetico.")


#RISOLUZIONE PUNTO 5
"""
Sostituite tutte le parole day, water e about con la parola PYTHON in tutti i versi
"""

#con .replace sostituisco le parole, sia maiuscole che minuscole
testo_modificato = testo.replace("Day", "PYTHON").replace("day", "PYTHON")
testo_modificato = testo_modificato.replace("Water", "PYTHON").replace("water", "PYTHON")
testo_modificato = testo_modificato.replace("About", "PYTHON").replace("about", "PYTHON")

#stampo il risultato 
print(testo_modificato)


#RISOLUZIONE PUNTO 6
"""
Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo
"""

#preparo lista
righe_modificate = []

#divido il testo in singole righe
for riga in testo.split("\n"):
    parole = riga.split()
    nuove_parole = []

    #traccio posizione con enumerate, funzione che cicla la seguenza
    for indice, parola in enumerate(parole, start=1):
        if indice % 2 != 0:
            #tutte le posizione dispari le metto in maiuscolo
            nuove_parole.append(parola.upper())
        else:
            #tutte le posizione pari lascio com'è
            nuove_parole.append(parola)

    # Ricomponiamo la riga unendo le parole con uno spazio
    righe_modificate.append(" ".join(nuove_parole))

#ricostriusco testo con a capo
testo_finale = "\n".join(righe_modificate)
print(testo_finale)


#RISOLUZIONE PUNTO 7
"""
Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto.
"""

#divido il testo in una lista di righe
righe = testo.split("\n")

#inverto l'ordine delle righe dall'ultima alla prima
righe_invertite = righe[::-1]

#ricostriusco testo con a capo
testo_finale = "\n".join(righe_invertite)
print(testo_finale)


#RISOLUZIONE PUNTO 8 
"""
Riscrivete il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè 
al contrario carattere per carattere: Ad esempio, questa frase’ –> ‘esarf atseuq ,oipmese dA’)
"""

#separo in strofe usando i doppi a capo (\n\n)
strofe = testo.split("\n\n")

#preparo lista 
strofe_modificate = []

#separo in versi
for strofa in strofe:
    versi = strofa.split("\n")
    versi_modificati = []

    #uso enumerate() per accedere sia all'indice (i) che al verso
    for i, verso in enumerate(versi):
        #il secondo verso ha indice 1 (in Python si parte da 0)
        if i == 1:
            #[::-1] inverte la stringa carattere per carattere
            verso_a_specchio = verso[::-1]
            versi_modificati.append(verso_a_specchio)
        else:
            versi_modificati.append(verso)

    #ricostriusco strofa unendo i versi con un a capo
    strofe_modificate.append("\n".join(versi_modificati))

#ricostruisco testo modificato
testo_finale = "\n\n".join(strofe_modificate)

#stampo risultato
print(testo_finale)


#RISOLUZIONE PUNTO 9
"""
Trovate eventuali parole che compaiono in tutte le strofe
"""

#modulo per lavorare con pattern
import re

#divido in versi non vuoti
versi = [linea for linea in testo.split("\n") if linea.strip()]

#raggruppo in strofe
strofe = [versi[i : i + 4] for i in range(0, len(versi), 4)]

#preparo lista
parole_per_strofa = []

#ciclo per ogni strofa
for strofa in strofe:
    #raggruppo i versi di una strofa e rendo tutto minuscolo
    testo_strofa = " ".join(strofa).lower()

    #uso re. per estrarre solo le parole, escludendo punteggiatura 
    parole = re.findall(r"\b\w+\b", testo_strofa)

    #converto lista in set per eliminare doppioni
    parole_per_strofa.append(set(parole))

#trovo l'intersezione tra i set di tutte le strofe
#*parole_per_strofa "spacchetta" la lista passando i 4 set alla funzione intersection
parole_comuni = set.intersection(*parole_per_strofa)

#stampo il risultato 
if parole_comuni:
    print(f"Le parole che compaiono in tutte le strofe sono: {', '.join(parole_comuni)}")
    
else:
    print("Nessuna parola compare in tutte le strofe.")


#RISOLUZIONE PUNTO 10
"""
Create la lista univoca di tutte le parole che compaiono nel testo, ordinatela per lunghezza 
delle parole e visualizzatela
"""

#modulo per lavorare con pattern
import re

#prendo tutte le parole in minuscolo e uso set() per eliminare doppioni
parole_pulite = re.findall(r"\b\w+\b", testo.lower())
parole_univoche = set(parole_pulite)

#ordino lista in base alla lunghezza (len)
parole_ordinate = sorted(parole_univoche, key=len)

#stampo il risultato
print(f"Ci sono in totale {len(parole_ordinate)} parole univoche.\n")
print("Ecco la lista ordinata per lunghezza:")
print(parole_ordinate)


#RISOLUZIONE PUNTO 11
"""
Create un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo 
(valore) e visualizzatelo
"""

#creo dizionario vuoto per memorizzare le occorrenze
mappa_caratteri = {}

#scorro il testo
for carattere in testo:
    if carattere in mappa_caratteri:
        mappa_caratteri[carattere] += 1
    else:
        mappa_caratteri[carattere] = 1

#stampo chiave e valore
print("Mappatura completa dei caratteri e delle loro occorrenze:\n")
for chiave, valore in sorted(mappa_caratteri.items()):
    #rappresentazione speciale per rendere visibili gli spazi e gli "a capo"
    if chiave == " ":
        nome_chiave = "' ' (spazio)"
    elif chiave == "\n":
        nome_chiave = "'\\n' (a capo)"
    else:
        nome_chiave = f"'{chiave}'"

    print(f"Carattere {nome_chiave:<15} -> Occorrenze: {valore}")


#RISOLUZIONE PUNTO 12
"""
Create un dizionario come il precedente per i soli caratteri alfanumerici (no caratteri speciali),
ignorando maiuscole e minuscole
"""

#creo dizionario vuoto per memorizzare le occorrenze
mappa_alfanumerici = {}

#converto il testo in minuscolo
for carattere in testo.lower():
    #prendo solo alfanumerici
    if carattere.isalnum():
        if carattere in mappa_alfanumerici:
            mappa_alfanumerici[carattere] += 1
        else:
            mappa_alfanumerici[carattere] = 1

#stampo i riusltati
print("Mappatura dei soli caratteri alfanumerici (case-insensitive):\n")
for chiave, valore in sorted(mappa_alfanumerici.items()):
    print(f"Carattere '{chiave}' -> Occorrenze: {valore}")