import argparse
import json
import sys

#mi ha ricopiato anche es 3, quindi togli o vedi come chiamare da altro file se serve



# Il dizionario di partenza della rubrica
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


def stampa_messaggio_auguri(nome, dati):
    desinenza = "o" if dati["sesso"] == "M" else "a"
    print(
        f"Car{desinenza} {nome}, sei nat{desinenza} il {dati['giorno']} di "
        f"{dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. "
        f"Ti manderemo gli auguri a {dati['mail']}"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Programma di gestione Rubrica avanzato con esportazione TXT e JSON."
    )

    # Opzioni flag (True/False) per i punti precedenti
    parser.add_argument(
        "--mostra_rubrica",
        action="store_true",
        help="Punto 1: Visualizza la rubrica",
    )
    parser.add_argument(
        "--lista_ordinata",
        action="store_true",
        help="Punto 2: Ordina per età crescente",
    )
    parser.add_argument(
        "--lista_invertita",
        action="store_true",
        help="Punto 3: Lista età invertita",
    )
    parser.add_argument(
        "--auguri_tutti",
        action="store_true",
        help="Punto 4: Auguri a tutti i membri",
    )

    # Nuove opzioni richieste per file TXT e JSON
    parser.add_argument(
        "--esporta_txt",
        action="store_true",
        help="Esporta la rubrica in un file di testo 'rubrica.txt' separato da virgole",
    )
    parser.add_argument(
        "--esporta_json",
        action="store_true",
        help="Esporta la rubrica in un file 'rubrica.json'",
    )
    parser.add_argument(
        "--leggi_json",
        action="store_true",
        help="Legge il file 'rubrica.json' e ne visualizza il contenuto",
    )

    # Opzioni parametriche
    parser.add_argument(
        "--cerca_chiave",
        type=str,
        choices=["giorno", "mese", "anno", "età", "sesso", "mail"],
        help="Punto 5: Visualizza i valori della chiave inserita",
    )
    parser.add_argument(
        "--nome",
        type=str,
        help="Punto 6: Stampa il messaggio di auguri SOLO per il nome indicato",
    )

    args = parser.parse_args()

    # Se non viene passata nessuna opzione, mostra l'aiuto ed esce
    if not any(vars(args).values()):
        parser.print_help()
        print(
            "\n[Nota]: Nessuna opzione selezionata. Usa uno o più flag per eseguire le funzioni."
        )
        sys.exit(0)

    # --- ESECUZIONE OPZIONI PRECEDENTI ---
    if args.mostra_rubrica:
        print("\n--- PUNTO 1: Contenuto formattato ---")
        for nome, dati in rubrica.items():
            dettagli = [f"'{k}' {repr(v)}" for k, v in dati.items()]
            print(f"'{nome}', " + ", ".join(dettagli))

    if args.lista_ordinata:
        print("\n--- PUNTO 2: Ordinamento per età ---")
        nomi_ordinati_eta = sorted(
            rubrica.keys(), key=lambda x: rubrica[x]["età"]
        )
        eta_crescente = [rubrica[nome]["età"] for nome in nomi_ordinati_eta]
        print(f"Lista delle età (crescente): {eta_crescente}")
        for nome in nomi_ordinati_eta:
            print(f"  - {nome} ({rubrica[nome]['età']} anni)")

    if args.lista_invertita:
        print("\n--- PUNTO 3: Lista età invertita ---")
        nomi_ordinati_eta = sorted(
            rubrica.keys(), key=lambda x: rubrica[x]["età"]
        )
        eta_crescente = [rubrica[nome]["età"] for nome in nomi_ordinati_eta]
        print(f"Lista delle età invertita (decrescente): {eta_crescente[::-1]}")

    if args.auguri_tutti:
        print("\n--- PUNTO 4: Auguri a tutti ---")
        for nome, dati in rubrica.items():
            stampa_messaggio_auguri(nome, dati)

    if args.cerca_chiave:
        print(
            f"\n--- PUNTO 5: Valori per la chiave '{args.cerca_chiave}' ---"
        )
        for nome, dati in rubrica.items():
            print(f"  - {nome}: {dati[args.cerca_chiave]}")

    if args.nome:
        print(f"\n--- PUNTO 6: Filtro auguri per '{args.nome}' ---")
        if args.nome in rubrica:
            stampa_messaggio_auguri(args.nome, rubrica[args.nome])
        else:
            print(f"Errore: Il nome '{args.nome}' non è presente in rubrica.")

    # =========================================================================
    # NUOVA OPZIONE: ESPORTAZIONE IN TXT
    # =========================================================================
    if args.esporta_txt:
        print("\n--- Generazione di rubrica.txt ---")
        try:
            with open("rubrica.txt", "w", encoding="utf-8") as f:
                for nome, dati in rubrica.items():
                    # Componiamo la riga inserendo il nome seguito dai valori interni separati da virgole
                    linea = f"{nome}, {dati['giorno']}, {dati['mese']}, {dati['anno']}, {dati['età']}, {dati['sesso']}, {dati['mail']}\n"
                    f.write(linea)
            print("File 'rubrica.txt' creato con successo!")
        except Exception as e:
            print(f"Si è verificato un errore durante la scrittura: {e}")

    # =========================================================================
    # NUOVA OPZIONE: ESPORTAZIONE IN JSON
    # =========================================================================
    if args.esporta_json:
        print("\n--- Generazione di rubrica.json ---")
        try:
            with open("rubrica.json", "w", encoding="utf-8") as f:
                # Scriviamo il dizionario così com'è. indent=4 lo rende leggibile ad occhio nudo
                json.dump(rubrica, f, indent=4, ensure_ascii=False)
            print("File 'rubrica.json' creato correttamente!")
        except Exception as e:
            print(f"Si è verificato un errore durante il salvataggio JSON: {e}")

    # =========================================================================
    # NUOVA OPZIONE: LETTURA E VISUALIZZAZIONE DA JSON
    # =========================================================================
    if args.leggi_json:
        print("\n--- Lettura e visualizzazione da rubrica.json ---")
        try:
            with open("rubrica.json", "r", encoding="utf-8") as f:
                rubrica_caricata = json.load(f)

            # Visualizziamo il contenuto del dizionario importato
            print("Dati importati correttamente dal file JSON:")
            print(json.dumps(rubrica_caricata, indent=2, ensure_ascii=False))
        except FileNotFoundError:
            print(
                "Errore: Il file 'rubrica.json' non esiste. Generalo prima con l'opzione --esporta_json"
            )
        except Exception as e:
            print(f"Si è verificato un errore durante la lettura: {e}")


if __name__ == "__main__":
    main()