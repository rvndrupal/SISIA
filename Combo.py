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


ruta="file:///C:/SISIA/combo.html"


#cls
class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(2)

    # @unittest.skip("Para pruebas de datos")
    # Primero
    def test01_tabla(self):
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        #driver.get("http://10.16.3.29:8004/login")
        # driver.get("http://10.16.3.36:8004/login")
        driver.get(ruta)
        path = excel
        f.combo_index("//*[@id='cars']", 0)
        f.tiempo(5)
        a = random.randint(1, 4)
        print(a)
        f.tiempo(2)

        val2=f.combo_index_existe2("//*[@id='cars']")
        print(val2[1])
        val=f.combo_index_existe("//*[@id='cars']")
        if val > 0:
            for r in range(1, val+1):
                print(r)
            if a==1:
                f.combo_index("//*[@id='cars']",0)
            elif a==2:
                f.combo_index("//*[@id='cars']", 1)
            elif a==3:
                f.combo_index("//*[@id='cars']", 2)
            elif a==4:
                f.combo_index("//*[@id='cars']", 3)
















    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







