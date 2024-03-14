import requests # Para pingar na url.
from bs4 import BeautifulSoup # Para navegar dentro da página.
import json # 
from datetime import datetime
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')

def extract_information(url):
    response = requests.get(url) # Fazendo requisição na página

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        page = soup.find('title')
        titles = soup.find_all('h2')
        links = soup.find_all('a', href=True)
        
        tokenized_titles = []
        stop_words = set(stopwords.words('portuguese'))
        # print(f'Títulos:')
        for title in titles:
            # print(title.text)
            tokens = [token.lower() for token in nltk.word_tokenize(title.text) if token.isalnum and token.lower() not in stop_words]
            tokenized_titles.extend(tokens)
        
        inverted_index = {}
        for token in tokenized_titles:
            inverted_index.setdefault(token, []).extend([link['href'] for link in links])
        
        # print(f'\nLinks:')
        # for link in links:
        #    print(link['href'])
        
        return [page.text.strip(), inverted_index]
    else:
        print(f'Falha ao carregar a página: {response.status_code}')
        return []

def save_index(index, filename):
    with open(filename, 'w') as file:
        json.dump(index, file, indent=4)

#url = 'https://www.ifmg.edu.br/ribeiraodasneves'
urls = ['https://www.ifmg.edu.br/ribeiraodasneves', 'http://www.ufop.br', 'https://www.serpro.gov.br', 'https://www.caixa.gov.br']

for url in urls:
    page, inverted_list = extract_information(url)
    
    if inverted_list:
        print(f'Lista invertida: ')
        for token, links in inverted_list.items():
            print(f'Token: {token}')
            print(f'\tLinks: ')
            for link in links:
                print(f'{link}')
            print()
            
        save_index(inverted_list, f"index-{page}.json")
        print(f'Lista invertida salva em index.json')