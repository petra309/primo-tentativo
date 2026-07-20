

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

