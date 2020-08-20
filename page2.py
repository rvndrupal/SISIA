from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from funciones import *
from excel import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from datetime import timedelta
import string


class Sisia(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_dos(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        hoja = "Hoja4"
        rows = fe.getRowCount(path, hoja)
        for r in range(3, rows + 1):
            user = fe.readData(path, "Hoja4", r, 1)
            passw = fe.readData(path, "Hoja4", r, 2)
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@href='/administracion-planeacion']")
            f.Click("//a[contains(.,'Registro de Programa')]")
            f.tiempo(.5)

            #Seleccion Campaña
            ind3 = fe.readData(path, "Hoja4", r, 3)
            presu = fe.readData(path, "Hoja4", r, 4)

            f.combo_index("//select[@id='proyectoCampana']",ind3)
            f.combo_index("//select[@formcontrolname='presupuestoRadio']",presu)


            #Datos Generales
            fi = datetime.now()
            fi = fi.strftime('%d/%m/%Y')
            fii =  str(fi)
            fecha2 = fe.readData(path, "Hoja4", r, 5)
            fechaf = datetime.now() + timedelta(days=fecha2)
            fechaf = fechaf.strftime('%d/%m/%Y')
            tg = fe.readData(path, "Hoja4", r, 6)


            f.scrolling(300)
            f.Click("//a[contains(.,'Datos Generales')]")
            f.tiempo(1)
            f.texto("//input[@id='fecha_inicial']",fii)
            f.texto("//input[@id='fecha_termino']",fechaf)
            f.scrolling(100)
            f.texto("//textarea[@formcontrolname='introduccion']",tg)
            f.texto("//textarea[@formcontrolname='objetivo_general']",tg)
            f.texto("//textarea[@formcontrolname='objetivo_particular']",tg)
            f.texto("//textarea[@formcontrolname='justificacion']",tg)
            f.texto("//textarea[@formcontrolname='viabilidad']",tg)
            f.texto("//textarea[@formcontrolname='prioridad']",tg)
            f.texto("//textarea[contains(@formcontrolname,'sanitario')]",tg)
            f.texto("//textarea[@formcontrolname='proyeccion']",tg)
            f.texto("//textarea[@formcontrolname='riesgo_accion']",tg)
            f.texto("//textarea[contains(@formcontrolname,'resultado_esperado')]",tg)
            #falta guardar


            #poblacion,estatus
            ind6 = fe.readData(path, "Hoja4", r, 7)
            f.scrolling(-1400)
            f.tiempo(1)
            f.Click("//a[contains(.,'Población, Estatus Fitozoosanitario y Localización de Acciones Programadas')]")
            f.scrolling(180)
            f.combo_index("//select[contains(@title,'Municipio')]",ind6)
            f.tiempo(.7)
            f.combo_index("//select[contains(@title,'Unidad de medida')]",ind3)
            f.combo_index("(//select[@formcontrolname='cultivoEspecie'])[1]",ind6)










            #SALIR
            '''
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)
            '''







    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")


if __name__ == '__main__':
    unittest.main()








