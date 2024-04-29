class Persona2:
    def __init__(self, nombre: str = "Julieta", apellido: str = "Miranda", dni: int = 15048322):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni
    
    def mostrar_datos(self):
        print(
            "Nombre:",self.__nombre__,
            "Apellido:", self.__apellido__,
            "DNI:", self.__dni__
            )