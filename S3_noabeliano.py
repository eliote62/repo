""" DEMOSTRACION mediante el metodo del CONTRAEJEMPLO del TEOREMA DE TEORIA DE GRUPOS:
dado un conjunto finito X con n elementos, el GRUPO SIMETRICO Sn con n>=3, cuyos elementos son las
 aplicaciones biyectivas entre los elementos de X

 Para el grupo S3, tomamos un conjunto finito X con 3 elementos (X={1,2,3}), que cumple
 la condicion del teorema n>=3, de modo que el grupo simetrico formado por el 
conjunto S3 de todas las aplicaciones biyectivas posibles entre los elementos de X,
siendo un numero de n!=3!=3·2·1=6 aplicaciones biyectivas distintas,
con la operación composición de funciones tiene ESTRUCTURA ALGEBRAICA DE GRUPO"""

#asignamos los valores del conjunto X mediante una lista
X = [1, 2, 3]                               

#definimos las funciones que no haran falta en la demostracion
def f(x):
    """
    definimos la funcion f, que es un elemento de S3 por ser aplicacion biyectiva.

    args:
        x: x es lo que sea

    return:
        retorna lo que sea
    """
    if x == 1 :             #si x=1
        return  2           #entonces f(x=1)=2
    elif x== 2 :
        return  3
    else :
        return  1
         

def g(y):
    """
    definimos la función g, otro elemento de S3..

    args:
        y: y es lo que sea

    return:
        retorna lo que sea
    """
    if y == 1 :
        return 2
    elif y == 2 :
        return 1
    else :
        return 3

def abeliano(elemento):
    """definimos una funcion para saber si la operacion hace que los elementos
    conmunren cuando operan entre si"""
    """operamos los dos elementos de S3, f compuesta con g : g(f(x))
    preimero se llama a la funcion f(x) y despues a la g(y)"""
    composicion_gf = g(f(elemento))             
    print("f compuesta con g es g(f(elemento)) = " + str(composicion_gf))
    composicion_fg = f(g(elemento))
    # conmutamos la operacion, g compuesta con f : f(g(x))
    print("g compuesta con f es f(g(elemento)) = " + str(composicion_fg))
    return composicion_gf == composicion_fg

"""escribimos el script propiamente dicho usando las funciones anteriores"""
if __name__ == "__main__":
    # introducimos por teclado uno de los elementos de X
    print("introduce un elemento de X={1, 2, 3} = ")
    elemento = int(input())

    # comprobamos si los elementos del conjunto S3 cumplen la propiedad conmutativa
    if  abeliano(elemento):
        print(" El conjunto S3 es ABELIANO")
    else :
        print(" El conjunto S3 no es ABELIANO, ya que g(f(elemento) no es igual a f(g(elemento))")