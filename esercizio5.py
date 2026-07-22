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
# Description: Programma risolutivo dell'esercizio 5, lezione 7
#
'''

#riporto il file per esegiure l'esercizio
#
# File: Otto_regine.py
#
# Author: E.Romelli, D.Tavagnacco
#
# Date: 2026/04/14
#
# Version: 1.0
#
# Description: Example program to solve 8 queen-like problem 
#              using brute force + random approach
#

def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    # distanza lungo y
    dy = abs(y1 - y0)
    
    # distanza lungo x
    dx = abs(x1 - x0) 

    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy     


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):     
        # la coordinata X (la riga) è indice (c) 
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True  
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne        
    return False   


def soluzione_ok(soluzione_posizioni):
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni 
       (colonne dela permatazione) ogni colonna incrocia la diagonale
       di qualche altra posizione
    '''

    for col in range(1, len(soluzione_posizioni)):
        # verifica se incrocia
        #if incrocia_colonne(soluzione_posizioni, col) == True:
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False 

    # Se non è ritornato prima, 
    # allora nessun incrocio trvato: posizioni della soluzione valide 
    return True 


import random
import time 

def main():
    # inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # preparo la "possibile soluzione" con posizoni da testare
    scacchiera = list(range(8)) 
    
    # conto le soluzioni trovate, inizio da 0           
    solutions = 0                 
    
    # misuro il tempo di partenza per la ricerca della soluzione
    start_time = time.time()            
    
    # loop finchè non trovo una soluzione
    while solutions < 1:
    
        # permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera) 
        
        # verifica se la permutazione casuale e' soluzione  
        #if soluzione_ok(scacchiera) == True: 
        if soluzione_ok(scacchiera): 
            # se la soluzione è buona, scrive
            print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
            
            # incremento contatore soluzioni trovate (condizione stop loop)
            solutions += 1      
            
            # reset timer ricerca soluzione
            start_time = time.time()


# chiamo la funzione principale, ho bloccato per non ottenere 11 soluzioni
# main()


#RISOLUZIONE PUNTO 1
"""
Trovate 10 soluzioni per il gioco delle regine con il metodo delle permutazioni: quanto è il 
tempo medio necessario a trovare una soluzione?
"""

def main1():
    # inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # preparo la "possibile soluzione" con posizoni da testare
    scacchiera = list(range(8)) 
    
    # conto le soluzioni trovate, inizio da 0           
    solutions = 0                 
    
    # misuro il tempo di partenza per la ricerca della soluzione
    start_time = time.time()            
    
    # misuro partenza per media
    start_contatore_tempo = time.time()

    # loop finchè non trovo una soluzione
    while solutions < 10:
    
        # permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera) 

        # verifica se la permutazione casuale e' soluzione  
        #if soluzione_ok(scacchiera) == True: 
        if soluzione_ok(scacchiera): 
            # se la soluzione è buona, scrive
            print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
            
            # incremento contatore soluzioni trovate (condizione stop loop)
            solutions = solutions + 1      

            # reset timer ricerca soluzione
            start_time = time.time()

    #faccio media dei tempi
    contatore_tempo = time.time() - start_contatore_tempo
    print(f"Il tempo medio è {contatore_tempo/10}")
    #contatorediviso 10

# chiamo la funzione principale 
main1()


#Risoluzione punto 2
"""
Contate quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine
"""

def main2():
    # Inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # Preparo la "possibile soluzione" con posizioni da testare
    scacchiera = list(range(8)) 
    
    # Conto le soluzioni trovate, inizio da 0           
    solutions = 0                 
    
    #imposto conteggio tentativi
    totale_tentativi_globali = 0
    tentativi_soluzione_corrente = 0

    print("Ricerca delle soluzioni e conteggio dei tentativi...\n")

    #loop finché non trovo 10 soluzioni
    while solutions < 10:
        #incremento il contatore a ogni shuffle
        tentativi_soluzione_corrente += 1

        #permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera) 

        #verifico se la permutazione casuale è soluzione  
        if soluzione_ok(scacchiera): 
            solutions = solutions + 1      
            
            #stampo risultato con i tentativi della soluzione corrente
            print(f'Found solution {scacchiera} in {tentativi_soluzione_corrente} tentativi.')
            
            # Reset del contatore per la prossima ricerca
            tentativi_soluzione_corrente = 0

# chiamo la funzione principale 
main2()


