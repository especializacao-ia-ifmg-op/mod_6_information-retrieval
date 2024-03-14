import json
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

class IndexadorUm:
    def __init__(self, url) -> None:
        self.url = url
        self.tokenized_titles = []
        self.stop_words = set(stopwords.words('portuguese'))
        self.inverted_index = {}
        
    def inverted_index_generator(self):
        for title in self.url.titles:
            # print(title.text)
            tokens = [token.lower() for token in nltk.word_tokenize(title.text) if token.isalnum and token.lower() not in self.stop_words]
            self.tokenized_titles.extend(tokens)

        for token in self.tokenized_titles:
            self.inverted_index.setdefault(token, []).extend([link['href'] for link in self.url.links])

    def save_index(self):
        filename = self.url.page.text.replace('\n', '').strip()
        with open(f"index-{filename}.json", 'w') as file:
            json.dump(self.inverted_index, file, indent=4)
        print(f'index-{filename}.json = {len(self.inverted_index.keys())}')
            
class IndexadorN:
    def __init__(self, coletor) -> None:
        self.coletor = coletor
        self.tokenized_titles = []
        self.stop_words = set(stopwords.words('portuguese'))
        self.inverted_index = {}
        
    def inverted_index_generator(self):
        for object in self.coletor.objects_url:
            for title in object.titles:
                # print(title.text)
                tokens = [token.lower() for token in nltk.word_tokenize(title.text) if token.isalnum and token.lower() not in self.stop_words]
                self.tokenized_titles.extend(tokens)

            for token in self.tokenized_titles:
                self.inverted_index.setdefault(token, []).extend([link['href'] for link in object.links])

    def save_index(self):
        filename = self.coletor.codigo
        with open(f"index-{filename}.json", 'w') as file:
            json.dump(self.inverted_index, file, indent=4)
        print(f'index-{filename}.json = {len(self.inverted_index.keys())}')