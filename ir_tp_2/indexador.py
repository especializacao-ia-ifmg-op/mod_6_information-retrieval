import json
import math
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

class Indexador:
    def __init__(self, coletor) -> None:
        self.coletor = coletor
        #self.tokenized_titles = []
        self.stop_words = set(stopwords.words('portuguese'))
        self.inverted_index = {}
        self.F = {}
        
    def inverted_index_generator(self):
        for object in self.coletor.objects_url:
            tokenized_titles = []
            for title in object.titles: # Os h2!
                tokens = [token for token in [token.lower().replace('\u200b', '') for token in nltk.word_tokenize(title.text) if token.lower() not in self.stop_words] if token.isalnum()] # Lista de palavras relevantes!
                tokenized_titles.extend(tokens)

            f = {}
            for token in tokenized_titles:
                if token not in f:
                    f[token] = 1
                    if token not in self.F:
                        self.F[token] = 0
                else:
                    f[token] += 1
            
            # Term Frequency:
            #         / 1 + log(f) if fi,j(k) > 0, 
            #   tf = { 
            #         \ 0, otherwise
            #
            # Inverse Document Frequency:
            #   idf = log N / ni
            #   N = len((self.coletor.objects_url)
            
            for token in tokenized_titles: # f(k), F(k), n(k), idf
                self.inverted_index.setdefault(token, {}).update({object.url: [f[token], self.F[token], 0, 0]}) # Link e peso do token!
                
            for token in self.inverted_index.keys():
                if token in f:
                    self.F[token] += f[token]
                    
    def update_F(self):
        for token in self.inverted_index.keys():
            for object_url in self.inverted_index[token].keys():
                self.inverted_index[token][object_url][1] = self.F[token] # F(k)
                self.inverted_index[token][object_url][2] = len(self.inverted_index[token].keys()) # n(k)
                self.inverted_index[token][object_url][3] = math.log(len(self.coletor.objects_url)/self.inverted_index[token][object_url][2]) # idf(k)
            
    def save_index(self):
        filename = self.coletor.codigo
        with open(f"index-{filename}.json", 'w') as file:
            json.dump(self.inverted_index, file, indent=4)
        print(f'[indexador] index-{filename}.json = {len(self.inverted_index.keys())}')