'''
a = input('bogio')

print(a)
'''
'''
#
# File: HelloWorld.py
#
# Author: E.Romelli, D.Tavagnacco
#
# Date: 2026/03/03
#
# Version: 1.0
#
# Description: My First Project Program to print "Hello, World!".
#

print('Hello, World!')
'''
'''
import turtle               # Importo modulo turtle

window = turtle.Screen()    # Creo una finestra dove lavorare
raffaello = turtle.Turtle() # Creo una tartaruga e la assegno alla variabile "raffaello"
window.bgcolor("lightgrey")
raffaello.color('violet')

#for i in [0,1,2,3]:
#for i in range(0,4,1):

#for i in ['green','blue','red','yellow']:
 #raffaello.color(i)
  #  raffaello.forward(50)       
   # raffaello.left(90) 

'''
'''
raffaello.forward(50)       # Dico a "raffaello" di andare avanti di 30 passi
raffaello.left(90)  
raffaello.forward(50)
raffaello.left(90)  
raffaello.forward(50)
raffaello.left(90)  
'''

#leonardo = turtle.Turtle()
#leonardo.color('violet')
'''
leonardo.forward(50)
leonardo.left(120)
leonardo.forward(50)
leonardo.left(120)
leonardo.forward(50)
leonardo.left(120)
'''
'''
def disegna_triangolo(tartaruga, size) :
  for i in range(3) :
    tartaruga.forward(size)
    tartaruga.left(120)


def disegna_quadrato(tartaruga, size) :
  for i in range(4)  :
    tartaruga.forward(size)
    tartaruga.left(90)

def somma(a, b) :
 # risultato = a + b
 # return risultato
  return a + b
  
  
  
result = somma(3 ,4)
print(result)


raffaello.pensize(5)


donatello = turtle.Turtle()
donatello.color('lightgreen')
donatello.pensize(3)

disegna_quadrato(raffaello, 100)

disegna_quadrato(raffaello, -30)

disegna_triangolo(donatello, 50)
'''


import turtle               # Importo modulo turtle
window = turtle.Screen()    # Creo una finestra dove lavorare
raffaello = turtle.Turtle() # Creo una tartaruga e la assegno alla variabile "raffaello"
window.bgcolor("lightgrey")
raffaello.color('violet')

raffaello.forward(-100)

def koch(t, order, size):
    """
       La tartaruga t disegna frattale Koch di 'order' and 'size'
       lasciando la tartaruga nella direzioni iniziale
    """

    if order == 0:          
        # caso base che termina la ricorsione
        t.forward(size)
    else:
        # caso ricorsivo (ordine 1) in cui disegna i 4 segmenti
        koch(t, order-1, size/3)  
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        ##

koch(raffaello, 3, 200)

window.mainloop()           # Attende che l'utente chiuda la finestra di gioco o fermi il programma
