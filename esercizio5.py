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





"""
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
    print(contatore_tempo/10)
    #contatorediviso 10

# chiamo la funzione principale 
main()
"""

#punto 1 
#loop per dare 10 soluzioni ma messo prima while solution <1
'''
for sol in range(10):
    main()
'''



import random
import time

def soluzione_ok(soluzione_posizioni):
    """Controlla tutte le posizioni della possibile soluzione
    'soluzione_posizioni' per verificare se ognuna delle posizioni
    (colonne dela permatazione) ogni colonna incrocia la diagonale
    di some qualcun altra posizione
    """
    for col in range(1, len(soluzione_posizioni)):
        # verifica se incrocia
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False

    # Se non è ritornato prima,
    # allora nessun incrocio trvato: posizioni della soluzione valide
    return True


def main():
    # inizializzo generatore permutazioni
    random_generator = random.Random()

    # preparo la "possibile soluzione" con posizoni da testare
    scacchiera = list(range(8))

    # conto le soluzioni trovate, inizio da 0
    solutions = 0

    # Lista per memorizzare i tempi di calcolo di ciascuna soluzione
    tempi_soluzioni = []

    # Misuro il tempo di partenza assoluto
    start_time = time.time()

    # loop finchè non trovo 10 soluzioni
    while solutions < 10:

        # permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera)

        # verifica se la permutazione casuale e' soluzione
        if soluzione_ok(scacchiera):
            # Calcolo il tempo impiegato per QUESTA specifica soluzione
            ora = time.time()
            tempo_singolo = ora - start_time
            tempi_soluzioni.append(tempo_singolo)

            # se la soluzione è buona, scrive
            print(
                f"Soluzione {solutions + 1}: {scacchiera} trovata in {tempo_singolo:.5f} secondi"
            )

            # incremento contatore soluzioni trovate (condizione stop loop)
            solutions = solutions + 1

            # reset timer per la ricerca della PROSSIMA soluzione
            start_time = time.time()

    print("-" * 60)
    # Calcolo la media matematica dei tempi registrati nella lista
    tempo_medio = sum(tempi_soluzioni) / len(tempi_soluzioni)

    print(f"TEMPO MEDIO NECESSARIO A TROVARE UNA SOLUZIONE:")
    print(f"-> {tempo_medio:.6f} secondi ({tempo_medio * 1000:.2f} millisecondi)")


# chiamo la funzione principale
if __name__ == "__main__":
    main()



#tempo medio


#punto 2

def main():
    # Inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # Preparo la "possibile soluzione" con posizioni da testare
    scacchiera = list(range(8)) 
    
    # Conto le soluzioni trovate, inizio da 0           
    solutions = 0                 
    
    # --- PARTE NUOVA: CONTATORI PER I TENTATIVI ---
    totale_tentativi_globali = 0
    tentativi_soluzione_corrente = 0

    print("Ricerca delle soluzioni e conteggio dei tentativi...\n")

    # Loop finché non trovo 10 soluzioni
    while solutions < 10:
        # Incrementiamo il contatore a ogni shuffle
        tentativi_soluzione_corrente += 1

        # Permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera) 

        # Verifica se la permutazione casuale è soluzione  
        if soluzione_ok(scacchiera): 
            solutions = solutions + 1      
            
            # Stampa del risultato con i tentativi della soluzione corrente
            print(f'Found solution {scacchiera} in {tentativi_soluzione_corrente} tentativi.')
            
            # Accumulo il conteggio parziale nel totale globale
            totale_tentativi_globali += tentativi_soluzione_corrente
            
            # Reset del contatore per la prossima ricerca
            tentativi_soluzione_corrente = 0

    # --- PARTE NUOVA: CALCOLO DELLA MEDIA FINALE ---
    print("-" * 50)
    media_tentativi = totale_tentativi_globali / 10
    print(f"Media tentativi per soluzione: {media_tentativi:.1f}")




#punto 3
#Alcune soluzioni possono essere ripetute: fate in modo che le soluzioni siano “uniche”
#ho foto di 14/4


