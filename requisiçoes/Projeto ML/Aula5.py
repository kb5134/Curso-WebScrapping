import requests
from bs4 import BeautifulSoup

urlBase= 'https://lista.mercadolivre.com.br/'

ProdutoURL = input('Insira o produto que deseja buscar: ')

response = requests.get((urlBase + ProdutoURL).replace(' ','-'))


site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class':'ui-search-item__title shops__item-title'})


    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})
    if centavos:
        print(f"preço do produto: R$ {real.text}, {centavos.text}")
    else:
        print(f"Preço do produto: R$ {real.text}")
    print(f"titulo do produto: {titulo.text}")
    print(f"link do produto: {link['href']} \n")
