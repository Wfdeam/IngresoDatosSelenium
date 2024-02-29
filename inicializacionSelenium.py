from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

class inicioSelenium():

    try:
        def __init__(self, paginaWeb, nombre, correo, direccionActual, submitButton, direccionPermanente, df):
            self.driver = webdriver.Edge()
            self.correoXpath = correo
            self.paginaWeb = paginaWeb
            self.nombre = nombre
            self.direccionActual = direccionActual
            self.direccionPermanente = direccionPermanente
            self.submitButton = submitButton
            self.df = df

        def inicioSesion(self):
            #Se expande la ventana del navegador
            self.driver.maximize_window()
            # Abre la página de Google
            self.driver.get(self.paginaWeb)

        def ingresodatos(self,nombreAIngressar, correoElectronico, direccion, direccionPersonal):

            #ingreso de los datos a la plataforma
            self.driver.find_element(by='xpath', value=self.nombre).send_keys(nombreAIngressar)
            self.driver.find_element(by='xpath', value=self.correoXpath).send_keys(correoElectronico)
            self.driver.find_element(by='xpath', value=self.direccionActual).send_keys(direccion)
            self.driver.find_element(by='xpath', value=self.direccionPermanente).send_keys(direccionPersonal)
            print(".....Todos los datos fueron ingresados.....")
            self.driver.execute_script("window.scrollTo(0,500)")
            self.driver.find_element(by='xpath', value=self.submitButton).click()
            print(".....El click se realizó completamente.....")
            time.sleep(5)
            self.driver.refresh()
            
        
        def fin(self):
            self.driver.close()

    except Exception as e:
        print(f'el error generado es {e}')

