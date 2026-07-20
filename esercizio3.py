

rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}
#parte 1
print (rubrica)


#parte 2


# 1. Costruiamo la lista delle sole età e la ordiniamo
lista_età = sorted([dati['età'] for dati in rubrica.values()])


# 2. Ordiniamo i nomi direttamente in base all'età contenuta nel dizionario
nomi_ordinati = sorted(rubrica, key=lambda nome: rubrica[nome]['età'])

# 3. Visualizziamo i nomi ordinati
print("Nomi in ordine crescente di età:")
for nome in nomi_ordinati:
    print(f"- {nome} ({rubrica[nome]['età']} anni)")

#33333333333333

lista_età_inversa = sorted(lista_età, reverse=True)
#o lista_età.reverse()

# 2. Ordiniamo anche i nomi in ordine decrescente di età 
# Basta aggiungere reverse=True all'interno della funzione sorted
nomi_invertiti = sorted(rubrica, key=lambda nome: rubrica[nome]['età'], reverse=True)

# 3. Visualizziamo i risultati
print("Nomi in ordine decrescente di età:")
for nome in nomi_invertiti:
    print(f"- {nome} ({rubrica[nome]['età']} anni)")



#punto 4

for nome, dati in rubrica.items():
    # Scegliamo la desinenza corretta in base al sesso
    desinenza = "o" if dati['sesso'] == "M" else "a"
    
    # Stampiamo il messaggio formattato
    print(f"Car{desinenza} {nome}, sei nat{desinenza} il {dati['giorno']} di {dati['mese']} del {dati['anno']} "
          f"e quindi a breve compirai {dati['età']} anni. Ti manderemo gli auguri a {dati['mail']}\n")

#punto 5
"""
import sys
#per chiedere la chiave
# Chiediamo la chiave direttamente a schermo
chiave_cercata = input("Quale chiave vuoi cercare? (giorno, mese, anno, età, sesso, mail): ").lower()

# Verifichiamo se la chiave esiste
if chiave_cercata in ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']:
    print(f"\n--- Valori per '{chiave_cercata}' ---")
    for nome, dati in rubrica.items():
        print(f"{nome}: {dati[chiave_cercata]}")
else:
    print("Chiave non valida.")

#1
if len(sys.argv) >= 2:
    chiave = sys.argv[1]
else:
    sys.exit(1)
    print("Ti sei dimenticato di inserire l'argomento!")


# 2. Recuperiamo la chiave passata come argomento (es. "mail" o "età")
chiave_cercata = sys.argv[1].lower()

# Elenco delle chiavi valide nel dizionario interno
chiavi_valide = ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']

# 3. Controlliamo se la chiave inserita esiste davvero
if chiave_cercata not in chiavi_valide:
    print(f"Errore: '{chiave_cercata}' non è una chiave valida. Scegli tra {chiavi_valide}")
    sys.exit(1)

print(f"--- Valori corrispondenti alla chiave '{chiave_cercata}' ---")

# 4. Iteriamo nella rubrica ed estraiamo solo il valore legato a quella chiave
for nome, dati in rubrica.items():
    valore = dati[chiave_cercata]
    print(f"{nome}: {valore}")
"""

import sys


# 1. Controlliamo se l'argomento è stato passato da terminale
if len(sys.argv) >= 2:
    # Se c'è, lo prendiamo direttamente
    chiave_cercata = sys.argv[1].lower()
else:
    # Se NON c'è, invece di crashare o chiudere, lo chiediamo a schermo!
    print("Nessun argomento passato da terminale.")
    chiave_cercata = input("Quale chiave vuoi cercare? (giorno, mese, anno, età, sesso, mail): ").lower()


# Elenco delle chiavi valide nel dizionario interno
chiavi_valide = ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']

# 2. Controlliamo se la chiave (da terminale o da input) esiste davvero
if chiave_cercata not in chiavi_valide:
    print(f"Errore: '{chiave_cercata}' non è una chiave valida. Scegli tra {chiavi_valide}")
    sys.exit(1)

print(f"\n--- Valori corrispondenti alla chiave '{chiave_cercata}' ---")

