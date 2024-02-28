from dotenv import load_dotenv 
import os 
from inicializacionSelenium import inicioSelenium
from lecturaDatos import lecturaPersonal

#Se cargan los datos del .env
load_dotenv() 

if __name__ == "__main__":
    try:
        #Se obtienen los xpath del ambiente
        
        nombre = os.getenv('nameXpath')
        correo = os.getenv('emailXpath')
        direccionActual = os.getenv('direccionActual')
        direccionPermanente = os.getenv('direccionPermanente')
        submitButton = os.getenv('submit')

        #Se obtiene la url del ambiente
        paginaWeb = os.getenv('pagina')
        paginaWeb = "https://demoqa.com/text-box"

        #Se obtiene la ruta del archivo del ambiente
        rutaArchivo = os.getenv('rutaArchivo')

        #Se realiza la lectura de los datos
        lecturaDatos = lecturaPersonal(rutaArchivo)
        df = lecturaDatos.lecturaCSV()

        print('.....lectura cvs completa.....')

        #Se envian los valores a la clase que contiene la apertura del navegador
        inicializacionSelenium = inicioSelenium(paginaWeb, nombre, correo, direccionActual, submitButton, direccionPermanente, df)
        #Se llama la funcion que abre el navegados
        inicializacionSelenium.inicioSesion()
        print('.....Inicio browswer completo.....')
        for indice, fila in df.iterrows():
            nombreAIngressar = fila['nombre']
            print(f'el nombre a ingresar es {nombreAIngressar}')
            correoElectronico = fila['correo']
            print(correoElectronico)
            direccion = fila['direccion']
            print(direccion)
            direccionPersonal = fila['direccionPermanente']
            print(direccionPersonal)
            inicializacionSelenium.ingresodatos(nombreAIngressar, correoElectronico, direccion, direccionPersonal)
            print('.....Ingreso de datos.....')
        inicializacionSelenium.fin()
        print('.....fin......')
    except Exception as e:
        print(e)
