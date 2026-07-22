'''
#
# File: rubrica_esercizio6.py
#
# Author: Petra Zurini
#
# Date: 20/07/2026
#
# Version: 1.0
#
# Description: Programma ausiliario dell'esercizio 6, lezione 8, contenente la classe Rubrica
#
'''

#RISOLUZIONE PUNTO 1 
"""
in un file separato, create una classe rubrica

la classe rubrica deve fare 5 azioni:
aprire una rubrica leggendola da un file (JSON oppure testo) - APRI
aggiungere un elemento alla rubrica - AGGIUNGI
rimuovere un elemento dalla rubrica (dato il nome) - RIMUOVI
salvare la rubrica su un file (JSON o testo) - SALVA
stampare tutte le informazioni di un contatto (data il nome), come nell’eserczio 3 - STAMPA

la classe rubrica deve inizializzarsi con un dizionario (come nell’esercizio 3)

la classe rubrica deve avere un classmethod per inizializzarla con un file JSON

la classe rubrica deve avere un classmethod per inizializzarla con un file testo

Per “aggiungere un elemento”, bisogna aver prima aperto una rubrica, altrimenti si ottine un messaggio di errore “Prima apri una rubrica”

Per “rimuivere un elemento”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”. Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”

Per “stampare le informazioni”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”. Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”

Per salvare la rubrica su file (JSON o txt deciso dall’estensione del nome del file), la rubrica non deve essere vuota, altrimenti si ottine un messaggio di errore “La rubrica è vuota”
"""

import json
import os

#creo la classe
class Rubrica:

    def __init__(self, dati_iniziali=None):
        """Inizializza la rubrica con un dizionario di contatti.
        Se viene passato None, la rubrica viene considerata non aperta/non
        inizializzata.
        """
        if dati_iniziali is not None:
            self.contatti = dati_iniziali
            self.is_aperta = True
        else:
            self.contatti = {}
            self.is_aperta = False

    # --- CLASSMETHODS ---

    @classmethod
    def da_json(cls, filepath):
        """Classmethod per inizializzare la rubrica caricandola da un file JSON."""
        istanza = cls()
        istanza.apri_json(filepath)
        return istanza

    @classmethod
    def da_testo(cls, filepath):
        """Classmethod per inizializzare la rubrica caricandola da un file di testo."""
        istanza = cls()
        istanza.apri_testo(filepath)
        return istanza

    #aprire la rubrica

    #aprendo la rubrica da file json
    def apri_json(self, filepath):
        """Apre e carica una rubrica da un file JSON."""
        if not os.path.exists(filepath):
            print(f"Il file '{filepath}' non esiste.")
            return False
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.contatti = json.load(f)
            self.is_aperta = True
            print(f"Rubrica caricata con successo dal file JSON '{filepath}'.")
            return True
        except Exception as e:
            print(f"Errore durante la lettura del file JSON: {e}")
            return False

    #aprendo la rubrica da file txt
    def apri_testo(self, filepath):
        """Apre e carica una rubrica da un file di testo (.txt).
        Formato atteso per riga:
        Nome|giorno|mese|anno|età|sesso|mail
        """
        if not os.path.exists(filepath):
            print(f"Il file '{filepath}' non esiste.")
            return False
        try:
            nuova_rubrica = {}
            with open(filepath, 'r', encoding='utf-8') as f:
                for riga in f:
                    riga = riga.strip()
                    if not riga:
                        continue
                    parti = riga.split('|')
                    if len(parti) == 7:
                        nome, giorno, mese, anno, eta, sesso, mail = parti
                        nuova_rubrica[nome] = {
                            'giorno': int(giorno),
                            'mese': mese,
                            'anno': int(anno),
                            'età': int(eta),
                            'sesso': sesso,
                            'mail': mail,
                        }
            self.contatti = nuova_rubrica
            self.is_aperta = True
            print(
                f"Rubrica caricata con successo dal file testo '{filepath}'."
            )
            return True
        except Exception as e:
            print(f"Errore durante la lettura del file di testo: {e}")
            return False

    #aggiungere un elemento

    def aggiungi(self, nome, giorno, mese, anno, eta, sesso, mail):
        """Aggiunge un contatto. Richiede che la rubrica sia stata precedentemente aperta."""
        if not self.is_aperta:
            print("Prima apri una rubrica")
            return

        self.contatti[nome] = {
            'giorno': int(giorno),
            'mese': mese,
            'anno': int(anno),
            'età': int(eta),
            'sesso': sesso.upper(),
            'mail': mail,
        }
        print(f"Contatto '{nome}' aggiunto con successo in rubrica!")

    #rimozione di un elemento

    def rimuovi(self, nome):
        """Rimuove un contatto dato il nome."""
        if not self.contatti:
            print("La rubrica è vuota")
            return

        if nome not in self.contatti:
            print(f"Il contatto {nome} non esiste in rubrica")
            return

        del self.contatti[nome]
        print(f"🗑️ Contatto '{nome}' rimosso con successo.")

    #stampo un elemento

    def stampa_contatto(self, nome):
        """Stampa il messaggio formattato per il contatto (come nell'Esercizio 3)."""
        if not self.contatti:
            print("La rubrica è vuota")
            return

        if nome not in self.contatti:
            print(f"Il contatto {nome} non esiste in rubrica")
            return

        dati = self.contatti[nome]
        desinenza = 'o' if dati['sesso'] == 'M' else 'a'

        messaggio = (
            f"Car{desinenza} {nome},\n"
            f"sei nat{desinenza} il {dati['giorno']} di {dati['mese']} del {dati['anno']} "
            f"e quindi a breve compirai {dati['età']} anni.\n"
            f"Ti manderemo gli auguri a {dati['mail']}"
        )
        print(f"\n--- SCHEDA CONTATTO ---\n{messaggio}\n-----------------------")

    #salvataggio della rubrica

    def salva(self, filepath):
        """Salva la rubrica su file (.json o .txt in base all'estensione)."""
        if not self.contatti:
            print("La rubrica è vuota")
            return

        estensione = os.path.splitext(filepath)[1].lower()

        try:
            if estensione == '.json':
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(self.contatti, f, ensure_ascii=False, indent=4)
                print(f"Rubrica salvata con successo in JSON su '{filepath}'")

            elif estensione == '.txt':
                with open(filepath, 'w', encoding='utf-8') as f:
                    for nome, dati in self.contatti.items():
                        riga = f"{nome}|{dati['giorno']}|{dati['mese']}|{dati['anno']}|{dati['età']}|{dati['sesso']}|{dati['mail']}\n"
                        f.write(riga)
                print(
                    f"Rubrica salvata con successo in TESTO su '{filepath}'"
                )

            else:
                print(
                    "Estensione non supportata. Utilizza un file '.json' o '.txt'."
                )

        except Exception as e:
            print(f"Errore durante il salvataggio del file: {e}")