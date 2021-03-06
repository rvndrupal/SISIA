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
        cls.driver.implicitly_wait(8)
        cls.driver.maximize_window()

    def test_login(self):
        ti = .1
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        hoja = "Hoja3"
        rows = fe.getRowCount(path, hoja)
        for r in range(1, rows + 1):
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            mision = fe.readData(path, "Hoja3", r, 10)
            vision = fe.readData(path, "Hoja3", r, 11)
            fecha = fe.readData(path, "Hoja3", r, 12)
            fecha2 = datetime.now() + timedelta(days=fecha)
            fecha2 = fecha2.strftime('%d/%m/%Y')
            registro = str(fe.readData(path, "Hoja3", r, 13))
            telefono = str(fe.readData(path, "Hoja3", r, 14))
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            rt = random.choice(sample_letters)
            r = random.randint(1, 9)
            rfc = str(fe.readData(path, "Hoja3", r, 15))
            rfcc = rfc + rt + str(r)
            curp = str(fe.readData(path, "Hoja3", r, 16))
            curpp = curp + rt + str(r)
            presidente = str(fe.readData(path, "Hoja3", r, 17))
            secretario = str(fe.readData(path, "Hoja3", r, 18))
            tesorero = str(fe.readData(path, "Hoja3", r, 19))
            pdf1 = str(fe.readData(path, "Hoja3", r, 20))
            pdf2 = str(fe.readData(path, "Hoja3", r, 21))
            pdf3 = str(fe.readData(path, "Hoja3", r, 22))

            # Seccion Personal
            nom = str(fe.readData(path, "Hoja3", r, 23))
            ap = str(fe.readData(path, "Hoja3", r, 24))
            am = str(fe.readData(path, "Hoja3", r, 25))
            email = str(fe.readData(path, "Hoja3", r, 26))
            puesto = str(fe.readData(path, "Hoja3", r, 27))
            costo = str(fe.readData(path, "Hoja3", r, 28))
            laboral = str(fe.readData(path, "Hoja3", r, 29))

            # instalacion
            instalacion = str(fe.readData(path, "Hoja3", r, 30))
            descripcion = str(fe.readData(path, "Hoja3", r, 31))
            calle = str(fe.readData(path, "Hoja3", r, 32))
            colonia = str(fe.readData(path, "Hoja3", r, 33))
            cp = str(fe.readData(path, "Hoja3", r, 34))
            estado = str(fe.readData(path, "Hoja3", r, 35))

            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            f.Click("//a[@href='/recursos-humanos-materiales']")
            f.scrolling(300)
            f.texto("//textarea[@formcontrolname='mision']", mision)
            f.texto("//textarea[contains(@formcontrolname,'vision')]", vision)
            f.texto("(//input[contains(@formcontrolname,'fecha')])[1]", fecha2)
            f.combo_texto("(//select[contains(@formcontrolname,'anioRegistro')])[2]", registro)
            f.texto("(//input[contains(@type,'text')])[7]", telefono)
            f.texto("(//input[@formcontrolname='rfc'])[2]", rfcc)
            f.tiempo(1)
            f.texto("(//input[contains(@type,'text')])[9]", curpp)
            f.tiempo(1)
            f.texto("(//input[contains(@maxlength,'80')])[1]", presidente)
            f.texto("(//input[contains(@maxlength,'80')])[2]", secretario)
            f.texto("(//input[@maxlength='80'])[3]", tesorero)
            f.scrolling(600)
            f.upload("(//input[contains(@type,'file')])[1]", pdf1)
            f.upload("(//input[contains(@type,'file')])[2]", pdf2)
            f.upload("(//input[contains(@type,'file')])[3]", pdf3)
            # falta guardar
            f.scrolling(-1400)
            f.tiempo(1)

            # Sección personal
            f.Click("(//a[@data-toggle='tab'])[2]")
            f.tiempo(1)
            f.scrolling(300)
            f.texto("(//input[contains(@formcontrolname,'nombre')])[1]", nom)
            f.texto("//input[@formcontrolname='paterno']", ap)
            f.texto("//input[contains(@formcontrolname,'materno')]", am)
            f.texto("(//input[contains(@formcontrolname,'rfc')])[1]", rfcc)
            f.texto("//input[contains(@formcontrolname,'curp')]", curpp)
            res = f.Validar_Elemento_xpat(
                "//span[@class='help-block'][contains(.,'El curp está compuesto por 18 caracteres')]")
            if (res == True):
                {
                    f.texto("//input[contains(@formcontrolname,'curp')]", curpp)
                }
            f.texto("//input[contains(@formcontrolname,'correo')]", email)
            f.texto("(//input[@formcontrolname='telefono'])[1]", telefono)
            f.scrolling(550)
            f.tiempo(1)
            f.combo_index("//select[@formcontrolname='puesto']", puesto)
            f.texto("//input[contains(@formcontrolname,'costoMensual')]", costo)
            f.combo_index("//select[contains(@formcontrolname,'ubicacionLaboral')]", laboral)
            f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[1]")
            f.tiempo(1)
            f.Click("//button[@class='btn btn-default'][contains(.,'Entendido')]")
            f.tiempo(1)
            f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[1]")
            f.tiempo(8)

            # instalacion
            '''
            f.scrolling(-1400)
            f.tiempo(1)
            f.Click("(//a[contains(@data-toggle,'tab')])[3]")
            f.tiempo(1)
            f.scrolling(300)
            f.combo_index("//select[contains(@formcontrolname,'tipoInstalacion')]",instalacion)
            f.combo_index("//select[contains(@formcontrolname,'nombreResponsable')]",1)
            f.texto("(//textarea[contains(@formcontrolname,'descripcion')])[1]",descripcion)
            f.texto("//input[contains(@formcontrolname,'calle')]",calle)
            f.texto("//input[contains(@formcontrolname,'colonia')]",colonia)
            f.texto("//input[@formcontrolname='cp']",cp)
            f.combo_index("//select[@formcontrolname='estado']",estado)
            f.tiempo(2)
            f.combo_index("//select[contains(@formcontrolname,'municipio')]",estado)
            f.tiempo(5)
            f.combo_index("//select[contains(@formcontrolname,'localidad')]",estado)
            f.tiempo(80)
            f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[2]")
            f.tiempo(2)
            f.Click("//button[@class='btn btn-default'][contains(.,'Entendido')]")
            f.scrolling(700)
            f.tiempo(10)
            #Falta Guardar
            '''

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")


if __name__ == '__main__':
    unittest.main()








