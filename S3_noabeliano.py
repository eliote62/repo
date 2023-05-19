# DEMOSTRACION mediante el metodo del CONTRAEJEMPLO del TEOREMA DE TEORIA DE GRUPOS:
# dado un conjunto finito X con n elementos, el GRUPO SIMETRICO Sn con n>=3, cuyos elementos son las
# aplicaciones biyectivas entre los elementos de X

# tomamos un conjunto finito X con 3 elementos, que cumple la condicion del teorema n>=3
X = [1, 2, 3] 

def f(x):
    """
    definimos la funcion f, que es un elemento de S3 por ser aplicacion biyectiva.

    args:
        x: x es lo que sea

    return:
        retorna lo que sea
    """
    if x == 1 :
        return  2
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
    # operamos los dos elementos de S3, f compuesta con g : g(f(x))
    composicion_gf = g(f(elemento))
    print("f compuesta con g es g(f(elemento)) = " + str(composicion_gf))
    composicion_fg = f(g(elemento))
    # conmutamos la operacion, g compuesta con f : f(g(x))
    print("g compuesta con f es f(g(elemento)) = " + str(composicion_fg))
    return composicion_gf == composicion_fg

if __name__ == "__main__":
    # introducimos por teclado uno de los elementos de X
    print("introduce un elemento de X={1, 2, 3} = ")
    elemento = int(input())

    # comprobamos si los elementos del conjunto S3 cumplen la propiedad conmutativa
    if  abeliano(elemento):
        print(" El conjunto S3 es ABELIANO")
    else :
        print(" El conjunto S3 no es ABELIANO, ya que g(f(elemento) no es igual a f(g(elemento))")