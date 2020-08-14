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


class Sisia(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()


    
    def test_login(self):
        ti = .1
        driver=self.driver
        driver.get("http://10.16.3.29:8004/login")
        f=Funciones(driver)
        fe=Funexcel(driver)
        path = "C://SISIA//Documentacion//Usuariosv3.xlsx"
        hoja = "Hoja3"
        rows = fe.getRowCount(path, hoja)
        for r in range(1, rows + 1):
            user = fe.readData(path, "Hoja3", r, 1)
            passw = fe.readData(path, "Hoja3", r, 9)
            mision= fe.readData(path, "Hoja3", r, 10)
            vision= fe.readData(path, "Hoja3", r, 11)
            fecha= fe.readData(path,"Hoja3",r,12)
            fecha2=datetime.now()+timedelta(days=fecha)
            fecha2=fecha2.strftime('%d/%m/%Y')
            registro= str(fe.readData(path,"Hoja3",r,13))
            telefono= str(fe.readData(path,"Hoja3",r,14))
            rfc= str(fe.readData(path,"Hoja3",r,15))
            curp= str(fe.readData(path,"Hoja3",r,16))
            presidente= str(fe.readData(path,"Hoja3",r,17))
            secretario= str(fe.readData(path,"Hoja3",r,18))
            tesorero= str(fe.readData(path,"Hoja3",r,19))
            pdf1= str(fe.readData(path,"Hoja3",r,20))
            pdf2= str(fe.readData(path,"Hoja3",r,21))
            pdf3= str(fe.readData(path,"Hoja3",r,22))
            nom= str(fe.readData(path,"Hoja3",r,23))
            ap= str(fe.readData(path,"Hoja3",r,24))
            am= str(fe.readData(path,"Hoja3",r,25))








            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary pull-right'][contains(.,'Iniciar sesión')]")
            f.Click("//a[@aria-expanded='false'][contains(.,'Configuraciones')]")
            f.Click("//a[@href='/recursos-humanos-materiales']")
            f.scrolling(300)
            f.texto("//textarea[@formcontrolname='mision']", mision)
            f.texto("//textarea[contains(@formcontrolname,'vision')]", vision)
            f.texto("(//input[contains(@formcontrolname,'fecha')])[1]",fecha2)
            f.combo_texto("(//select[contains(@formcontrolname,'anioRegistro')])[2]",registro)
            f.texto("(//input[contains(@type,'text')])[7]",telefono)
            f.texto("(//input[@formcontrolname='rfc'])[2]",rfc)
            f.texto("(//input[contains(@type,'text')])[9]",curp)
            f.texto("(//input[contains(@maxlength,'80')])[1]",presidente)
            f.texto("(//input[contains(@maxlength,'80')])[2]",secretario)
            f.texto("(//input[@maxlength='80'])[3]",tesorero)
            f.scrolling(600)
            f.upload("(//input[contains(@type,'file')])[1]",pdf1)
            f.upload("(//input[contains(@type,'file')])[2]",pdf2)
            f.upload("(//input[contains(@type,'file')])[3]",pdf3)
            #falta guardar
            f.scrolling(-1400)
            f.tiempo(1)

            #Sección personal
            f.Click("(//a[@data-toggle='tab'])[2]")
            f.tiempo(1)
            f.scrolling(300)
            f.texto("(//input[contains(@formcontrolname,'nombre')])[1]",nom)
            f.texto("//input[@formcontrolname='paterno']",ap)
            f.texto("//input[contains(@formcontrolname,'materno')]",am)
            f.texto("(//input[contains(@formcontrolname,'rfc')])[1]",rfc)
            f.texto("//input[contains(@formcontrolname,'curp')]",curp)
            f.tiempo(2)





            f.tiempo(4)








    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")


if  __name__ == '__main__':
    unittest.main()








