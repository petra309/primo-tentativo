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




#####programma di gem completo
"""
Ecco le due versioni del gioco dell'impiccato richieste. Per entrambe le versioni assumiamo 
l'esistenza di un file chiamato parole.json strutturato in questo modo:

JSON
["python", "programmazione", "funzione", "dizionario", "scacchiera"]
Prima di passare al codice, ricordiamo brevemente la differenza concettuale tra i due approcci:

LBYL (Look Before You Leap): Si controllano esplicitamente tutte le condizioni (con if, 
os.path.exists, controlli di tipo o lunghezza) prima di effettuare un'operazione che potrebbe 
fallire.

EAFP (Easier to Ask for Forgiveness than Permission): Si tenta direttamente di eseguire 
l'operazione all'interno di un blocco try e si catturano le eccezioni specifiche (except) 
se qualcosa va storto. È l'approccio più idiomatico in Python.

1. Versione LBYL (Look Before You Leap)
In questa versione ogni potenziale errore (file mancante, JSON corrotto, input vuoto o non alfabetico) viene prevenuto usando verifiche preventive con strutture condizionali if.
"""

Python
import json
import os
import random


def gioca_impiccato_lbyl():
    print("=== IL GIOCO DELL'IMPICCATO (Approccio LBYL) ===")
    nome_file = "parole.json"

    # Controllo preventivo: il file esiste?
    if not os.path.exists(nome_file):
        print(f"Errore: Il file '{nome_file}' non esiste sul disco.")
        return

    # Controllo preventivo: il file è vuoto?
    if os.path.getsize(nome_file) == 0:
        print(f"Errore: Il file '{nome_file}' è vuoto.")
        return

    with open(nome_file, "r", encoding="utf-8") as f:
        contenuto = f.read()

    # Per verificare se è un JSON valido in modo LBYL puro senza try-except,
    # dovremmo scrivere un intero parser. Python non offre un metodo integrato "is_json()".
    # Utilizziamo eccezionalmente json.loads dopo aver verificato la struttura base.
    # Nota: se il JSON è strutturalmente invalido, json.loads solleverà comunque un errore,
    # evidenziando perché l'approccio LBYL puro con il parsing dei file sia complesso in Python.
    parole = json.loads(contenuto)

    if not isinstance(parole, list) or len(parole) == 0:
        print("Errore: Il file JSON non contiene una lista valida di parole.")
        return

    # Scelta casuale della parola e inizializzazione variabili
    parola_segreta = random.choice(parole).lower()
    lettere_indovinate = set()
    lettere_errate = set()
    tentativi_rimasti = 6

    while tentativi_rimasti > 0:
        # Visualizzazione dello stato attuale della parola
        visualizzazione = ""
        for lettera in parola_segreta:
            if lettera in lettere_indovinate:
                visualizzazione += lettera + " "
            else:
                visualizzazione += "_ "

        print(f"\nParola: {visualizzazione.strip()}")
        print(f"Tentativi rimasti: {tentativi_rimasti}")
        print(f"Lettere errate: {', '.join(sorted(lettere_errate))}")

        # Controllo vittoria
        vittoria = True
        for lettera in parola_segreta:
            if lettera not in lettere_indovinate:
                vittoria = False

        if vittoria:
            print(
                f"\n🎉 Complimenti! Hai indovinato la parola: '{parola_segreta}'!"
            )
            return

        # Richiesta input all'utente
        input_utente = (
            input("Inserisci una lettera o indovina l'intera parola: ")
            .strip()
            .lower()
        )

        # Controlli preventivi (LBYL) sull'input dell'utente
        if not input_utente:
            print("Non hai inserito nulla. Riprova.")
            continue

        if not input_utente.isalpha():
            print("L'input contiene caratteri non validi. Usa solo lettere.")
            continue

        # Caso A: L'utente prova a indovinare l'intera parola
        if len(input_utente) > 1:
            if input_utente == parola_segreta:
                print(
                    f"\n🎉 Fantastico! Hai indovinato la parola intera: '{parola_segreta}'!"
                )
                return
            else:
                print(f"Sbagliato! '{input_utente}' non è la parola segreta.")
                tentativi_rimasti -= 1
                continue

        # Caso B: L'utente ha inserito una singola lettera
        lettera = input_utente
        if lettera in lettere_indovinate or lettera in lettere_errate:
            print(f"Hai già provato la lettera '{lettera}'.")
            continue

        if lettera in parola_segreta:
            print(f"Ottimo! La lettera '{lettera}' è presente.")
            lettere_indovinate.add(lettera)
        else:
            print(f"Peccato! La lettera '{lettera}' non è presente.")
            lettere_errate.add(lettera)
            tentativi_rimasti -= 1

    print(
        f"\n💥 Tentativi esauriti! Hai perso. La parola era: '{parola_segreta}'."
    )


