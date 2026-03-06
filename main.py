# Clase Persona
class Persona:
    nombre=""
    edad=0
    altura=0
    genero=""

    def __init__(self, atr_nombre,atr_edad,atr_altura,atr_genero):
        self.nombre = atr_nombre
        self.edad=atr_edad
        self.altura=atr_altura
        self.genero=atr_genero

    def caminar(self):
        return f'Hola soy {self.nombre} Me encuentro Caminado'
    
    def __str__(self):
        return f'Hola soy {self.nombre} tengo la edad de {self.edad} y mido {self.altura} mi genero es: {self.genero}'
 # Persona -> Objeto   Persona-> Clase

personas_encuestadas=[]
op=""
while True:
    op=int(input("""Escoge la opción
                  1. Ingresar Datos
                  2. Ver el listado
                  0. Salir
                  """))


    if op == 0:
        break

    if op == 1:
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese Edad: "))
        altura=float(input("Ingrese la Altura :"))
        genero=input("Ingresar el Gerero: ")

        persona=Persona(nombre,edad,altura,genero)

        personas_encuestadas.append(persona)

        
    if op == 2:
        for persona in personas_encuestadas:
            print(persona)
        

