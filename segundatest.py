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
from selenium.common.exceptions import NoSuchElementException

ren = 1
campana=1
excel="C://SISIA//Documentacion//Usuariosv4.xlsx"
casos=1


class Sisia(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
    #Ok listo
    def test_generales(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)

        #path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        path = excel

        hoja = "Hoja4"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja4", r, 1)
            passw = fe.readData(path, "Hoja4", r, 2)
            user = fe.readData(path, "Hoja4", r, 1)
            passw = fe.readData(path, "Hoja4", r, 2)
            ind3 = fe.readData(path, "Hoja4", r, 3)
            presu = fe.readData(path, "Hoja4", r, 4)
            fi = datetime.now()
            fi = fi.strftime('%d/%m/%Y')
            fii = str(fi)
            fecha2 = fe.readData(path, "Hoja4", r, 5)
            fechaf = datetime.now() + timedelta(days=fecha2)
            fechaf = fechaf.strftime('%d/%m/%Y')
            fechaf = str(fechaf)
            tg = fe.readData(path, "Hoja4", r, 6)
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@href='/administracion-planeacion']")
            f.tiempo(2)

            v = f.existe_try("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
            if (v == "Existe"):
                f.Click("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
                re=f.combo_index_existe("//select[@id='proyectoCampana']",campana)
                print(r)
                f.tiempo(1)
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.tiempo(1)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.tiempo(4)
                f.scrolling(250)
            elif (v == "Falso"):
                f.Click("//a[contains(.,'Registro de Programa')]")
                f.tiempo(4)
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.tiempo(1)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.tiempo(2)
                f.scrolling(200)

            # Seleccion Campaña

            # generales
            f.Click("//a[contains(.,'Datos Generales')]")
            f.tiempo(1)
            f.texto("//input[@id='fecha_inicial']", fii)
            f.texto("//input[@id='fecha_termino']", fechaf)
            f.scrolling(100)
            f.texto("//textarea[@formcontrolname='introduccion']", tg)
            f.texto("//textarea[@formcontrolname='objetivo_general']", tg)
            f.texto("//textarea[@formcontrolname='objetivo_particular']", tg)
            f.texto("//textarea[@formcontrolname='justificacion']", tg)
            f.texto("//textarea[@formcontrolname='viabilidad']", tg)
            f.texto("//textarea[@formcontrolname='prioridad']", tg)
            f.texto("//textarea[contains(@formcontrolname,'sanitario')]", tg)
            f.texto("//textarea[@formcontrolname='proyeccion']", tg)
            f.texto("//textarea[@formcontrolname='riesgo_accion']", tg)
            f.texto("//textarea[contains(@formcontrolname,'resultado_esperado')]", tg)
            f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[1]")
            f.tiempo(8)
            f.scrolling(-800)
            f.tiempo(1)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)
            print("Valor de R: "+str(r))
            if (r == casos):
                break

    #Ok listo
    def test_poblacion(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        #path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        path = excel
        hoja = "Hoja4"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja4", r, 1)
            passw = fe.readData(path, "Hoja4", r, 2)
            presu = fe.readData(path, "Hoja4", r, 4)
            ind6 = fe.readData(path, "Hoja4", r, 7)
            pob = fe.readData(path, "Hoja4", r, 8)
            ind3 = fe.readData(path, "Hoja4", r, 3)
            fecha2 = fe.readData(path, "Hoja4", r, 5)
            tg = fe.readData(path, "Hoja4", r, 6)

            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@href='/administracion-planeacion']")
            f.scrolling(140)
            f.tiempo(2)

            #element = self.driver.find_element_by_xpath("(//span[contains(@aria-hidden,'true')])[1]")
            #self.driver.find_element_by_xpath("//span[contains(@aria-hidden,'true')])[1]")
            v=f.existe_try("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
            if(v=="Existe"):
                f.Click("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
                f.tiempo(2)
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.tiempo(2)
            elif(v=="Falso"):
                f.Click("//a[contains(.,'Registro de Programa')]")
                f.tiempo(4)
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.tiempo(2)
                f.scrolling(200)

            f.tiempo(2)
            f.Click("//a[contains(.,'Población, Estatus Fitozoosanitario y Localización de Acciones Programadas')]")
            f.scrolling(200)
            f.tiempo(1)
            f.combo_index("//select[contains(@title,'Municipio')]", ind3)
            f.tiempo(.7)
            f.tiempo(1)
            f.combo_index("//select[contains(@title,'Unidad de medida')]", ind3)
            f.tiempo(1)
            f.combo_index("(//select[@formcontrolname='cultivoEspecie'])[1]", ind6)
            f.tiempo(1)
            f.texto("//input[contains(@formcontrolname,'poblacionPotencial')]", fecha2)
            f.texto("//input[@formcontrolname='poblacionObjetivo']", pob)
            f.texto("//textarea[contains(@formcontrolname,'estatusSanitario')]", tg)
            f.scrolling(100)
            f.tiempo(2)
            f.tab("//textarea[contains(@formcontrolname,'estatusSanitario')]")
            f.Click("(//button[contains(.,'Agregar')])[1]")
            f.tiempo(1)
            ex=f.existe_try("//div[contains(@class,'alert alert-warning ng-star-inserted')]")
            if(ex=="Existe"):
                f.scrolling(300)
                f.tiempo(2)
                f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[2]")
                f.tiempo(8)
                f.scrolling(-900)
                f.tiempo(1)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
                f.tiempo(2)
            elif(ex=="Falso"):
                f.tiempo(1)
                f.Click("//button[contains(.,'Entendido')]")
                f.scrolling(300)
                f.tiempo(2)
                f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[2]")
                f.tiempo(8)
                f.scrolling(-900)
                f.tiempo(1)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
                f.tiempo(2)

            '''
            f.Click("//button[contains(.,'Entendido')]")
            f.scrolling(300)
            f.tiempo(2)
            f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[2]")
            f.tiempo(8)
            f.scrolling(-900)
            f.tiempo(1)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)
            f.tiempo(2)
            '''
            if (r == casos):
                break


    #ok listo
    def test_estrategias(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        #path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        path = excel
        hoja = "Hoja4"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja4", r, 1)
            passw = fe.readData(path, "Hoja4", r, 2)
            et = fe.readData(path, "Hoja4", r, 9)
            vp = fe.readData(path, "Hoja4", r, 10)
            ind6 = fe.readData(path, "Hoja4", r, 7)
            ind3 = fe.readData(path, "Hoja4", r, 3)
            fecha2 = fe.readData(path, "Hoja4", r, 5)
            pob = fe.readData(path, "Hoja4", r, 8)
            presu = fe.readData(path, "Hoja4", r, 4)

            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@href='/administracion-planeacion']")
            f.scrolling(200)
            f.tiempo(3)

            v = f.existe_try("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
            print(v)
            if (v == "Existe"):
                f.Click("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
                f.tiempo(2)
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.tiempo(1)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.tiempo(3)
            elif (v == "Falso"):
                f.Click("//a[contains(.,'Registro de Programa')]")
                f.tiempo(3)
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.tiempo(1)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.tiempo(2)
                f.scrolling(200)

            f.Click("//a[contains(.,'Estrategias e Impactos Sanitarios')]")
            f.tiempo(1)
            f.scrolling(180)
            f.texto("//textarea[contains(@formcontrolname,'estatusActPlagas')]", et)
            f.texto("//textarea[@formcontrolname='estrategias']", et)
            f.combo_index("(//select[contains(@formcontrolname,'municipio')])[2]", ind3)
            f.combo_index("//select[@formcontrolname='destinoProduccion']", ind3)
            f.texto("//input[contains(@formcontrolname,'superficie')]", fecha2)
            f.texto("//input[@formcontrolname='nProductores']", pob)
            f.combo_index("(//select[contains(@formcontrolname,'cultivoEspecie')])[2]", ind6)
            f.combo_index("(//select[@formcontrolname='unidadMedida'])[2]", ind3)
            f.texto("//input[@formcontrolname='volTotalProduccion']", pob)
            f.texto("//input[@formcontrolname='valTotalProduccion']", vp)
            f.texto("//input[@formcontrolname='productoresEntidad']", fecha2)
            f.texto("//input[contains(@ng-reflect-name,'unidadesAtenderCoberturaFitosa')]", pob)
            f.texto("//input[@formcontrolname='productoresAtender']", vp)
            f.combo_index("//select[@formcontrolname='plagasEnfermedadesCultivoEspecie']", ind6)
            f.Click("(//button[contains(@class,'btn btn-primary btn-block btn-sm')])[2]")
            f.tiempo(1)
            v=f.existe_try("(//div[contains(@class,'alert alert-warning ng-star-inserted')])[1]")
            if(v=="Existe"):
                #f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                f.tiempo(1)
                f.scrolling(500)
                f.tiempo(2)
                f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[3]")
                f.tiempo(6)
                f.scrolling(-900)
                f.tiempo(1)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
            elif(v=="Falso"):
                f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                f.scrolling(500)
                f.tiempo(3)
                f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[3]")
                f.tiempo(6)
                f.scrolling(-900)
                f.tiempo(1)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
            if(r == casos):
                break


    #ok Listo
    def test_calendarizacion(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        #path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        path = excel
        hoja = "Hoja4"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja4", r, 1)
            passw = fe.readData(path, "Hoja4", r, 2)
            mes1 = fe.readData(path, "Hoja4", r, 11)
            mes2 = fe.readData(path, "Hoja4", r, 12)
            mes3 = fe.readData(path, "Hoja4", r, 13)
            ind3 = fe.readData(path, "Hoja4", r, 3)
            vp = fe.readData(path, "Hoja4", r, 10)
            presu = fe.readData(path, "Hoja4", r, 4)

            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.scrolling(50)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@href='/administracion-planeacion']")
            f.tiempo(1)

            v = f.existe_try("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
            if (v == "Existe"):
                f.Click("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.tiempo(1)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.tiempo(3)
            elif (v == "Falso"):
                f.Click("//a[contains(.,'Registro de Programa')]")
                f.tiempo(3)
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.tiempo(2)


            f.scrolling(200)
            f.tiempo(1)
            f.Click("//a[@data-toggle='tab'][contains(.,'Calendarización de Actividades y Responsabilidades por Proyecto')]")
            f.tiempo(3)
            f.scrolling(180)
            f.combo_index("(//select[contains(@formcontrolname,'accion')])[1]", ind3)
            f.tiempo(1)
            f.combo_index("(//select[@formcontrolname='actividad'])[1]", 1)
            f.tiempo(1)
            f.combo_index("(//select[contains(@formcontrolname,'unidadMedida')])[3]", 1)
            f.tiempo(1)
            f.combo_index("//select[@formcontrolname='responsableActividad']", 1)
            f.tiempo(1)
            f.scrolling(100)
            f.texto("//input[@id='" + str(mes1) + "']", mes2)
            f.texto("//input[@id='" + str(mes2) + "']", vp)
            f.texto("//input[@id='" + str(mes3) + "']", mes1)
            f.scrolling(120)
            f.tiempo(2)
            f.scrolling(200)
            f.tiempo(1)
            #f.tab("//input[@id='" + str(mes3) + "']")
            #f.Click("//button[contains(.,'Agregar Distribución')]")
            f.Click("//button[contains(.,'Agregar Distribución')]")
            f.tiempo(1)


            #v=f.existe_try("//button[contains(.,'Entendido')]")
            v = f.existe_try("(//div[contains(@class,'alert alert-warning ng-star-inserted')])[1]")
            if (v == "Existe"):
                f.tiempo(1)
                #f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                print("si existe Entendido")
                f.scrolling(150)
                f.tiempo(2)
                f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[4]")
                f.tiempo(8)
                f.scrolling(-1200)
                f.tiempo(2)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
            elif (v == "Falso"):
                f.tiempo(1)
                print("No existe Entendido")
                f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                f.scrolling(150)
                f.tiempo(2)
                f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[4]")
                f.tiempo(8)
                f.scrolling(-1200)
                f.tiempo(2)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
                f.tiempo(2)
            if (r == casos):
                break




    #ok listo
    def test_necesidades(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        #path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        path = excel
        hoja = "Hoja4"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja4", r, 1)
            passw = fe.readData(path, "Hoja4", r, 2)
            mes1 = fe.readData(path, "Hoja4", r, 11)
            mes2 = fe.readData(path, "Hoja4", r, 12)
            ind3 = fe.readData(path, "Hoja4", r, 3)
            presu = fe.readData(path, "Hoja4", r, 4)

            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.scrolling(50)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@href='/administracion-planeacion']")
            f.tiempo(1)


            #if registro
            v = f.existe_try("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
            print(v)
            if (v == "Existe"):
                f.Click("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.tiempo(1)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.scrolling(100)
                f.tiempo(3)
            elif (v == "Falso"):
                f.Click("//a[contains(.,'Registro de Programa')]")
                f.scrolling(100)
                f.tiempo(3)
                f.combo_index("//select[@id='proyectoCampana']", campana)
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.scrolling(270)
                f.tiempo(10)


            # Necesidades Físicas
            f.Click("//a[@data-toggle='tab'][contains(.,'Necesidades Físicas Financieras')]")
            f.tiempo(6)
            f.scrolling(300)
            f.combo_index("(//select[@formcontrolname='persona'])[1]", 1)
            f.combo_index("//select[@formcontrolname='meses']", mes1)
            f.texto("//input[contains(@formcontrolname,'costoTotal')]", 2)
            f.scrolling(80)
            v=f.existe_try("//input[contains(@formcontrolname,'inversionGOF')]")
            if(v=="Existe"):
                f.scrolling(100)
                f.tiempo(2)
                val=f.campo_enabled("//input[contains(@formcontrolname,'inversionGOF')]")
                if(val=="Activo"):
                    f.tiempo(1)
                    f.texto("//input[contains(@formcontrolname,'inversionGOF')]",1)
                    f.texto("//input[contains(@formcontrolname,'inversionGTP')]",1)
                    f.tiempo(1)
                    f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[3]")
                    f.tiempo(1)
                    e = f.existe_try("//div[@class='alert alert-warning ng-star-inserted']")
                    if(e == "Existe"):
                        f.tiempo(3)
                        f.scrolling(1200)
                        f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                        f.tiempo(8)
                        f.scrolling(-1300)
                        f.tiempo(1)
                        f.Click("//a[contains(.,'Salir')]")
                        f.tiempo(2)
                        if (r == casos):
                            break

                    elif (e == "Falso"):
                        f.tiempo(1)
                        f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                        f.tiempo(4)
                        f.scrolling(250)
                        f.tiempo(3)
                        f.scrolling(1200)
                        f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                        f.tiempo(8)
                        f.scrolling(-1300)
                        f.tiempo(1)
                        f.Click("//a[contains(.,'Salir')]")
                        f.tiempo(2)
                        if (r == casos):
                            break
                elif(val=="Inactivo"):
                    f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[3]")
                    f.tiempo(1)
                    e = f.existe_try("//div[@class='alert alert-warning ng-star-inserted']")
                    if (e == "Existe"):
                        f.tiempo(3)
                        f.scrolling(1200)
                        f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                        f.tiempo(8)
                        f.scrolling(-1300)
                        f.tiempo(1)
                        f.Click("//a[contains(.,'Salir')]")
                        f.tiempo(2)
                        if (r == casos):
                            break

                    elif (e == "Falso"):
                        f.tiempo(1)
                        f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                        f.tiempo(4)
                        f.scrolling(250)
                        f.tiempo(3)
                        f.scrolling(1200)
                        f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                        f.tiempo(8)
                        f.scrolling(-1300)
                        f.tiempo(1)
                        f.Click("//a[contains(.,'Salir')]")
                        f.tiempo(2)
                        if (r == casos):
                            break


            elif (v == "Falso"):
                f.tiempo(1)
                f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[3]")
                f.tiempo(3)

                e = f.existe_try("//div[@class='alert alert-warning ng-star-inserted']")
                if (e == "Existe"):
                    f.tiempo(3)
                    f.scrolling(1200)
                    f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                    f.tiempo(8)
                    f.scrolling(-1300)
                    f.tiempo(1)
                    f.Click("//a[contains(.,'Salir')]")
                    f.tiempo(2)
                    if (r == casos):
                        break
                elif (e == "Falso"):
                    f.tiempo(1)
                    f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                    f.tiempo(3)
                    f.scrolling(1200)
                    f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                    f.tiempo(8)
                    f.scrolling(-1300)
                    f.tiempo(1)
                    f.Click("//a[contains(.,'Salir')]")
                    f.tiempo(2)
                    if (r == casos):
                        break



            '''
            # Recursos Materiales
            f.combo_index("(//select[contains(@formcontrolname,'concepto')])[1]", ind3)
            f.scrolling(100)
            f.tiempo(2)
            f.combo_index("(//select[@formcontrolname='unidadMedida'])[4]", 1)
            f.texto("(//input[contains(@formcontrolname,'cantidad')])[1]", 5)
            f.texto("(//input[@formcontrolname='costoUnitario'])[1]", 2)
            f.scrolling(130)
            f.tiempo(1)

            v=f.existe_try("(//input[contains(@formcontrolname,'inversionGOF')])[1]")
            if(v == "Existe"):
                f.texto("(//input[contains(@formcontrolname,'inversionGOF')])[1]", 5)
                f.texto("(//input[@ng-reflect-name='inversionGTP'])[2]", 5)
                f.tiempo(2)
                f.Click("(//button[contains(.,'Agregar')])[4]")
                f.tiempo(1)
                e = f.existe_try("//div[@class='alert alert-warning ng-star-inserted']")
                if(e == "Existe"):
                    f.tiempo(1)
                    f.tiempo(1)
                elif(e == "Falso"):
                    f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                    f.tiempo(1)
                    f.scrolling(100)
            elif(v == "Falso"):
                f.tiempo(2)
                #f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[3]")
                print("Se oprimio")
                f.tiempo(2)
                #f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
                #f.tiempo(3)





            # Servicios
            f.scrolling(400)
            f.combo_index("(//select[contains(@formcontrolname,'concepto')])[2]", ind3)
            f.tiempo(2)
            f.combo_index("(//select[contains(@formcontrolname,'unidadMedida')])[5]", 1)
            f.texto("(//input[@formcontrolname='cantidad'])[2]", 5)
            f.texto("(//input[@formcontrolname='costoUnitario'])[2]", 2)
            f.scrolling(130)
            f.tiempo(2)
            v=f.existe_try("//input[contains(@formcontrolname,'inversionGOF')]")
            if (v == "Existe"):
                f.texto("//input[contains(@formcontrolname,'inversionGOF')]",5)
                f.tiempo(1)
                #f.texto("(//input[@ng-reflect-name='inversionGTP'])[2]",1000)

                f.texto("//*[@id='tab-05']/div/app-necesidades-fisicas-servicios/div/fieldset/div[7]/div/div[2]/div/div/input",5)
                f.tiempo(2)
                f.scrolling(50)
                f.tiempo(1)
                f.Click("//*[@id='tab-05']/div/app-necesidades-fisicas-servicios/div/fieldset/div[7]/div/div[3]/div/button")
                print("Se presiono el boton servicios agregar")
                f.tiempo(1)
                e = f.existe_try("//strong[contains(.,'Unidad de Medida:')]")
                print("e " + e)
                if (e =="Existe"):
                    f.tiempo(1)
                    f.scrolling(400)
                    f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                    f.tiempo(8)
                    f.scrolling(-1200)
                    f.Click("//a[contains(.,'Salir')]")
                    f.tiempo(2)
                elif(e =="Falso"):
                    f.Click("//button[contains(.,'Entendido')]")
                    f.tiempo(1)
                    f.scrolling(400)
                    f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                    f.tiempo(8)
                    f.scrolling(-1200)
                    f.Click("//a[contains(.,'Salir')]")
                    f.tiempo(2)

            elif(v == "Falso"):             
                f.tiempo(1)
                f.scrolling(400)
                f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
                f.tiempo(8)
                f.scrolling(-1200)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
                f.tiempo(2)
            if (r == casos):
                break
            '''




    #ok listo
    def test_acciones(self):
        driver = self.driver
        driver.get("http://10.16.3.29:8004/login")
        f = Funciones(driver)
        fe = Funexcel(driver)
        #path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        path = excel
        hoja = "Hoja4"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, "Hoja4", r, 1)
            passw = fe.readData(path, "Hoja4", r, 2)
            ind3 = fe.readData(path, "Hoja4", r, 3)
            presu = fe.readData(path, "Hoja4", r, 4)

            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.scrolling(50)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@href='/administracion-planeacion']")
            f.scrolling(150)
            f.tiempo(1)

            # if registro
            v = f.existe_try("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
            print(v)
            if (v == "Existe"):
                f.Click("(//span[contains(@class,'glyphicon glyphicon-pencil')])[1]")
                f.scrolling(100)
                f.tiempo(1)
            elif (v == "Falso"):
                f.Click("//a[contains(.,'Registro de Programa')]")
                f.scrolling(100)
                f.tiempo(1)


            f.combo_index("//select[@id='proyectoCampana']", 1)

            f.tiempo(1)
            v = f.existe_try("//span[@class='help-block'][contains(.,'Campo requerido')]")
            if (v == "Existe"):
                f.tiempo(1)
                f.Click("//a[contains(.,'Salir')]")
            else:
                f.combo_index("//select[@formcontrolname='presupuestoRadio']", presu)
                f.scrolling(170)
                f.tiempo(1)

            f.Click("//a[contains(.,'Indicadores por Acciones')]")
            f.tiempo(2)
            f.scrolling(150)
            f.combo_index("(//select[contains(@formcontrolname,'accion')])[2]", 1)
            f.tiempo(1)
            f.combo_index("(//select[contains(@ng-reflect-name,'actividad')])[2]", 1)
            f.tiempo(1)
            f.combo_index("(//select[@ng-reflect-name='unidadMedida'])[6]", 1)
            f.tiempo(2)
            f.Click("//*[@id='tab-07']/div/app-indicadores-por-acciones/form/fieldset/div[6]/div/button")
            f.tiempo(2)
            #e = f.existe_try("//button[contains(.,'Entendido')]")
            e = f.existe_try("//div[contains(@class,'alert alert-warning ng-star-inserted')]")
            if (e == "Existe"):
                print("EXISTE LA VENTANA")
                f.tiempo(1)
                #f.Click("//button[contains(.,'Entendido')]")
                f.scrolling(30)
                f.tiempo(1)
                f.Click("(//button[contains(.,'Guardar')])[7]")
                f.tiempo(8)
                f.scrolling(-1200)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
            elif(e=="Falso"):
                print("NO EXISTE LA VENTANA")
                f.tiempo(1)
                f.Click("//button[contains(.,'Entendido')]")
                f.scrolling(30)
                f.tiempo(1)
                f.Click("(//button[contains(.,'Guardar')])[7]")
                f.tiempo(8)
                f.scrolling(-1200)
                f.Click("//a[contains(.,'Salir')]")
                f.tiempo(2)
                f.tiempo(2)
            if(r == casos):
                break















    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")


if __name__ == '__main__':
    unittest.main()