def main():
    # Inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # Preparo la "possibile soluzione" con posizioni da testare
    scacchiera = list(range(8)) 
    
    # --- PARTE NUOVA: SET PER SOLUZIONI UNICHE E CONTATORI ---
    soluzioni_trovate = set()
    totale_tentativi_globali = 0
    tentativi_soluzione_corrente = 0

    print("Ricerca di 10 soluzioni UNICHE e conteggio dei tentativi...\n")

    # Il loop continua finché il set non contiene 10 elementi unici
    while len(soluzioni_trovate) < 10:
        # Incrementiamo il contatore a ogni shuffle
        tentativi_soluzione_corrente += 1

        # Permutazione casuale della soluzione
        random_generator.shuffle(scacchiera) 

        # Trasformiamo la scacchiera in tupla per poterla controllare/inserire nel set
        configurazione_attuale = tuple(scacchiera)

        # La soluzione è valida SOLO se passa il controllo E non è già stata trovata
        if configurazione_attuale not in soluzioni_trovate and soluzione_ok(scacchiera): 
            # Aggiungiamo la tupla al set delle soluzioni uniche
            soluzioni_trovate.add(configurazione_attuale)
            
            # Stampa del risultato
            print(f'Found unique solution {len(soluzioni_trovate)}: {scacchiera} in {tentativi_soluzione_corrente} tentativi.')
            
            # Accumulo nel totale globale e reset per la prossima ricerca
            totale_tentativi_globali += tentativi_soluzione_corrente
            tentativi_soluzione_corrente = 0

    # Calcolo della media finale basata sulle 10 soluzioni uniche
    print("-" * 50)
    media_tentativi = totale_tentativi_globali / 10
    print(f"Media tentativi per soluzione unica: {media_tentativi:.1f}")



#punto 4

def main():
    # Inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # Preparo la "possibile soluzione" con posizioni da testare
    scacchiera = list(range(8)) 
    
    # --- PARTE NUOVA: DIZIONARIO PER CONTARE LE RIPETIZIONI E CONTATORI ---
    frequenza_duplicati = {}
    totale_tentativi_globali = 0
    tentativi_soluzione_corrente = 0

    print("Ricerca di 10 soluzioni UNICHE e tracciamento dei duplicati...\n")

    # Il loop continua finché non abbiamo 10 chiavi uniche nel dizionario
    while len(frequenza_duplicati) < 10:
        tentativi_soluzione_corrente += 1
        random_generator.shuffle(scacchiera) 

        # Trasformiamo in tupla per l'uso come chiave del dizionario
        configurazione_attuale = tuple(scacchiera)

        # Se lo shuffle genera una configurazione che è una soluzione valida...
        if soluzione_ok(scacchiera):
            
            # CASO A: È una soluzione NUOVA (mai vista prima)
            if configurazione_attuale not in frequenza_duplicati:
                frequenza_duplicati[configurazione_attuale] = 1 # Inizializza il conteggio a 1 (la prima volta)
                
                print(f'Found unique solution {len(frequenza_duplicati)}: {scacchiera} in {tentativi_soluzione_corrente} tentativi.')
                
                totale_tentativi_globali += tentativi_soluzione_corrente
                tentativi_soluzione_corrente = 0
            
            # CASO B: È una soluzione RIPETUTA (era già nel dizionario)
            else:
                frequenza_duplicati[configurazione_attuale] += 1
                print(f'   [Duplicato] La soluzione {list(configurazione_attuale)} è comparsa di nuovo! (Vista in totale: {frequenza_duplicati[configurazione_attuale]} volte)')

    # --- PARTE NUOVA: RESOCONTO FINALE DEI DUPLICATI ---
    print("-" * 50)
    print("RESOCONTO FINALE DELLE RIPETIZIONI:")
    qualche_duplicato = False
    
    for i, (soluzione, conteggio) in enumerate(frequenza_duplicati.items(), 1):
        # Se il conteggio è maggiore di 1, significa che è stata ripetuta
        if conteggio > 1:
            qualche_duplicato = True
            print(f"Soluzione {i} {list(soluzione)} -> Ripetuta {conteggio - 1} volte extra (generata {conteggio} volte in totale)")
            
    if not qualche_duplicato:
        print("Nessuna delle 10 soluzioni si è ripetuta durante questa esecuzione (sei stato fortunato!).")
        
    print("-" * 50)
    media_tentativi = totale_tentativi_globali / 10
    print(f"Media tentativi per soluzione unica: {media_tentativi:.1f}")


#punto 5

Python
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


def main():
    # =========================================================================
    # CONFIGURAZIONE DIMENSIONE SCACCHIERA (N)
    # Modifica questo valore per cambiare la dimensione (es. 4, 6, 8, 10...)
    # =========================================================================
    N = 8

    random_generator = random.Random()

    # Genera la scacchiera dinamicamente in base a N
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

            # CASO A: Nuova soluzione
            if configurazione_attuale not in frequenza_duplicati:
                frequenza_duplicati[configurazione_attuale] = 1

                print(
                    f"Found unique solution {len(frequenza_duplicati)}: {scacchiera} in {tentativi_soluzione_corrente} tentativi."
                )

                totale_tentativi_globali += tentativi_soluzione_corrente
                tentativi_soluzione_corrente = 0

            # CASO B: Soluzione ripetuta
            else:
                frequenza_duplicati[configurazione_attuale] += 1
                print(
                    f"   [Duplicato] La soluzione {list(configurazione_attuale)} è comparsa di nuovo! (Vista: {frequenza_duplicati[configurazione_attuale]} volte)"
                )

    print("-" * 50)
    print("RESOCONTO FINALE DELLE RIPETIZIONI:")
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


