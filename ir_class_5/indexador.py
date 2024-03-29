import json
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

# class IndexadorUm:
    # def __init__(self, url) -> None:
        # self.url = url
        # self.tokenized_titles = []
        # self.stop_words = set(stopwords.words('portuguese'))
        # self.inverted_index = {}
        
    # def inverted_index_generator(self):
        # for title in self.url.titles:
            # # print(title.text)
            # tokens = [token.lower() for token in nltk.word_tokenize(title.text) if token.isalnum and token.lower() not in self.stop_words]
            # self.tokenized_titles.extend(tokens)

        # for token in self.tokenized_titles:
            # self.inverted_index.setdefault(token, []).extend([link['href'] for link in self.url.links])

    # def save_index(self):
        # filename = self.url.page.text.replace('\n', '').strip()
        # with open(f"index-{filename}.json", 'w') as file:
            # json.dump(self.inverted_index, file, indent=4)
        # print(f'index-{filename}.json = {len(self.inverted_index.keys())}')
            
# class IndexadorN:
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
            
            for token in tokenized_titles: # f(k), F(k), n(k)
                self.inverted_index.setdefault(token, {}).update({object.url: [f[token], self.F[token], 0]}) # Link e peso do token!
                
            for token in self.inverted_index.keys():
                if token in f:
                    self.F[token] += f[token]
                    
    def update_F(self):
        for token in self.inverted_index.keys():
            for object_url in self.inverted_index[token].keys():
                self.inverted_index[token][object_url][1] = self.F[token]
                self.inverted_index[token][object_url][2] = len(self.inverted_index[token].keys())
            
    def save_index(self):
        filename = self.coletor.codigo
        with open(f"index-{filename}.json", 'w') as file:
            json.dump(self.inverted_index, file, indent=4)
        print(f'[indexador] index-{filename}.json = {len(self.inverted_index.keys())}')