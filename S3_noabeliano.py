#DEMOSTRACION mediante el metodo del CONTRAEJEMPLO del TEOREMA DE TEORIA DE GRUPOS:
#dado un conjunto finito X con n elementos, el GRUPO SIMETRICO Sn con n>=3, cuyos elementos son las
#aplicaciones biyectivas entre los elementos de X

X = [1, 2, 3] #tomamos un conjunto finito X con 3 elementos, que cumple la condicion del teorema n>=3

def f(x):               #definimos la funcion f, que es un elemento de S3 por ser aplicacion biyectiva
    if x == 1 :
        resultado = 2
    elif x== 2 :
        resultado = 3
    else :
        resultado = 1
    return resultado     
def g(y):               #definimos la función g, otro elemento de S3.
    if y == 1 :
        resultado = 2
    elif y == 2 :
        resultado = 1
    else :
        resultado = 3
    return resultado
print("introduce un elemento de X={1, 2, 3} = ")   
elemento = int(input())                                 #introducimos por teclado uno de los elementos de X

composicion_gf = g(f(elemento))                        #operamos los dos elementos de S3, f compuesta con g : g(f(x))
print("f compuesta con g es g(f(elemento)) = " + str(composicion_gf))
composicion_fg = f(g(elemento))
print("g compuesta con f es f(g(elemento)) = " + str(composicion_fg))                                   #conmutamos la operacion, g compuesta con f : f(g(x))

if composicion_gf == composicion_fg :                   #comprobamos si los elementos del conjunto S3 cumplen la propiedad conmutativa
    print(" El conjunto S3 es ABELIANO")
else :
    print(" El conjunto S3 no es ABELIANO, ya que g(f(elemento) no es igual a f(g(elemento))")