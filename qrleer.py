import cv2
import tkinter as tk #para las interfaces
from PIL import Image, ImageTk #trabajar con imagenes(Pillow)
import datetime
import GeneradorQR 
import Conexion
from io import BytesIO

def update_frame():
    ret, frame = capture.read() #lee lo que captura la imagen
    frame = cv2.resize(frame, (480, 400), interpolation=cv2.INTER_AREA) # dimensionamos el frame a 640x480 píxeles
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame) #detectar y decodificar códigos QR en el frame.

    # Obtener la fecha actual
    fecha_actual = datetime.date.today()
    # Obtener la hora actual
    hora_actual = datetime.datetime.now().time()

    con = Conexion.conexion_base()
    if con:
        consulta = Conexion.leer_dato_por_llave(con, data)
    
    if consulta:    #Si se detecta un código QR y contiene información, imprime el dato y actualiza el texto
        resultados=[]
        
        for fila in consulta:
            print(f'Dato: {fila}')
            resultados.append(fila)

        dic = {
            'Dni' : resultados[0],
            'Nombres': resultados[1],
            'Apellidos' : resultados[2],
            'Nacionalidad' : resultados[3],
            'Numero' : resultados[4],
            'Descripcion' : resultados[5],  
            'Edad': resultados[7],
            'Fecha' : fecha_actual,
            'Hora' : hora_actual
        }
    
        
        imagen = Image.open(BytesIO(resultados[6]))
        # Convertir la foto a un formato compatible con Tkinter para poder mostrarla en la ventana.
        foto_tk = ImageTk.PhotoImage(imagen)
        
        text_resultados = '\n'.join([f"{key}: {value}" for key, value in dic.items()] )
        concatenar = f"{text_resultados}\nFoto:"
        label_info = tk.Label(info_label, text=concatenar)
        label_info.pack()
        label_foto = tk.Label(info_label, image=foto_tk)
        label_foto.pack()
    else:
        info_label.config(text='No QR Code detected')
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    photo = ImageTk.PhotoImage(image=image) #Convierte la imagen a un formato compatible con Tkinter
    video_label.config(image=photo) #Actualiza el contenido de video_label con la nueva imagen.
    video_label.image = photo
    video_label.after(10, update_frame) #Programa  la función update_frame para ejecutarse nuevamente después de 10 milisegundos.

root = tk.Tk()
root.title("DETECTOR DE QR") #Crea la ventana principal

capture = cv2.VideoCapture(0) #Inicia la captura de video desde la cámara (en este caso, la cámara con índice 0)
qrDetector = cv2.QRCodeDetector() #detectar y decodificar códigos QR en imágenes

video_label = tk.Label(root)
video_label.pack()

info_label = tk.Label(root, text='No QR Code detected', font=('Helvetica', 12))
info_label.pack()

update_frame() # inicia el bucle de actualización del video.

root.mainloop() #mantener la interfaz gráfica en ejecución y permitir la interacción continua del usuario con la aplicación 

capture.release()
cv2.destroyAllWindows()