# 3. Iteriamo nella rubrica ed estraiamo il valore
for nome, dati in rubrica.items():
    valore = dati[chiave_cercata]
    print(f"{nome}: {valore}")

#666

import argparse
"""
rivedere tutta sta parte
import argparse

rubrica = {
  'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
  'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
  'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
  'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

# 1. Configurazione di argparse
parser = argparse.ArgumentParser(description="Stampa messaggio personalizzato dalla rubrica.")

# Aggiungiamo l'opzione --nome (facoltativa)
parser.add_argument('--nome', type=str, help="Il nome del membro della rubrica per cui stampare il messaggio")

# Leggiamo gli argomenti passati da terminale
args = parser.parse_args()

# Funzione interna per formattare e stampare il messaggio di un singolo contatto
def stampa_messaggio(nome, dati):
    desinenza = "o" if dati['sesso'] == "M" else "a"
    print(f"Car{desinenza} {nome}, sei nat{desinenza} il {dati['giorno']} di {dati['mese']} del {dati['anno']} "
          f"e quindi a breve compirai {dati['età']} anni. Ti manderemo gli auguri a {dati['mail']}")

# 2. Logica di filtraggio basata sull'opzione --nome
if args.nome:
    # Se l'utente ha inserito un nome, verifichiamo se esiste nella rubrica
    if args.nome in rubrica:
        stampa_messaggio(args.nome, rubrica[args.nome])
    else:
        print(f"Errore: Il nome '{args.nome}' non è presente in rubrica.")
else:
    # Se non viene specificato nessun nome, lo eseguiamo per OGNI membro
    print("Nessun nome specificato. Stampa per tutta la rubrica:\n" + "-"*50)
    for nome, dati in rubrica.items():
        stampa_messaggio(nome, dati)
"""

==========================================
    # ESECUZIONE PUNTO 5 (Spostato da sys.argv ad argparse)
    # =========================================================================
    if args.cerca_chiave:
        print(
            f"\n--- ESECUZIONE PUNTO 5: Valori per la chiave '{args.cerca_chiave}' ---"
        )
        for nome, dati in rubrica.items():
            print(f"  - {nome}: {dati[args.cerca_chiave]}")

# punto 7

if args.nome:
        print(f"\n--- ESECUZIONE PUNTO 6: Filtro auguri per '{args.nome}' ---")
        if args.nome in rubrica:
            stampa_messaggio_auguri(args.nome, rubrica[args.nome])
        else:
            print(f"Errore: Il nome '{args.nome}' non è presente in rubrica.")


if __name__ == "__main__":
    main()



















