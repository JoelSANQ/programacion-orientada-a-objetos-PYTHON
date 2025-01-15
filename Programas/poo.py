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
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-defensa:", self.__defensa)
        print("-vida:", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def vivo(self):
        return self.__vida > 0

    def muerto(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
        #return self.muerto <= 0
    
    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño=self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida-daño
        if daño <= 0:  # Caso donde la fuerza no supera la defensa
            print(f"{self.__nombre} no pudo atravesar la defensa de {enemigo.__nombre}.")
        else:
            enemigo.__vida -= daño
            print(f"{self.__nombre} ha realizado {daño} puntos de daño a {enemigo.__nombre}.")
            if enemigo.__vida <= 0:
                enemigo.muerto()
            else:
                print(f"La vida de {enemigo.__nombre} ahora es {enemigo.__vida}.")
    
    def get_fuerza(self):
            return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0 :
            print("error")
        self.__fuerza = fuerza

            

# Creación del objeto mi_personaje
mi_personaje = Personaje("homero simpson", 1000, 3, 70, 100)
#mi_personaje.imprimir_atributos()
#mi_personaje.subir_nivel(10, 1, 5)
#mi_personaje.imprimir_atributos()
mi_enemigo = Personaje("Ned flanders", 70, 30,70,100)
#mi_personaje.fuerza
#mi_personaje.fuerza = 0
#mi_personaje.imprimir_atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.imprimir_atributos()
mi_personaje.set_fuerza(-5)
print(mi_personaje.set_fuerza())

#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.vivo())
#print(mi_personaje.muerto())

# Sobreescritura de atributos (comentada en este caso)
# mi_personaje.__nombre = "elbarto"
# mi_personaje.__fuerza = 3000
# mi_personaje.__inteligencia = 2
# mi_personaje.__defensa = 2
# mi_personaje.__vida = 2



