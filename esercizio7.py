'''
#
# File: esercizio5.py
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

#creo generatore 
def generatore_tabellina(numero):
    """generatore infinito di multipli di 'numero'"""
    n=0
    #loop infinito perchè non mi serve fermarmi a 10
    while(True):
        yield n*numero
        n = n +1
#####

num =int( input ('si scelga un numero') )
numero_intero = int(num)

print(f'Giocheremo con il numero (numero_intero)')
g = generatore_tabellina(numero_intero)
numero_tabellina = next(g)

#2 punto 

#
continua = False
while continua == True:
    #posso anche togliere ==True xchè è stessa cosa di verificare variabile

    guess = input(f'il numero affuale è (numero_tabellina). Qual'è il prossimo numero?')

    #controllo se fermare il gioco
    if guess == 'FINE':
        continua = False

    numero_tabellina = next(g)

    if numero_tabellina == guess :
        print('hai indovinato!')
    else:
        print('riprova')
  

print('esco dal gioco')


#aggiustare guess in int anche se giusto dice riprova  fine fare else perche riesce riprova




#tutto programma di gem riscrivi e confronta

"""
ome vengono soddisfatti i requisiti:
Il Generatore: La funzione generatore_tabellina(numero) usa yield. Non calcola l'intera tabellina
 subito, ma sputa fuori la coppia (moltiplicatore, risultato_atteso) una riga alla volta solo 
 quando il ciclo for principale lo richiede.

Loop Interattivo: Il ciclo while not tentativo_valido costringe il programma a rimanere sulla 
stessa domanda finché l'utente non indovina (o non decide di uscire), senza passare al calcolo 
successivo se si sbaglia.

Gestione Alfanumerici e Caratteri Speciali: La funzione pulisci_ed_esegui_input avvolge la 
conversione in un blocco try ... except ValueError. Se scrivi lettere (es. "abc"), parole a 
caso o simboli speciali (es. "$%&"), il programma cattura l'errore senza crashare, stampa un 
messaggio di avviso personalizzato e ti ripresenta la stessa domanda.

Numeri Decimali: L'input viene convertito in float. Questo significa che il programma è in grado 
di accettare risposte decimali, e permette persino di giocare con tabelline avanzate (ad esempio,
 se selezioni la tabellina del 7.5, il programma calcolerà correttamente operazioni come 
 2 x 7.5 = 15).

Chiusura Personalizzata: In qualsiasi momento (sia durante la scelta della tabellina sia
 durante le domande), digitando la stringa EXIT (o esci, o quit), il programma intercetta 
 il comando, stampa un messaggio di ringraziamento personalizzato e si chiude in modo pulito 
 con sys.exit(0).
"""


import sys


def generatore_tabellina(numero):
    """Generatore che calcola la tabellina del numero inserito da 0 a 10.

    Produce tuple nella forma: (moltiplicatore, risultato_atteso)
    """
    moltiplicatore = 0
    while moltiplicatore <= 10:
        risultato_atteso = moltiplicatore * numero
        yield moltiplicatore, risultato_atteso
        moltiplicatore += 1


def pulisci_ed_esegui_input(messaggio):
    """Gestisce l'input dell'utente convertendolo in float se possibile.

    Gestisce caratteri alfanumerici, speciali e stringhe di uscita.
    """
    stringa_input = input(messaggio).strip().upper()

    # Gestione della chiusura personalizzata
    if stringa_input in ["EXIT", "ESCI", "QUIT"]:
        print("\nHai scelto di uscire. Grazie per aver giocato! Alla prossima!")
        sys.exit(0)

    try:
        # Gestiamo sia numeri interi che decimali (es. 7.5 o 14.0)
        valore = float(stringa_input)
        # Se il float è equivalente a un intero (es. 14.0), lo convertiamo per estetica
        if valore.is_integer():
            return int(valore)
        return valore
    except ValueError:
        # Se l'input contiene lettere o caratteri speciali non numerici
        return None


def main():
    print("=" * 50)
    print("           IL GIOCO DELLE TABELLINE            ")
    print("=" * 50)
    print("Nota: Puoi digitare 'EXIT' in qualsiasi momento per uscire.\n")

    # 1. Scelta della tabellina iniziale con validazione dell'input
    while True:
        scelta = input("Quale tabellina vuoi ripassare? (Inserisci un numero): ")

        if scelta.strip().upper() in ["EXIT", "ESCI", "QUIT"]:
            print("Gioco chiuso prima di iniziare. Alla prossima!")
            return

        try:
            # Il gioco supporta tabelline di numeri interi o decimali (es. la tabellina del 2.5)
            numero_tabellina = float(scelta.strip())
            if numero_tabellina.is_integer():
                numero_tabellina = int(numero_tabellina)
            break
        except ValueError:
            print(
                "[ATTENZIONE] Input non valido (lettere o caratteri speciali rilevati)."
            )
            print("Per favore, inserisci un numero valido (es. 7 oppure 5.5).\n")

    print(f"\nPerfetto! Iniziamo con la tabellina del {numero_tabellina}.\n")

    # Inizializziamo il generatore
    tabellina = generatore_tabellina(numero_tabellina)

    # 2. Loop interattivo di gioco
    for moltiplicatore, valore_corretto in tabellina:
        tentativo_valido = False

        while not tentativo_valido:
            risposta_utente = pulisci_ed_esegui_input(
                f"Quanto fa {moltiplicatore} x {numero_tabellina}? -> "
            )

            # Se la risposta è None, significa che l'input era alfanumerico errato o carattere speciale
            if risposta_utente is None:
                print(
                    "[ERRORE] Hai inserito lettere o caratteri speciali non validi."
                )
                print("Inserisci un numero come risposta oppure digita 'EXIT'.\n")
                continue

            # Verifica del risultato
            if risposta_utente == valore_corretto:
                print("Correct! Incredibile! 🎉\n")
                tentativo_valido = True
            else:
                print(
                    f"Sbagliato! ❌ Riprova, pensa bene a quanto fa {moltiplicatore} x {numero_tabellina}."
                )

    print("=" * 50)
    print(
        f"Ottimo lavoro! Hai completato tutta la tabellina del {numero_tabellina}!"
    )
    print("=" * 50)


if __name__ == "__main__":
    main()