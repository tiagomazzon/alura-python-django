from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:\\Users\\tiago.mazzon\\PythonProjects\\alura-python-django\\tdd\\busca_animal\\chromedriver.exe')

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
        # Ele vê um campo para pesquisar animal

        # Ele pesquisa por Leão e clica no botão    