#RISOLUZIOEN PUNTO 3
"""
Alcune soluzioni possono essere ripetute: fate in modo che le soluzioni siano “uniche”
"""

def main3():
    # Inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # Preparo la "possibile soluzione" con posizioni da testare
    scacchiera = list(range(8)) 
    
    #preparo set per soluzioni trovate
    soluzioni_trovate = set()

    print("Ricerca di 10 soluzioni UNICHE e conteggio dei tentativi...\n")

    #il loop continua finché il set non contiene 10 elementi unici
    while len(soluzioni_trovate) < 10:

        #permutazione casuale della soluzione
        random_generator.shuffle(scacchiera) 

        #trasformo la scacchiera in tupla per poterla controllare/inserire nel set
        configurazione_attuale = tuple(scacchiera)

        #soluzione è valida solo se passa il controllo e non è già stata trovata
        if configurazione_attuale not in soluzioni_trovate and soluzione_ok(scacchiera): 
            #aggiungmo la tupla al set delle soluzioni uniche
            soluzioni_trovate.add(configurazione_attuale)
            
            #stampo risultato
            print(f'Found unique solution {len(soluzioni_trovate)}: {scacchiera}')


#chiamo la funzione principale 
main3()


#RISOLUZIONE PUNTO 4
"""
Se ci sono soluzioni ripetute, contate quante volte ogni soluzione è ripetuta
"""

def main4():
    # Inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # Preparo la "possibile soluzione" con posizioni da testare
    scacchiera = list(range(8)) 
    
    #preparo variabili e dizionario per ripetizioni
    frequenza_duplicati = {}
    totale_tentativi_globali = 0
    tentativi_soluzione_corrente = 0

    print("Ricerca di 10 soluzioni UNICHE e tracciamento dei duplicati...\n")

    #il loop continua finché non abbiamo 10 chiavi uniche nel dizionario
    while len(frequenza_duplicati) < 10:
        tentativi_soluzione_corrente += 1
        random_generator.shuffle(scacchiera) 

        #trasformo in tupla per l'uso come chiave del dizionario
        configurazione_attuale = tuple(scacchiera)

        #se lo shuffle genera una configurazione che è una soluzione valida
        if soluzione_ok(scacchiera):
            
            #se è soluzione nuova
            if configurazione_attuale not in frequenza_duplicati:
                frequenza_duplicati[configurazione_attuale] = 1 # Inizializza il conteggio a 1 (la prima volta)
                
                print(f'Found unique solution {len(frequenza_duplicati)}: {scacchiera} in {tentativi_soluzione_corrente} tentativi.')
                
                totale_tentativi_globali += tentativi_soluzione_corrente
                tentativi_soluzione_corrente = 0
            
            #se è soluzione ripetuta (presente nel dizionario)
            else:
                frequenza_duplicati[configurazione_attuale] += 1
                print(f'   [Duplicato] La soluzione {list(configurazione_attuale)} è comparsa di nuovo! (Vista in totale: {frequenza_duplicati[configurazione_attuale]} volte)')

    #stampo resoconto dei duplicati
    print("-" * 50)
    print("Resoconto finale delle ripetizioni:")
    qualche_duplicato = False
    
    #se ci sono stati duplicati
    for i, (soluzione, conteggio) in enumerate(frequenza_duplicati.items(), 1):
        #se il conteggio è maggiore di 1, significa che è stata ripetuta
        if conteggio > 1:
            qualche_duplicato = True
            print(f"Soluzione {i} {list(soluzione)} -> Ripetuta {conteggio - 1} volte extra (generata {conteggio} volte in totale)")

    #se non ci sono stati duplicati  
    if not qualche_duplicato:
        print("Nessuna delle 10 soluzioni si è ripetuta durante questa esecuzione")
        
    print("-" * 50)
    media_tentativi = totale_tentativi_globali / 10
    print(f"Media tentativi per soluzione unica: {media_tentativi:.1f}")

#chiamo la funzione principale 
main4()


#RISOLUZIONE PUNTO 5
"""
Generalizzate il programma per risolvere una scacchiera di qualunque dimensione NxN
"""

import random

def stessa_diagonale(x0, y0, x1, y1):
    """Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale" """
    return abs(y1 - y0) == abs(x1 - x0)


def incrocia_colonne(posizioni, col):
    """Ritorna Vero se la colonna 'col' incrocia la diagonale di qualcuna

    delle posizioni delle regine precedenti
    """
    for c in range(col):
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True
    return False


