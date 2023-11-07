import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class PruebaSelenium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get('https://demoqa.com/')

    #   Scroll hacia abajo
    def scroll_down(self, pixels):
        scroll_script = f"window.scrollTo(0, {pixels});"
        self.driver.execute_script(scroll_script)
        time.sleep(3)

    #   Recibe valor XPATH y el tiempo de espera
    def clickElemento(self,valorPATH,StandbyTime):
        driver = self.driver
        driver.find_element(By.XPATH, f"{valorPATH}").click()
        time.sleep(StandbyTime)

    def escribirElemento(self,valorPATH,textElement,StandbyTime):
        driver = self.driver
        driver.find_element(By.XPATH, f"{valorPATH}").send_keys(f"{textElement}")
        time.sleep(StandbyTime)

    #   1.	Ingresar al módulo “Elements”
    def flujo1(self):
        self.clickElemento("//*[@id='app']/div/div/div[2]/div/div[1]/div/div[1]",1)
        self.clickElemento("//*[@id='item-1']",1)
        self.clickElemento("//*[@id='tree-node']/div/button[1]",1)
        self.scroll_down(400)
        self.clickElemento("//*[@id='tree-node']/ol/li/ol/li[3]/ol/li[1]/span/label",1)
        self.clickElemento("//*[@id='tree-node']/ol/li/ol/li[3]/ol/li[2]/span/label",1)


    #   2.	Ingresar al apartado de “Dynamic Properties”
    def flujo2(self):
        self.scroll_down(500)
        self.clickElemento("//*[@id='item-8']",1)
        time.sleep(5)
        self.clickElemento("//*[@id='enableAfter']",1)

    #3.	Luego Buscar el apartado de “Web Tables”
    def flujo3(self):
        self.scroll_down(500)
        self.clickElemento("//*[@id='item-3']", 3)
        self.scroll_down(300)
        time.sleep(3)
        self.clickElemento("//*[@id='delete-record-1']", 1)
        self.clickElemento("//*[@id='addNewRecordButton']", 1)
        self.escribirElemento("//*[@id='firstName']","Juan",1)
        self.escribirElemento("//*[@id='lastName']","Perez",1)
        self.escribirElemento("//*[@id='userEmail']", "test@test.bi.com.gt", 1)
        self.escribirElemento("//*[@id='age']", "23", 1)
        self.escribirElemento("//*[@id='salary']", "8000", 1)
        self.escribirElemento("//*[@id='department']", "Guatemala", 1)
        self.clickElemento("//*[@id='submit']", 1)




    def flujo4(self):
        self.scroll_down(500)

        self.clickElemento("//*[@id='app']/div/div/div[2]/div[1]/div/div/div[2]",1)
        self.clickElemento("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/ul/li",1)
        self.scroll_down(500)


        self.escribirElemento("//*[@id='firstName']","Bernabé",1)
        self.escribirElemento("//*[@id='lastName']", "Sánchez", 1)
        self.escribirElemento("//*[@id='userEmail']", "test@test.bi.com.gt", 1)

        self.clickElemento("//*[@id='genterWrapper']/div[2]/div[1]/label", 1)

        self.escribirElemento("//*[@id='userNumber']", "1234567890", 1)
        self.escribirElemento("//*[@id='dateOfBirthInput']", "28 Dec 1999", 2)
        self.clickElemento("//*[@id='dateOfBirth-label']", 1)


        # Encuentra el campo de entrada para el SELECT
        input_element = self.driver.find_element(By.XPATH, "//*[@id='subjectsInput']")
        # Ingresa texto en el campo de entrada
        input_element.send_keys("Maths")
        # Envía la tecla "Enter"
        input_element.send_keys(Keys.RETURN)
        time.sleep(2)

        self.clickElemento("//*[@id='hobbiesWrapper']/div[2]/div[2]/label",3)
        self.clickElemento("//*[@id='hobbiesWrapper']/div[2]/div[3]/label",3)


        # Encuentra el elemento de entrada de tipo file
        file_input = self.driver.find_element(By.ID, 'uploadPicture')
        # Ingresa la ruta del archivo
        file_input.send_keys('C:\\Users\\Usuario\\Downloads\\texto.txt')
        time.sleep(3)

        self.escribirElemento("//*[@id='currentAddress']", "Banco Industrial Zona 4. 7ª. Avenida 5-10, Zona 4 Centro Financiero Torre I", 3)
        self.scroll_down(600)

        input_element1 = self.driver.find_element(By.XPATH, "//*[@id='react-select-3-input']") # Encuentra el campo de entrada para el SELECT
        input_element1.send_keys("NCR") # Ingresa texto en el campo de entrada
        input_element1.send_keys(Keys.RETURN) # Envía la tecla "Enter"
        time.sleep(2)

        input_element2 = self.driver.find_element(By.XPATH, "//*[@id='react-select-4-input']") # Encuentra el campo de entrada para el SELECT
        input_element2.send_keys("Delhi") # Ingresa texto en el campo de entrada
        input_element2.send_keys(Keys.RETURN) # Envía la tecla "Enter"


        # time.sleep(2)
        # self.clickElemento("//*[@id='submit']", 2)
        # time.sleep(2)
        # self.clickElemento("//*[@id='closeLargeModal']", 2)
        # time.sleep(2)

    #   5.	Ingresar al módulo “Book Store Aplication”
    def flujo5(self):

        self.scroll_down(800)
        self.clickElemento("//*[@id='app']/div/div/div[2]/div[1]/div/div/div[6]", 2)
        self.scroll_down(800)
        self.clickElemento("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[2]",2)
        self.escribirElemento("//*[@id='searchBox']", "Understanding ECMAScript 6", 2)
        self.scroll_down(300)
        self.clickElemento("//*[@id='see-book-Understanding ECMAScript 6']/a",2)
        self.scroll_down(800)
        # self.clickElemento("//*[@id='userName-value']",2)
        # self.clickElemento("//label[@id='userName-value']", 6)
        self.clickElemento("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[8]/div[2]/label",6)


    def test_NewUser_Admi(self):
        # Realiza el desplazamiento hacia abajo
        self.scroll_down(300)
        self.flujo1()
        self.flujo2()
        self.flujo3()
        self.flujo4()
        self.flujo5()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output='PruebaBI', report_name='pruebaSelenium'))
