import requests
from bs4 import BeautifulSoup
from url import Url

class Coletor: # 1 para N
    def __init__(self, codigo) -> None:
        self.codigo = codigo
        # self.urls = []
        self.urls = {}
        self.objects_url = []
        
    def add_url(self, url) -> None:
        # self.urls += [url]
        if url not in self.urls.keys(): # Não permite incluir urls repetidas!
            self.urls[url] = False # Chegando agora! Ainda não foi processada!
        
    def extract_information(self) -> None:
        good_urls = [url for url in self.urls.keys() if not self.urls[url]]
        # for url in self.urls:
        #for url in self.urls.keys():
        for url in good_urls:
            # if self.urls[url] == False:
            response = requests.get(url, allow_redirects=True) # Fazendo requisição na página
            if response.status_code == 200:
                self.objects_url += [Url(url, BeautifulSoup(response.text, 'html.parser'))]
                self.urls[url] = True
            else:
                print(f'[coletor  ] Falha ao carregar a página: {response.status_code}')