def soluzione_ok(soluzione_posizioni):
    """Controlla tutte le posizioni della possibile soluzione"""
    for col in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, col):
            return False
    return True


def main5():
    #chiedo lato scacchiera all'utente
    N = int(input ("Che dimensione deve avere il lato della scacchiera?"))

    if N > 6 or N == 5:

        random_generator = random.Random()

        #genera la scacchiera dinamicamente in base a N
        scacchiera = list(range(N))

        frequenza_duplicati = {}
        totale_tentativi_globali = 0
        tentativi_soluzione_corrente = 0

        print(
            f"Ricerca di 10 soluzioni UNICHE per una scacchiera {N}x{N} e tracciamento duplicati...\n"
        )

        while len(frequenza_duplicati) < 10:
            tentativi_soluzione_corrente += 1
            random_generator.shuffle(scacchiera)

            configurazione_attuale = tuple(scacchiera)

            if soluzione_ok(scacchiera):

                #Nuova soluzione
                if configurazione_attuale not in frequenza_duplicati:
                    frequenza_duplicati[configurazione_attuale] = 1

                    print(
                        f"Found unique solution {len(frequenza_duplicati)}: {scacchiera} in {tentativi_soluzione_corrente} tentativi."
                    )

                    totale_tentativi_globali += tentativi_soluzione_corrente
                    tentativi_soluzione_corrente = 0

                #Soluzione ripetuta
                else:
                    frequenza_duplicati[configurazione_attuale] += 1
                    print(
                        f"   [Duplicato] La soluzione {list(configurazione_attuale)} è comparsa di nuovo! (Vista: {frequenza_duplicati[configurazione_attuale]} volte)"
                    )

        print("-" * 50)
        print("Resoconto finale delle ripetizioni:")
        qualche_duplicato = False

        for i, (soluzione, conteggio) in enumerate(frequenza_duplicati.items(), 1):
            if conteggio > 1:
                qualche_duplicato = True
                print(
                    f"Soluzione {i} {list(soluzione)} -> Ripetuta {conteggio - 1} volte extra"
                )

        if not qualche_duplicato:
            print("Nessuna soluzione si è ripetuta in questa esecuzione.")

        print("-" * 50)
        media_tentativi = totale_tentativi_globali / 10
        print(f"Media tentativi per soluzione unica: {media_tentativi:.1f}")

    #dimensione (N)Soluzioni Uniche solo se N diverso da 1, 2, 3, 4, 6
    else:
        print(f"Una schacchiera a lato {N} non ha 10 soluzioni")

if __name__ == "__main__":
    main5()


#RISOLUZIONE PUNTO 6
"""
Trovate quale è la scacchiera con lato N più grande possibile per cui si riesce a trovare 1 
soluzione in meno di 15s
"""

import random
import time


def stessa_diagonale(x0, y0, x1, y1):
    """Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale" """
    return abs(y1 - y0) == abs(x1 - x0)


def incrocia_colonne(posizioni, col):
    """Ritorna Vero se la colonna 'col' incrocia la diagonale di qualcuna
    delle posizioni delle regine precedenti
    """
    for c in range(col):
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True
    return False


def soluzione_ok(soluzione_posizioni):
    """Controlla tutte le posizioni della possibile soluzione"""
    for col in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, col):
            return False
    return True


def trova_soluzione_con_timeout(N, max_secondi=15.0):
    """Cerca 1 soluzione per una scacchiera NxN.
    Si interrompe se supera max_secondi. Ritorna una tupla: (trovata: bool,
    tempo_impiegato: float, tentativi: int)
    """
    scacchiera = list(range(N))
    tentativi = 0
    inizio = time.time()

    while True:
        tempo_trascorso = time.time() - inizio

        # Controllo timeout
        if tempo_trascorso > max_secondi:
            return False, tempo_trascorso, tentativi

        tentativi += 1
        random.shuffle(scacchiera)

        if soluzione_ok(scacchiera):
            return True, tempo_trascorso, tentativi


