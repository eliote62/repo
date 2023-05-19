#Demostración de la PROPOSICIÓN :el elemento neutro de una estructura algebraica de GRUPO es UNICO.
#demostraremos la proposición por REDUCCIÓN AL ABSURDO
print("DEMOSTRACIÓN DE LA UNICIDAD DEL ELEMENTO NEUTRO DE UN GRUPO") 
#supondremos un conjunto cualquiera cuyos elementos los nombramos con letras, por ejemplo G={a,b,c...}")
#suponemos una operación para el grupo que suponemos implicita al relacionar dos elementos, pro ejemplo ab (a operado con b)")
#suponemos que el conjunto G con la operación º tienen estructura algebraica de GRUPO")
#aplicaremos el método de REDUCCION AL ABSURDO, por lo que negamos la proposición que 
#queremos demostrar y suponmemos que hay dos elementos neutros distintos, de modo que 
#si llegamos a una CONTRADICCIÓN, la proposición de UNICIDAD es cierta.c.q.d.

print("elgir letra e, como primer neutro = ")          #comenzamos aplicando la HIPOTESIS DE REDUCCION,       
n_1 = str(input())                                      #por lo que suponemos que hay dos neutros distintos
print("elegir letra u, como segundo neutro distinto= ") #y los elegimos por el teclado, por ejemplo las letras e y u.
n_2 = str(input())

op_1 = n_1 + n_2                                #relacionamos los dos neutros mediante la operación del GRUPO, que no se muestra por el convenio inicial.
print(op_1)                                     #imprimo la operacion por CURIOSIDAD, para comproba la forma que tiene
op_2 = n_2 + n_1                                #misma operacion pero conmutando el orden para que se cumpla la definicion de elemento neutro (TAUTOLOGIA) 
print(op_2)

op_1 = n_1                      # si tomamos a n_2 como el neutro, se cumple la definicion de la proppiedad de elemento neutro.
op_2 = n_1  
if op_1==op_2 :                 #esta condición la debecumplirse para todo elemento neutro
    print("entonces " + str(n_1 + n_2) + "=" + str(n_2+n_1)+ "=" + n_1 + " y " +n_2+ " es elemento neutro")
    ope_1 = n_1 + n_2           #definimos una nueva variable para relacionar los dos neutros elegidos, con la intencion
    ope_2 = n_2 + n_1           #de elegir n_1 como elemento neutro en lugar de n_2 como se hizo anteriormente
    ope_1 = n_2          # si tomamos a n_1 como el neutro
    ope_2 = n_2
    if ope_1==ope_2 :

        print("entonces " + str(n_1 + n_2) + "=" + str(n_2+n_1)+ "=" + n_2 + " y " +n_1+ " es elemento neutro")
        if op_2 == ope_2 and op_2 == n_1 and ope_2 == n_2 :
            print ("EXISTEN DOS NEUTROS DISTINTOS PARA EL GRUPO")
        else :
            print (" ue=ue=u=e, se produce una CONTRADICCIÓN pues u es distinto de e, entonces la PROPOSICIÓN es CIERTA, c.q.d.")    #si se obtiene este resultado, la PROPOSICION queda DEMOSTRADA como VERDADERA
    else:
        print (n_1 + " no es neutro")
else:
    print (n_2 + " no es neutro")
