class Profesor:
    def __init__(self, nombre, email):
        self.__nombre__ = nombre
        self.__email__ = email
        
    def tu_nombre(self):
        return self.__nombre__
    def tu_email(self):
        return self.__email__

class Alumno:
    def __init__(self, nombre):
        self.__nombre__ = nombre
        self.__inasistencias__ = 0     
        self.__mentor__ = None
        self.__dieta__ = ""

    def mentoria(self, profesor):
        self.__mentor__ = "El mentor de " + self.__nombre__ + " es el profesor " + profesor

    def faltas(self):
        self.__inasistencias__ += 1
    
    def esta_libre(self):
        if self.__inasistencias__ >= 5:
            return "El alumno " + self.__nombre__ + " Esta Libre."   
        else:
            return "El alumno " + self.__nombre__ + " no esta libre."

    def tu_nombre(self):
        return self.__nombre__
    
    def elegir_dieta(self, dieta):
        self.__dieta__ = "Dieta del alumno " + self.__nombre__ + ": " + dieta
    
    def es_vegano(self):
        self.__dieta__ = "El alumno " + self.__nombre__ + " es Vegano"
    
        
prof_elio = Profesor("Elio", "elio@gmail.com")
prof_gabi = Profesor("Gabriel", "gabi@gmail.com")

alumn_elio = Alumno("Elio")
alumn_pedro = Alumno("Pedro")
alumn_jose = Alumno("Jose")

alumn_elio.faltas()
alumn_elio.faltas()
alumn_elio.faltas()
alumn_elio.faltas()
alumn_elio.faltas()
print(alumn_elio.esta_libre())

alumn_pedro.faltas()
print(alumn_pedro.esta_libre())

alumn_pedro.elegir_dieta("Celiaco")
print(alumn_pedro.__dieta__)

alumn_jose.es_vegano()
print(alumn_jose.__dieta__)

alumn_jose.mentoria(prof_gabi.tu_nombre())
print(alumn_jose.__mentor__)
#import ipdb; ipdb.set_trace()