if __name__ == "__main__":
    main()





#punto 6

import random
import sys
import time


def stessa_diagonale(x0, y0, x1, y1):
    return abs(y1 - y0) == abs(x1 - x0)


def incrocia_colonne(posizioni, col):
    for c in range(col):
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True
    return False


def soluzione_ok(soluzione_posizioni):
    for col in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, col):
            return False
    return True


def main():
    # MODIFICA QUESTO VALORE PER TESTARE IL LIMITE (PROVA 12, 13 E 14)
    N = 13

    random_generator = random.Random()
    scacchiera = list(range(N))
    tentativi = 0

    print(f"Tentativo di risoluzione per N = {N} con limite di 15 secondi...")

    start_time = time.time()

    while True:
        tentativi += 1

        # Controllo timeout
        elapsed_time = time.time() - start_time
        if elapsed_time > 15.0:
            print(
                f"\n[TIMEOUT] Tempo scaduto! Raggiunti 15 secondi dopo {tentativi} tentativi senza trovare soluzioni."
            )
            break

        random_generator.shuffle(scacchiera)

        if soluzione_ok(scacchiera):
            print(f"\n[SUCCESSO] Soluzione trovata per N = {N}!")
            print(f"Configurazione: {scacchiera}")
            print(f"Tempo impiegato: {elapsed_time:.3f} secondi")
            print(f"Tentativi necessari: {tentativi}")
            break


if __name__ == "__main__":
    main()

"""
La dimensione massima del lato $N$ per trovare una soluzione in meno di 15 secondi è 
$N = 12$ o $N = 13$ (a seconda della potenza di calcolo della CPU e della fortuna nei lanci).
"""

#punto 7

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


def ruota_180(soluzione):
    """Ruota la configurazione di 180 gradi."""
    N = len(soluzione)
    nuova = [0] * N
    for x in range(N):
        y = soluzione[x]
        nuova[N - 1 - x] = N - 1 - y
    return nuova


def ruota_270(soluzione):
    """Ruota la configurazione di 270 gradi in senso orario."""
    N = len(soluzione)
    nuova = [0] * N
    for x in range(N):
        y = soluzione[x]
        nuova[N - 1 - y] = x
    return nuova


def ottieni_rotazioni(soluzione):
    """Ritorna una lista contenente le 4 rotazioni (0, 90, 180, 270 gradi)

    sotto forma di tuple.
    """
    r0 = tuple(soluzione)
    r90 = tuple(ruota_90(soluzione))
    r180 = tuple(ruota_180(soluzione))
    r270 = tuple(ruota_270(soluzione))
    return [r0, r90, r180, r270]


def main():
    random_generator = random.Random()
    scacchiera = list(range(8))

    # Insieme che conterrà TUTTE le varianti (originarie e ruotate) per evitare ripetizioni
    tutte_le_simmetrie = set()

    # Contatore delle soluzioni fondamentali distinte trovate
    soluzioni_fondamentali = 0

    print(
        "Ricerca di 5 soluzioni uniche e generazione delle loro simmetrie...\n"
    )

    while soluzioni_fondamentali < 5:
        random_generator.shuffle(scacchiera)

        configurazione_attuale = tuple(scacchiera)

        # La soluzione è valida solo se non è un doppione geometrico di una già vista
        if (
            configurazione_attuale not in tutte_le_simmetrie
            and soluzione_ok(scacchiera)
        ):
            soluzioni_fondamentali += 1

            # Calcoliamo la famiglia completa delle 4 rotazioni
            rotazioni = ottieni_rotazioni(scacchiera)

            print(f"=== SOLUZIONE FONDAMENTALE {soluzioni_fondamentali} ===")
            print(f"  0°   (Originale): {list(rotazioni[0])}")
            print(f"  90°  (Orario):     {list(rotazioni[1])}")
            print(f"  180° (Simmetrica):  {list(rotazioni[2])}")
            print(f"  270° (Antiorario):  {list(rotazioni[3])}\n")

            # Aggiungiamo tutte e 4 le varianti al set di controllo
            for r in rotazioni:
                tutte_le_simmetrie.add(r)


if __name__ == "__main__":
    main()



