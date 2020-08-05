from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

WEBDRIVER = webdriver.Chrome
WEBSITE = 'https://portaleps.epssura.com/ServiciosUnClick/#/solicitudes/medicamentos'

class MedicinesRequest():

    def __init__(self, web_driver, web_site):
        self.driver = web_driver()
        self.page = web_site

        self.driver.get(self.page)
        sleep(10)
    
    def fill_data(self, elem, data, by='name'):
        
        if by == 'name':
            elem_ = self.driver.find_element_by_name(elem)
        elif by == 'id':
            elem_ = self.driver.find_element_by_id(elem)
        elif by == 'tag':
            elem_ = self.driver.find_element_by_tag_name(elem)
        elif by == 'css':
            elem_ = self.driver.find_element_by_css_selector(elem)
        else:
            raise Exception("Unexpected input for 'by' parameter!")

        elem_.clear()
        elem_.send_keys(data)

        sleep(1.5)
    
    def select_option(self, elem_name, option):
        select = Select(self.driver.find_element_by_name(elem_name))
        select.select_by_visible_text(option)

        sleep(1.5)

    def submit_data(self, elem_id):
        self.driver.find_element_by_id(elem_id).click()

    def close_driver(self):
        self.driver.close()

def main():
    sura_request = MedicinesRequest(WEBDRIVER, WEBSITE)

    sura_request.select_option('selectTipoDoc', 'CÉDULA DE CIUDADANÍA')
    sura_request.fill_data('numeroDocumento', '26414306', 'name')
    sura_request.fill_data('.ng-empty.ng-valid-date', '19/11/1939', 'css')

    input('Press any key to continue')
    
    sura_request.submit_data('btnLoginSolicitudMedicamentos')

    close = input('Close de driver? (y/n) \n -->')
    if close == 'y':
        sura_request.close_driver()

if __name__ == '__main__':
    main()