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
#pytest page1.py  page2.py  page3.py  page4.py  page5.py  page6.py  -n 6

ren=2


class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.implicitly_wait(25)
        cls.driver.maximize_window()





    #@unittest.skip("Para pruebas de datos")
    def test_datos(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
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
            fecha2 = datetime.now() + timedelta(days=fecha)
            fecha2 = fecha2.strftime('%d/%m/%Y')
            fecha3 = datetime.now()
            fecha4 = fecha3.strftime('%d/%m/%Y')
            registro = str(fe.readData(path, "Hoja3", r, 13))
            telefono = str(fe.readData(path, "Hoja3", r, 14))
            sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
            sample = 'XFTRGERDFRESCDFTYUIOPKASDR'
            rt = random.choice(sample_letters)
            rt2 = random.choice(sample)
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

            #Login
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            f.Click("//a[@href='/recursos-humanos-materiales']")
            f.scrolling(100)

            # DATOS IE
            f.tiempo(5)
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
            f.scrolling(300)
            f.upload("(//input[contains(@type,'file')])[1]", pdf1)
            f.upload("(//input[contains(@type,'file')])[2]", pdf2)
            f.upload("(//input[contains(@type,'file')])[3]", pdf3)
            f.Click("//button[@class='btn btn-primary ng-star-inserted'][contains(.,'Guardar')]")
            f.tiempo(25)
            f.scrolling(120)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)

    #@unittest.skip("Para pruebas de personas")
    def test_persona(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
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
            r = random.randint(1, 9)
            rfc = str(fe.readData(path, "Hoja3", r, 15))
            rfcc = rfc + rt + str(r)
            curp = str(fe.readData(path, "Hoja3", r, 16))
            curpp = curp + rt + str(r)

            # Login
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            f.Click("//a[@href='/recursos-humanos-materiales']")
            f.scrolling(100)

            # Sección personal
            f.tiempo(10)
            f.Click("//a[@data-toggle='tab'][contains(.,'Personal')]")
            f.tiempo(8)
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
            f.tiempo(1)
            f.Click("//button[@class='btn btn-default'][contains(.,'Entendido')]")
            f.tiempo(1)
            f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[1]")
            f.tiempo(15)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)

    #@unittest.skip("Para instalaciones")
    def test_instalacion(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
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
            f.Click("//a[@href='/recursos-humanos-materiales']")
            f.scrolling(100)

            # instalacion
            f.scrolling(150)
            f.tiempo(8)
            f.Click("//a[contains(.,'Instalaciones')]")
            f.tiempo(8)
            f.scrolling(400)
            f.combo_index("//select[contains(@formcontrolname,'tipoInstalacion')]", instalacion)
            f.combo_index("//select[contains(@formcontrolname,'nombreResponsable')]", 1)
            f.texto("(//textarea[contains(@formcontrolname,'descripcion')])[1]", descripcion)
            f.tiempo(3)
            f.texto("//input[contains(@formcontrolname,'calle')]", calle)
            f.texto("//input[contains(@formcontrolname,'colonia')]", colonia)
            f.texto("//input[@formcontrolname='cp']", cp)
            f.combo_index("//select[@formcontrolname='estado']", estado)
            f.tiempo(3)
            f.combo_index("//select[contains(@formcontrolname,'municipio')]", 3)
            f.tiempo(3)
            f.combo_index("//select[contains(@formcontrolname,'localidad')]", estado)
            f.tiempo(2)
            f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[3]")
            f.tiempo(2)
            f.Click("//button[@class='btn btn-default'][contains(.,'Entendido')]")
            f.scrolling(700)
            f.tiempo(2)
            f.Click("(//button[contains(.,'Guardar')])[3]")
            f.tiempo(6)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)

    def test_inventario(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
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
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            f.Click("//a[@href='/recursos-humanos-materiales']")
            f.scrolling(100)
            f.tiempo(10)
            #inventario
            f.Click("//a[@data-toggle='tab'][contains(.,'Inventario Vehicular')]")
            f.tiempo(8)
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
            f.Click("//input[contains(@ng-reflect-value,'1')]")
            f.scrolling(550)
            f.tiempo(1)
            f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[2]")
            f.Click("//button[@class='btn btn-default'][contains(.,'Entendido')]")
            f.scrolling(200)
            f.tiempo(2)
            f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[2]")
            f.tiempo(7)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)

    def test_bien(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
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
            f.Click("//a[@href='/recursos-humanos-materiales']")
            f.scrolling(100)
            f.tiempo(8)

            f.Click("//a[@data-toggle='tab'][contains(.,'Bien o Servicio')]")
            f.tiempo(6)
            f.scrolling(120)
            f.combo_index("(//select[contains(@formcontrolname,'anioRegistro')])[3]", 1)
            f.combo_index("//select[contains(@formcontrolname,'tipoBien')]", tv)
            f.combo_index("//select[contains(@formcontrolname,'concepto')]", po)
            f.texto("(//textarea[contains(@formcontrolname,'descripcion')])[2]", mision)
            f.scrolling(100)
            f.texto("(//input[@formcontrolname='numInventario'])[2]", nf)
            f.texto("(//input[@formcontrolname='marca'])[2]", marcam)
            f.texto("(//input[contains(@formcontrolname,'modelo')])[2]", modelom)
            f.combo_index("//select[contains(@formcontrolname,'estadoBien')]", tv)
            f.texto("(//input[@formcontrolname='numSerie'])[2]", ns)
            f.texto("(//input[contains(@formcontrolname,'numFactura')])[2]", nf)
            f.texto("(//input[@formcontrolname='valorFactura'])[2]", vf)
            f.combo_index("(//select[contains(@formcontrolname,'nombreResguardante')])[2]", 1)
            f.combo_index("//select[contains(@formcontrolname,'ubicacionBien')]", po)
            f.combo_index("//select[@formcontrolname='proyecto']", po)
            f.scrolling(120)
            f.texto("(//input[@formcontrolname='fecha'])[2]", fecha4)
            f.Click("(//input[contains(@name,'tipoRecurso')])[2]")
            f.Click("(//button[@class='btn btn-primary btn-block btn-sm'])[4]")
            f.tiempo(1)
            f.Click("(//button[contains(.,'Entendido')])[1]")
            f.scrolling(300)
            f.Click("(//button[contains(.,'Guardar')])[5]")
            f.tiempo(15)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()








