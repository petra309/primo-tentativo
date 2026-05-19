#if else
#try exept

#intestazione ricorda
#Esercizio 8
#Autore .
#Data:

# non lascia inserire parola inyera
#lista parole leggere con funzione da file json
# def 
import random

def gioco_impiccato():
    '''Dovumentazione su cosa fa la funzione'''

    # Lista di parole possibili per il gioco
    lista_parole = ["python", "programmazione", "computer", "sviluppatore", "algoritmo", "funzione"]
    
    # Scelta casuale della parola segreta
    parola_segreta = random.choice(lista_parole).lower()
    #lower anche per es vecchio della poesia
    
    # Set per tenere traccia delle lettere indovinate e di quelle tentate
    lettere_indovinate = set()
    lettere_tentate = set()
    
    # Numero di tentativi massimi (errori consentiti)
    tentativi_rimasti = 6
    
    print("--- Benvenuto al Gioco dell'Impiccato! ---")
    
    # Loop principale del gioco
    while tentativi_rimasti > 0:
        # Mostra lo stato attuale della parola (es. p _ t h _ n)
        parola_visualizzata = []
        for lettera in parola_segreta:
            if lettera in lettere_indovinate:
                parola_visualizzata.append(lettera)
            else:
                parola_visualizzata.append("_")
        
        print("\nParola da indovinare: " + " ".join(parola_visualizzata))
        print(f"Tentativi rimasti: {tentativi_rimasti}")
        if lettere_tentate:
            print(f"Lettere già provate: {', '.join(sorted(lettere_tentate))}")
            
        # Controlla se il giocatore ha indovinato tutte le lettere
        if "_" not in parola_visualizzata:
            print(f"\n🎉 Complimenti! Hai indovinato la parola: '{parola_segreta}'!")
            break
            
        # Input del giocatore
        tentativo = input("Inserisci una lettera: ").lower().strip()
        
        # Validazione dell'input
        if len(tentativo) != 1 or not tentativo.isalpha():
            print("❌ Input non valido. Inserisci una singola lettera.")
            continue
            
        if tentativo in lettere_tentate:
            print("⚠️ Hai già provato questa lettera. Scegline un'altra.")
            continue
            
        # Aggiunge la lettera all'elenco dei tentativi effettuati
        lettere_tentate.add(tentativo)
        
        # Verifica se la lettera è nella parola
        if tentativo in parola_segreta:
            print(f"👍 Ottimo! La lettera '{tentativo}' è presente.")
            lettere_indovinate.add(tentativo)
        else:
            print(f"👎 Peccato! La lettera '{tentativo}' non è presente.")
            tentativi_rimasti -= 1
            
    else:
        # Questo blocco viene eseguito solo se il ciclo while termina perché i tentativi sono finiti
        print(f"\n💥 Game Over! Hai esaurito i tentativi. La parola era: '{parola_segreta}'.")


# Per avviare il gioco, basta chiamare la funzione:
gioco_impiccato()


'''
try:
    _ = lettere_indovinate.index (tentativo)
exept Valueerror:
    pass
else:
    print(f"Hai già provato la lettera '(tantativo)'.")
    continue



'''
#eafp

