#aula para entender o beautifulsoup
import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')
content = response.content

site = BeautifulSoup(content, 'html.parser')
post = site.find('div', attrs={'class': 'feed-post-body'}) #o find procura a primeira div que tem a classe que definimos
titulo = post.find('a', attrs={'class': 'feed-post-link'})
print(titulo.text)

subtitulo = post.find('div', attrs={'class': 'feed-post-body-resumo'})
print(subtitulo.text)