"""
import argparse
import sys

# Dizionario di partenza fornito
rubrica = {
    "Paolino Paperino": {
        "giorno": 9,
        "mese": "giugno",
        "anno": 1934,
        "età": 93,
        "sesso": "M",
        "mail": "paolino.paperin0@disney.org",
    },
    "Ron Weasley": {
        "giorno": 1,
        "mese": "marzo",
        "anno": 1980,
        "età": 46,
        "sesso": "M",
        "mail": "ron_weasley80@hogwards.uk",
    },
    "Ramona Flowers": {
        "giorno": 19,
        "mese": "ottobre",
        "anno": 2004,
        "età": 22,
        "sesso": "F",
        "mail": "ramona.fls@gmail.com",
    },
    "Madoka Ayukawa": {
        "giorno": 25,
        "mese": "maggio",
        "anno": 1969,
        "età": 57,
        "sesso": "F",
        "mail": "madoka_sax@asahi_net.jp",
    },
}


# --- FUNZIONE AUSILIARIA PER IL PUNTO 4 ---
def stampa_messaggio_auguri(nome, dati):
    """Genera e stampa il messaggio personalizzato in base al sesso."""
    desinenza = "o" if dati["sesso"] == "M" else "a"
    messaggio = (
        f"Car{desinenza} {nome}, sei nat{desinenza} il {dati['giorno']} di "
        f"{dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. "
        f"Ti manderemo gli auguri a {dati['mail']}"
    )
    print(messaggio)


def main():
    # =========================================================================
    # PUNTO 1: Visualizzazione formattata del dizionario annidato
    # =========================================================================
    print("--- PUNTO 1: Contenuto della rubrica ---")
    for nome, dati in rubrica.items():
        # Creiamo una lista di stringhe 'chiave' valore per i dati interni
        dettagli = [f"'{k}' {repr(v)}" for k, v in dati.items()]
        # Uniamo il nome con i suoi dettagli
        print(f"'{nome}', " + ", ".join(dettagli))

    # =========================================================================
    # PUNTO 2 & 3: Liste delle età, ordinamenti e inversione
    # =========================================================================
    print("\n--- PUNTO 2 & 3: Analisi dell'età ---")

    # Ordiniamo i nomi in base all'età contenuta nel dizionario interno
    nomi_ordinati_eta = sorted(rubrica.keys(), key=lambda x: rubrica[x]["età"])

    # Creiamo la lista delle età in ordine crescente
    eta_crescente = [rubrica[nome]["età"] for nome in nomi_ordinati_eta]
    print(f"Lista delle età (crescente): {eta_crescente}")

    print("Nomi in ordine crescente di età:")
    for nome in nomi_ordinati_eta:
        print(f"  - {nome} ({rubrica[nome]['età']} anni)")

    # PUNTO 3: Invertiamo la lista precedentemente costruita (ordine decrescente)
    eta_decrescente = eta_crescente[::-1]
    print(f"Lista delle età invertita (decrescente): {eta_decrescente}")

    # =========================================================================
    # PUNTO 4: Stampa del messaggio per OGNI membro
    # =========================================================================
    print("\n--- PUNTO 4: Messaggi di auguri per tutti ---")
    for nome, dati in rubrica.items():
        stampa_messaggio_auguri(nome, dati)

    # =========================================================================
    # PUNTO 5: Utilizzo di sys.argv (args posizionali da riga di comando)
    # Per testarlo: python esercizio_rubrica.py mail
    # =========================================================================
    print("\n--- PUNTO 5: Ricerca valori tramite sys.argv ---")
    # Verifichiamo se è stato passato almeno un argomento posizionale oltre al nome del file
    if len(sys.argv) > 1:
        chiave_cercata = sys.argv[1]
        # Validiamo che la chiave esista in uno dei record di esempio
        if chiave_cercata in [
            "giorno",
            "mese",
            "anno",
            "età",
            "sesso",
            "mail",
        ]:
            print(
                f"Valori corrispondenti alla chiave '{chiave_cercata}' (da sys.argv):"
            )
            for nome, dati in rubrica.items():
                print(f"  - {nome}: {dati[chiave_cercata]}")
        else:
            print(
                f"Nota: '{chiave_cercata}' non è una chiave valida per la ricerca posizionale."
            )
    else:
        print(
            "Nessun argomento posizionale fornito a sys.argv. (Es: esegui 'python esercizio_rubrica.py mail')"
        )

    # =========================================================================
    # PUNTO 6: Utilizzo di argparse per filtrare il Punto 4 sul nome
    # Per testarlo: python esercizio_rubrica.py --nome "Madoka Ayukawa"
    # =========================================================================
    print("\n--- PUNTO 6: Filtro Argparse per nome ---")
    parser = argparse.ArgumentParser(
        description="Filtra il messaggio di auguri per un nome specifico."
    )
    parser.add_argument(
        "--nome",
        type=str,
        help="Il nome del membro della rubrica di cui stampare il messaggio del punto 4",
    )

    # Nota: usiamo parse_known_args() per evitare conflitti con l'argomento posizionale del punto 5
    args, _ = parser.parse_known_args()

    if args.nome:
        if args.nome in rubrica:
            print(f"Esecuzione Punto 4 SOLO per l'opzione --nome '{args.nome}':")
            stampa_messaggio_auguri(args.nome, rubrica[args.nome])
        else:
            print(f"Errore: Il nome '{args.nome}' non è presente in rubrica.")
    else:
        print(
            "Opzione --nome non utilizzata. (Es: esegui 'python esercizio_rubrica.py --nome \"Madoka Ayukawa\"')"
        )


if __name__ == "__main__":
    main()
"""    