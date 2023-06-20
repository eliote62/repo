class Personaje:  # creamos las clase (objeto) Personaje
    """nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0"""

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):  # constructor
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".fuerza:", self.fuerza)
        print(".inteligencia:", self.inteligencia)
        print(".defensa:", self.defensa)
        print(".vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño,
              "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


mi_personaje = Personaje("Eliote", 10, 1, 5, 100)
# print("el nombre del jugador es", mi_personaje.nombre)
# print("la fuerza del jugador es", mi_personaje.fuerza)
mi_enemigo = Personaje("Dragon", 8, 5, 3, 100)
"""mi_personaje.atributos()
mi_personaje.subir_nivel(1, 2, 0)
mi_personaje.atributos()
print(mi_personaje.esta_vivo())
mi_personaje.morir()"""
# print(mi_personaje.daño(mi_enemigo))
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
