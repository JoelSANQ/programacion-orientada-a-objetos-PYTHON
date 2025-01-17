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

class Guerrero(Personaje):
    #sobreescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    #sobreescribir impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)
    def elegir_arma(self):
        opcion= int(input("elige un arma: \n (1)Lanza de obsidiana, daño 10 (2) lanza de chaya, daño(5)\n>>>>>>>>"))
        if opcion ==1:
            self.espada = 10

        elif opcion ==2:
            self.espada = 8
        else:
            self.elegir_arma()

    #sobreescribir calculo de daño
def daño (self, enemigo):
    return self.fuerza*self.espada - enemigo.defensa

class MAGO(Personaje):
    #sobreescribir constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #sobreescribir impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.libro)
    def elegir_arma(self):
        opcion= int(input("elige un arma: \n (1)hechizos de ensamblador, daño 10 (2) recetario de chaya, daño(2)\n>>>>>>>>"))
        if opcion ==1:
            self.libro = 10

        elif opcion ==2:
            self.libro = 8
        else:
            self.elegir_arma()

def daño (self, enemigo):
    return self.arma*self.arma - enemigo.defensa


            


michael_jackson = Personaje("michael jackson", 20,15,30,100,)
tlatoani = Guerrero("tlatoani", 50,70,30,100,5)
merlin = MAGO("merlin", 50,70,30,100,5)

#tlatoani.elegir_arma()
#merlin.elegir_arma
michael_jackson.atacar(tlatoani)
tlatoani.atacar(merlin)
merlin.atacar(michael_jackson)


#imprimir atributos antes de la tragedia
tlatoani.imprimir_atributos()
merlin.imprimir_atributos()
michael_jackson.imprimir_atributos()


# Creación del objeto mi_personaje
# mi_personaje = Personaje("homero simpson", 1000, 3, 70, 100,)
# mi_personaje.imprimir_atributos()
# mi_personaje.subir_nivel(10, 1, 5)
# mi_personaje.imprimir_atributos()
# mi_enemigo = Personaje("Ned flanders", 70, 30,70,100)
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.imprimir_atributos()

# print(mi_personaje.dañar(mi_enemigo))
# print(mi_personaje.vivo())
# print(mi_personaje.muerto())

# Sobreescritura de atributos (comentada en este caso)
# mi_personaje.nombre = "elbarto"
# mi_personaje.fuerza = 3000
# mi_personaje.inteligencia = 2
# mi_personaje.defensa = 2
# mi_personaje.vida = 2

