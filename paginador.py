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


ruta="https://datatables.net/extensions/select/examples/initialisation/checkbox.html"


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
        f.scrolling(400)
        f.tiempo(1)

        vt=f.obtenerTexto("//h1[contains(.,'Checkbox selection')]")
        if(vt== "Checkbox selection"):
            print("Existe el titulo de la pagina")
        else:
            print("No esta el titulo del combo")

        tam=driver.find_element_by_css_selector("#example_paginate > span > a")
        #t=len(tam)
        #print("Total: "+str(t))
        f.combo_index("//select[contains(@name,'length')]",0)
        f.tiempo(1)
        val = driver.find_element_by_xpath("//div[contains(@id,'info')]").text
        tot = float(val[19:21])
        bloques=10
        tot = tot / bloques
        print("Encontrado: " + str(tot))
        entero = str(tot).split(".")
        ent = int(entero[0])
        dec = int(entero[1])
        print("Entero: " + str(ent))
        print("Decimal: " + str(dec))


        for r in range(1,ent+2):
            f.Click("//a[@data-dt-idx='"+str(r)+"']")
            if (r == ent+1):
                for ult in range(1, dec + 1):
                    f.Click("(//td[@class=' select-checkbox'])[" + str(ult) + "]")
                    nom = driver.find_element_by_xpath("(//td[contains(@class,'1')])[" + str(ult) + "]").text
            else:
                for c in range(1,bloques+1):
                    print(c)
                    f.Click("(//td[@class=' select-checkbox'])["+str(c)+"]")
                    nom=driver.find_element_by_xpath("(//td[contains(@class,'1')])["+str(c)+"]").text
                    #ap = driver.find_element_by_xpath("//*[@id='example']/tbody/tr["+str(c)+"]/td["+str(c)+"]").text
                    print(nom)
                print("primer ciclo: "+str(r))





















    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







