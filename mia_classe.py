# esercizio lezio8

class Punto:
    """Una classe per rappresentare e operere con una coppia di coordinate x,y"""
    
    @classmethod
    def origin(cls) :
        """Metodo della classe che imposta i valori x=0, y=0"""
        return cls(0, 0)   # cls contiene tutte le informazioni sulla classe
                
    def __init__(self, x, y):
        """Inizializza le coordinate del punto"""
        self.x = x
        self.y = y
        
    def distanza_da_punto(self, altro_punto):
        # distanza = ( (x2 - x1)**2 + (y2 - y1)**2)**0.5
        dist = ( (altro_punto.x - self.x)**2 + (altro_punto.y - self.y)**2)**0.5
        return dist

    def __str__(self):
        testo = f"E' un punto di coordinata x={self.x} e y={self.y}"
        return testo


class PuntoMassa(Punto):
    """Una classe per rappresentare una massa puntiforme"""
    g = 9,81

    def __init__(self, x=0, y=0, m=0):
        """Sovvrascrive l'int di Punto per tenere conto della massa"""
        super().__init__(self, x, y) #per le coordinate uso l'init  di Punto
        self.m = m #aggiungo attributo massa

    def peso(self):
        """Restituisce il peso dell'oggetto"""
        return self.m*self.g