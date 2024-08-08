import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import Conexion
import io


class Persona:
    def __init__(self, nombre, apellido, edad, dni, nacionalidad, numero, descripcion, foto=None, fecha=None, hora=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.nacionalidad = nacionalidad
        self.numero = numero
        self.descripcion = descripcion
        self.foto = foto
        self.fecha = fecha
        self.hora = hora

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, nueva_fecha):
        self._fecha = nueva_fecha
    # Métodos get y set para hora
    def get_hora(self):
        return self._hora

    def set_hora(self, nueva_hora):
        self._hora = nueva_hora


def generar_codigo_qr(dni, output_path): # recibe los valores de los datos personales
    try:
        # Crear el código QR con los datos personales
        qr = qrcode.QRCode( # Establecemos los paremetros de Qr
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        #Convierte el diccionario datos_personales en una cadena de texto donde cada clave y valor se representan en una línea separada.
        
        qr.add_data(dni) # Agrega los datos a la instancia de Qrcode
        qr.make(fit=True) # Crea el qr

        # Crear una imagen del código QR
        img = qr.make_image(fill_color="black", back_color="white") 
    
        # Guardar la imagen resultante
        img.save(output_path)

        print("Código QR generado con éxito.")
    except Exception as e:
        print(f"Error al generar el código QR: {e}")

class GeneradorQRApp: # Clase principal.
    def __init__(self, root): # Creamos una nueva instancia de tipo root.
        self.root = root # Almacena la ventana principal de la aplicación.
        self.root.title("FORMULARIO DE REGISTRO") # Asignamos un titulo a la ventana.
        self.root.geometry("390x600")
        self.root.resizable(0,0)
        self.root.config(bd=10)

        # Metodo para configurar interfaz gráfica.
        self.setup_gui() 

    # Funcion de la creacion de la ventana principal.
    def setup_gui(self):
        
        # TITULO
        label = tk.Label(self.root, text="REGISTRO DE USUARIO", fg="black",font=("Comic Sans",13,"bold"),pady=2)
        label.pack()
        
        # LOGO
        imagen_usuario = Image.open("logo.png")
        nueva_imagen = imagen_usuario.resize((40,40))
        render = ImageTk.PhotoImage(nueva_imagen)
        label = tk.Label(self.root, image=render) 
        label.image = render
        label.pack(pady=1)
        
        # Etiquetas y entradas para los datos
        label = tk.Label(self.root, text="Nombre:") # Crea una etiqueta le dan la referencia de la ventana, nombre y la posisicion.
        label.pack()
        self.nombre_entry = tk.Entry(self.root) # Declara una variable donde se guardara lo que se ingrese en la caja de texto.
        self.nombre_entry.pack() #   

        label = tk.Label(self.root, text="Apellidos:")
        label.pack()
        self.apellidos_entry = tk.Entry(self.root)
        self.apellidos_entry.pack()

        label = tk.Label(self.root, text="Edad:")
        label.pack()
        self.edad_entry = tk.Entry(self.root)
        self.edad_entry.pack()

        label = tk.Label(self.root, text="DNI:")
        label.pack()
        self.dni_entry = tk.Entry(self.root)
        self.dni_entry.pack()

        label = tk.Label(self.root, text="Nacionalidad:")
        label.pack()
        self.nacionalidad_entry = tk.Entry(self.root)
        self.nacionalidad_entry.pack()

        label = tk.Label(self.root, text="Número:")
        label.pack()
        self.numero_entry = tk.Entry(self.root)
        self.numero_entry.pack()

        label = tk.Label(self.root, text="Descripción:")
        label.pack()
        self.descripcion_entry = tk.Entry(self.root)
        self.descripcion_entry.pack()

        # Botón para seleccionar la foto
        boton = tk.Button(self.root, text="Seleccionar Foto", command=self.seleccionar_foto, height=1,width=20,bg="wheat1")
        boton.pack(pady=5, padx=10)
        # Crea un boton, le asigna la ventana, le da un nombre, la accion al presionar, le da una posicion.

        # Botón para generar el código QR
        boton_1 = tk.Button(self.root, text="Generar Código QR", command=self.generar_qr, height=1,width=20,bg="sky blue")
        boton_1.pack(pady=5, padx=10) # Estos son parámetros que especifican el espacio de relleno vertical (pady) y horizontal (padx)
        # Crea un boton, le asigna la ventana, le da un nombre, la accion al presionar, le da una posicion.

    #def imagenAbinary(image_path):
     #   with open(image_path, 'rb') as image_file:
      #      binary_data = image_file.read()
       #     return binary_data

    # Funcion para seleccionar foto.
    def seleccionar_foto(self):
        # Abrir archivero para seleccionar la foto en los formatos seleccionados.
        file_path = filedialog.askopenfilename(filetypes=[("Imagen", "*.png;*.jpg;*.jpeg")]) # Guarda la ruta de la imagen.
        
        # Mostrar la foto seleccionada en la interfaz.
        if file_path: # ¿Esta vacia? , de contrario ejecuta lo de adentro.
            # Abrir la foto seleccionada con la biblioteca PIL (Pillow).
            foto = Image.open(file_path)
            # Redimensionar la foto a 100x100 píxeles, mejora la calidad de la imagen.
            foto = foto.resize((100, 100), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else 2)
            # Convertir la foto a un formato compatible con Tkinter para poder mostrarla en la ventana.
            self.foto_tk = ImageTk.PhotoImage(foto)

            buffer = io.BytesIO()
            foto.save(buffer, format="JPEG")
            bytes_imagen = buffer.getvalue()
            self.ph = bytes_imagen

            # Mostrar la foto en un Label.
            foto_label = tk.Label(self.root, image=self.foto_tk) # Crea el label e inserta la foto
            foto_label.pack()
            
            
    
    
    # Funcion para generar Qr.
    def generar_qr(self):
        
        pe = Persona(
            nombre = self.nombre_entry.get(),
            apellido = self.apellidos_entry.get(),
            edad = self.edad_entry.get(),
            dni = self.dni_entry.get(),
            nacionalidad= self.nacionalidad_entry.get(),
            numero = self.numero_entry.get(),
            descripcion= self.descripcion_entry.get(),
            foto= self.ph,
            fecha = "00/00/0000",
            hora = "00:00"
        )
        
        con = Conexion.conexion_base()
        if con:
            Conexion.insertar_datos(con, pe.nombre, pe.apellido, pe.edad, pe.dni, pe.nacionalidad, pe.numero, pe.descripcion, pe.foto)

        
        # Generar el código QR utilizando los datos proporcionados
        #if 'foto' in pe: # Verifica si la foto esta presente 
            ruta_salida_qr = 'qr.jpg'  # Reemplaza con la ruta de salida deseada
            generar_codigo_qr(pe.dni, ruta_salida_qr)
            messagebox.showinfo("Información","Código QR generado con éxito y guardado los datos.")
        #else:
            #messagebox.showerror("Error", "Por favor, seleccione una foto antes de generar el código QR.")

# MAIN
if __name__ == "__main__":
    root = tk.Tk() # Se crea la ventana principal
    app = GeneradorQRApp(root) #  Se instancia la clase GeneradorQRApp y se le pasa la ventana principal
    root.mainloop() #  Inicia el bucle principal para manejar eventos de la interfaz de usuario

