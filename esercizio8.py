'''
#
# File: esercizio8.py
#
# Author: Petra Zurini
#
# Date: 20/07/2026
#
# Version: 1.0
#
# Description: Programma risolutivo dell'esercizio 8, lezione 12
#
'''

"""
Scrivete un programma per “il gioco dell’impiccato” in cui:

leggete una lista di parole da un file JSON
scegliete una parola a caso con cui giocare dalla lista letta, tramite random
chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola

La rappresentazione grafica del gioco è libera, così come il numero dei “tentativi” disponibili.
"""

#RISOLUZIONE PUNTO 1
"""
Scrivete il programma con un approccio totalmente LBYL
LBYL (Look Before You Leap): Si controllano esplicitamente tutte le condizioni (con if, 
os.path.exists, controlli di tipo o lunghezza) prima di effettuare un'operazione che potrebbe 
fallire.
"""

import json
import os
import random

#funzione di gioco con approccio lbyl
def gioco_impiccato_lbyl():
    print("=== IL GIOCO DELL'IMPICCATO (Approccio LBYL) ===")
    #file delle parole da indovinare
    nome_file = "parole_per_gioco_esercizio8.json"

    #controllo se il file esiste
    if not os.path.exists(nome_file):
        print(f"Errore: Il file '{nome_file}' non esiste sul disco.")
        return

    #controllo se il file è vuoto
    if os.path.getsize(nome_file) == 0:
        print(f"Errore: Il file '{nome_file}' è vuoto.")
        return

    with open(nome_file, "r", encoding="utf-8") as f:
        contenuto = f.read()

    # Per verificare se è un JSON valido in modo LBYL puro senza try-except,
    # dovremmo scrivere un intero parser. Python non offre un metodo integrato "is_json()".
    # Utilizziamo eccezionalmente json.loads dopo aver verificato la struttura base.
    # Nota: se il JSON è strutturalmente invalido, json.loads solleverà comunque un errore,
    # evidenziando perché l'approccio LBYL puro con il parsing dei file sia complesso in Python.
    parole = json.loads(contenuto)

    #controllo se nel file ci sono parole valide
    if not isinstance(parole, list) or len(parole) == 0:
        print("Errore: Il file JSON non contiene una lista valida di parole.")
        return

    #scelgo casualmente la parola e inizializzo variabili
    parola_segreta = random.choice(parole).lower()
    lettere_indovinate = set()
    lettere_errate = set()
    tentativi_rimasti = 6

    #ciclo dei tentativi per indovinare
    while tentativi_rimasti > 0:
        #visualizzazione dello stato attuale della parola
        visualizzazione = ""
        #visualizzo solo letter indovinate
        for lettera in parola_segreta:
            if lettera in lettere_indovinate:
                visualizzazione += lettera + " "
            #le lettere non indovinate rimangono vuote
            else:
                visualizzazione += "_ "

        #stampo risulati
        print(f"\nParola: {visualizzazione.strip()}")
        print(f"Tentativi rimasti: {tentativi_rimasti}")
        print(f"Lettere errate: {', '.join(sorted(lettere_errate))}")

        #controllo vittoria
        vittoria = True
        #controllo che la parola sia giusta
        for lettera in parola_segreta:
            if lettera not in lettere_indovinate:
                vittoria = False

        #se la parola è giusta avvisa l'utente
        if vittoria:
            print(
                f"\nComplimenti! Hai indovinato la parola: '{parola_segreta}'!"
            )
            return

        #richiesta input all'utente
        input_utente = (
            input("Inserisci una lettera o indovina l'intera parola: ")
            .strip() #rimuove gli spazi iniziali e finali
            .lower() #rende minuscolo
        )

        #controllo l'input utente
        if not input_utente:
            print("Non hai inserito nulla. Riprova.")
            continue

        if not input_utente.isalpha():
            print("L'input contiene caratteri non validi. Usa solo lettere.")
            continue

        #se l'utente prova a indovinare l'intera parola
        if len(input_utente) > 1:
            #se giusta
            if input_utente == parola_segreta:
                print(
                    f"\nHai indovinato la parola intera: '{parola_segreta}'!"
                )
                return
            
            #se sbagliata
            else:
                print(f" '{input_utente}' non è la parola segreta.")
                tentativi_rimasti -= 1
                continue

        #se l'utente ha inserito una singola lettera
        lettera = input_utente
        #se lettera già provata
        if lettera in lettere_indovinate or lettera in lettere_errate:
            print(f"Hai già provato la lettera '{lettera}'.")
            continue

        #se lettera giusta
        if lettera in parola_segreta:
            print(f"La lettera '{lettera}' è presente.")
            lettere_indovinate.add(lettera)
        #se lettera sbagliata
        else:
            print(f"La lettera '{lettera}' non è presente.")
            lettere_errate.add(lettera)
            tentativi_rimasti -= 1

    #se avvengono 6 sbagli l'utente ha perso
    print(
        f"\nTentativi esauriti. Hai perso. La parola era: '{parola_segreta}'."
    )

