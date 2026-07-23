'''
#
# File: progetto_esame.py
#
# Author: Petra Zurini
#
# Date: 20/07/2026
#
# Version: 1.0
#
# Description: Programma di simulazione outfit per occasioni eleganti, casual, sportive in
               estate/primavera e inverno/autunno
#
'''

# importo modulo per generazione casuale
import random

# funzione per chiedere all'utente un'opzione tra quelle valide
def chiedi_opzione(messaggio, opzioni_valide):
    while True:

        #l'input viene pulito e messo in minuscolo
        risposta = input(messaggio).strip().lower()
        #se la risposta scelta è accettata
        if risposta in opzioni_valide:
            return risposta
        #se la risposta scelta non è accettata
        print("SCELTA NON VALIDA. RIPROVA.\n")

# funzione per gestire la conferma generica (outfit o colori)
def conferma_scelta(messaggio_domanda):
    while True:

        # avviso l'utente sui comandi per continuare o fermarsi
        scelta = input(messaggio_domanda).strip().lower()
        #se l'utente sceglie affermativamente
        if scelta in ['y', 'yes', 'si']:
            return True
        #se l'utente sceglie negativamente
        elif scelta in ['n', 'no']:
            return False
        #se l'input non è accettato
        else:
            print("RISPOSTA NON VALIDA. SCRIVI 'SI' PER ACCETTARE O 'NO' PER CONTINUARE.")

