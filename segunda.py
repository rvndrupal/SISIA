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

            f.combo_index("//select[@id='proyectoCampana']",1)
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

            pob = fe.readData(path, "Hoja4", r, 8)

            f.scrolling(-1400)
            f.tiempo(1)
            f.Click("//a[contains(.,'Población, Estatus Fitozoosanitario y Localización de Acciones Programadas')]")
            f.scrolling(180)
            f.combo_index("//select[contains(@title,'Municipio')]",ind6)
            f.tiempo(.7)
            f.combo_index("//select[contains(@title,'Unidad de medida')]",ind3)
            f.combo_index("(//select[@formcontrolname='cultivoEspecie'])[1]",ind6)
            f.texto("//input[contains(@formcontrolname,'poblacionPotencial')]",fecha2)
            f.texto("//input[@formcontrolname='poblacionObjetivo']",pob)
            f.texto("//textarea[contains(@formcontrolname,'estatusSanitario')]",tg)
            f.Click("(//button[contains(.,'Agregar')])[1]")
            f.tiempo(1)
            f.Click("//button[contains(.,'Entendido')]")
            f.scrolling(300)
            f.tiempo(2)
            #f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[2]")


            #Estrategias

            et = fe.readData(path, "Hoja4", r, 9)
            vp = fe.readData(path, "Hoja4", r, 10)

            f.scrolling(-1400)
            f.tiempo(1)
            f.Click("//a[@data-toggle='tab'][contains(.,'Estrategias e Impactos Sanitarios')]")
            f.tiempo(1)
            f.scrolling(180)
            f.texto("//textarea[contains(@formcontrolname,'estatusActPlagas')]",et)
            f.texto("//textarea[@formcontrolname='estrategias']",et)
            f.combo_index("(//select[contains(@formcontrolname,'municipio')])[2]",ind6)
            f.combo_index("//select[@formcontrolname='destinoProduccion']",ind3)
            f.texto("//input[contains(@formcontrolname,'superficie')]",fecha2)
            f.texto("//input[@formcontrolname='nProductores']",pob)
            f.combo_index("(//select[contains(@formcontrolname,'cultivoEspecie')])[2]",ind6)
            f.combo_index("(//select[@formcontrolname='unidadMedida'])[2]",ind3)
            f.texto("//input[@formcontrolname='volTotalProduccion']",pob)
            f.texto("//input[@formcontrolname='valTotalProduccion']",vp)
            f.texto("//input[@formcontrolname='productoresEntidad']",fecha2)
            f.texto("//input[contains(@ng-reflect-name,'unidadesAtenderCoberturaFitosa')]",pob)
            f.texto("//input[@formcontrolname='productoresAtender']",vp)
            f.combo_index("//select[@formcontrolname='plagasEnfermedadesCultivoEspecie']",ind6)
            f.Click("(//button[contains(@class,'btn btn-primary btn-block btn-sm')])[2]")
            f.tiempo(1)
            f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
            f.tiempo(1)
            f.scrolling(300)
            f.tiempo(2)
            #f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[3]")



            #Calendarización
            mes1 = fe.readData(path, "Hoja4", r, 11)
            mes2 = fe.readData(path, "Hoja4", r, 12)
            mes3 = fe.readData(path, "Hoja4", r, 13)

            f.scrolling(-1400)
            f.tiempo(1)
            f.Click("//a[@data-toggle='tab'][contains(.,'Calendarización de Actividades y Responsabilidades por Proyecto')]")
            f.tiempo(3)
            f.scrolling(180)
            f.combo_index("(//select[contains(@formcontrolname,'accion')])[1]",ind6)
            f.tiempo(1)
            f.combo_index("(//select[@formcontrolname='actividad'])[1]",1)
            f.combo_index("(//select[contains(@formcontrolname,'unidadMedida')])[3]",1)
            f.combo_index("//select[@formcontrolname='responsableActividad']",ind3)
            f.texto("//input[@id='"+str(mes1)+"']",mes2)
            f.texto("//input[@id='"+str(mes2)+"']",vp)
            f.texto("//input[@id='"+str(mes3)+"']",mes1)
            f.tiempo(1)
            f.scrolling(100)
            f.Click("//button[contains(.,'Agregar Distribución')]")
            f.tiempo(1)
            f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
            f.tiempo(1)
            f.scrolling(200)
            #f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[4]")
            f.tiempo(2)



            #Necesidades Físicas
            f.scrolling(-1400)
            f.tiempo(1)
            f.Click("//a[@data-toggle='tab'][contains(.,'Necesidades Físicas Financieras')]")
            f.tiempo(2)
            f.scrolling(200)
            f.combo_index("(//select[@formcontrolname='persona'])[1]",1)
            f.combo_index("//select[@formcontrolname='meses']",mes1)
            f.texto("//input[contains(@formcontrolname,'costoTotal')]",1)
            f.scrolling(100)
            f.tiempo(1)
            f.Click("(//button[@class='btn btn-primary btn-block btn-sm'][contains(.,'Agregar')])[3]")
            f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
            f.tiempo(1)
            f.scrolling(350)
            f.tiempo(1)
            #Recursos Materiales
            f.combo_index("(//select[contains(@formcontrolname,'concepto')])[1]",ind6)
            f.combo_index("(//select[@formcontrolname='unidadMedida'])[4]",1)
            f.texto("(//input[contains(@formcontrolname,'cantidad')])[1]",5)
            f.texto("(//input[@formcontrolname='costoUnitario'])[1]",2)
            f.texto("//input[@formcontrolname='inversionGOF']",5)
            f.texto("//input[@formcontrolname='inversionGTP']",5)
            f.Click("(//button[contains(.,'Agregar')])[3]")
            f.tiempo(1)
            f.Click("//button[@class='btn btn-default ng-star-inserted'][contains(.,'Entendido')]")
            f.tiempo(1)
            #Agregar Pendiente

            #Servicios
            f.scrolling(400)
            f.combo_index("(//select[contains(@formcontrolname,'concepto')])[2]",ind6)
            f.combo_index("(//select[contains(@formcontrolname,'unidadMedida')])[5]",1)
            f.texto("(//input[@formcontrolname='cantidad'])[2]",mes1)
            f.texto("(//input[@formcontrolname='costoUnitario'])[2]",mes2)
            f.tiempo(1)
            f.scrolling(50)
            f.Click("//*[@id='tab-05']/div/app-necesidades-fisicas-servicios/div/fieldset/div[7]/div/div[2]/div/button")
            f.tiempo(1)
            f.Click("//button[contains(.,'Entendido')]")
            f.tiempo(1)
            f.scrolling(400)
            #f.Click("(//button[@class='btn btn-primary'][contains(.,'Guardar')])[5]")
            f.tiempo(1)





            #Indicaciones por Acciones
            f.scrolling(-1800)
            f.tiempo(2)
            f.Click("//a[contains(.,'Indicadores por Acciones')]")
            f.tiempo(2)
            f.scrolling(450)
            f.combo_index("(//select[contains(@formcontrolname,'accion')])[2]",ind6)
            f.tiempo(1)
            f.combo_index("(//select[contains(@ng-reflect-name,'actividad')])[2]",1)
            f.combo_index("(//select[@ng-reflect-name='unidadMedida'])[6]",1)
            f.tiempo(2)
            f.Click("//*[@id='tab-07']/div/app-indicadores-por-acciones/form/fieldset/div[6]/div/button")
            f.tiempo(1)
            f.Click("//button[contains(.,'Entendido')]")
            f.scrolling(200)
            f.tiempo(1)
            #f.Click("(//button[contains(.,'Guardar')])[7]")
            f.tiempo(2)



            #SALIR
            f.scrolling(-1800)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)








    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")


if __name__ == '__main__':
    unittest.main()








