class Url:
    def __init__(self, url, soup) -> None:        
        self.url = url # Só um atributo de informação!
        self.page = soup.find('title')
        self.titles = soup.find_all('[h1, h2]') # Tags de texto
        self.links = soup.find_all('a', href=True)