# avvio del programma principale
def genera_outfit():
    # inizio del programma
    print("=== BENVENUTO NEL GENERATORE DI OUTFIT CASUALE ===\n")
    
    # richiesta della stagione
    stagione = chiedi_opzione("SELEZIONA LA STAGIONE (1: PRIMAVERA/ESTATE, 2: INVERNO/AUTUNNO): ", ['1', '2', 'primavera/estate', 'inverno/autunno'])
    
    # imposto parametro iniziale
    include_felpa = False
    # gestione del ramo primavera/estate per includere volendo una felpa
    if stagione in ['1', 'primavera/estate']:
        ans = chiedi_opzione("VUOI INCLUDERE ANCHE UNA FELPA/MAGLIA A MANICA LUNGA? (SI/NO): ", ['si', 'no', 's', 'n', 'y', 'yes'])
        if ans in ['si', 's', 'y', 'yes']:
            include_felpa = True

    # richiesta dell'occasione, casual, elegante o sportiva
    occasione = chiedi_opzione("SELEZIONA L'OCCASIONE (CASUAL, ELEGANTE, SPORTIVA): ", ['casual', 'elegante', 'sportiva'])

    # imposto 
    outfit_scelto = []
    approvato_outfit = False

    # ciclo che continua a proporre outfit finche' l'utente non approva uno
    while not approvato_outfit:
        outfit_scelto = []

        # logica per primavera / estate
        if stagione in ['1', 'primavera/estate']:

            # logica per occasione casual
            if occasione == 'casual':
                # se sceglie vestitino, genera solo quello
                opzioni_sopra = ['maglietta', 'top', 'canottiera', 'vestitino']
                # generazione casuale di un pezzo sopra
                sopra = random.choice(opzioni_sopra)
                
                #se sceglie vestitino non vienen generato pezzo sotto
                if sopra == 'vestitino':
                    outfit_scelto.append('vestitino')
                else:
                    outfit_scelto.append(sopra)
                    #generazione casuale di un pezzo sotto
                    sotto = random.choice(['pantaloni lunghi', 'pantaloncini corti', 'gonna lunga', 'gonna corta'])
                    outfit_scelto.append(sotto)

                # aggiunta eventuale della felpa
                if include_felpa:
                    #generazione casuale di una felpa
                    strato_extra = random.choice(['felpa', 'maglioncino', 'maglia manica lunga'])
                    outfit_scelto.append(strato_extra)

            # logica per occasione sportiva
            elif occasione == 'sportiva':
                #generazione casuale di un pezzo sopra
                sopra = random.choice(['maglietta', 'canottiera'])
                #generazione casuale di un pezzo sotto
                sotto = random.choice(['pantaloni lunghi', 'pantaloni corti'])
                outfit_scelto.extend([sopra, sotto])

                # aggiunta eventuale della felpa
                if include_felpa:
                    #generazione casuale di una felpa
                    strato_extra = random.choice(['felpa', 'maglia manica lunga'])
                    outfit_scelto.append(strato_extra)

            # logica per occasione elegante
            elif occasione == 'elegante':
                # se sceglie vestitino o vestito, genera solo quello
                opzioni_sopra = ['maglietta', 'top', 'vestitino', 'vestito']
                # generazione casuale di un pezzo sopra
                sopra = random.choice(opzioni_sopra)

                #se sceglie vestitino non vienen generato pezzo sotto
                if sopra in ['vestitino', 'vestito']:
                    outfit_scelto.append(sopra)
                else:
                    outfit_scelto.append(sopra)
                    # generazione casuale di un pezzo sotto
                    sotto = random.choice(['pantaloni lunghi', 'pantaloncini corti', 'gonna lunga', 'gonna corta'])
                    outfit_scelto.append(sotto)

                # aggiunta eventuale della felpa
                if include_felpa:
                    #generazione casuale di una felpa
                    strato_extra = random.choice(['maglioncino', 'maglia manica lunga', 'scaldacuore'])
                    outfit_scelto.append(strato_extra)

        # logica per inverno / autunno
        else:
            # logica per occasione casual
            if occasione == 'casual':
                # generazione casuale di un pezzo sopra e sotto e copriabito
                sopra = random.choice(['felpa con cappuccio', 'felpa senza cappuccio', 'maglia con il collo alto'])
                sotto = random.choice(['pantaloni', 'jeans', 'leggins'])
                giacca = random.choice(['cappotto', 'giubotto'])
                outfit_scelto.extend([sopra, sotto, giacca])

            # logica per occasione sportiva
            elif occasione == 'sportiva':
                # generazione casuale di un pezzo sopra e sotto
                sopra = random.choice(['felpa con cappuccio', 'felpa senza cappuccio'])
                sotto = random.choice(['pantaloni', 'leggins', 'tuta'])
                # in questo caso e' sempre giubotto
                outfit_scelto.extend([sopra, sotto, 'giubotto'])

            # logica per occasione elegante
            elif occasione == 'elegante':
                # generazione casuale di un pezzo sopra e sotto 
                sopra = random.choice(['maglia con il collo alto', 'maglia girocollo', 'gilet'])
                sotto = random.choice(['pantaloni', 'jeans'])
                # in questo caso e' sempre cappotto
                outfit_scelto.extend([sopra, sotto, 'cappotto'])

        # stampa dell'outfit generato 
        print("\n----------------------------------------")
        print("OUTFIT PROPOSTO:")
        for capo in outfit_scelto:
            print(f"- {capo.upper()}")
        print("----------------------------------------")

        # verifica se l'utente accetta l'outfit propostogli
        approvato_outfit = conferma_scelta("\nTI PIACE QUESTO OUTFIT? DIGITA 'Y', 'YES' O 'SI' PER ACCETTARE, OPPURE 'N' O 'NO' PER CONTINUARE: ")

    # gestione e scelta dei colori dopo l'approvazione dell'outfit
    colori_disponibili = ['nero', 'bianco', 'giallo', 'colorato']
    
    # controlla se tra i capi scelti sono presenti i jeans, in caso aggiungi colore tra opzioni
    if 'jeans' in outfit_scelto:
        colori_disponibili.append('color jeans')

    # imposto
    approvato_colori = False
    colori_abbinati = []

    # ciclo di selezione e approvazione dell'abbinamento colori
    while not approvato_colori:
        # estrazione casuale di 2 o 3 colori con possibile ripetizione (random.choices)
        num_colori = random.choice([2, 3])
        colori_abbinati = random.choices(colori_disponibili, k=num_colori)

        print("\n----------------------------------------")
        print("ABBINAMENTO COLORI PROPOSTO:")
        print(", ".join(colori_abbinati).upper())
        print("----------------------------------------")

        # verifica se l'utente accetta l'abbinamento colori propostogli
        approvato_colori = conferma_scelta("\nTI PIACE QUESTO ABBINAMENTO DI COLORI? DIGITA 'Y', 'YES' O 'SI' PER ACCETTARE, OPPURE 'N' O 'NO' PER CONTINUARE: ")

    print("\n========================================")
    print("OUTFIT E COLORI APPROVATI CON SUCCESSO!")

    # messaggio finale sui gioielli per le occasioni casual ed elegante
    if occasione in ['casual', 'elegante']:
        print("\nRICORDATI DI METTERTI I GIOIELLI!")
    print("========================================\n")

# esecuzione dello script
if __name__ == "__main__":
    genera_outfit()