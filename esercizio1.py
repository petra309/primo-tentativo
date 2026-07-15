#ESERCIZIO 1
#introduzione

'''
Nome del programma: calcolatrice.py
Autore: Mario Rossi
Data: 23/07/2026
Versione: 1.0
Descrizione: Semplice script per eseguire le quattro operazioni base.
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
    """ Se il numero è intero e positivo applica la funzione is_pari"""

    if type(n) == int and n > 0 :
        is_pari(n) 

    else :
        print("numero non accettabile, riprovare")






#main()
numero = int( input('Dammi un numero: ') )
print(type(numero))
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




