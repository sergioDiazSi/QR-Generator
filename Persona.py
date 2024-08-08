class Persona:
    def __init__(self, nombre, apellido, edad, dni, nacionalidad, numero, descripcion, foto=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.nacionalidad = nacionalidad
        self.numero = numero
        self.descripcion = descripcion
        self.foto = foto

    def __str__(self):
        return f"Persona: {self.nombre} {self.apellido}\nEdad: {self.edad}\nDNI: {self.dni}\nNacionalidad: {self.nacionalidad}\nNúmero: {self.numero}\nDescripción: {self.descripcion}\nFoto: {self.foto}"

# Crear una instancia de la clase Persona con una foto de ejemplo
persona_ejemplo = Persona(
    nombre='NA',
    apellido='NA',
    edad=100,
    dni='12345678',
    nacionalidad='Peruana',
    numero='123456789',
    descripcion='zzzzz',
    foto='xxxxxxxxxx'
)

# Imprimir la información de la persona
print(persona_ejemplo)
