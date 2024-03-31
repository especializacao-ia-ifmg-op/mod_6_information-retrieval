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
        # É necessário remover as stop words das queries? Aparentemente, não precisa!
        for token in query_tokens:
            if token in self.inverted_index:
                relevant_links.update(self.inverted_index[token])
        return relevant_links
            
    def new_search(self, query) -> set:
        query_tokens = nltk.word_tokenize(query)        
        token_relevant_links = {}
        # print(f'{self.inverted_index}')
        for token in query_tokens:
            if token in self.inverted_index:
                token_relevant_links[token] = set()
                token_relevant_links[token].update(self.inverted_index[token])
        # print(f'{token_relevant_links.values()}')
        list_relevant_links = list(token_relevant_links.values())
        # print(f'{len(list_relevant_links)}')
        final_relevant_links = []
        if len(list_relevant_links) > 0:
            final_relevant_links = list_relevant_links[0]
            for set_relevant_links in list_relevant_links[1:]:
                final_relevant_links = final_relevant_links.intersection(set_relevant_links)
        return final_relevant_links