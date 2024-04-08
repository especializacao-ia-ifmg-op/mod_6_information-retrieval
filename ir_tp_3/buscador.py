import json
import nltk

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
                   
    def new_search(self, query, query_type=1) -> set:
        query_tokens = nltk.word_tokenize(query)        
        token_relevant_links = {}
        # print(f'{self.inverted_index}')
        for token in query_tokens:
            #print(f'self.inverted_index[token] = {self.inverted_index[token]}')
            # Preciso ranquear self.inverted_index[token]!!!
            if token in self.inverted_index:
                #ordered_inverted_index = dict(sorted(self.inverted_index[token].items(), key=lambda item: item[1]))
                #print(f'\nOrdered inverted_index[{token}]["tf-idf"] = {dict(sorted(self.inverted_index[token].items(), key=lambda item: item[1][3], reverse=True))}')
                token_relevant_links[token] = set()
                #token_relevant_links[token].update(self.inverted_index[token])
                # O ranqueamento está sendo feito aqui, pelo 'tf-idf'.
                token_relevant_links[token].update(dict(sorted(self.inverted_index[token].items(), key=lambda item: item[1][3], reverse=True)))
                #print(f'token_relevant_links[token] = {token_relevant_links[token]}')
        #print(f'\n{list(token_relevant_links.values())}')
        list_relevant_links = list(token_relevant_links.values())
        #print(f'{(list_relevant_links)}')
        final_relevant_links = []
        if len(list_relevant_links) > 0:
            final_relevant_links = list_relevant_links[0]
            for set_relevant_links in list_relevant_links[1:]:
                match query_type:
                    case 1:
                        final_relevant_links = final_relevant_links.intersection(set_relevant_links)
                    case 2:
                        final_relevant_links = final_relevant_links.union(set_relevant_links)
        return final_relevant_links
        
    def precision(self, relevants, results):
        results_size = len(results)
        intersection_size = len([link for link in results if link in relevants])
        return intersection_size / results_size
        
    def recall(self, relevants, results):
        relevants_size = len(relevants)
        intersection_size = len([link for link in results if link in relevants])
        return intersection_size / relevants_size