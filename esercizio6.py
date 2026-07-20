import rubrica 


rb = rubrica.Rubrica()

print(rb.data)

rb.APRI()




#punto 1 con gem

# gestore_rubrica.py
import json


class Rubrica:

    def __init__(self):
        # Inizializziamo una rubrica vuota sotto forma di dizionario
        self.dati = {}

    # --- AZIONE 1: APRI ---
    def apri(self, nome_file):
        """Carica la rubrica da un file JSON."""
        try:
            with open(nome_file, "r", encoding="utf-8") as f:
                self.dati = json.load(f)
            print(f"[OK] Rubrica caricata con successo da '{nome_file}'.")
        except FileNotFoundError:
            print(
                f"[INFO] Il file '{nome_file}' non esiste. Verrà creata una nuova rubrica al salvataggio."
            )
            self.dati = {}
        except json.JSONDecodeError:
            print(
                f"[ERRORE] Il file '{nome_file}' non è un JSON valido. Inizializzazione vuota."
            )
            self.dati = {}

    # --- AZIONE 2: AGGIUNGI ---
    def aggiungi(self, nome, giorno, mese, anno, eta, sesso, mail):
        """Aggiunge o aggiorna un contatto nella rubrica."""
        self.dati[nome] = {
            "giorno": giorno,
            "mese": mese,
            "anno": anno,
            "età": eta,
            "sesso": sesso,
            "mail": mail,
        }
        print(f"[OK] Contatto '{nome}' aggiunto/aggiornato con successo.")

    # --- AZIONE 3: RIMUOVI ---
    def rimuovi(self, nome):
        """Rimuove un contatto dalla rubrica dato il nome."""
        if nome in self.dati:
            del self.dati[nome]
            print(f"[OK] Contatto '{nome}' rimosso dalla rubrica.")
        else:
            print(f"[AVVISO] Impossibile rimuovere: '{nome}' non è in rubrica.")

    # --- AZIONE 4: SALVA ---
    def salva(self, nome_file):
        """Salva lo stato attuale della rubrica in un file JSON."""
        try:
            with open(nome_file, "w", encoding="utf-8") as f:
                json.dump(self.dati, f, indent=4, ensure_ascii=False)
            print(f"[OK] Rubrica salvata con successo nel file '{nome_file}'.")
        except Exception as e:
            print(f"[ERRORE] Impossibile salvare il file: {e}")

    # --- AZIONE 5: STAMPA ---
    def stampa_contatto(self, nome):
        """Stampa il messaggio formattato dell'Esercizio 3 per un singolo contatto."""
        if nome in self.dati:
            info = self.dati[nome]
            desinenza = "o" if info["sesso"] == "M" else "a"
            messaggio = (
                f"Car{desinenza} {nome}, sei nat{desinenza} il {info['giorno']} di "
                f"{info['mese']} del {info['anno']} e quindi a breve compirai {info['età']} anni. "
                f"Ti manderemo gli auguri a {info['mail']}"
            )
            print(messaggio)
        else:
            print(
                f"[AVVISO] Impossibile stampare: '{nome}' non è presente in rubrica."
            )


# main.py
from gestore_rubrica import Rubrica


def main():
    # Creiamo un'istanza della classe Rubrica
    mia_rubrica = Rubrica()

    # 1. Test AZIONE: AGGIUNGI (Carichiamo i dati storici dell'Esercizio 3)
    print("--- 1. Test Aggiunta Contatti ---")
    mia_rubrica.aggiungi(
        "Paolino Paperino",
        9,
        "giugno",
        1934,
        93,
        "M",
        "paolino.paperin0@disney.org",
    )
    mia_rubrica.aggiungi(
        "Ron Weasley", 1, "marzo", 1980, 46, "M", "ron_weasley80@hogwards.uk"
    )
    mia_rubrica.aggiungi(
        "Ramona Flowers",
        19,
        "ottobre",
        2004,
        22,
        "F",
        "ramona.fls@gmail.com",
    )
    mia_rubrica.aggiungi(
        "Madoka Ayukawa",
        25,
        "maggio",
        1969,
        57,
        "F",
        "madoka_sax@asahi_net.jp",
    )

    # 2. Test AZIONE: SALVA
    print("\n--- 2. Test Salvataggio su File ---")
    mia_rubrica.salva("archivio_rubrica.json")

    # 3. Test AZIONE: RIMUOVI
    print("\n--- 3. Test Rimozione Contatto ---")
    mia_rubrica.rimuovi("Ron Weasley")

    # 4. Test AZIONE: STAMPA (Verifica della formattazione del punto 4, es. 3)
    print("\n--- 4. Test Stampa Informazioni Formattate ---")
    print("Tentativo su un contatto esistente (femminile):")
    mia_rubrica.stampa_contatto("Ramona Flowers")

    print("\nTentativo su un contatto eliminato:")
    mia_rubrica.stampa_contatto("Ron Weasley")

    # 5. Test AZIONE: APRI (Ripristiniamo la rubrica originaria salvata prima)
    print("\n--- 5. Test Apertura e Ripristino da File ---")
    nuova_istanza = Rubrica()
    nuova_istanza.apri("archivio_rubrica.json")

    print("\nVerifica post-ripristino (Ron dovrebbe essere di nuovo presente):")
    nuova_istanza.stampa_contatto("Ron Weasley")


