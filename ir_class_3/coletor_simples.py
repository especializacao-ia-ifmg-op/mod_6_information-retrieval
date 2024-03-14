import requests # Para pingar na url.
from bs4 import BeautifulSoup # Para navegar dentro da página.

#url = 'https://www.ifmg.edu.br/ribeiraodasneves'
urls = ['https://www.ifmg.edu.br/ribeiraodasneves', 'http://www.ufop.br', 'https://www.serpro.gov.br', 'https://www.caixa.gov.br']

for url in urls:
    response = requests.get(url) # Fazendo requisição na página

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2')
        links = soup.find_all('a', href=True)
        
        print(f'Títulos:')
        for title in titles:
            print(title.text)
        
        print(f'\nLinks:')
        for link in links:
            print(link['href'])
    else:
        print(f'Falha ao carregar a página: {response.status_code}')