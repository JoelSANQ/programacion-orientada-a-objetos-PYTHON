class Personaje:
    # Definición de atributos iniciales comentados
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    # Indicar que no se haga nada en este momento

    # Constructor para inicializar atributos
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-defensa:", self.defensa)
        print("-vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def vivo(self):
        return self.vida > 0

    def muerto(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        #return self.muerto <= 0
    
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño=self.dañar(enemigo)
        enemigo.vida = enemigo.vida-daño
        print(self.nombre, "a realizado", daño, "puntos de daño a" , enemigo.nombre)
        print("vida de" , enemigo.nombre, "Es", enemigo.vida)

# Creación del objeto mi_personaje
mi_personaje = Personaje("homero simpson", 1000, 3, 70, 100,)
mi_personaje.imprimir_atributos()
mi_personaje.subir_nivel(10, 1, 5)
mi_personaje.imprimir_atributos()
mi_enemigo = Personaje("Ned flanders", 70, 30,70,100)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.imprimir_atributos()

print(mi_personaje.dañar(mi_enemigo))
print(mi_personaje.vivo())
print(mi_personaje.muerto())

# Sobreescritura de atributos (comentada en este caso)
# mi_personaje.nombre = "elbarto"
# mi_personaje.fuerza = 3000
# mi_personaje.inteligencia = 2
# mi_personaje.defensa = 2
# mi_personaje.vida = 2



