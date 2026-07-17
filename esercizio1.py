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




"""
def generatore(n):
    """Se il numero è intero e positivo applica la funzione is_pari, 

    altrimenti richiede un nuovo numero e riprova.
    """
    # 1. Controlliamo se n è un intero e se è maggiore di 0
    if type(n) == int and n > 0:
        return is_pari(n)

    # 2. Se il numero non è valido, entriamo qui
    else:
        print("Numero non accettabile, riprovare.")

        # Chiediamo un NUOVO input all'utente per sostituire quello vecchio
        nuovo_input = input("Inserisci un intero positivo: ")

        # Verifichiamo se il nuovo input è fatto di cifre prima di convertirlo
        if nuovo_input.isdigit():
            n_aggiornato = int(nuovo_input)
        else:
            n_aggiornato = 0  # Forza il fallimento al prossimo giro se inserisce lettere

        # Richiamiamo la funzione passando il NUOVO numero aggiornato
        return generatore(n_aggiornato)



    while True:
        try:
            valore = int(input("Inserisci un numero intero positivo: "))
            if valore > 0:
                return valore
            else:
                print("Errore: il numero deve essere maggiore di zero.")
        except ValueError:
            print("Errore: devi inserire un numero intero valido.")

while
"""


#main()

# 1. Chiediamo il numero all'utente
numero = generatore(int (input('Dammi un numero: ')))

result = generatore(numero)

print(result)

#RISOLUZIONE PUNTO 2





#risoluzione punto 5

def ricerca(lista) :
# che scorra la lista e stampi solo i numeri della sequenza che sono divisibili per 5. Se non ce ne sono, va stampato un messaggio dedicato.
    for i in lista:
        #i elemento lista punto 3
        if i%5 != 0 :
            
            print(i)

        else:
            print("non ci sono numeri divisibili per 5")
    #brake ???




