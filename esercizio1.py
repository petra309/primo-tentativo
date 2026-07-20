#ESERCIZIO 1
#introduzione

'''
#
# File: Programma.py
#
# Author: E.Romelli, D.Tavagnacco
#
# Date: 2026/03/03
#
# Version: 1.0
#
# Description: My First Project Program to print "Hello, World!".
#
'''



#RISOLUZIONE PUNTO 1
# consegna magari aggiungi


def is_pari(n) :
    """ Ritorna vero se "n" è pari, se no ritorna falso """
  
    risultato = False

    if n%2 == 0 :
        #% da resto divisione
        risultato = True

    return risultato
###

#RISOLUZIONE PUNTO 2
def generatore(n) :
    """ Se il numero è intero e positivo applica la funzione is_pari, richiedi numero se non"""

    while True:
        if type(int (n)) == int and n > 0 :
            return is_pari(n) 

        else :
            print("numero non accettabile, riprovare")
            False
            return generatore()


def genera_intero_positivo():
    """
    Chiede all'utente un numero intero positivo e lo restituisce.
    Continua a richiederlo se l'input non è valido (negativo, zero o non intero).
    """
    while True:
        try:
            valore = int(input("Inserisci un numero intero positivo (maggiore di 0): "))
            if valore > 0:
                return valore
            else:
                print("Errore: il numero deve essere maggiore di zero. Riprova.")
        except ValueError:
            print("Errore: devi inserire un numero intero valido. Riprova.")


# 1. Generiamo il numero positivo dall'input dell'utente
numero_utente = genera_intero_positivo()

# 2. Controlliamo se è pari o dispari
if is_pari(numero_utente):
    print(f"Il numero {numero_utente} è pari!")
else:
    print(f"Il numero {numero_utente} è dispari!")



#main()

# 1. Chiediamo il numero all'utente
numero = generatore(int (input('Dammi un numero: ')))

result = generatore(numero)

print(result)

#RISOLUZIONE PUNTO 2

# punto tree
"""
Scrivete una funzione che usando il numero scelto dall’utente, generi una lista seguendo 
questa regola: se il numero è pari, va diviso per 2; se è dispari, va moltiplicato per 3 
e aggiunto 1. Il processo va ripetuto finchè si arriva a 1 o la lista abbia piu’ di 100 
numeri
"""
def generazione_lista() :
#def genera_sequenza_collatz(n):
    """
    Genera una lista di numeri partendo da n seguendo la regola di Collatz.
    Si ferma quando arriva a 1 o quando la lista supera i 100 elementi.
    """
    # Inizializziamo la lista inserendo il numero di partenza scelto dall'utente
    lista = [n]
    
    # Il ciclo continua finché l'ultimo numero inserito non è 1 
    # E finché la lunghezza della lista è inferiore a 100
    while n != 1 and len(lista) < 100:
        if is_pari(n):
            n = n // 2  # Usiamo la divisione intera per mantenere il tipo int
        else:
            n = n * 3 + 1
        
        lista.append(n)
        
    return lista


#punto 4

"""
Scrivete una funzione analizza_sequenza(lista) che riceva la lista generata e restituisca
 tre valori: il valore massimo raggiunto, la lunghezza della sequenza e la somma di tutti 
 i numeri.
"""
def analizza_sequenza(lista) :
    # Se per qualche motivo la lista fosse vuota, gestiamo il caso per evitare errori
    #if not lista:
    #    return 0, 0, 0
        
    if lista == [0]
        return 0, 0, 0

    massimo = max(lista)
    lunghezza = len(lista)
    somma = sum(lista)
    
    return massimo, lunghezza, somma


#risoluzione punto 5

def ricerca(lista) :
# che scorra la lista e stampi solo i numeri della sequenza che sono divisibili per 5. Se non ce ne sono, va stampato un messaggio dedicato.
    for i in lista:
        #i elemento lista punto 3
        if i%5 == 0 :
            
            print(i)
            print(f"Numero divisibile per 5 trovato: {numero}")

        else:
            print("non ci sono numeri divisibili per 5")
    #brake ???




