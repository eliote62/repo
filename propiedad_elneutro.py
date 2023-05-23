"""PROPIEDAD DEL ELEMENTO NEUTRO
Este script determina si exite o no el ELEMENTO NEUTRO de un conjunto,
 en este caso el conjunto G (conjunto finito de números enteros),
 respecto de una operación, en este caso la SUMA. Tambien cuenta el numero de
 elementos NEUTROS que hay en el conjuno estudiado"""

# necesario para generar numeros random
# (https://www.mclibre.org/consultar/python/lecciones/python-biblioteca-random.html)
import random

"""PRIMERO: asignamos mediante un lista los elementos del conjunto"""


def get_conjunto(n_elems):
    """
    @brief genera un array de numeros random de longitud n_elems con valores
        enteros entre 0 y n_elems.
    @param n_elems: numero de elementos del array.
    @return list[n_elems]
    """
    # list comprehension
    # (https://www.w3schools.com/python/python_lists_comprehension.asp)
    return [random.randrange(n_elems) for _ in range(0, n_elems)]


"""SEGUNDO: definimos la operación que relaciona los elementos del conjunto, la suma"""


def sumar(a, b):
    """operacion de suma"""
    return a + b


def multiplicar(a, b):
    """operacion de multiplicar"""
    return b * a


"""TERCERO: comprobamos la definición de elemento neutro, es decir, que de manera conmutativa
la suma del neutro con cualquier otro elemento del conjunto da como resultado este elemento """


def buscar_neutros(G, op):
    """
    @brief genera un array de numeros random de longitud n_elems con valores
        enteros entre 0 y n_elems.
    @param G: conjunto de entrada.
    @param op: operacion apra la que buscar el neutro.
    @return (resultado: str, acum: int)
    """
    resultado = "neutro no encontrado para " + op.__name__
    acum = 0
    # hay mejores maneras de hacer esto, pero en este caso es suficientemente
    # legible para un script didactico
    for i in G:
        for j in G:
            if op(i, j) == j:  # op i+j=j
                if op(j, i) == j:  # conmuta la op, j+i=j, condicion para ser neutro
                    # por cada elemento neutro va a sobrescribir la variable resultado con el mimo valor
                    # lo cual es ineficiente, sin embargo es necesario continuar para calcular el acum
                    # pernsar como podria hacerse esto mejor
                    resultado = str(
                        i) + " es el ELEMENTO NEUTRO del conjunto G respecto de la operación " + op.__name__
                    acum = acum + 1

    # como necesitamos retornar 2 cosas y las funciones solo permiten retornar una sola
    # podemos devolver una tupla, una tupla es como una especie de array
    return (resultado, acum)


G = get_conjunto(10)

print(G)
# podemos desempaquetar la tupla de retorno directamente poniendo dos
# variables separadas por comas
resultado, acum = buscar_neutros(G, sumar)
print(resultado)
print("numero de elementos neutros: " + str(acum / len(G)))
print("numero de elementos neutros: " + str(acum / len(G)))

resultado, acum = buscar_neutros(G, multiplicar)
print(resultado)
print("numero de elementos neutros: " + str(acum / len(G)))
print("numero de elementos neutros: " + str(acum / len(G)))


"""DUDAS:
1.como podria programarse para un conjunto G con infinitos elementos?
    - En principio ya podria funcionar sobre un conjunto G de tamano N el
            problema es como definir los elementos de G
    - mi propuesta es encapsular la definicion del conjunto G en una funcion
        que dado un tamaño devuelva un array de elementos aleatorios con valores entre 0-tamaño
2.como podría programarse de modo más sencillo?
    - la simplicidad radica siempre en al abstraccion, oculta las partes complejas detras abstracciones (funciones)
        permite que el cuerpo principal de tu programa sea legible utilizando estas funciones
3.como podría definirse una operación arbitraria?
    - la manera mas adecuada en esta situacion es utilizando el concepto de high order (function https://www.geeksforgeeks.org/higher-order-functions-in-python/)
        una high order function es una funcion que acepta otra funcion como argumento
        - para ello rpimero encapsulamos la logica de hayar el elemento neutro en una funcion
"""

"""CAMBIOS
1. autopep8 aplicado
2. definicion de G encapsulada
3. implementacion random de definicion de conjunto G
4. encapsular logica de busqueda del elemento neutro
    - high order function
    - retornar tupla
"""

"""EJERCICIOS
1- por que multiplicar fucniona a veces mal?
2- es buena idea hayar el neutro y calcular el num de neutros en la misma funcion?
3- que pasa con la variable resultado en la funcion buscar_neutros
"""
