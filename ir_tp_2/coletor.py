import requests
from bs4 import BeautifulSoup
from url import Url

class Coletor:
    #def __init__(self, codigo) -> None:
    def __init__(self, codigo, max_depth=2) -> None:
        self.codigo = codigo
        self.max_depth = max_depth # Máximo nível de aprofundamento na busca por novas páginas.        
        self.urls = {}
        self.objects_url = []
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"} # Para não ser bloqueado.
        
    def add_url(self, url) -> None:
        if url not in self.urls.keys(): # Não permite incluir urls repetidas!
            self.urls[url] = False # Chegando agora! Ainda não foi processada!
            print(f'[INFO]: add_url                 - new url added = {url}.')
        
    def extract_information(self) -> None:
        good_urls = [url for url in self.urls.keys() if not self.urls[url]]
        for url in good_urls:
            response = requests.get(url, allow_redirects=True) # Fazendo requisição na página
            if response.status_code == 200:
                self.objects_url += [Url(url, BeautifulSoup(response.text, 'html.parser'))]
                self.urls[url] = True
            else:
                print(f'[coletor  ] Falha ao carregar a página: {response.status_code}')

    def bfs_extract_information(self, depth) -> None: # Breadth-First Search (Busca em Largura)
        print(f'[INFO]: bfs_extract_information - depth = {depth}.')
        print(f'[INFO]: bfs_extract_information - urls size = {len(self.urls)}.')
        if depth > self.max_depth:
            return
            
        good_urls = [url for url in self.urls.keys() if not self.urls[url]] # Seleciona os itens do dicionário, cujos valores são False (não visitadas: {'url2': False, 'url3': False, 'url4': False, 'url5': False}).
        print(f'[INFO]: bfs_extract_information - good_urls size = {len(good_urls)}.')
        for url in good_urls: # good_urls = ['url2', 'url3', 'url4', 'url5']
            print(f'[INFO]: bfs_extract_information - current url in good_urls = {url}.')
            try:
                response = requests.get(url, headers = self.headers, allow_redirects=True)#, verify=False) # Fazendo requisição na página
                            # Verifica se houve redirecionamento
                if response.history:
                    print(f'[INFO]: bfs_extract_information - redirect detected ({url}).')
                if response.status_code == 200:
                    print(f'[INFO]: bfs_extract_information - response.status_code ({url}) = {response.status_code}.')
                    url_obj = Url(url, BeautifulSoup(response.text, 'html.parser'))
                    self.objects_url += [url_obj] # Cada item dessa lista tem a url e o conteúdo das tags <title> (título da página), <h2> (conteúdos de texto), <a> (links encontrados).
                    self.urls[url] = True # Valor da url no dicionário é alterado para True (página visitada!)
                    new_urls = [link['href'] for link in url_obj.links if ('href' in link.attrs) and (link['href'].startswith('http')) and (link['href'] not in self.urls.keys())]
                    print(f'[INFO]: bfs_extract_information - new_urls size = {len(new_urls)}.')
                    for url in new_urls:
                        print(f'[INFO]: bfs_extract_information - url = {url}.')
                        self.add_url(url)
                    print(f'[INFO]: bfs_extract_information - next recursive call, depth = {depth + 1}.')
                else:
                    print(f'[ERROR]: bfs_extract_information - response error = {response.status_code}.')
            except Exception as e:
                print(f'[ERROR]: bfs_extract_information - response error = [{url}] -> {e}.')
        self.bfs_extract_information(depth + 1)

    def print_results(self): # Somente as URLs encontradas!
        print(f'print_results:\n')
        url_set = set(self.objects_url)
        for obj in url_set:
            print(f'\turl = {obj.url}')
            
    def save_results(self): # Somente as URLs encontradas!
        filename = self.codigo
        with open(f"index-{filename}.txt", 'w', encoding='utf-8') as file:
            url_set = set(self.objects_url)
            for obj in url_set:
                file.write(obj.url+'\n')                