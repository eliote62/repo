"""PROPIEDAD DEL ELEMENTO NEUTRO
Este script determina si exite (y el número de ellos) o no el ELEMENTO NEUTRO de un conjunto,
 en este caso el conjunto G={3,5,1,0}  (un conjunto finito de números enteros), 
 respecto de una operación, en este caso la SUMA """

#PRIMERO: asignamos mediante un lista los elementos del conjunto
G=[3,5,1,0]      

#SEGUNDO: definimos la operación que relaciona los elementos del conjunto, la suma
def sumar(a,b):
    return a+b

"""TERCERO: comprobamos la definición de elemento neutro, es decir, que de manera conmutativa
la suma del neutro con cualquier otro elemento del conjunto da como resultado este elemento """
acum = 0
for i in G:
  if sumar(i,G[0])==G[0] and sumar(i,G[1])==G[1] and sumar(i,G[2])==G[2] and sumar(i,G[3])==G[3]:
    if sumar(G[0],i)==G[0] and sumar(G[1],i)==G[1] and sumar(G[2],i)==G[2] and sumar(G[3],i)==G[3]:
        print(str(i)+ " es el ELEMENTO NEUTRO del conjunto G respecto de la operación suma")
        acum = acum + 1
        print("numero de elementos neutros: " + str(acum))
  else:
    print(str(i) + " no es el neutro") 

"""DUDAS:
1.como podria programarse para un conjunto G con infinitos elementos?
2.como podría programarse de modo más sencillo?
3.como podría definirse una operación arbitraria?"""

     