if __name__ == "__main__":
    main()


#punto 2 


import json
import os


class Rubrica:

    def __init__(self, dizionario_iniziale=None):
        """Inizializza la classe con un dizionario (come nell'esercizio 3).

        Se non viene passato nulla, si imposta a None per tracciare lo stato di
        'non aperta'.
        """
        self.dati = dizionario_iniziale

    # --- METODI DI CLASSE PER L'INIZIALIZZAZIONE (APRI) ---

    @classmethod
    def da_json(cls, nome_file):
        """Classmethod per inizializzare la rubrica leggendola da un file JSON."""
        try:
            with open(nome_file, "r", encoding="utf-8") as f:
                dati_caricati = json.load(f)
            print(f"[OK] Rubrica inizializzata dal file JSON '{nome_file}'.")
            return cls(dati_caricati)
        except FileNotFoundError:
            print(
                f"[INFO] Il file JSON '{nome_file}' non esiste. Inizializzo una rubrica vuota."
            )
            return cls({})  # Creiamo una rubrica vuota (ma aperta)
        except json.JSONDecodeError:
            print(
                f"[ERRORE] Il file '{nome_file}' non è un JSON valido. Inizializzazione fallita."
            )
            return cls(None)

    @classmethod
    def da_testo(cls, nome_file):
        """Classmethod per inizializzare la rubrica leggendola da un file di testo (.txt)

        in cui i dati sono separati da virgole.
        """
        dati_caricati = {}
        try:
            with open(nome_file, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    # Separiamo i campi togliendo gli spazi bianchi in eccesso
                    parti = [p.strip() for p in linea.split(",")]
                    if len(parti) == 7:
                        nome, giorno, mese, anno, eta, sesso, mail = parti
                        dati_caricati[nome] = {
                            "giorno": int(giorno),
                            "mese": mese,
                            "anno": int(anno),
                            "età": int(eta),
                            "sesso": sesso,
                            "mail": mail,
                        }
            print(f"[OK] Rubrica inizializzata dal file testo '{nome_file}'.")
            return cls(dati_caricati)
        except FileNotFoundError:
            print(
                f"[INFO] Il file di testo '{nome_file}' non esiste. Inizializzo una rubrica vuota."
            )
            return cls({})
        except ValueError:
            print(
                f"[ERRORE] Formato dati non valido all'interno del file '{nome_file}'."
            )
            return cls(None)

    # --- AZIONE 2: AGGIUNGI ---
    def aggiungi(self, nome, giorno, mese, anno, eta, sesso, mail):
        """Aggiunge un elemento solo se la rubrica è già stata aperta/inizializzata."""
        if self.dati is None:
            print("Prima apri una rubrica")
            return

        self.dati[nome] = {
            "giorno": giorno,
            "mese": mese,
            "anno": anno,
            "età": eta,
            "sesso": sesso,
            "mail": mail,
        }
        print(f"[OK] Contatto '{nome}' aggiunto.")

    # --- AZIONE 3: RIMUOVI ---
    def rimuovi(self, nome):
        """Rimuove un elemento verificando lo stato di riempimento della rubrica."""
        if self.dati is None or len(self.dati) == 0:
            print("La rubrica è vuota")
            return

        if nome not in self.dati:
            print(f"Il contatto {nome} non esiste in rubrica")
            return

        del self.dati[nome]
        print(f"[OK] Contatto '{nome}' rimosso.")

    # --- AZIONE 5: STAMPA ---
    def stampa_contatto(self, nome):
        """Stampa le info del contatto verificando la presenza dei dati."""
        if self.dati is None or len(self.dati) == 0:
            print("La rubrica è vuota")
            return

        if nome not in self.dati:
            print(f"Il contatto {nome} non esiste in rubrica")
            return

        info = self.dati[nome]
        desinenza = "o" if info["sesso"] == "M" else "a"
        print(
            f"Car{desinenza} {nome}, sei nat{desinenza} il {info['giorno']} di "
            f"{info['mese']} del {info['anno']} e quindi a breve compirai {info['età']} anni. "
            f"Ti manderemo gli auguri a {info['mail']}"
        )

    # --- AZIONE 4: SALVA (Decide il formato dall'estensione) ---
    def salva(self, nome_file):
        """Salva la rubrica se non è vuota.

        Il formato (JSON o TXT) viene rilevato dall'estensione.
        """
        if self.dati is None or len(self.dati) == 0:
            print("La rubrica è vuota")
            return

        # Estrarre l'estensione del file in minuscolo
        _, estensione = os.path.splitext(nome_file.lower())

        if estensione == ".json":
            with open(nome_file, "w", encoding="utf-8") as f:
                json.dump(self.dati, f, indent=4, ensure_ascii=False)
            print(f"[SALVATO] Esportato correttamente in JSON: '{nome_file}'")

        elif estensione == ".txt":
            with open(nome_file, "w", encoding="utf-8") as f:
                for nome, dati in self.dati.items():
                    linea = f"{nome}, {dati['giorno']}, {dati['mese']}, {dati['anno']}, {dati['età']}, {dati['sesso']}, {dati['mail']}\n"
                    f.write(linea)
            print(f"[SALVATO] Esportato correttamente in Testo: '{nome_file}'")
        else:
            print(
                f"[ERRORE] Estensione '{estensione}' non supportata. Usa .json o .txt"
            )



"""
Esempio pratico per verificare la gestione degli errori
Puoi usare questo script di test per verificare che tutti
 i nuovi messaggi di errore scattino al momento giusto:

# test_errori.py
from gestore_rubrica import Rubrica

# Dizionario di partenza dell'esercizio 3
dizionario_iniziale = {
    "Paolino Paperino": {
        "giorno": 9,
        "mese": "giugno",
        "anno": 1934,
        "età": 93,
        "sesso": "M",
        "mail": "paolino.paperin0@disney.org",
    }
}

print("--- 1. TEST DIARIO NON INIZIALIZZATO ---")
rubrica_chiusa = Rubrica()  # Non passiamo nessun dizionario
rubrica_chiusa.aggiungi(
    "Ron Weasley", 1, "marzo", 1980, 46, "M", "ron@hogwards.uk"
)
# Output atteso: Prima apri una rubrica

print("\n--- 2. TEST CONTROLLI SU RUBRICA VUOTA ---")
rubrica_vuota = Rubrica({})  # Aperta, ma vuota
rubrica_vuota.rimuovi("Paolino Paperino")  # Output: La rubrica è vuota
rubrica_vuota.stampa_contatto("Paolino Paperino")  # Output: La rubrica è vuota
rubrica_vuota.salva("rubrica.json")  # Output: La rubrica è vuota

print("\n--- 3. TEST CONTROLLI SU ELEMENTO INESISTENTE ---")
rubrica_attiva = Rubrica(dizionario_iniziale)  # Inizializzazione corretta
rubrica_attiva.stampa_contatto("Madoka Ayukawa")
# Output atteso: Il contatto Madoka Ayukawa non esiste in rubrica
rubrica_attiva.rimuovi("Madoka Ayukawa")
# Output atteso: Il contatto Madoka Ayukawa non esiste in rubrica

print("\n--- 4. TEST DI SALVATAGGIO DINAMICO PER ESTENSIONE ---")
rubrica_attiva.salva("archivio.txt")  # Riconosce ed esporta in txt
rubrica_attiva.salva("archivio.json")  # Riconosce ed esporta in json

print("\n--- 5. TEST RE-INIZIALIZZAZIONE DA FILE (CLASSMETHODS) ---")
# Carichiamo la rubrica partendo dai file appena salvati
rubrica_da_txt = Rubrica.da_testo("archivio.txt")
rubrica_da_txt.stampa_contatto("Paolino Paperino")
"""

#punto 2 
#metti su un altro file

import sys
from gestore_rubrica import Rubrica


def mostra_menu():
    print("\n" + "=" * 45)
    print("         GESTORE RUBRICA INTERATTIVO         ")
    print("=" * 45)
    print("Digitare una delle seguenti opzioni:")
    print("  APRI     - Inizializza la rubrica da un file (.txt o .json)")
    print("  AGGIUNGI - Aggiunge un nuovo contatto alla rubrica")
    print("  RIMUOVI  - Rimuove un contatto esistente")
    print("  SALVA    - Salva la rubrica su file (.txt o .json)")
    print("  STAMPA   - Stampa i dettagli di un contatto")
    print("  EXIT     - Chiude il programma")
    print("=" * 45)


def main():
    # Creiamo un'istanza iniziale della rubrica (non ancora aperta)
    mio_archivio = Rubrica()

    opzioni_valide = {"APRI", "AGGIUNGI", "RIMUOVI", "SALVA", "STAMPA"}

    while True:
        mostra_menu()
        scelta = input("Scegli un'azione: ").strip().upper()

        if scelta == "EXIT":
            print("\nChiusura del programma in corso... Arrivederci!")
            break

        if scelta not in opzioni_valide:
            print(
                f"\n[ERRORE] L'azione '{scelta}' non esiste. Riprova o digita EXIT."
            )
            continue

        # ---------------------------------------------------------------------
        # AZIONE: APRI
        # ---------------------------------------------------------------------
        if scelta == "APRI":
            nome_file = input(
                "Inserisci il nome del file da aprire (.json o .txt): "
            ).strip()
            if nome_file.lower().endswith(".json"):
                mio_archivio = Rubrica.da_json(nome_file)
            elif nome_file.lower().endswith(".txt"):
                mio_archivio = Rubrica.da_testo(nome_file)
            else:
                print(
                    "[ERRORE] Estensione non riconosciuta. Il file deve terminare in .json o .txt"
                )

        # ---------------------------------------------------------------------
        # AZIONE: AGGIUNGI
        # ---------------------------------------------------------------------
        elif scelta == "AGGIUNGI":
            # Nota: se la rubrica è None, il metodo interno stamperà "Prima apri una rubrica"
            if mio_archivio.dati is None:
                mio_archivio.aggiungi(None, 0, "", 0, 0, "", "")
                continue

            nome = input("Nome e Cognome: ").strip()
            try:
                giorno = int(input("Giorno di nascita (numero): "))
                mese = input("Mese di nascita: ").strip()
                anno = int(input("Anno di nascita: "))
                eta = int(input("Età: "))
                sesso = input("Sesso (M/F): ").strip().upper()
                mail = input("Indirizzo e-mail: ").strip()

                mio_archivio.aggiungi(nome, giorno, mese, anno, eta, sesso, mail)
            except ValueError:
                print(
                    "[ERRORE] Inserimento non valido. Giorno, anno ed età devono essere valori numerici."
                )

        # ---------------------------------------------------------------------
        # AZIONE: RIMUOVI
        # ---------------------------------------------------------------------
        elif scelta == "RIMUOVI":
            nome = input("Inserisci il nome del contatto da rimuovere: ").strip()
            mio_archivio.rimuovi(nome)

        # ---------------------------------------------------------------------
        # AZIONE: SALVA
        # ---------------------------------------------------------------------
        elif scelta == "SALVA":
            nome_file = input(
                "Inserisci il nome del file su cui salvare (.json o .txt): "
            ).strip()
            mio_archivio.salva(nome_file)

        # ---------------------------------------------------------------------
        # AZIONE: STAMPA
        # ---------------------------------------------------------------------
        elif scelta == "STAMPA":
            nome = input("Inserisci il nome del contatto da stampare: ").strip()
            mio_archivio.stampa_contatto(nome)


if __name__ == "__main__":
    main()