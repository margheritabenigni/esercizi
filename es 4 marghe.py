#dato un insieme di punti su un piano cartesiano,
#random compresi nell'intervallo 0,10 . calcolare il
#punto con ascissaminima e coordinata minima.

import random

ascissa(0)
ordinata(0)

x=[]
y=[]

punti:[]

for i in range(0,20):
   x.append(indice)(random.randint(0,10))
   y.append(indice(random.randint(0,10)))
#ascissa massima ?
#scorrere la lista delle x , trova il massimo e salvare l'indice
#visualizzare poi con una print il numero

for x in range(0,20):
    if x[i]>massimo:
 print (massimo)
# ho aggiunto la ricerca del punto con ascissa massima

for i in range(0,20):
    if y[i]<minimo:
        minimo=y[i]
print(minimo,x[minimo])

punti_cartesiano=[]
for i in range(0,20):
    punto = (random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
             
#come accedere alla x del primo punto
print(punti_cartesiano[0][0])

#come accedere alla y del primo punto
print(punti_cartesiano[0][1])