def main6():
    print(
        " Ricerca della dimensione N massima risolvibile entro 15 secondi \n"
    )

    #scacchiere N < 4 o N = 6 non sono un problema qui perché cerchiamo SOLO 1 soluzione (per N=4 bastano 2 sol. esistenti)
    N = 4
    ultimo_N_valido = None

    while True:
        # Per N=2 e N=3 non esistono soluzioni matematiche, le saltiamo
        if N in (2, 3):
            N += 1
            continue

        print(f"Testing N = {N}...", end=" ", flush=True)

        trovata, tempo, tentativi = trova_soluzione_con_timeout(
            N, max_secondi=15.0
        )

        if trovata:
            print(
                f"✓ SOLUZIONE TROVATA in {tempo:.2f}s ({tentativi:,} tentativi)"
            )
            ultimo_N_valido = N
            N += 1
        else:
            print(
                f"✗ TIMEOUT (> 15.0s) dopo {tentativi:,} tentativi effettuati."
            )
            break

    print("\n" + "=" * 50)
    if ultimo_N_valido:
        print(
            f"RISULTATO FINALE: La dimensione massima N per cui si trova 1 soluzione in meno di 15s è: N = {ultimo_N_valido}"
        )
    else:
        print("Nessuna dimensione testata è riuscita a completarsi entro 15s.")
    print("=" * 50)

if __name__ == "__main__":
    main6()


#RISOLUZIONE PUNTO 7
"""
Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. 
Scrivete delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano 
le 4 soluzioni simmetriche per rotazione. Trovate 5 soluzioni “uniche” e le rispettive 
soluzioni simmetriche per rotazione per una scacchiera 8x8
"""

#simmetria rotazione 90°
def ruota_90(soluzione):
    """Ruota la configurazione di 90 gradi in senso orario."""

    N = len(soluzione)
    nuova = [0] * N
    for x in range(N):
        y = soluzione[x]
        # La vecchia riga (y) diventa la nuova colonna
        # La vecchia colonna (x) determina la nuova riga dal basso
        nuova[y] = N - 1 - x
    return nuova

#simmetria rotazione 180°
def ruota_180(soluzione):
    """Ruota la configurazione di 180 gradi."""

    N = len(soluzione)
    nuova = [0] * N
    for x in range(N):
        y = soluzione[x]
        nuova[N - 1 - x] = N - 1 - y
    return nuova

#simmetria rotazione 270°
def ruota_270(soluzione):
    """Ruota la configurazione di 270 gradi in senso orario."""

    N = len(soluzione)
    nuova = [0] * N
    for x in range(N):
        y = soluzione[x]
        nuova[N - 1 - y] = x
    return nuova

#stampa le 4 simmetrie di una soluzione
def ottieni_rotazioni(soluzione):
    """Ritorna una lista contenente le 4 rotazioni (0, 90, 180, 270 gradi)
    sotto forma di tuple.
    """
    r0 = tuple(soluzione)
    r90 = tuple(ruota_90(soluzione))
    r180 = tuple(ruota_180(soluzione))
    r270 = tuple(ruota_270(soluzione))
    return [r0, r90, r180, r270]


def main7():
    random_generator = random.Random()
    scacchiera = list(range(8))

    #set di tutte le varianti (originarie e ruotate) per evitare ripetizioni
    tutte_le_simmetrie = set()

    #contatore delle soluzioni fondamentali distinte trovate
    soluzioni_fondamentali = 0

    print(
        "Ricerca di 5 soluzioni uniche e generazione delle loro simmetrie...\n"
    )

    #ciclo finchè non si ha 5 soluzioni
    while soluzioni_fondamentali < 5:
        random_generator.shuffle(scacchiera)

        configurazione_attuale = tuple(scacchiera)

        #soluzione valida solo se non è un doppione geometrico di una già vista
        if (
            configurazione_attuale not in tutte_le_simmetrie
            and soluzione_ok(scacchiera)
        ):
            soluzioni_fondamentali += 1

            #calcolo la famiglia completa delle 4 rotazioni
            rotazioni = ottieni_rotazioni(scacchiera)

            print(f"=== SOLUZIONE FONDAMENTALE {soluzioni_fondamentali} ===")
            print(f"  0°   (Originale): {list(rotazioni[0])}")
            print(f"  90°  (Orario):     {list(rotazioni[1])}")
            print(f"  180° (Simmetrica):  {list(rotazioni[2])}")
            print(f"  270° (Antiorario):  {list(rotazioni[3])}\n")

            #aggiungo tutte e 4 le varianti al set di controllo
            for r in rotazioni:
                tutte_le_simmetrie.add(r)


if __name__ == "__main__":
    main7()