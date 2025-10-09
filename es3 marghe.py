"""
un laboratorio campiona 10 parti di un liquido e misura il ph.
il ph è midurato tra 1 e 5 intero .
infine associa ad ogni campione un colore in base al risultato( a piacere)

1) generare una lista di 10 numeri compresi tra 1 e 5
2) generare una seconda lista di colori associando ad ogni valore di
ph il colore corretto usando un dizionario .
"""
import random

ph_numero = []
p_colri = []

for i in range(0,10):
    numero= random.randint(1,5)
    ph_numero.append(numero)
    
mydict= {1:"rosso",2:"blu",3:"verde",4:"giallo",5:"nero"}

for i in range(0,10):
  colore = mydict[ph_numero[i]
  ph_colori.append(colore)
                  
#contare il numero delle occorrenze "verde"
                  