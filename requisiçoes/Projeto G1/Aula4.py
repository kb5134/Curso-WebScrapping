# aula para entender o beautifulsoup
import requests
from bs4 import BeautifulSoup
import pandas as pd

ListaNoticias = []

response = requests.get('https://g1.globo.com/')
content = response.content

site = BeautifulSoup(content, 'html.parser')

posts = site.findAll('div', attrs={'class': 'feed-post-body'})

for post in posts:
    titulo = post.find('a', attrs={'class': 'feed-post-link'})
    subtitulo = post.find('div', attrs={'class': 'feed-post-body-resumo'})
    if subtitulo:
        ListaNoticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        ListaNoticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(ListaNoticias, columns=['Titulo','Subtitulo', 'Link'])
news.to_csv('Noticias.csv', index=False)
