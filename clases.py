class Persona:
    def __init__(self, tipo_documento, numero_documento, nombres, apellidos, correo, genero, telefono):
        self.__tipo_documento = tipo_documento
        self.__numero_documento = numero_documento
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__correo = correo
        self.__genero = genero
        self.__telefono = telefono

    def get_tipo_documento(self):
        return self.__tipo_documento

    def get_numero_documento(self):
        return self.__numero_documento
    
    def get_nombres(self):
        return self.__nombres

    def get_apellidos(self):
        return self.__apellidos

    def get_correo(self):
        return self.__correo

    def get_genero(self):
        return self.__genero

    def get_telefono(self):
        return self.__telefono

    def set_genero(self, genero):
        self.__genero = genero

    def set_correo(self, correo):
        self.__correo = correo

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def hablar(self):
        print("Hola, buenos dias")

    def preguntar(self):
        pass

    def asistir(self):
        pass

    def quejarse(self):
        pass

class Profesor(Persona):

    def __init__(self, tipo_documento, numero_documento, nombres, apellidos, correo, genero, telefono, especialidad):
        super().__init__(tipo_documento, numero_documento, nombres, apellidos, correo, genero, telefono)
        self.__especialidad = especialidad

    def hablar(self):
        print("Buen dia, jovenes, sientense que vamos a empezar")

    def ensenar(self):
        print("Yo enseño")

    def calificar(self):
        print("No moleste, estoy calificando")

class Estudiante(Persona):
    def __init__(self, codigo, tipo_documento, numero_documento, nombres, apellidos, correo, genero, telefono, edad, grado):
        super().__init__(tipo_documento, numero_documento, nombres, apellidos, correo, genero, telefono)
        self.__codigo = codigo
        self.__edad = edad
        self.__grado = grado

    def hablar(self):
        print(f"Profe, soy {self.get_nombres()}, puedo ir al baño")

    def quejarse(self):
        print("Profe, no entiendo lo que dice")

    def rogar(self):
        print("Tengo 50.000 razones para pasar la materia")
        
    def set_nombres(self, nombres):
        self.__nombres = nombres
