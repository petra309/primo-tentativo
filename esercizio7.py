#creo generatore 1 punto
def generatore_tabellina(numero):
    """generatore infinito di multipli di 'numero'"""
    n=0
    #loop infinito perchè non mi serve fermarmi a 10
    while(True):
        yield n*numero
        n = n +1
#####

num =int( input ('si scelga un numero') )
numero_intero = int(num)

print(f'Giocheremo con il numero (numero_intero)')
g = generatore_tabellina(numero_intero)
numero_tabellina = next(g)

#2 punto 

#
continua = False
while continua == True:
    #posso anche togliere ==True xchè è stessa cosa di verificare variabile

    guess = input(f'il numero affuale è (numero_tabellina). Qual'è il prossimo numero?')

    #controllo se fermare il gioco
    if guess == 'FINE':
        continua = False

    numero_tabellina = next(g)

    if numero_tabellina == guess :
        print('hai indovinato!')
    else:
        print('riprova')
  

print('esco dal gioco')


#aggiustare guess in int anche se giusto dice riprova  fine fare else perche riesce riprova
