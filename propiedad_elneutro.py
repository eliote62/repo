"""PROPIEDAD DEL ELEMENTO NEUTRO
Este script determina si exite o no el ELEMENTO NEUTRO de un conjunto,
 en este caso el conjunto G (conjunto finito de números enteros), 
 respecto de una operación, en este caso la SUMA. Tambien cuenta el numero de 
 elementos NEUTROS que hay en el conjuno estudiado"""

"""PRIMERO: asignamos mediante un lista los elementos del conjunto"""
G=[3,0,1,0,7,11,29,12,0,0]      
n = len(G)                                    #numero de elementos del conjunto G

"""SEGUNDO: definimos la operación que relaciona los elementos del conjunto, la suma"""
def sumar(a,b):
    return a+b

"""TERCERO: comprobamos la definición de elemento neutro, es decir, que de manera conmutativa
la suma del neutro con cualquier otro elemento del conjunto da como resultado este elemento """
acum = 0
for i in G:
    for j in G:
        if sumar(i,j)==j:                     #suma i+j=j
           if sumar(j,i)==j:                  #conmuta la suma, j+i=j, condicion para ser neutro
              resultado=str(i)+ " es el ELEMENTO NEUTRO del conjunto G respecto de la operación suma"
              acum = acum + 1
 
print(resultado)    
print("numero de elementos neutros: "+ str(acum/n)) 
#print("numero de elementos neutros, " + str(i) + " : "+ str(acum/n)) 

  

"""DUDAS:
1.como podria programarse para un conjunto G con infinitos elementos?
2.como podría programarse de modo más sencillo?
3.como podría definirse una operación arbitraria?"""

     