if __name__ == "__main__":
    gioca_impiccato_lbyl()


"""
2. Versione EAFP (Easier to Ask for Forgiveness than Permission)
In questa versione ci si lancia direttamente nelle operazioni (apertura file, parsing JSON, 
logiche di gioco). Se si verificano anomalie, il flusso viene deviato e gestito nei blocchi 
except.
"""




Python
import json
import random
import sys


def gioca_impiccato_eafp():
    print("=== IL GIOCO DELL'IMPICCATO (Approccio EAFP) ===")
    nome_file = "parole.json"

    # Tentiamo direttamente l'apertura e il parsing (EAFP)
    try:
        with open(nome_file, "r", encoding="utf-8") as f:
            parole = json.load(f)

        # Intercettiamo un'eventuale struttura dati non indicizzabile o vuota
        parola_segreta = random.choice(parole).lower()

    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file}' non è stato trovato.")
        return
    except json.JSONDecodeError:
        print(f"Errore: Il file '{nome_file}' non contiene un JSON valido.")
        return
    except (IndexError, TypeError):
        print(
            "Errore: La struttura interna del file JSON non è una lista valida di parole."
        )
        return

    lettere_indovinate = set()
    lettere_errate = set()
    tentativi_rimasti = 6

    while True:
        try:
            # Generazione della stringa visualizzata
            visualizzazione = [
                let if let in lettere_indovinate else "_"
                for let in parola_segreta
            ]
            print(f"\nParola: {' '.join(visualizzazione)}")
            print(f"Tentativi rimasti: {tentativi_rimasti}")
            print(f"Lettere errate: {', '.join(sorted(lettere_errate))}")

            # Condizione di vittoria: se non ci sono più '_' nella lista
            if "_" not in visualizzazione:
                print(
                    f"\n🎉 Complimenti! Hai indovinato la parola: '{parola_segreta}'!"
                )
                break

            # Sconfitta
            if tentativi_rimasti <= 0:
                print(
                    f"\n💥 Tentativi esauriti! La parola segreta era: '{parola_segreta}'."
                )
                break

            input_utente = (
                input("Inserisci una lettera o indovina l'intera parola: ")
                .strip()
                .lower()
            )

            # Validazione EAFP dell'input
            if not input_utente.isalpha():
                # Solleviamo intenzionalmente un'eccezione per gestire l'input non valido
                raise ValueError(
                    "L'input contiene caratteri non validi o è vuoto."
                )

            # Caso A: Tentativo parola intera
            if len(input_utente) > 1:
                if input_utente == parola_segreta:
                    print(
                        f"\n🎉 Fantastico! Hai indovinato la parola intera: '{parola_segreta}'!"
                    )
                    break
                else:
                    print(
                        f"Sbagliato! '{input_utente}' non è la parola segreta."
                    )
                    tentativi_rimasti -= 1
                    continue

            # Caso B: Singola lettera
            lettera = input_utente
            if lettera in lettere_indovinate or lettera in lettere_errate:
                raise KeyError(f"Hai già inserito la lettera '{lettera}'.")

            if lettera in parola_segreta:
                print(f"Ottimo! La lettera '{lettera}' è presente.")
                lettere_indovinate.add(lettera)
            else:
                print(f"Peccato! La lettera '{lettera}' non è presente.")
                lettere_errate.add(lettera)
                tentativi_rimasti -= 1

        except ValueError as ve:
            # Cattura errori di digitazione o stringhe vuote
            print(f"[ATTENZIONE] {ve} Riprova inserendo solo lettere dell'alfabeto.")
        except KeyError as ke:
            # Cattura lettere già inserite sfruttando il flusso logico delle eccezioni
            # Nota: togliamo le virgolette extra inserite automaticamente da KeyError sull'argomento
            print(f"[INFO] {str(ke).strip(chr(39))}")


if __name__ == "__main__":
    gioca_impiccato_eafp()