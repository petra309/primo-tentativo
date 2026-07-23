'''
#
# File: esercizio6.py
#
# Author: Petra Zurini
#
# Date: 20/07/2026
#
# Version: 1.0
#
# Description: Programma risolutivo dell'esercizio 6, lezione 8
#
'''

#RISOLUZIONE PUNTO 2
"""
In un file separato importate la classe rubrica appena creata e scrivete un programma che in
modo interattivo chieda all’utente di quale delle 5 operazioni della classe rubrica svolgere. 
Se l’azione richiesta non esiste, il programma continua a chiedere l’azione da svolgere finchè
non viene indicata la stringa “EXIT”
"""

#importo la rubrica descritta nel file ausiliario
from rubrica_esercizio6 import Rubrica

#dizionario dell'esercizio 3
dati_iniziali ={
    'Paolino Paperino': {
        'giorno': 9,
        'mese': 'giugno',
        'anno': 1934,
        'età': 93,
        'sesso': 'M',
        'mail': 'paolino.paperin0@disney.org',
    },
    'Ron Weasley': {
        'giorno': 1,
        'mese': 'marzo',
        'anno': 1980,
        'età': 46,
        'sesso': 'M',
        'mail': 'ron_weasley80@hogwards.uk',
    },
    'Ramona Flowers': {
        'giorno': 19,
        'mese': 'ottobre',
        'anno': 2004,
        'età': 22,
        'sesso': 'F',
        'mail': 'ramona.fls@gmail.com',
    },
    'Madoka Ayukawa': {
        'giorno': 25,
        'mese': 'maggio',
        'anno': 1969,
        'età': 57,
        'sesso': 'F',
        'mail': 'madoka_sax@asahi_net.jp',
    },
}

rubrica_iniziale = {
    'Paolino Paperino': {
        'giorno': 9,
        'mese': 'giugno',
        'anno': 1934,
        'età': 93,
        'sesso': 'M',
        'mail': 'paolino.paperin0@disney.org',
    },
    'Ron Weasley': {
        'giorno': 1,
        'mese': 'marzo',
        'anno': 1980,
        'età': 46,
        'sesso': 'M',
        'mail': 'ron_weasley80@hogwards.uk',
    },
    'Ramona Flowers': {
        'giorno': 19,
        'mese': 'ottobre',
        'anno': 2004,
        'età': 22,
        'sesso': 'F',
        'mail': 'ramona.fls@gmail.com',
    },
    'Madoka Ayukawa': {
        'giorno': 25,
        'mese': 'maggio',
        'anno': 1969,
        'età': 57,
        'sesso': 'F',
        'mail': 'madoka_sax@asahi_net.jp',
    },
}

#esplicito le azioni possibili all'utente
def mostra_menu():
    print("\n" + "=" * 45)
    print("         GESTIONE RUBRICA          ")
    print("=" * 45)
    print("Azioni disponibili:")
    print("  1. APRI      - Carica una rubrica da file (JSON/TXT)")
    print("  2. AGGIUNGI  - Aggiungi un nuovo contatto")
    print("  3. RIMUOVI   - Rimuovi un contatto esistente")
    print("  4. STAMPA    - Visualizza la scheda di un contatto")
    print("  5. SALVA     - Salva la rubrica su file (JSON/TXT)")
    print("  EXIT         - Chiudi il programma")
    print("=" * 45)


def main():
    #inizializzo l'oggetto Rubrica vuoto (non aperto)
    rubrica = Rubrica()

    AZIONI_VALIDE = [
        'APRI',
        'AGGIUNGI',
        'RIMUOVI',
        'STAMPA',
        'SALVA',
        'EXIT',
    ]

    while True:
        mostra_menu()
        #chiedo l'azione all'utente
        scelta = (
            input("Inserisci l'azione da svolgere: ").strip().upper()
        )

        if scelta not in AZIONI_VALIDE:
            print(f"Azione '{scelta}' non valida! Riprova.")
            continue

        if scelta == 'EXIT':
            print("\nChiusura del programma.")
            break

        elif scelta == 'APRI':
            #chiedo come aprire all'utente
            filepath = input(
                "Inserisci il percorso del file da aprire (.json o .txt): "
            ).strip()
            if filepath.lower().endswith('.json'):
                rubrica.apri_json(filepath)
            elif filepath.lower().endswith('.txt'):
                rubrica.apri_testo(filepath)
            else:
                print(
                    "Estensione file non riconosciuta. Usa file .json o .txt"
                )

        elif scelta == 'AGGIUNGI':
            #se la rubrica non è aperta, la validazione dentro il metodo mostrerà il messaggio d'errore richiesto
            if not rubrica.is_aperta:
                rubrica.aggiungi('', 0, '', 0, 0, '', '')
                continue

            print("\n--- Inserisci i dati del nuovo contatto ---")
            nome = input("Nome e Cognome: ").strip()
            try:
                giorno = int(input("Giorno di nascita (1-31): "))
                mese = input("Mese di nascita: ").strip()
                anno = int(input("Anno di nascita: "))
                eta = int(input("Età: "))
                sesso = input("Sesso (M/F): ").strip()
                mail = input("Email: ").strip()

                rubrica.aggiungi(nome, giorno, mese, anno, eta, sesso, mail)
            except ValueError:
                print(
                    "Errore nell'inserimento dei dati numerici (giorno/anno/età)."
                )

        elif scelta == 'RIMUOVI':
            nome = input(
                "Inserisci il NOME del contatto da rimuovere: "
            ).strip()
            rubrica.rimuovi(nome)

        elif scelta == 'STAMPA':
            nome = input(
                "Inserisci il NOME del contatto da stampare: "
            ).strip()
            rubrica.stampa_contatto(nome)

        elif scelta == 'SALVA':
            #chiedo all'utente come salvare il file
            filepath = input(
                "Inserisci il nome del file su cui salvare (es. rubrica.json o rubrica.txt): "
            ).strip()
            rubrica.salva(filepath)


if __name__ == '__main__':
    main()