'''
#
# File: esercizio7.py
#
# Author: Petra Zurini
#
# Date: 20/07/2026
#
# Version: 1.0
#
# Description: Programma risolutivo dell'esercizio 7, lezione 11
#
'''

#RISOLUZIONE PUNTO 1
"""
contenere un generatore che, dato un numero (ad esempio 7), generi la tabellina corrispondente
al numero selezionato (0x7 = 0; 1x7 = 7; 2x7 = 14; ecc…);
"""

import sys

#creo generatore
def generatore_tabellina(numero):
    """Generatore che restituisce una tupla (fattore, risultato)
    Es: per numero 7 produce (0, 0), (1, 7), (2, 14), ...
    """
    for i in range(11):
        yield i, i * numero


#RISOLUZIONE PUNTO 3, 4, 5
"""
gestire tutti i caratteri alfanumerici (non deve “rompersi” se l’utente sceglie una lettera)

gestire caretteri speciali o numeri decimali

gestire la chiusura del gioco in modo personalizzato.
"""

def leggi_input_valido(messaggio_prompt):
    """Gestisce l'input dell'utente proteggendo il programma da:

    - Lettere e caratteri alfanumerici
    - Simboli speciali e numeri decimali (es. 3.5 o 7,2)
    - Comandi di chiusura personalizzati ('exit', 'esci')
    """
    while True:
        scelta = input(messaggio_prompt).strip().lower()

        #Gestione della chiusura personalizzata, punto 5
        if scelta in ['q', 'exit', 'esci']:
            return 'ESCI'

        try:
            valore = int(scelta)
            if valore < 0:
                print("Inserisci un numero intero positivo!")
                continue
            return valore
        except ValueError:
            print(
                "Input non valido! Inserisci solo numeri interi (no lettere, decimali o simboli)."
            )


#RISOLUZIONE PUNTO 2
"""
contenere un loop che chieda in modo interrattivo all’utente di indovinare il valore corrente
nella tabellina selezionata
"""

def gioco_tabelline(numero):
    """Gestisce la partita per la tabellina del numero selezionato."""
    tabellina = generatore_tabellina(numero)

    print(f"\nInizio gioco: Tabellina del {numero} ")
    print("(Digita 'esci' o 'exit' in qualsiasi momento per uscire)\n")

    for fattore, risultato_corretto in tabellina:
        mentre_indovina = True

        while mentre_indovina:
            prompt = f"Quanto fa {fattore} x {numero}? "
            risposta = leggi_input_valido(prompt)

            #chiusura durante la partita
            if risposta == "ESCI":
                return False

            if risposta == risultato_corretto:
                print("Risposta esatta\n")
                mentre_indovina = False
            else:
                print(
                    f"Risposta sbagliata. Riprova a calcolare {fattore} x {numero}."
                )

    print(
        f"Complimenti! Hai completato tutta la tabellina del {numero}!\n"
    )
    return True


#RISOLUZIONE PROGRAMMA

#unisco tutte le funzioni nel programma intero
def main():
    print("=" * 45)
    print(" BENVENUTO AL GIOCO DELLE TABELLINE!")
    print("=" * 45)

    giocando = True
    while giocando:
        print("\nQuale tabellina vuoi ripassare?")
        scelta_numero = leggi_input_valido(
            "Inserisci un numero (o 'esci' per chiudere): "
        )

        if scelta_numero == "ESCI":
            giocando = False
        else:
            #avvia la sessione di gioco con la tabellina scelta
            continua = gioco_tabelline(scelta_numero)
            if not continua:
                giocando = False

    # Messaggio di chiusura personalizzato
    print("\n" + "=" * 45)
    print("Chiusura del gioco")
    print("=" * 45)


if __name__ == "__main__":
    main()