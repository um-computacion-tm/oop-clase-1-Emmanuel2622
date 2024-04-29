from persona import Persona1
from persona2 import Persona2

if __name__ == '__main__':

    def mostrar_persona1():
        print("Persona1")
        persona = Persona1("Pepe", "Jose", 54715076)
        print(persona.mostrar_datos())

    def mostrar_persona2():
        print("Persona2")
        persona = Persona2("Camila", "Cerati", 71507612)
        print(persona.mostrar_datos())

    mostrar_persona1()
    mostrar_persona2()