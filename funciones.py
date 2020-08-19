import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Funciones():
    def __init__(self, driver):
        self.driver= driver

        self.name = "(//input[contains(@type,'text')])[2]"
        self.password = "//input[contains(@id,'txtPassword')]"
        self.button="//input[contains(@id,'btnLogin')]"


    def login(self,name,password):
        self.driver.find_element_by_xpath(self.name).send_keys(name)
        self.driver.find_element_by_xpath(self.password).send_keys(password)
        self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//login.png")
        self.driver.find_element_by_xpath(self.button).click()




    def texto(self,xpath,texto):
        r = random.randint(1, 1000)
        t=self.driver.find_element_by_xpath(xpath).send_keys(texto)
        self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//texto"+str(r)+".png")
        return t

    def Click(self,xpath):
        r = random.randint(1,10000)
        e = self.driver.find_element_by_xpath(xpath).click()
        self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Click"+str(r)+".png")
        return e


    
    def combo_texto(self,xpath,texto):
        r = random.randint(1, 1000)
        ct=Select(self.driver.find_element_by_xpath(xpath))
        ct.select_by_visible_text(texto)
        self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Combo_texto" + str(r) + ".png")
        return ct

    def combo_index(self,xpath,index):
        r = random.randint(1, 1000)
        ct=Select(self.driver.find_element_by_xpath(xpath))
        ct.select_by_index(index)
        self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Combo_index" + str(r) + ".png")
        return ct

    def check(self,xpath):
        r = random.randint(1, 1000)
        ck=self.driver.find_element_by_xpath(xpath).click()
        self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Check" + str(r) + ".png")
        return ck

    def tiempo(self,tiempo):
        t=time.sleep(tiempo)
        return t

    def upload(self,xpath,ruta):
        r = random.randint(1, 1000)
        up=self.driver.find_element_by_xpath(xpath).send_keys(ruta)
        self.driver.save_screenshot("C://SELENIUM//Page_objects//IMAGENES//Upload" + str(r) + ".png")
        return up

    def Validar_Elemento(self,id):
        wait = WebDriverWait(self.driver, 10)
        v = wait.until(EC.visibility_of_element_located((By.ID,id)))
        return v

    def Validar_avilitado_xpat(self,xpath):
        e=self.driver.find_element_by_xpath(xpath)
        re=str(e.is_enabled())
        return re

    def scrolling(self, y):
        s = self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(y) + ")")
        return s

    def obtener_valor(self, xpath):
        val = self.driver.find_element_by_xpath(xpath).value
        return val






