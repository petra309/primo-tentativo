'''
#
# File: esercizio3.py
#
# Author: Petra Zurini
#
# Date: 20/07/2026
#
# Version: 1.0
#
# Description: Programma risolutivo dell'esercizio 3, lezione 5
#
'''

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


#RISOLUZIONE PUNTO 1
"""
Partendo dal dizionario annidato rubrica visualizzate il contenuto del dizionario stampando 
a schermo delle stringhe formattate che contengano la chiave ed il valor di ognuno degli 
elementi(Esempio: ‘Paolino Paperino’, ‘giorno’ 9, ‘mese’ ‘giugno’, …)
"""

#ciclo per ciascun contatto nella rubrica
for nome, dati in rubrica.items():
    #preparo lista di stringhe formattate del tipo: 'chiave' valore
    dettagli = []
    for chiave, valore in dati.items():
        #se il valore è una stringa aggiungiamo i singoli apici, altrimenti stampiamo il numero
        valore_formattato = f"'{valore}'" if isinstance(valore, str) else valore
        dettagli.append(f"'{chiave}' {valore_formattato}")

    #unisco e separo con virgola
    stringa_dettagli = ", ".join(dettagli)

    #stampo il nome del contatto e la sua scheda
    print(f"'{nome}', {stringa_dettagli}")

"""
oppure
print("=== PUNTO 1: Visualizzazione formattata ===")
for nome, dati in rubrica.items():
    dettagli = ', '.join([f"'{k}' {v!r}" for k, v in dati.items()])
    print(f"'{nome}', {dettagli}")
"""

#RISOLUZIONE PUNTO 2
"""
A partire dalla rubrica, costruire la lista delle età, ordinata in ordine crescente e 
visualizzate i nomi in ordine crescente di età
"""

#costruisco lista delle sole età e la ordino
lista_età = sorted([dati['età'] for dati in rubrica.values()])

#ordino i nomi in base all'età contenuta nel dizionario
nomi_ordinati = sorted(rubrica, key=lambda nome: rubrica[nome]['età'])

#stampo i nomi ordinati
print("Nomi in ordine crescente di età:")
for nome in nomi_ordinati:
    print(f"- {nome} ({rubrica[nome]['età']} anni)")


#RISOLUZIOEN PUNTO 3
"""
Invertire l’ordine della lista precedentemente costruita e visualizzatela
"""

#inverto la lista delle età
lista_età_inversa = sorted(lista_età, reverse=True)
# oppure lista_età.reverse()

#ordino i nomi in ordine decrescente di età, con reverse=True all'interno della funzione sorted
nomi_invertiti = sorted(rubrica, key=lambda nome: rubrica[nome]['età'], reverse=True)

#stampo i risultati
print("Nomi in ordine decrescente di età:")
for nome in nomi_invertiti:
    print(f"- {nome} ({rubrica[nome]['età']} anni)")


#RISOLUZIONE PUNTO 4
"""
Utilizzare la rubrica e scrivere su schermo per OGNI membro della rubrica, il seguente messaggio:

'''Car[o/a] [Nome],
sei nat[o/a] il [giorno] di [mese] del [anno] e quindi a breve compirai [età] anni.
Ti manderemo gli auguri a [mail]'''

dove [o/a] deve essere adattato all’attributo [M/F]
"""

#ciclo per ogni contatto
for nome, dati in rubrica.items():
    #prendo la desinenza corretta in base al sesso
    desinenza = "o" if dati['sesso'] == "M" else "a"
    
    #stampo il messaggio 
    print(f"Car{desinenza} {nome}, sei nat{desinenza} il {dati['giorno']} di {dati['mese']} del {dati['anno']} "
          f"e quindi a breve compirai {dati['età']} anni. Ti manderemo gli auguri a {dati['mail']}\n")


#RISOLUZIONE PUNTO 5
"""
Utilizzando argv passate in input al vostro programma una chiave [giorno, mese, anno, età, sesso,
mail] e visualizzate tutto il contenuto della rubrica (valori) che corrispondono a questa chiave
"""

#per testare 6 e 7 togliere 5
"""
import sys

#controllo che l'argomento venga dato
if len(sys.argv) >= 2:
    chiave = sys.argv[1]
else:
    print("Ti sei dimenticato di inserire l'argomento!")
    sys.exit(1)

#prendo la chiave passata come argomento 
chiave_cercata = sys.argv[1].lower()

#elenco delle chiavi valide nel dizionario 
chiavi_valide = ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']

#controllo chela chiave inserita esista
if chiave_cercata not in chiavi_valide:
    print(f"Errore: '{chiave_cercata}' non è una chiave valida. Scegli tra {chiavi_valide}")
    sys.exit(1)

print(f"--- Valori corrispondenti alla chiave '{chiave_cercata}' ---")

#ciclo nella rubrica e prendo valore della chiave
for nome, dati in rubrica.items():
    valore = dati[chiave_cercata]
    print(f"{nome}: {valore}")
"""

    
#RISOLUZIONE PUNTO 6
"""
Utilizzando argparse visualizzate la stringa al punto 4 SOLO per il nome fornito come opzione
al vostro programma (esempio: python esercizio_3.py –nome ‘Madoka Ayukawa’ –> esegue punto 4 
solo per il nome indicato)
"""

import argparse
import sys

#costruisco oggetto ArgumentParser e lo assegno alla variabilie parser
parser = argparse.ArgumentParser(
    description='Gestione rubrica con opzioni da riga di comando.'
)
parser.add_argument(
    '--nome',
    type=str,
    help='Nome della persona per cui visualizzare il messaggio del punto 4',
)