#risuluzione pumto 6 da rivedere bene tutto 

# --- 1. FUNZIONI DI SUPPORTO (PUNTI PRECEDENTI) ---

def is_pari(n):
    """Restituisce True se il numero è pari, False altrimenti."""
    return n % 2 == 0


def genera_intero_positivo(messaggio="Inserisci un numero intero positivo: "):
    """Chiede un intero positivo all'utente, continuando a oltranza in caso di input errato."""
    while True:
        try:
            valore = int(input(messaggio))
            if valore > 0:
                return valore
            print("Errore: il numero deve essere maggiore di zero.")
        except ValueError:
            print("Errore: inserisci un numero intero valido.")


def genera_sequenza_collatz(n):
    """Genera la sequenza applicando le regole fino a 1 o al limite di 100 elementi."""
    sequenza = [n]
    while n != 1 and len(sequenza) < 100:
        if is_pari(n):
            n = n // 2
        else:
            n = n * 3 + 1
        sequenza.append(n)
    return sequenza


def analizza_sequenza(lista):
    """Restituisce il valore massimo, la lunghezza e la somma degli elementi."""
    if not lista:
        return 0, 0, 0
    return max(lista), len(lista), sum(lista)


def ricerca(lista):
    """Stampa i numeri divisibili per 5 o un messaggio se non ce ne sono."""
    trovato = False
    for numero in lista:
        if numero % 5 == 0:
            print(f"   -> Numero divisibile per 5 trovato: {numero}")
            trovato = True
    if not trovato:
        print("   -> Nella sequenza non è presente alcun numero divisibile per 5.")


# --- 2. MAIN PROGRAM ---

def main():
    print("=== PROGRAMMA DI ANALISI DELLE SEQUENZE ===")
    
    # Chiediamo quanti numeri totali l'utente vuole testare
    quantita = genera_intero_positivo("Quanti numeri vuoi testare in totale? ")
    
    # Variabili per tenere traccia della sequenza più lunga nel riepilogo
    miglior_numero_iniziale = None
    lunghezza_massima = -1

    # Loop principale per elaborare ciascun numero
    for i in range(1, quantita + 1):
        print(f"\n--- ANALISI NUMERO {i} di {quantita} ---")
        
        # Generazione dell'input valido per il test corrente
        num_scelto = genera_intero_positivo(f"Inserisci il numero intero positivo n.{i}: ")
        
        # 1. Generazione della sequenza
        sequenza = genera_sequenza_collatz(num_scelto)
        print(f"Sequenza generata: {sequenza}")
        
        # 2. Analisi (Massimo, Lunghezza, Somma)
        val_massimo, lung_sequenza, somma_totale = analizza_sequenza(sequenza)
        print(f"Risultati analisi:")
        print(f"  - Lunghezza sequenza: {lung_sequenza}")
        print(f"  - Valore massimo raggiunto: {val_massimo}")
        print(f"  - Somma dei numeri: {somma_totale}")
        
        # 3. Ricerca divisibili per 5
        ricerca(sequenza)
        
        # 4. Aggiornamento delle statistiche per il riepilogo finale
        if lung_sequenza > lunghezza_massima:
            lunghezza_massima = lung_sequenza
            miglior_numero_iniziale = num_scelto

    # --- 3. RIEPILOGO FINALE ---
    print("\n================ RIEPILOGO ================")
    if miglior_numero_iniziale is not None:
        print(f"Il numero iniziale che ha generato la sequenza più lunga è stato: {miglior_numero_iniziale}")
        print(f"Ha raggiunto una lunghezza totale di {lunghezza_massima} elementi.")
    else:
        print("Nessun numero è stato analizzato.")
    print("===========================================")

# Questo costrutto assicura che il main parta solo se il file viene eseguito direttamente
if __name__ == "__main__":
    main()