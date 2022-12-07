from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:\\Users\\tiago.mazzon\\PythonProjects\\alura-python-django\\tdd\\busca_animal\\chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        ''' 
        Teste se um usuário encontra um animal na pesquisa
        '''
        # Vini deseja encontrar um novo animal para adotar

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        # Ele vê um campo para pesquisar animais pelo nome.
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...')

        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        #time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR,'form button').click()

        # O site exibe 4 características do animal pesquisa.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Ele desiste adotar um leão.

