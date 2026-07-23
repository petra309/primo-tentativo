'''
#
# File: esercizio1.py
#
# Author: Petra Zurini
#
# Date: 20/07/2026
#
# Version: 1.0
#
# Description: Programma risolutivo dell'esercizio 1, lezione 3
#
'''

#RISOLUZIONE PUNTO 1
"""
Scrivete una funzione di controllo, is_pari(n), che accetti come parametro un numero intero e 
restituisca True se il numero è pari, False altrimenti.
"""

def is_pari(n) :
    """ Ritorna vero se "n" è pari, falso se "n" è dispari """
  
    risultato = False

    #con divisione per due controllo se è pari
    if n%2 == 0 :
        #% da resto divisione
        risultato = True
    
    return risultato
    

#RISOLUZIONE PUNTO 2
"""
Create una funzione di generazione che chieda all’utente un numero intero positivo e lo 
restituisca come risultato della funzione. Se l’utente inserisce un numero non valido 
(es. negativo o zero), il ciclo deve continuare a richiederlo finché l’input non è corretto.
"""

def generatore(messaggio = "Quanti numeri vuoi testare in totale?") :
    """ Se il numero è intero e positivo applica la funzione is_pari, richiedi numero se non"""

    #ciclo finchè accettato il numero in input
    while True:
        stringa_input = input("Inserisci un numero intero positivo: ")
        
        # con .isdigit controllo che sia int, con > 0 che sia positivo
        if stringa_input.isdigit() and int(stringa_input) > 0:
            return int(stringa_input)
        
        else :
            print("Errore: devi inserire un numero intero positivo valido")

"""
#se voglio solo generare un numero e controllare se è pari o dispari

#genero numero dall'input 
numero_utente = generatore()

#controlliamo se è pari o dispari
if is_pari(numero_utente):
    print(f"Il numero {numero_utente} è pari")
else:
    print(f"Il numero {numero_utente} è dispari")
"""

#RISOLUZIONE PUNTO 3
"""
Scrivete una funzione che usando il numero scelto dall’utente, generi una lista seguendo 
questa regola: se il numero è pari, va diviso per 2; se è dispari, va moltiplicato per 3 e 
aggiunto 1. Il processo va ripetuto finchè si arriva a 1 o la lista abbia piu’ di 100 numeri
"""

def generazione_lista(n) :
    """ Genera una lista partendo dall'input dell'utente, se input pari divido per due, se dispari
    moltiplico per 3 e aggiungo 1 finchè non ottengo 1 o la lista supera i 100 elementi """

    #creo lista con input dall'utente
    lista = [n]
    
    #ciclo finché ottengo 1 lunghezza della lista è inferiore a 100
    while n != 1 and len(lista) < 100:
        #se pari
        if is_pari(n):
            n = n // 2  # Usiamo la divisione intera per mantenere il tipo int
        #se dispari
        else:
            n = n * 3 + 1
        
        lista.append(n)
        
    return lista


#RISOLUZIONE PUNTO 4
"""
Scrivete una funzione analizza_sequenza(lista) che riceva la lista generata e restituisca tre 
valori: il valore massimo raggiunto, la lunghezza della sequenza e la somma di tutti i numeri.
"""

def analizza_sequenza(lista) :
    """ Restituisce valore massimo, lunghezza sequenza e somma di tutti i numeri della lista"""
     
    #caso lista vuota 
    if not lista:
        return 0, 0, 0

    massimo = max(lista)
    lunghezza = len(lista)
    somma = sum(lista)
    
    return massimo, lunghezza, somma


#RISOLUZIONE PUNTO 5
"""
Scrivete una funzione ricerca(lista) che scorra la lista e stampi solo i numeri della sequenza 
che sono divisibili per 5. Se non ce ne sono, va stampato un messaggio dedicato.
"""

def ricerca(lista) :
    """ Stampa numeri della lista divisibili per 5 """

    #scorro la lista e stampo solo i numeri divisibili per 5
    for i in lista:
        if i%5 == 0 :
            
            print(f"Numero divisibile per 5 trovato: {i}")

    #caso nessun numero divisibile per 5
    print("non ci sono numeri divisibili per 5")
    

#RISOLUZIONE PUNTO 6
"""
Unite il tutto in un main program che chieda all’inizio all’utente quanti numeri vuole testare.
Usate uno o più loop per chiedere all’utente i numeri da analizzare e per eseguire i punti 
precedenti per ogni numero. Alla fine stampate un riepilogo che mostri quale numero iniziale 
ha generato la sequenza più lunga.
""" 

def main():
    """ Con input utente eseguo tutte le altre funzioni. Trovo che numero ha generato la sequenza più 
    lunga """

    print("=== Inizio main program ===")
    
    #richiedo quanti numeri l'utente vuole testare
    quantità = generatore("Quanti numeri vuoi testare in totale?")
    
    #variabili per tenere traccia della sequenza più lunga nel riepilogo
    miglior_numero_iniziale = None
    lunghezza_massima = -1

    #ciclo principale per analizzare ogni numero
    for i in range(1, quantità + 1):
        print(f"\n--- Analizzo il numero {i} di {quantità} ---")
        
        #chiedo input valido
        numero_scelto = generatore(f"Inserisci il numero intero positivo n.{i}: ")
        
        #genero la sequenza
        sequenza = generazione_lista(numero_scelto)
        print(f"Sequenza generata: {sequenza}")
        
        #analizzo la sequenza (massimo, lunghezza, somma)
        valore_massimo, lunghezza_sequenza, somma_totale = analizza_sequenza(sequenza)
        print(f"Risultati analisi:")
        print(f"  - Lunghezza sequenza: {lunghezza_sequenza}")
        print(f"  - Valore massimo raggiunto: {valore_massimo}")
        print(f"  - Somma dei numeri: {somma_totale}")
        
        #ricerco i numeri divisibili per 5
        ricerca(sequenza)
        
        #aggiorno le statistiche per il riepilogo finale
        if lunghezza_sequenza > lunghezza_massima:
            lunghezza_massima = lunghezza_sequenza
            miglior_numero_iniziale = numero_scelto

    
    print("\n===  Riepilogo  ===")
    
    #indico che numero ha generato la sequenza più lunga
    if miglior_numero_iniziale is not None:
        print(f"Il numero iniziale che ha generato la sequenza più lunga è stato: {miglior_numero_iniziale}")
        print(f"Ha raggiunto una lunghezza totale di {lunghezza_massima} elementi.")
    else:
        print("Nessun numero è stato analizzato.")

#eseguo main()
main()