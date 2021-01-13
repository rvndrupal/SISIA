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

#pytest -v -s --html=report1.html --self-contained-html page3_1.py
#pytest -v -s --html=prueba_p1.html --self-contained-html prueba_p.py


#pytest page3_1.py -v --junitxml="page3_1.xml"

#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py  page3_6.py page3_7.py page3_8.py page3_9.py page3_10.py page3_11.py page3_12.py page3_13.py page3_14.py -n 14

#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py -n 5
#pytest page3_6.py page3_7.py page3_8.py page3_9.py page3_10.py -n 5
#pytest page3_11.py page3_12.py page3_13.py page3_14.py page3_15.py -n 5
#pytest page3_16.py page3_17.py page3_18.py page3_19.py page3_20.py -n 5
#pytest page3_21.py page3_22.py page3_23.py page3_24.py page3_25.py -n 5
#pytest page3_26.py page3_27.py page3_28.py page3_29.py page3_30.py -n 5
#pytest page3_31.py page3_32.py page3_33.py page3_34.py page3_35.py -n 5
#pytest page3_36.py  page3_37.py  page3_38.py  page3_39.py  page3_40.py -n 5
#pytest page3_41.py  page3_42.py  page3_43.py  page3_44.py  page3_45.py -n 5
#pytest page3_46.py  page3_47.py  page3_48.py  page3_49.py  page3_50.py -n 5



ren = 5
excel="C://SISIA//Documentacion//respaldo_ok.xlsx"
casos= 5
#ruta="https://prod.senasica.gob.mx/sisia/login"

#ruta="http://10.16.3.36:8004/login"

ruta="http://127.0.0.1:8000/admin/login/?next=/admin/"
#nueva con los id

#Produccion.
#ruta="https://prod.senasica.gob.mx/sisia/login"


class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        #cls.driver = webdriver.Firefox()
        #cls.driver=webdriver.Ie()
        cls.driver.maximize_window()
        driver = cls.driver
        f = Funciones(driver)
        f.tiempo(2)
        cls.driver.implicitly_wait(30)


    # @unittest.skip("Para pruebas de datos")
    # Primero
    def test01_datos(self):
        self.driver.get(ruta)
        self.driver.implicitly_wait(5)
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.tiempo(.5)
        sample_letters = 'ABCDFEGHIJKLOPQRTSRETUIO'
        rt = random.choice(sample_letters)
        ra = random.randint(1, 100)
        com = random.randint(0,4)
        f.texto("id_username","rodrigo")
        f.texto("id_password","rorro13")
        f.Click_xpath("//input[@value='Iniciar sesión']")
        f.Click_xpath("//a[@href='/admin/auth/user/'][contains(.,'Usuarios')]")
        f.Click_xpath("//a[@href='/admin/'][contains(.,'Inicio')]")
        f.Click_xpath("//a[@href='/admin/persona/empleado/'][contains(.,'Empleados')]")
        f.Click_xpath("//a[@href='/admin/persona/empleado/add/'][contains(.,'Añadir empleado')]")
        f.texto_xpath("//input[contains(@id,'id_first_name')]","nombre"+rt+str(ra))
        f.texto_xpath("//input[contains(@id,'id_last_name')]","apellidos"+rt+str(ra))
        f.combo_index_xpath("//select[contains(@id,'id_job')]",com)
        f.combo_index_xpath("//select[contains(@id,'id_departamento')]",1)
        f.Click_xpath("//input[@value='Guardar']")
        f.tiempo(2)









    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







