class Persona1:
    def __init__(self, nombre: str = "Jose", apellido: str = "Maria", dni: int = 45715063):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni
    
    def mostrar_datos(self):
        print(
            "Nombre:",self.__nombre__,
            "Apellido:", self.__apellido__,
            "DNI:", self.__dni__
            )