#import HtmlTestRunner
#from allure_commons.types import AttachmentType
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
#reporte simple python page3.py
#pytest -v -s --alluredir=C:\SISIA\reportes  C:\SISIA\page3.py
#pytest -v -s --html=report12.html --self-contained-html page3_12.py

#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py  page3_6.py page3_7.py page3_8.py page3_9.py page3_10.py page3_11.py page3_12.py page3_13.py page3_14.py -n 14
#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py -n 5

ren = 12
excel="C://SISIA//Documentacion//respaldo_ok.xlsx"
casos= 12
#ruta="https://prod.senasica.gob.mx/sisia/login"

ruta="http://10.16.3.29:8004/login"


class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    # @unittest.skip("Para pruebas de datos")
    # Primero
    def test01_datos(self):
        self.driver.implicitly_wait(30)
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.tiempo(20)
        #driver.get("http://10.16.3.29:8004/login")
        # driver.get("http://10.16.3.36:8004/login")
        driver.get(ruta)

        path = excel
        hoja = "Hoja3"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            mision = fe.readData(path, "Hoja3", r, 10)
            vision = fe.readData(path, "Hoja3", r, 11)
            fecha = fe.readData(path, "Hoja3", r, 12)
            #fecha2 = datetime.now() + timedelta(days=fecha)
            fecha2 = datetime.now()
            fecha2 = fecha2.strftime('%d/%m/%Y')
            fecha3 = datetime.now()
            fecha4 = fecha3.strftime('%d/%m/%Y')
            registro = str(fe.readData(path, "Hoja3", r, 13))
            telefono = str(fe.readData(path, "Hoja3", r, 14))
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            sample = 'XFTRGERDFRESCDFTYUIOPKASDR'
            rt = random.choice(sample_letters)
            rt2 = random.choice(sample)
            raa = random.randint(1, 9)
            ra1 = random.randint(1, 9)
            rfc = str(fe.readData(path, "Hoja3", r, 15))
            rfcc = rfc + str(ra1)+ rt + str(raa)
            curpp = str("SENASICA/01-31/2019")
            # curpp = curp + rt + str(r)
            presidente = str(fe.readData(path, "Hoja3", r, 17))
            secretario = str(fe.readData(path, "Hoja3", r, 18))
            tesorero = str(fe.readData(path, "Hoja3", r, 19))
            pdf1 = str(fe.readData(path, "Hoja3", r, 20))
            pdf2 = str(fe.readData(path, "Hoja3", r, 21))
            pdf3 = str(fe.readData(path, "Hoja3", r, 22))

            # Login
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            #f.Click("//a[@href='/recursos-humanos-materiales']")
            f.Click("//*[@id='menuSisia']/ul/li[2]/ul/li[1]/a")
            f.scrolling(100)

            # DATOS IE
            f.tiempo(3)
            f.limpiar("//textarea[@formcontrolname='mision']")
            f.texto("//textarea[@formcontrolname='mision']", mision)
            f.limpiar("//textarea[contains(@formcontrolname,'vision')]")
            f.texto("//textarea[contains(@formcontrolname,'vision')]", vision)
            f.texto("(//input[contains(@formcontrolname,'fecha')])[1]", fecha2)
            #f.combo_texto("(//select[contains(@formcontrolname,'anioRegistro')])[2]", registro)
            #f.combo_index("/html/body/main/app-root/div/div/app-datos-ie-plantillas/div[5]/div/div/div/div/form/div[5]/div/fieldset/select",registro)
            #cambio
            f.combo_texto("//select[@ng-reflect-name='anioRegistro']",registro)
            f.texto("(//input[contains(@type,'text')])[7]", telefono)
            #cambios
            f.limpiar("//input[@ng-reflect-name='rfc']")
            f.texto("//input[@ng-reflect-name='rfc']",rfcc)
            #cambios
            #f.texto("(//input[@formcontrolname='rfc'])[2]", rfcc)
            f.limpiar("//input[@ng-reflect-name='claveAutorizacion']")
            f.tiempo(.5)
            f.texto("//input[@ng-reflect-name='claveAutorizacion']", curpp)
            f.tiempo(.5)
            f.limpiar("(//input[contains(@maxlength,'80')])[1]")
            f.texto("(//input[contains(@maxlength,'80')])[1]", presidente)
            f.limpiar("(//input[contains(@maxlength,'80')])[2]")
            f.texto("(//input[contains(@maxlength,'80')])[2]", secretario)
            f.limpiar("(//input[@maxlength='80'])[3]")
            f.texto("(//input[@maxlength='80'])[3]", tesorero)
            f.scrolling(150)
            driver.implicitly_wait(2)
            pdf = f.existe_try("(//input[contains(@type,'file')])[1]")
            print(pdf)
            if (pdf == "Existe"):
                f.upload("(//input[contains(@type,'file')])[1]", pdf1)
                f.upload("(//input[contains(@type,'file')])[2]", pdf2)
                f.upload("(//input[contains(@type,'file')])[3]", pdf3)
                f.Click("//button[@class='btn btn-primary ng-star-inserted'][contains(.,'Guardar')]")
                f.tiempo(28)
                f.Click("//button[contains(.,'Ok')]")
                f.tiempo(2)
                f.scrolling(-1200)
                f.tiempo(1)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(1)
            print("Valor de R: " + str(r))
            if(r == casos):
                break

            elif (pdf == "Falso"):
                f.tiempo(1)
                f.Click("//button[contains(.,'Guardar cambios')]")
                f.tiempo(2)
                f.Click("//button[contains(.,'Ok')]")
                f.scrolling(-1200)
                f.tiempo(1)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(1)
            print("Valor de R: " + str(r))
            if (r == casos):
                break




    #ok listo
    #@unittest.skip("Para pruebas de personas")
    def test02_persona(self):
        driver = self.driver
        driver.get(ruta)
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = excel
        hoja = "Hoja3"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            # Seccion Personal
            nom = str(fe.readData(path, "Hoja3", r, 23))
            ap = str(fe.readData(path, "Hoja3", r, 24))
            am = str(fe.readData(path, "Hoja3", r, 25))
            email = str(fe.readData(path, "Hoja3", r, 26))
            puesto = str(fe.readData(path, "Hoja3", r, 27))
            costo = str(fe.readData(path, "Hoja3", r, 28))
            laboral = str(fe.readData(path, "Hoja3", r, 29))
            telefono = str(fe.readData(path, "Hoja3", r, 14))
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            sample = 'XFTRGERDFRESCDFTYUIOPKASDR'
            rt = random.choice(sample_letters)
            rt2 = random.choice(sample)
            ra = random.randint(1, 9)
            ra1 = random.randint(1, 9)
            rfc = str(fe.readData(path, "Hoja3", r, 15))
            rfcc = rfc + str(ra1) + rt + str(ra)
            curp = str(fe.readData(path, "Hoja3", r, 16))
            curpp = curp + rt + str(ra)

            # Login
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            #f.Click("//a[@href='/recursos-humanos-materiales']")
            f.Click("//*[@id='menuSisia']/ul/li[2]/ul/li[1]/a")
            f.scrolling(100)

            # Sección personal
            f.tiempo(3)
            #f.Click("//a[@data-toggle='tab'][contains(.,'Personal')]")
            f.Click("//a[contains(.,'Personal')]")
            f.tiempo(6)
            f.scrolling(300)
            f.texto("(//input[contains(@formcontrolname,'nombre')])[1]", nom)
            f.texto("//input[@formcontrolname='paterno']", ap)
            f.texto("//input[contains(@formcontrolname,'materno')]", am)
            f.texto("(//input[contains(@formcontrolname,'rfc')])[1]", rfcc)
            f.texto("//input[contains(@formcontrolname,'curp')]", curpp)
            f.texto("//input[contains(@formcontrolname,'correo')]", email)
            f.texto("(//input[@formcontrolname='telefono'])[1]", telefono)
            f.scrolling(550)
            f.tiempo(1)
            f.combo_index("//select[@formcontrolname='puesto']", puesto)
            f.texto("//input[contains(@formcontrolname,'costoMensual')]", costo)
            f.combo_index("//select[contains(@formcontrolname,'ubicacionLaboral')]", laboral)
            f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[1]")
            driver.implicitly_wait(8)
            f.tiempo(8)
            v = f.existe_try("//button[@class='btn btn-default'][contains(.,'Entendido')]")
            if (v == "Existe"):
                f.Click("//button[@class='btn btn-default'][contains(.,'Entendido')]")
                f.tiempo(1)
                f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[1]")
                f.tiempo(12)
                f.scrolling(-1200)
                f.tiempo(1)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(1)

            print("Valor de R: " + str(r))
            if (r == casos):
                break






    #ok listo
    #@unittest.skip("Para instalaciones")
    def test03_instalacion(self):
        driver = self.driver
        driver.get(ruta)
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = excel
        hoja = "Hoja3"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            instalacion = str(fe.readData(path, "Hoja3", r, 30))
            descripcion = str(fe.readData(path, "Hoja3", r, 31))
            calle = str(fe.readData(path, "Hoja3", r, 32))
            colonia = str(fe.readData(path, "Hoja3", r, 33))
            cp = str(fe.readData(path, "Hoja3", r, 34))
            estado = str(fe.readData(path, "Hoja3", r, 35))

            # Login
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            #f.Click("//a[@href='/recursos-humanos-materiales']")
            f.Click("//*[@id='menuSisia']/ul/li[2]/ul/li[1]/a")
            f.scrolling(100)

            # instalacion
            f.scrolling(150)
            f.tiempo(2)
            f.Click("//a[contains(.,'Instalaciones')]")
            f.tiempo(2)
            f.scrolling(400)
            f.combo_index("//select[contains(@formcontrolname,'tipoInstalacion')]", instalacion)
            f.combo_index("//select[contains(@formcontrolname,'nombreResponsable')]", 1)
            f.tiempo(1)
            f.texto("(//textarea[contains(@formcontrolname,'descripcion')])[1]", descripcion)
            f.tiempo(1)
            f.texto("//input[contains(@formcontrolname,'calle')]", calle)
            f.texto("//input[contains(@formcontrolname,'colonia')]", colonia)
            f.texto("//input[@formcontrolname='cp']", cp)
            driver.implicitly_wait(8)
            f.combo_index("//select[@formcontrolname='estado']", estado)
            driver.implicitly_wait(8)
            f.combo_index("//select[contains(@formcontrolname,'municipio')]", 3)
            driver.implicitly_wait(8)
            f.tiempo(3)
            f.combo_index("//select[contains(@formcontrolname,'localidad')]", estado)
            driver.implicitly_wait(8)
            f.tiempo(8)
            f.scrolling(100)
            f.tiempo(2)
            #f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[3]")
            f.Click("/html/body/main/app-root/div/div/app-instalaciones-plantillas/div[5]/div/div/div/div/form/div[18]/div[2]/button")
            f.tiempo(2)
            f.Click("//button[@class='btn btn-default'][contains(.,'Entendido')]")
            f.scrolling(700)
            f.tiempo(2)
            f.Click("/html/body/main/app-root/div/div/app-instalaciones-plantillas/div[5]/div/div/div/div/div[2]/div[3]/div/div[2]/button")
            f.tiempo(6)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)
            if (r == casos):
                break


    #ok listo
    def test04_inventario(self):
        driver = self.driver
        driver.get(ruta)
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = excel
        hoja = "Hoja3"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            ano = str(fe.readData(path, "Hoja3", r, 36))
            ni = str(fe.readData(path, "Hoja3", r, 37))
            ni = str(fe.readData(path, "Hoja3", r, 37))
            tv = str(fe.readData(path, "Hoja3", r, 38))
            marcam = str(fe.readData(path, "Hoja3", r, 39))
            modelom = str(fe.readData(path, "Hoja3", r, 40))
            placam = str(fe.readData(path, "Hoja3", r, 41))
            ns = str(fe.readData(path, "Hoja3", r, 42))
            cil = str(fe.readData(path, "Hoja3", r, 43))
            vf = str(fe.readData(path, "Hoja3", r, 44))
            nf = str(fe.readData(path, "Hoja3", r, 45))
            kil = str(fe.readData(path, "Hoja3", r, 46))
            po = str(fe.readData(path, "Hoja3", r, 47))
            # Login
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.tiempo(1)
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            #f.Click("//a[@href='/recursos-humanos-materiales']")
            f.Click("//*[@id='menuSisia']/ul/li[2]/ul/li[1]/a")
            f.scrolling(100)
            f.tiempo(2)
            #inventario
            #f.Click("//a[@data-toggle='tab'][contains(.,'Inventario Vehicular')]")
            f.Click("//a[contains(.,'Inventario Vehicular')]")
            f.tiempo(2)
            f.texto("(//select[contains(@formcontrolname,'anioRegistro')])[1]", ano)
            f.texto("(//input[contains(@formcontrolname,'numInventario')])[1]", ni)
            f.combo_index("//select[contains(@formcontrolname,'tipoVehiculo')]", tv)
            f.texto("(//input[contains(@formcontrolname,'marca')])[1]", marcam)
            f.texto("(//input[@formcontrolname='modelo'])[1]", modelom)
            f.texto("//input[contains(@formcontrolname,'placa')]", placam)
            f.scrolling(350)
            f.texto("(//input[contains(@formcontrolname,'numSerie')])[1]", ns)
            f.texto("//input[contains(@formcontrolname,'numCilindros')]", cil)
            f.texto("(//input[@formcontrolname='valorFactura'])[1]", vf)
            f.texto("(//input[contains(@formcontrolname,'numFactura')])[1]", nf)
            f.combo_index("//select[contains(@formcontrolname,'condicionVehiculo')]", tv)
            f.combo_index("(//select[contains(@formcontrolname,'nombreResguardante')])[1]", 1)
            f.texto("//input[@formcontrolname='kilometraje']", kil)
            f.combo_index("//select[contains(@formcontrolname,'proyectoOrigen')]", po)
            #f.Click("//*[@id='tab-02']/div/app-inventario-vehicular/form/div[22]/div/label[1]/input")
            f.Click("(//input[@name='tipoRecurso'])[2]")
            #f.Click("//input[contains(@ng-reflect-value,'1')]")
            f.scrolling(550)
            f.tiempo(2)
            #f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[2]")
            f.Click("/html/body/main/app-root/div/div/app-inventario-vehicular-plantillas/div[5]/div/div/div/div/form/div[22]/div[2]/button")
            f.Click("//button[@class='btn btn-default'][contains(.,'Entendido')]")
            f.scrolling(200)
            f.tiempo(1)
            f.Click("/html/body/main/app-root/div/div/app-inventario-vehicular-plantillas/div[5]/div/div/div/div/div[2]/div[3]/div/div[2]/button")
            f.tiempo(4)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(1)
            if (r == casos):
                break



    def test05_bien(self):
        driver = self.driver
        driver.get(ruta)
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = excel
        hoja = "Hoja3"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            tv = str(fe.readData(path, "Hoja3", r, 38))
            mision = fe.readData(path, "Hoja3", r, 10)
            marcam = str(fe.readData(path, "Hoja3", r, 39))
            nf = str(fe.readData(path, "Hoja3", r, 45))
            po = str(fe.readData(path, "Hoja3", r, 47))
            modelom = str(fe.readData(path, "Hoja3", r, 40))
            ns = str(fe.readData(path, "Hoja3", r, 42))
            vf = str(fe.readData(path, "Hoja3", r, 44))
            fecha3 = datetime.now()
            fecha4 = fecha3.strftime('%d/%m/%Y')
            # Login
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            #f.Click("//a[@href='/recursos-humanos-materiales']")
            f.Click("//*[@id='menuSisia']/ul/li[2]/ul/li[1]/a")
            f.scrolling(100)
            f.tiempo(2)

            f.Click("//a[contains(.,'Bien o Servicio')]")
            f.tiempo(3)
            f.scrolling(120)
            f.combo_index("//select[@ng-reflect-name='anioRegistro']", 1)

            f.combo_index("//select[contains(@formcontrolname,'tipoBien')]", tv)
            f.tiempo(2)
            f.combo_index("//select[contains(@formcontrolname,'concepto')]", po)
            f.texto("//textarea[@ng-reflect-name='descripcion']", mision)
            f.scrolling(100)
            f.texto("//input[@ng-reflect-name='numInventario']", nf)
            f.texto("//input[@ng-reflect-name='marca']", marcam)
            f.texto("//input[@ng-reflect-name='modelo']", modelom)
            f.combo_index("//select[contains(@formcontrolname,'estadoBien')]", tv)
            f.texto("//input[@ng-reflect-name='numSerie']", ns)
            f.texto("//input[@ng-reflect-name='numFactura']", nf)
            f.texto("//input[@ng-reflect-name='valorFactura']", vf)
            f.combo_index("//select[@ng-reflect-name='nombreResguardante']", 1)
            f.combo_index("//select[@ng-reflect-name='ubicacionBien']", po)
            f.combo_index("//select[@ng-reflect-name='proyecto']", po)
            f.scrolling(120)
            f.texto("//input[@ng-reflect-name='fecha']", fecha4)
            f.Click("(//input[@formcontrolname='tipoRecurso'])[2]")
            f.tiempo(2)
            f.Click("/html/body/main/app-root/div/div/app-bien-servicio-plantillas/div[5]/div/div/div/div/form/div[22]/div[2]/button")
            f.tiempo(1)
            f.Click("(//button[contains(.,'Entendido')])[1]")
            f.scrolling(300)
            f.Click("/html/body/main/app-root/div/div/app-bien-servicio-plantillas/div[5]/div/div/div/div/div[2]/div[3]/div/div[2]/button")
            f.tiempo(2)
            f.scrolling(-1200)
            f.tiempo(1)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(1)
            if (r == casos):
                break







    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







