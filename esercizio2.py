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


#PUNTO 4
"""
Chiedere all’utente una lettera e contate quante volte compare nel testo
"""
####################################################arrivata qua
contatore_variabile = 0
for variabile in lista_lettere:
    if lettera == variabile:
        contatore_variabile = contatore_variabile + 1

print(contatore_variabile)

#c'è qualcosa che non va pk non so come far chiedere la variabile
"""
# Chiediamo all'utente di inserire una lettera
lettera = input("Inserisci una lettera da cercare nel testo: ")

# Ci assicuriamo che l'utente abbia inserito un solo carattere ed effettivamente una lettera
if len(lettera) == 1 and lettera.isalpha():
    # Convertiamo tutto in minuscolo per un conteggio case-insensitive
    conteggio = testo.lower().count(lettera.lower())
    
    print(f"La lettera '{lettera}' compare {conteggio} volte nel testo.")
else:
    print("Errore: devi inserire un singolo carattere alfabetico.")

"""


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

# Sostituiamo le parole (gestendo sia le maiuscole che le minuscole)
testo_modificato = testo.replace("Day", "PYTHON").replace("day", "PYTHON")
testo_modificato = testo_modificato.replace("Water", "PYTHON").replace("water", "PYTHON")
testo_modificato = testo_modificato.replace("About", "PYTHON").replace("about", "PYTHON")

# Stampiamo il risultato finale
print(testo_modificato)


#punto 6

righe_modificate = []

# Dividiamo il testo in singole righe
for riga in testo.split("\n"):
    parole = riga.split()
    nuove_parole = []

    # Usiamo enumerate partendo da 1 per tracciare la posizione delle parole
    for indice, parola in enumerate(parole, start=1):
        if indice % 2 != 0:
            # Posizione dispari (1°, 3°, 5°...): tutto in maiuscolo
            nuove_parole.append(parola.upper())
        else:
            # Posizione pari: lasciamo la parola com'è
            nuove_parole.append(parola)

    # Ricomponiamo la riga unendo le parole con uno spazio
    righe_modificate.append(" ".join(nuove_parole))

# Uniamo tutte le righe modificate per ricreare il testo finale
testo_finale = "\n".join(righe_modificate)
print(testo_finale)



#punto 7

#forse non serve
# Dividiamo il testo in una lista di righe
righe = testo.split("\n")

# Invertiamo l'ordine delle righe dall'ultima alla prima
righe_invertite = righe[::-1]

# Ricomponiamo il testo unendo le righe invertite con un a capo
testo_finale = "\n".join(righe_invertite)
print(testo_finale)







#punto 8 

#come specchiare

#print(lista_righe)
#lista_righe[01]

#forse non serve vedi se usare questo o gem
for indice in [2, 7, 12, 17]:
    lista_prima_riga = list(lista_righe[indice])
    print (lista_prima_riga)


# Dividiamo il testo in una lista di versi
versi = testo.split("\n")
versi_modificati = []

# Iteriamo sui versi a blocchi di 4 (uno per ogni strofa)
for i in range(0, len(versi), 4):
    # Prendiamo i 4 versi della strofa corrente
    strofa = versi[i:i+4]
    
    # Il secondo verso della strofa (indice 1 del blocco) viene invertito a specchio
    strofa[1] = strofa[1][::-1]
    
    # Aggiungiamo i versi della strofa alla nostra lista finale
    versi_modificati.extend(strofa)

# Ricomponiamo il testo finale
testo_finale = "\n".join(versi_modificati)
print(testo_finale)


# punto 9


import re

# 1. Dividiamo il testo in linee ed eliminiamo eventuali righe vuote
versi = [linea for linea in testo.split("\n") if linea.strip()]

# 2. Raggruppiamo i versi in strofe (4 versi per ogni strofa)
strofe = [versi[i : i + 4] for i in range(0, len(versi), 4)]

# Lista che conterrà l'insieme delle parole di ciascuna strofa
parole_per_strofa = []

for strofa in strofe:
    # Uniamo i 4 versi della strofa in un unico testo in minuscolo
    testo_strofa = " ".join(strofa).lower()

    # Usiamo le espressioni regolari (regex) per estrarre solo le parole,
    # escludendo simboli di punteggiatura come virgole, punti e punti esclamativi
    parole = re.findall(r"\b\w+\b", testo_strofa)

    # Convertiamo la lista di parole in un set (elimina i duplicati interni alla strofa)
    parole_per_strofa.append(set(parole))

# 3. Troviamo l'intersezione tra i set di tutte le strofe
# (*parole_per_strofa "spacchetta" la lista passando i 4 set alla funzione intersection)
parole_comuni = set.intersection(*parole_per_strofa)

# 4. Stampiamo il risultato richiesto
if parole_comuni:
    print(
        f"Le parole che compaiono in tutte le strofe sono: {', '.join(parole_comuni)}"
    )
else:
    print("Nessuna parola compare in tutte le strofe.")



# punto 10000

import re

# 1. Estraiamo tutte le parole convertendole in minuscolo
#    e usiamo set() per eliminare automaticamente i duplicati
parole_pulite = re.findall(r"\b\w+\b", testo.lower())
parole_univoche = set(parole_pulite)

# 2. Ordiniamo la lista di parole in base alla loro lunghezza (len)
#    In caso di parità di lunghezza, Python le manterrà in ordine alfabetico naturale
parole_ordinate = sorted(parole_univoche, key=len)

# 3. Visualizziamo il risultato
print(f"Ci sono in totale {len(parole_ordinate)} parole univoche.\n")
print("Ecco la lista ordinata per lunghezza:")
print(parole_ordinate)


#punto  11

# Creiamo un dizionario vuoto per memorizzare le occorrenze
mappa_caratteri = {}

# Scorriamo il testo carattere per carattere
for carattere in testo:
    if carattere in mappa_caratteri:
        mappa_caratteri[carattere] += 1
    else:
        mappa_caratteri[carattere] = 1

# Per visualizzarlo in modo ordinato e leggibile, stampiamo chiave e valore
print("Mappatura completa dei caratteri e delle loro occorrenze:\n")
for chiave, valore in sorted(mappa_caratteri.items()):
    # Rappresentazione speciale per rendere visibili gli spazi e gli "a capo"
    if chiave == " ":
        nome_chiave = "' ' (spazio)"
    elif chiave == "\n":
        nome_chiave = "'\\n' (a capo)"
    else:
        nome_chiave = f"'{chiave}'"

    print(f"Carattere {nome_chiave:<15} -> Occorrenze: {valore}")


#punto 12

mappa_alfanumerici = {}

# Convertiamo il testo in minuscolo prima di analizzarlo
for carattere in testo.lower():
    # Selezioniamo solo i caratteri alfanumerici (lettere e numeri)
    if carattere.isalnum():
        if carattere in mappa_alfanumerici:
            mappa_alfanumerici[carattere] += 1
        else:
            mappa_alfanumerici[carattere] = 1

# Visualizziamo il dizionario ordinato in modo leggibile
print("Mappatura dei soli caratteri alfanumerici (case-insensitive):\n")
for chiave, valore in sorted(mappa_alfanumerici.items()):
    print(f"Carattere '{chiave}' -> Occorrenze: {valore}")



