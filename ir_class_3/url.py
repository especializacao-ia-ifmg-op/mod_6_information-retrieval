class Url:
    def __init__(self, soup) -> None:        
        self.page = soup.find('title')
        self.titles = soup.find_all('h2')
        self.links = soup.find_all('a', href=True)