# parse_known_args impedisce ad argparse di andare in errore se sono presenti altri argomenti di sys.argv
args, _ = parser.parse_known_args()

def genera_messaggio(nome, dati) :
    print(f"Car{desinenza} {nome}, sei nat{desinenza} il {dati['giorno']} di {dati['mese']} del {dati['anno']} "
          f"e quindi a breve compirai {dati['età']} anni. Ti manderemo gli auguri a {dati['mail']}\n")

#ciclo per stampare il messaggio
if args.nome:
    print(f"\n=== Messaggio personalizzato per {args.nome} ===")
    if args.nome in rubrica:
        print(genera_messaggio(args.nome, rubrica[args.nome]))
    else:
        print(f"Errore: '{args.nome}' non è presente in rubrica.")


#RISOLUZIONE PUNTO 7
"""
Utilizzando argparse introduceTe delle opzioni al vostro programma per eseguire i punti 
1, 2, 3, 4, 5 dell’esercizio (esempio: python esercizio_3.py –lista_ordinata –> esegue il 
punto 2 dell’esercizio)
"""

def punto_1():
    """PUNTO 1: Stampa formattata di chiavi e valori per ogni elemento."""
    print("=== PUNTO 1: Visualizzazione formattata ===")
    for nome, dati in rubrica.items():
        dettagli = ', '.join([f"'{k}' {v!r}" for k, v in dati.items()])
        print(f"'{nome}', {dettagli}")


def punto_2():
    """PUNTO 2: Lista delle età ordinata e nomi in ordine crescente di età."""
    print("=== PUNTO 2: Nomi e età in ordine crescente ===")
    
    lista_età = sorted([dati['età'] for dati in rubrica.values()])

    nomi_ordinati = sorted(rubrica, key=lambda nome: rubrica[nome]['età'])

    print("Nomi in ordine crescente di età:")
    for nome in nomi_ordinati:
        print(f"- {nome} ({rubrica[nome]['età']} anni)")


def punto_3():
    """PUNTO 3: Inversione dell'ordine della lista delle età."""
    print("=== PUNTO 3: Lista età invertita ===")
    
    lista_età = sorted([dati['età'] for dati in rubrica.values()])

    lista_età_inversa = sorted(lista_età, reverse=True)
    
    nomi_invertiti = sorted(rubrica, key=lambda nome: rubrica[nome]['età'], reverse=True)

    print("Nomi in ordine decrescente di età:")
    for nome in nomi_invertiti:
        print(f"- {nome} ({rubrica[nome]['età']} anni)")


def punto_4():
    """PUNTO 4: Messaggio di auguri personalizzato."""
    print("=== PUNTO 4: Messaggi di auguri ===")

    for nome, dati in rubrica.items():
        desinenza = "o" if dati['sesso'] == "M" else "a"
    
    print(f"Car{desinenza} {nome}, sei nat{desinenza} il {dati['giorno']} di {dati['mese']} del {dati['anno']} "
          f"e quindi a breve compirai {dati['età']} anni. Ti manderemo gli auguri a {dati['mail']}\n")


def punto_5(chiave):
    """PUNTO 5: Visualizza i valori della rubrica associati a una specifica chiave."""
    chiavi_valide = ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']
    if chiave not in chiavi_valide:
        print(
            f"Errore: '{chiave}' non è una chiave valida. Scegli tra: {chiavi_valide}"
        )
        return

    print(f"=== PUNTO 5: Valori per la chiave '{chiave}' ===")
    for nome, dati in rubrica.items():
        print(f"{nome} -> {chiave}: {dati[chiave]}")


#gestione comandi da terminale con argsparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Esegui i vari punti dell’esercizio sulla rubrica.'
    )

    #definizione delle opzioni (flag)
    parser.add_argument(
        '--p1',
        '--visualizza',
        action='store_true',
        help='Esegue il Punto 1 (Visualizza tutto il contenuto formattato)',
    )
    parser.add_argument(
        '--p2',
        '--lista_ordinata',
        action='store_true',
        help='Esegue il Punto 2 (Lista età e nomi in ordine crescente)',
    )
    parser.add_argument(
        '--p3',
        '--lista_invertita',
        action='store_true',
        help='Esegue il Punto 3 (Inverte la lista delle età)',
    )
    parser.add_argument(
        '--p4',
        '--auguri',
        action='store_true',
        help='Esegue il Punto 4 (Messaggio di auguri per tutti i contatti)',
    )
    parser.add_argument(
        '--p5',
        '--chiave',
        type=str,
        metavar='NOME_CHIAVE',
        help='Esegue il Punto 5 (Mostra i valori per una chiave specificata, es. mail, età)',
    )
    
    args = parser.parse_args()

    #se l'utente non passa alcun argomento mostriamo l'aiuto
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    #esecuzione in base alle opzioni passate
    if args.p1:
        punto_1()
        print()

    if args.p2:
        punto_2()
        print()

    if args.p3:
        punto_3()
        print()

    # Gestione combinata di --p4 e --nome
    if args.p4:
        punto_4()
        print()

    if args.p5:
        punto_5(args.p5)
        print()

"""
come eseguire effettivamente
# 1. Vedere l'aiuto con le opzioni disponibili
python esercizio3.py --help

# 2. Eseguire il Punto 1 e il Punto 2 insieme
python esercizio3.py --p1 --p2

# 3. Eseguire il Punto 5 cercando solo le email
python esercizio3.py --chiave mail

# 4. Eseguire il Punto 6 fornendo un nome specifico
python esercizio3.py --nome "Madoka Ayukawa"
"""