#eseguo il programma
if __name__ == "__main__":
    gioco_impiccato_lbyl()



#RISOLUZIONE PUNTO 2
"""
RI-scrivete il programma con un approccio totalmente EAFP
EAFP (Easier to Ask for Forgiveness than Permission): Si tenta direttamente di eseguire 
l'operazione all'interno di un blocco try e si catturano le eccezioni specifiche (except) 
se qualcosa va storto. È l'approccio più idiomatico in Python.
"""

import json
import random
import sys


#funzione di gioco con approccio eafp
def gioco_impiccato_eafp():
    print("=== IL GIOCO DELL'IMPICCATO (Approccio EAFP) ===")
    nome_file = "parole_per_gioco_esercizio8.json"

    #tento direttamente l'apertura e il parsing (EAFP)
    try:
        #provo ad aprire il file
        with open(nome_file, "r", encoding="utf-8") as f:
            parole = json.load(f)

        #intercetto un'eventuale struttura dati non indicizzabile o vuota
        parola_segreta = random.choice(parole).lower()

    #in caso di file non esistente
    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file}' non è stato trovato.")
        return
    #in caso di file non compilato
    except json.JSONDecodeError:
        print(f"Errore: Il file '{nome_file}' non contiene un JSON valido.")
        return
    #in caso di file non vuoto ma senza lista valida di parole    
    except (IndexError, TypeError):
        print(
            "Errore: La struttura interna del file JSON non è una lista valida di parole."
        )
        return

    #imposto variabili
    lettere_indovinate = set()
    lettere_errate = set()
    tentativi_rimasti = 6

    #ciclo per indovinare
    while True:
        try:
            #generazione della stringa visualizzata, _ se lettera non indovinata, se indovinata stampata
            visualizzazione = [
                let if let in lettere_indovinate else "_"
                for let in parola_segreta
            ]
            #stampo tentativo appena avvenuto
            print(f"\nParola: {' '.join(visualizzazione)}")
            print(f"Tentativi rimasti: {tentativi_rimasti}")
            print(f"Lettere errate: {', '.join(sorted(lettere_errate))}")

            #condizione di vittoria: se non ci sono più '_' nella lista
            if "_" not in visualizzazione:
                print(
                    f"\nHai indovinato la parola: '{parola_segreta}'!"
                )
                break

            #condizione sconfitta
            if tentativi_rimasti <= 0:
                print(
                    f"\nTentativi esauriti. Hai perso. La parola segreta era: '{parola_segreta}'."
                )
                break

            #chiedo all'utente la lettera o la parola
            input_utente = (
                input("Inserisci una lettera o indovina l'intera parola: ")
                .strip() #rimuove gli spazi iniziali e finali
                .lower() #rende minuscolo
            )

            #validazione eafp dell'input
            #se input non è lettera
            if not input_utente.isalpha():
                #sollevo intenzionalmente un'eccezione per gestire l'input non valido
                raise ValueError(
                    "L'input contiene caratteri non validi o è vuoto."
                )

            #se tento parola intera
            if len(input_utente) > 1:
                #se è giusta
                if input_utente == parola_segreta:
                    print(
                        f"\n Hai indovinato la parola intera: '{parola_segreta}'!"
                    )
                    break #finisce il ciclo
                #se sbagliata
                else:
                    print(
                        f"Hai sbagliato.'{input_utente}' non è la parola segreta."
                    )
                    tentativi_rimasti -= 1
                    continue #continua in ciclo

            #se tento singola lettera
            lettera = input_utente
            #se lettera già inserita
            if lettera in lettere_indovinate or lettera in lettere_errate:
                raise KeyError(f"Hai già inserito la lettera '{lettera}'.")

            #se lettera giusta
            if lettera in parola_segreta:
                print(f"La lettera '{lettera}' è presente.")
                lettere_indovinate.add(lettera)
            #se lettera sbagliata    
            else:
                print(f"Peccato! La lettera '{lettera}' non è presente.")
                lettere_errate.add(lettera)
                tentativi_rimasti -= 1

        except ValueError as ve:
            #cattura errori di digitazione o stringhe vuote
            print(f"[ATTENZIONE] {ve} Riprova inserendo solo lettere dell'alfabeto.")
        except KeyError as ke:
            #cattura lettere già inserite sfruttando il flusso logico delle eccezioni
            print(f"[INFO] {str(ke).strip(chr(39))}")

#eseguo il programma
if __name__ == "__main__":
    gioco_impiccato_eafp()
