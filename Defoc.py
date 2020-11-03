#import HtmlTestRunner
#from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import math
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


#
#pytest -v -s --html=report.html --self-contained-html page3.py

#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py  page3_6.py page3_7.py page3_8.py page3_9.py page3_10.py page3_11.py page3_12.py page3_13.py page3_14.py -n 14
#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py -n 5

ren = 1
excel="C://SISIA//Documentacion//Usuariosv3_1.xlsx"
casos= 2
#pytest -v -s --alluredir="C:\SISIA\reportes_allure"  page3.py
#allure serve C:\SISIA\reportes_allure


ruta="http://10.16.3.29:8003/consulta-solicitudes/vacunacion-antirrabica"
#Folios=RAB20200000028


#cls
class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # @unittest.skip("Para pruebas de datos")
    # Primero
    def test01_tabla(self):
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.tiempo(.5)
        #driver.get("http://10.16.3.29:8004/login")
        # driver.get("http://10.16.3.36:8004/login")
        driver.get(ruta)
        path = excel
        f.scrolling(100)
        f.tiempo(1)
        f.texto("//input[@id='username']","estela.flores")
        f.texto("//input[@id='password']","EFV2020")
        f.Click("//button[contains(.,'Acceder')]")
        f.tiempo(1)
        f.Click("//a[@href='consulta-unidad']")
        f.Click("//a[contains(@id,'solicitud')]")
        f.tiempo(1)
        f.scrolling(200)
        f.texto("(//input[@type='text'])[1]","RAB20200000028")
        f.scrolling(200)
        f.tiempo(2)
        f.Click("(//button[contains(@id,'solicitud')])[1]")
        f.scrolling(300)
        f.tiempo(4)
        f.Click("//button[@id='id_detalle_solicitud']")
        f.tiempo(2)
        f.Click("//button[@id='id_ir_registro_solicitud']")
        f.tiempo(4)
        f.scrolling(900)
        f.tiempo(4)
        f.combo_index("//select[contains(@id,'vacuna')]",1)
        f.texto("//input[contains(@id,'laboratorio')]","demo uno")
        f.texto("//input[contains(@id,'id_lote')]","Lote demo")
        f.texto("//input[contains(@id,'id_fecha_caducidad')]","16/10/2020")
        f.Click("//button[contains(@id,'vacuna')]")
        f.tiempo(1)
        f.scrolling(-30)
        f.combo_index("//select[contains(@id,'vacuna')]", 2)
        f.texto("//input[contains(@id,'laboratorio')]", "demo dos")
        f.texto("//input[contains(@id,'id_lote')]", "Lote dos")
        f.texto("//input[contains(@id,'id_fecha_caducidad')]", "16/10/2020")
        f.Click("//button[contains(@id,'vacuna')]")
        f.tiempo(1)
        f.scrolling(10)
        f.combo_index("//select[contains(@id,'vacuna')]", 1)
        f.texto("//input[contains(@id,'laboratorio')]", "demo tres")
        f.texto("//input[contains(@id,'id_lote')]", "Lote tres")
        f.texto("//input[contains(@id,'id_fecha_caducidad')]", "16/10/2020")
        f.Click("//button[contains(@id,'vacuna')]")
        f.tiempo(1)
        f.scrolling(1600)



        tot = 151
        bloques = 15
        tot = tot / bloques
        print("Encontrado: " + str(tot))
        entero = str(tot).split(".")
        ent = int(entero[0])
        dec = int(entero[1])
        print("Entero: " + str(ent))
        print("Decimal: " + str(dec))

        for r in range(1, 8 + 2):
            #f.Click("//a[@data-dt-idx='" + str(r) + "']")
            #f.Click(" // *[ @ id = 'animalitos'] / pagination - template / ul / li[3] / span[" + str(r) + "]")

            #// *[ @ id = "animalitos"] / pagination - template / ul / li[4] / a / span[2]
            print(r+2)
            f.Click("// *[ @ id = 'animalitos'] / pagination - template / ul / li[" + str(r+2) + "] / span[2]")




            #f.Click("(//span[contains(.,'" + str(r) + "')])[3]")

            f.tiempo(8)

            '''
            if (r == ent + 1):
                for ult in range(1, dec + 1):
                    f.Click("(//td[@class=' select-checkbox'])[" + str(ult) + "]")
                    nom = driver.find_element_by_xpath("(//td[contains(@class,'1')])[" + str(ult) + "]").text
            else:
                for c in range(1, bloques + 1):
                    print(c)
                    f.Click("(//td[@class=' select-checkbox'])[" + str(c) + "]")
                    nom = driver.find_element_by_xpath("(//td[contains(@class,'1')])[" + str(c) + "]").text
                    # ap = driver.find_element_by_xpath("//*[@id='example']/tbody/tr["+str(c)+"]/td["+str(c)+"]").text
                    print(nom)
                print("primer ciclo: " + str(r))
            '''








    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







