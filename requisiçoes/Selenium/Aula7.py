import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#opts = Options()
#opts.add_argument("--headless")
opts = webdriver.FirefoxOptions()
opts.add_argument("--width=400")
opts.add_argument("--height=800")

navegador = webdriver.Firefox(options=opts)

navegador.get('https://www.airbnb.com.br/')

sleep(2)

input_place = navegador.find_element(By.TAG_NAME, 'button').click()

sleep(2)
input_place = navegador.find_element(By.TAG_NAME, 'input').click()


sleep(1)
input_place = navegador.find_element(By.TAG_NAME, 'input')
input_place.send_keys('São Paulo')
input_place.submit()

sleep(0.5)
next_button = navegador.find_elements(By.TAG_NAME, 'button')[-4]
next_button.click()
sleep(0.5)
search_button = navegador.find_elements(By.TAG_NAME, 'button')[-1]
search_button.click()

sleep(4)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

print(site.prettify())

