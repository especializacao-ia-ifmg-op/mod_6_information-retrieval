import json
import nltk
# from nltk.corpus import stopwords
# nltk.download('stopwords')
# nltk.download('punkt')

class Buscador: # 1 para N
    def __init__(self, index_file) -> None:
        with open(index_file, 'r') as file:
            self.inverted_index = json.load(file)
            
    def search(self, query) -> set:
        query_tokens = nltk.word_tokenize(query)
        relevant_links = set()
        for token in query_tokens:           
            for chave in self.inverted_index.keys():
                if token in chave:
                    for item in self.inverted_index[chave].keys():
                        relevant_links.add(item)
                    break
        return relevant_links